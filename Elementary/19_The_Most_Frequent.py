def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    from collections import defaultdict

    words = ' '.join(data)

    d = defaultdict(int)
    for word in words.split():
        d[word] += 1

    max_value = (max(d.values()))
    for k in d:
        if d[k] == max_value:
            return k


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
