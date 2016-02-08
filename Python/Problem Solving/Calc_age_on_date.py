# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def isDateValid(y1, m1, d1, y2, m2, d2):
    if y1 < y2:
        return True
    elif y1 == y2:
        if m1 < m2:
            return True
        elif m1 == m2:
            if d1 <= d2:
                return True
        else:
            return "Please enter a valid initial date"
    else:
        return "Please enter a valid initial date"


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = 0
    if y1 < y2:
        for y in range(y1, y2):
            if isLeapYear(y) is True:
                days += 366
            else:
                days += 365

# def DaysInMonths(m1, m2, d1, d2):
    BirthDate = sum(daysOfMonths[0: m1 - 1]) + d1
    CurrentDate = sum(daysOfMonths[0: m2 - 1]) + d2
    days = days + CurrentDate - BirthDate
    return days

print daysBetweenDates(2001, 2, 3, 2004, 4, 12)
