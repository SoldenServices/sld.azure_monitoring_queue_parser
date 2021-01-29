from unittest.mock import patch

from azure.storage.queue import QueueClient

from azure_monitor_queue_parser import QueueMonitor


@patch('azure_monitor_queue_parser.queue_monitor.QueueClient', spec=QueueClient)
def test_queue_monitor_init_calls_from_connection_string(mock_queue_client):
    mock_queue_client.from_connection_string.return_value = None
    _ = QueueMonitor("foo", "bar")
    mock_queue_client.from_connection_string.assert_called_once_with("foo", "bar")
