from itertools import chain
import numbers


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """Return a list of BMI values calculated from height and weight."""
    assert (
        type(height) == list and type(weight) == list
    ), "Both arguments must be lists."
    assert len(height) == len(weight), "Both lists must have same length."
    assert all(
        isinstance(x, numbers.Number) for x in chain(height, weight)
    ), "Both lists must contain only numbers."
    return [w / h / h for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of booleans indicating whether BMI is above limit."""
    return [b > limit for b in bmi]
