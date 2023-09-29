import os
from time import time
from typing import Iterator


EIGHTS = " ▏▎▍▌▋▊▉█"
MIN_INTERVAL = 0.1


def clamp(num, min_value, max_value):
    """Clamp a number between a minimum and a maximum value."""
    return max(min(num, max_value), min_value)


def format_time(seconds):
    """Format a number of seconds into a human-readable string."""
    h, s = divmod(int(seconds), 3600)
    m, s = divmod(s, 60)
    return f"{h}:{m:02}:{s:02}" if h else f"{m:02}:{s:02}"


def fill_bar(width, prop):
    """Fill a progress bar with the appropriate number of characters."""
    increments = int(prop * width * 8)
    bar = []
    for _ in range(width):
        bar.append(EIGHTS[clamp(increments, 0, 8)])
        increments -= 8
    return "".join(bar)


def display_bar(i, len_, t0, last_print, width):
    """Display a progress bar."""
    current_time = time()
    if 0 < i < len_ and current_time - last_print < MIN_INTERVAL:
        return last_print
    prop = i / len_
    start = f"{int(100*prop):>3}%|"
    elapsed = current_time - t0
    estimated = "?" if i == 0 else format_time((1 - prop) * elapsed / i)
    its = "?" if i == 0 else f"{i / elapsed:.2f}"
    end = f"| {i:}/{len_} [{format_time(elapsed)}<{estimated}, {its}it/s]"
    remaining = max(1, width - len(start) - len(end))
    out = "\r" + start + fill_bar(remaining, prop) + end
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
        last_print = display_bar(i, len(lst), t0, last_print, width)
        yield elem
    display_bar(len(lst), len(lst), t0, 0, width)
