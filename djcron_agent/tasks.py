import os
import subprocess
import datetime
import tempfile
import logging
import socket

import pytz
import celery

from .types import Result, Host, Output, Timestamp


LOGGER = logging.getLogger(__name__)


@celery.task.task(name='djcron_agent')
def run_script(script=None, celery_id=None, *args, **kwargs):
    LOGGER.debug('DATA: %s, %s, %s, %s', script, celery_id, args, kwargs)

    task = Task(script, celery_id)
    return task.run()


class Task(object):
    def __init__(self, script, celery_id):
        self.celery_id = celery_id
        self.script = script

        self.tmpfile = None
        self.process = None
        self.rc = None
        self.stdout = None
        self.stderr = None

    def run(self):
        try:
            self._setup()
            self._run()
            LOGGER.debug('Success')
            return self._create_results()
        except Exception:
            LOGGER.exception('[%s] Problem running the script'
                             % self.celery_id)
            raise
        finally:
            self._teardown()

    def _setup(self):
        LOGGER.debug('[%s] Running script', self.celery_id)

        self.tmpfile = tempfile.NamedTemporaryFile(delete=False)
        LOGGER.debug('[%s] Created temporal file %s',
                     self.celery_id, self.tmpfile.name)

        with open(self.tmpfile.name, 'w+') as fd:
            fd.write(self.script)

    def _run(self):
        command = "sh %s" % self.tmpfile.name
        LOGGER.debug('[%s] Executing %s', self.celery_id, command)
        self.start = datetime.datetime.utcnow()
        self.process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            shell=True)

        self.rc = self.process.wait()
        self.end = datetime.datetime.utcnow()
        LOGGER.debug('[%s] End %s', self.celery_id, command)

        self.stdout = self.process.stdout.read()
        self.stderr = self.process.stderr.read()

        # fix times if necessary
        if self.start.tzinfo is None:
            self.start = self.start.replace(tzinfo=pytz.utc)
        if self.end.tzinfo is None:
            self.end = self.end.replace(tzinfo=pytz.utc)

    def _teardown(self):
        if self.tmpfile:
            os.unlink(self.tmpfile.name)

    def _create_results(self):
        host = Host(socket.getfqdn())
        output = Output(self.rc, self.stdout, self.stderr)
        timestamp = Timestamp(self.start, self.end)

        result = Result(host, output, timestamp)
        LOGGER.debug('Result: %s', result)
        return result
