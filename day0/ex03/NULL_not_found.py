import inspect
import re
import math
from types import FrameType
import typing


def get_var_name(current_frame: FrameType | None) -> str | None:
    """Return the name of the variable given ad argument in the given frame."""
    if current_frame is None:
        return None
    last_frame = current_frame.f_back
    if last_frame is None:
        return None
    code_line = last_frame.f_code.co_filename
    line_number = last_frame.f_lineno
    with open(code_line, "r") as f:
        lines = f.readlines()
        code_line = lines[line_number - 1]
    match = re.search(r"\((.*)\)", code_line)
    return match[1] if match else None


def NULL_not_found(obj: typing.Any) -> int:
    """Print the type of falsy objects."""
    var_name = get_var_name(inspect.currentframe()) or "Unknown"
    if type(obj) is float and math.isnan(obj) or not obj:
        print(f"{var_name}: {obj} {type(obj)}")
        return 0
    else:
        print("Type not Found")
        return 1
