import os
from time import time
from typing import Iterator


EIGHTS = " ▏▎▍▌▋▊▉█"
MIN_INTERVAL = 0.1


def _clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)


def _format_time(seconds):
    h, s = divmod(int(seconds), 3600)
    m, s = divmod(s, 60)
    return f"{h}:{m:02}:{s:02}" if h else f"{m:02}:{s:02}"


def _fill_bar(width, prop):
    increments = int(prop * width * 8)
    bar = []
    for _ in range(width):
        bar.append(EIGHTS[_clamp(increments, 0, 8)])
        increments -= 8
    return "".join(bar)


def _display_bar(i, len_, t0, last_print, width):
    current_time = time()
    if 0 < i < len_ and current_time - last_print < MIN_INTERVAL:
        return last_print
    prop = i / len_
    start = f"{int(100*prop):>3}%|"
    elapsed = current_time - t0
    estimated = "?" if i == 0 else _format_time((1 - prop) * elapsed / i)
    its = "?" if i == 0 else f"{i / elapsed:.2f}"
    end = f"| {i:}/{len_} [{_format_time(elapsed)}<{estimated}, {its}it/s]"
    remaining = max(1, width - len(start) - len(end))
    out = "\r" + start + _fill_bar(remaining, prop) + end
    print(out[: width + 1], end="")
    return current_time


def ft_tqdm(lst: range) -> Iterator[int]:
    """Decorate a range."""
    if len(lst) == 0:
        return
    width = os.get_terminal_size().columns
    t0 = time()
    last_print = 0
    for i, elem in enumerate(lst):
        last_print = _display_bar(i, len(lst), t0, last_print, width)
        yield elem
    _display_bar(len(lst), len(lst), t0, 0, width)
