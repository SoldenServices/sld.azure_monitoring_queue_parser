import pytest

from azure_monitor_queue_parser import QueueMonitor


def test_queue_monitor_class():
    queue_monitor = QueueMonitor("blah", "blah")
    assert isinstance(queue_monitor, object)


def test_queue_monitor_init_queue_name_param():
    # QueueMonitor() needs to take a connection string and a queue name as __init__ arguments
    with pytest.raises(TypeError) as excinfo:
        _ = QueueMonitor()
    assert "queue_name" in str(excinfo.value)


def test_queue_monitor_init_conn_str_param():
    # QueueMonitor() needs to take a connection string and a queue name as __init__ arguments
    with pytest.raises(TypeError) as excinfo:
        _ = QueueMonitor("foo")
    assert "conn_str" in str(excinfo.value)


def test_queue_monitor_init_min_message_cnt_stored():
    queue_monitor = QueueMonitor("foo", "bar", min_message_cnt=5)
    assert queue_monitor.min_message_cnt == 5


def test_queue_monitor_warn_threshold_is_none():
    queue_monitor = QueueMonitor("foo", "bar")
    assert queue_monitor.warn_threshold == queue_monitor.default_warn_threshold
