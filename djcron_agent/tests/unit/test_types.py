from djcron_agent import types


def test_host_contains_fqdn():
    sut = types.Host(fqdn='foo')

    assert hasattr(sut, 'fqdn')
    assert 'foo' == sut.fqdn


def test_output_has_rc_and_stdout_and_stderr():
    rc = object()
    stdout = object()
    stderr = object()
    sut = types.Output(rc=rc, stdout=stdout, stderr=stderr)

    assert rc == sut.rc
    assert stdout == sut.stdout
    assert stderr == sut.stderr


def test_timestamp_contains_start_and_end():
    start = object()
    end = object()
    sut = types.Timestamp(start=start, end=end)

    assert start == sut.start
    assert end == sut.end


def test_result_contains_host_output_and_timestamp():
    host = object()
    output = object()
    timestamp = object()

    sut = types.Result(host=host, output=output, timestamp=timestamp)

    assert host == sut.host
    assert output == sut.output
    assert timestamp == sut.timestamp
