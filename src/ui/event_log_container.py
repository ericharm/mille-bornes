from textual.app import ComposeResult
from textual.containers import (
    Horizontal,
    VerticalScroll,
)
from textual.widgets import Static

from src.models.event_log import EventLog


class EventLogContainer(Horizontal):
    def compose(self) -> ComposeResult:
        yield VerticalScroll(*[Static(message) for message in EventLog.messages])
