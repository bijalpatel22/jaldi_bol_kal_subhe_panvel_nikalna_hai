"""
1. find out if a year is leap year or not
2. find out number of days in the month, have to define year
"""

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    '''Returns True for leap years, False for non-leap years'''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month (year, month):
    '''Returns no of days in that month in that year'''
    if not 1 <= month <=12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

year = int(input('Input Year: '))
print (is_leap(year))


month = int (input ('Input month: '))
print (days_in_month(year, month))
