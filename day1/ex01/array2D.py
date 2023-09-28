def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2d list horizontally."""
    assert type(family) is list, "family must be must be a list."
    assert family, "family must not be empty."
    assert all(type(x) is list for x in family), "family must be a 2D list."
    assert len({len(x) for x in family}) <= 1, "family must be rectangular."
    result = family[start:end]
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print(f"My new shape is : ({len(result)}, {len(result[0])})")
    return result
