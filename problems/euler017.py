
def euler017(start, end):
    ''' Number letter counts
    
    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    how many letters would be used?

    >>> euler017(1, 5)
    19
    >>> euler017(1, 1000)
    21124
    '''
    number = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                   6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                   11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                   16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
                   30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 
                   90: 'ninety', 100: 'onehundred', 200: 'twohundred', 300: 'threehundred', 400: 'fourhundred', 
                   500: 'fivehundred', 600: 'sixhundred', 700: 'sevenhundred', 800: 'eighthundred', 
                   900: 'ninehundred', 1000: 'onethousand'}

    def written_length(n):
        ''' Only works up to 1000.  '''
        try:
            value = number[n]
            length = len(value)
        except KeyError:
            ones = n % 10
            tens = n % 100 - ones
            hundreds = n % 1000 - tens - ones
            if tens == 10:
                tens = ones + tens
                ones = 0
            if n > 100:
                conjunction = "and"
            else:
                conjunction = ""
            value = "".join([number[hundreds], conjunction, number[tens], number[ones]])
            length = len(value)
        finally:
            return length

    return sum(written_length(i) for i in xrange(start, end+1))
