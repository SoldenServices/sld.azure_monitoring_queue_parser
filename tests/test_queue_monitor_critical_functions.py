import pytest

from azure_monitor_queue_parser import QueueMonitor


@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        (["Foo", "Blah"], ["Foo", "Blah"]),
        (["Foo", "Blah", "Huh"], ["Foo", "Blah", "Huh"]),
    ]
)
def test_critical_functions_attribute_set(input_value, expected_value):
    queue_monitor = QueueMonitor("foo", "bar", critical_functions=input_value)
    assert queue_monitor.critical_functions == expected_value
