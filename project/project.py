#!/usr/bin/env python3

def is_divisible_by(year, b):
    return year % b == 0

def is_leap_year(year):
    ''' Return true if year is a leap year

    >>> is_leap_year(2000)
    True
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(1996)
    True
    '''
    if not is_divisible_by(year, 4):
        return False
    elif not is_divisible_by(year, 100):
        return True
    elif not is_divisible_by(year, 400):
        return False
    else:
        return True