from itertools import cycle


def booklet(num_pages):
    """Generate A5 booklet page order.

    Note:
        num_pages must be a multiple of 4 (I'd add blank pages to
        achieve this)

    Args:
        num_pages (int): Number of pages in the booklet.

    Returns:
        str: Pages in order of printing.
    """
    pages = range(1, num_pages + 1)
    toggle = cycle([False, True])
    pages_left = pages
    result = []
    while pages_left:
        if toggle.next():
            result += [pages_left[0], pages_left[-1]]
        else:
            result += [pages_left[-1], pages_left[0]]
        [pages_left.pop(i) for i in (0, -1) if pages_left]
    return ", ".join(map(str, result))

print booklet(60)

