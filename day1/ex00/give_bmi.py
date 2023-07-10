def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    assert len(height) == len(weight), "Both lists must have same length."
    return [w / h / h for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [b > limit for b in bmi]
