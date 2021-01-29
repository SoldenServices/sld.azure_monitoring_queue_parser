from unittest.mock import patch
from typing import Tuple

import pytest

from azure_monitor_queue_parser import QueueMonitor
from azure_monitor_queue_parser.queue_monitor import parse_threshold


@patch('azure_monitor_queue_parser.queue_monitor.QueueClient')
def test_queue_monitor_class(mock_queue_client):
    queue_monitor = QueueMonitor("blah", "blah")
    assert isinstance(queue_monitor, object)


@patch('azure_monitor_queue_parser.queue_monitor.QueueClient')
def test_queue_monitor_init_conn_str_param(mock_queue_client):
    # QueueMonitor() needs to take a connection string and a queue name as __init__ arguments
    with pytest.raises(TypeError) as excinfo:
        _ = QueueMonitor()
    assert "conn_str" in str(excinfo.value)


def test_queue_monitor_init_queue_name_param():
    # QueueMonitor() needs to take a connection string and a queue name as __init__ arguments
    with pytest.raises(TypeError) as excinfo:
        _ = QueueMonitor("foo")
    assert "queue_name" in str(excinfo.value)


@patch('azure_monitor_queue_parser.queue_monitor.QueueClient')
def test_queue_monitor_init_min_message_cnt_stored(mock_queue_client):
    queue_monitor = QueueMonitor("foo", "bar", min_message_cnt=5)
    assert queue_monitor.min_message_cnt == 5


@patch('azure_monitor_queue_parser.queue_monitor.QueueClient')
def test_queue_monitor_warn_threshold_is_none(mock_queue_client):
    queue_monitor = QueueMonitor("foo", "bar")
    assert queue_monitor.warn_threshold == queue_monitor.default_warn_threshold


@patch('azure_monitor_queue_parser.queue_monitor.QueueClient')
def test_queue_monitor_crit_threshold_is_none(mock_queue_client):
    queue_monitor = QueueMonitor("foo", "bar")
    assert queue_monitor.crit_threshold == queue_monitor.default_crit_threshold


@patch('azure_monitor_queue_parser.queue_monitor.QueueClient')
def test_queue_monitor_warn_threshold_is_str(mock_queue_client):
    queue_monitor = QueueMonitor("foo", "bar", warn_threshold="5, 80")
    assert queue_monitor.warn_threshold == (5, 80)


def test_parse_threshold_return_tuple():
    rtn_value = parse_threshold("1,90")
    assert isinstance(rtn_value, Tuple)


@pytest.mark.parametrize(
    "given_value, expected_value",
    [
        ("1,100", (1, 100)),
        ("2,99", (2, 99)),
        ("2, 99", (2, 99)),
        ("2, 99 ", (2, 99)),
        ("   2   ,   99   ", (2, 99)),
        ("1, 100, 200", (1, 100)),
    ]
)
def test_parse_threshold_return_value_from_str(given_value, expected_value):
    _value = parse_threshold(given_value)
    assert _value == expected_value


@patch('azure_monitor_queue_parser.queue_monitor.QueueClient')
def test_queue_monitor_warn_threshold_is_iterable(mock_queue_client):
    queue_monitor = QueueMonitor("foo", "bar", warn_threshold=[5, 80])
    assert queue_monitor.warn_threshold == (5, 80)


@pytest.mark.parametrize(
    "given_value, expected_value",
    [
        ([2, 99], (2, 99)),
        (["2", "99"], (2, 99)),
        ((2, 99), (2, 99)),
        (("2", "99"), (2, 99)),
        ((" 2 ", " 99 "), (2, 99)),
        ((2, 98.9), (2, 98)),
    ]
)
def test_parse_threshold_return_value_from_iterable(given_value, expected_value):
    _value = parse_threshold(given_value)
    assert _value == expected_value


@patch('azure_monitor_queue_parser.queue_monitor.QueueClient')
def test_queue_monitor_crit_threshold_is_str(mock_queue_client):
    queue_monitor = QueueMonitor("foo", "bar", crit_threshold="5, 80")
    assert queue_monitor.crit_threshold == (5, 80)


@patch('azure_monitor_queue_parser.queue_monitor.QueueClient')
def test_queue_monitor_crit_threshold_is_iterable(mock_queue_client):
    queue_monitor = QueueMonitor("foo", "bar", crit_threshold=[5, 80])
    assert queue_monitor.crit_threshold == (5, 80)
