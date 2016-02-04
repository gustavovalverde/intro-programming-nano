# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year % 4 != 0:
        return daysOfMonths
    elif year % 100 != 0:
        daysOfMonths[1] = 29
        return daysOfMonths
    elif year % 400 != 0:
        return daysOfMonths
    else:
        daysOfMonths[1] = 29
        return daysOfMonths

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    from_date = y1, m2, d1
    to_date = y2, m2, d2
    days = (sum(y1, m1) + d1) - (sum(y2, m2) + d2)
    return days

print daysBetweenDates(isLeapYear(2004), 2, 3, isLeapYear(2004), 4, 12)
