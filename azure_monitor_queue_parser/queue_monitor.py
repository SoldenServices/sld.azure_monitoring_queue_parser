from typing import Optional, Union, List


class QueueMonitor:
    default_warn_threshold = (1, 100)
    default_crit_threshold = (2, 100)

    def __init__(
            self,
            queue_name,
            conn_str,
            min_message_cnt: int = 1,
            warn_threshold: Optional[Union[str, List]] = None,
            crit_threshold: Optional[Union[str, List]] = None,
            essential_functions: Optional[List[str]] = None,
            critical_functions: Optional[List[str]] = None,
    ):
        self.queue_name = queue_name
        self.conn_str = conn_str
        self.min_message_cnt = min_message_cnt
        self._warn_threshold = None
        self._crit_threshold = None
        self.essential_functions = essential_functions
        self.critical_function = critical_functions
        self.warn_threshold = warn_threshold
        self.crit_threshold = crit_threshold

    @property
    def warn_threshold(self):
        return self._warn_threshold

    @warn_threshold.setter
    def warn_threshold(self, value):
        if value is None:
            self._warn_threshold = self.default_warn_threshold
        else:
            self._warn_threshold = value

    @property
    def crit_threshold(self):
        return self._crit_threshold

    @crit_threshold.setter
    def crit_threshold(self, value):
        if value is None:
            self._crit_threshold = self.default_crit_threshold
        else:
            self._crit_threshold = value
