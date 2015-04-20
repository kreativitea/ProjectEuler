from eutility.eumath import letter


def euler022(data):
    ''' Names scores

    Using problem022.txt, a 46K text file containing over five-thousand first names,
    begin by sorting it into alphabetical order. Then working out the alphabetical value
    for each name, multiply this value by its alphabetical position in the list to obtain
    a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth
    3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a
    score of 938 * 53 = 49714.

    What is the total of all the name scores in the file?

    >>> from eutility.fileops import data
    >>> with data('euler022.txt') as f:
    >>>     euler022(readcsv(f.next(), fn=lambda x: x.strip('"')))
    871198282
    '''
    return sum(
        sum(letter(p) for p in name) * index
        for index, name in enumerate(sorted(data), 1)
    )
