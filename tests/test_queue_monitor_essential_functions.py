from unittest.mock import patch
import pytest

from azure_monitor_queue_parser import QueueMonitor


@patch('azure_monitor_queue_parser.queue_monitor.QueueClient')
@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        (["Foo", "Blah"], ["Foo", "Blah"]),
        (["Foo", "Blah", "Huh"], ["Foo", "Blah", "Huh"]),
    ]
)
def test_essential_functions_attribute_set(mock_queue_client, input_value, expected_value):
    queue_monitor = QueueMonitor("foo", "bar", essential_functions=input_value)
    assert queue_monitor.essential_functions == expected_value
