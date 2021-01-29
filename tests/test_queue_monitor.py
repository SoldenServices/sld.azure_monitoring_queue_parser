import pytest

from azure_monitor_queue_parser import QueueMonitor


def test_queue_monitor_class():
    queue_monitor = QueueMonitor(queue_name="blah", conn_str="blah")
    assert isinstance(queue_monitor, object)


def test_queue_monitor_init_queue_name_param():
    # QueueMonitor() needs to take a connection string and a queue name as __init__ arguments
    with pytest.raises(TypeError) as excinfo:
        _ = QueueMonitor()
    assert "queue_name" in str(excinfo.value)


def test_queue_monitor_init_conn_str_param():
    # QueueMonitor() needs to take a connection string and a queue name as __init__ arguments
    with pytest.raises(TypeError) as excinfo:
        _ = QueueMonitor()
    assert "conn_str" in str(excinfo.value)
