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

def isDateValid(y1,y2):
    if y1 < y2:
        return True
    elif y1 == y2:
        if m1 < m2:
            return True
        elif m1 == m2:
            if d1 <= d2:
                return True
        else: return "Please enter a valid date"
    else:
        return "Please enter a valid initial date"

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = 0
    if y1 < y2:
        for y in range(y1, y2):
            days += sum(isLeapYear(y))
    m1 = sum(daysOfMonths[m1 - 1:])
    print days
    print m1

print daysBetweenDates(2004, 2, 3, 2009, 4, 12)
