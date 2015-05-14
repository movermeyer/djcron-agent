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
    assert result.output.stdout == b'foo\n'
    assert result.output.stderr == b''
    assert start_time <= result.timestamp.start <= end_time
    assert start_time <= result.timestamp.end <= end_time
    assert result.timestamp.start.tzinfo is not None
    assert result.timestamp.end.tzinfo is not None


def test_task_failing():
    script = 'foobarbazzquhr'
    celery_id = 'test'
    task = tasks.Task(script, celery_id)
    start_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

    result = task.run()
    end_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

    assert result.host.fqdn == socket.getfqdn()
    assert result.output.rc == 127
    assert result.output.stdout == b''
    assert b'not found' in result.output.stderr
    assert start_time <= result.timestamp.start <= end_time
    assert start_time <= result.timestamp.end <= end_time
    assert result.timestamp.start.tzinfo is not None
    assert result.timestamp.end.tzinfo is not None
