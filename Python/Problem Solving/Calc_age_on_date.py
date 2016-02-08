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
            print "Please enter a valid initial date"
            return False
    else:
        print "Please enter a valid initial date"
        return False


def daysinYear(y1, y2):
    days = 0
    if y1 < y2:
        for y in range(y1, y2):
            if isLeapYear(y) is True:
                days += 366
            else:
                days += 365
    return days


def daysInMonth(m1, d1, m2, d2):
    birthDate = sum(daysOfMonths[0: m1 - 1]) + d1
    currentDate = sum(daysOfMonths[0: m2 - 1]) + d2
    currentDays = currentDate - birthDate
    return currentDays


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    finalDays = daysinYear(y1, y2) + daysInMonth(m1, d1, m2, d2)
    if ((isLeapYear(y1) is True) and (m1 >= 3)) or (
        (isLeapYear(y2) is True) and (m2 >= 3)):
        finalDays += 1

    print "You are " + str(finalDays) + " days old"
    return finalDays


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
            print result
        else:
            print "Test case passed!"

test()
