import curses
import sys

from util import ROW, COL, start
from clip_cursor import ClipBuffer
from clip_fixed import ClipCursorFixed, ClipAppFixed


# [cursor]
class ViewportCursor(ClipCursorFixed):
    def __init__(self, buffer, window):
        super().__init__(buffer)
        self._window = window

    def left(self):
        super().left()
        self._fix()

    def right(self):
        super().right()
        self._fix()

    def _fix(self):
        self._pos[COL] = min(
            self._pos[COL],
            self._buffer.ncol(self._pos[ROW]) - 1,
            self._window.size()[COL] - 1
        )


# [/cursor]


# [buffer]
class ViewportBuffer(ClipBuffer):
    def __init__(self, lines):
        super().__init__(lines)
        self._top = 0
        self._height = None

    def lines(self):
        line_numbers = range(self._top + 1, self._top + self._height + 1)
        lines_with_numbers = [
            f"{line_number:{len(str(self.nrow()))}} | {line}"
            for line_number, line in zip(line_numbers, self._lines[self._top : self._top + self._height])
        ]
        return lines_with_numbers

    def set_height(self, height):
        self._height = height

    def _bottom(self):
        return self._top + self._height

    # [/buffer]

    # [transform]
    def transform(self, pos):
        result = (pos[ROW] - self._top, pos[COL])
        return result

    # [/transform]

    # [scroll]
    def scroll(self, row, col):
        old = self._top
        if (row == self._top - 1) and self._top > 0:
            self._top -= 1
        elif (row == self._bottom()) and (self._bottom() < self.nrow()):
            self._top += 1

    # [/scroll]


# [app]
class ViewportApp(ClipAppFixed):
    def _make_buffer(self):
        self._buffer = ViewportBuffer(self._lines)

    def _make_cursor(self):
        self._cursor = ViewportCursor(self._buffer, self._window)

    def _run(self):
        self._buffer.set_height(self._window.size()[ROW])
        while self._running:
            self._window.draw(self._buffer.lines())
            screen_pos = self._buffer.transform(self._cursor.pos())
            self._screen.move(*screen_pos)
            self._interact()
            self._buffer.scroll(*self._cursor.pos())


# [/app]

if __name__ == "__main__":
    size, lines = start()
    app = ViewportApp(size, lines)
    curses.wrapper(app)
