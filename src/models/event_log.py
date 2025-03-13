class EventLog:
    messages = []

    @staticmethod
    def append_message(message: str) -> None:
        EventLog.messages.append(message)
