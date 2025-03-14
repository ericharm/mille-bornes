class EventLog:
    messages: list[str] = []

    @staticmethod
    def append_message(message: str) -> None:
        EventLog.messages.append(message)
