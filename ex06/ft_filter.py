def ft_filter(fonction, iterable):
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if fonction is None:
        return (item for item in iterable if item)
    return (item for item in iterable if fonction(item))


print(ft_filter.__doc__)
# def est_pair(x):
#     return x % 2 == 0

# nombres = [1, 2, 3, 4, 5, 6]
# nombres_pairs = ft_filter(est_pair, nombres)
# print(list(nombres_pairs))  # [2, 4, 6]