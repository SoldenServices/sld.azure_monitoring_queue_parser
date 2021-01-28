from azure_monitor_queue_parser import QueueMonitor


def test_queue_monitor_class():
    queue_monitor = QueueMonitor()
    assert isinstance(queue_monitor, object)
