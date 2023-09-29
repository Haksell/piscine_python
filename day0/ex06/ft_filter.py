def identity(x):
    """Return the argument."""
    return x


def ft_filter(func, seq):
    """Filter."""
    if func is None:
        func = identity
    return (x for x in seq if func(x))


# My autoformatter insisted on adding tabs to lines 3 and 4
# when writing the following docstring.
ft_filter.__doc__ = """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
