import socket
import pytz
import datetime
from djcron_agent import tasks


def test_task_basic_execution():
    script = 'echo "foo"'
    celery_id = 'test'
    task = tasks.Task(script, celery_id)
    start_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

    result = task.run()
    end_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

    assert result.host.fqdn == socket.getfqdn()
    assert result.output.rc == 0
    assert result.output.stdout == 'foo\n'
    assert result.output.stderr == ''
    assert start_time <= result.timestamp.start <= end_time
    assert start_time <= result.timestamp.end <= end_time
    assert result.timestamp.start.tzinfo != None
    assert result.timestamp.end.tzinfo != None
