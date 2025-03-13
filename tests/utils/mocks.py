class MockCursesWindow:
    def __init__(self):
        self.lines = []

    def addstr(self, y: int, x: int, text: str) -> None:
        self.increase_line_count_to(y)
        self.increase_character_count_of_line_to(self.lines[y], x + len(text))

        for i, char in enumerate(text):
            self.lines[y][x + i] = char

    def addch(self, y: int, x: int, text: str) -> None:
        self.addstr(y, x, text)

    def increase_line_count_to(self, y: int) -> None:
        while len(self.lines) <= y:
            self.lines.append([])

    def increase_character_count_of_line_to(self, line: list[str], length: int) -> None:
        while len(line) < length:
            line.append(" ")

    def assert_output(self, expected_output: list[str]) -> None:
        assert self.output == "\n".join(expected_output)

    @property
    def output(self) -> str:
        return "\n".join(["".join(line) for line in self.lines])

    # @cached_property
    # def as_curses_window(self) -> window:
    #     return cast(window, self)
