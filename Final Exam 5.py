"""
 Calculates the number of days that have passed since the given birthday.
    Only full years are counted.
    The birth year and the current year are excluded.

    :param birthday: string in format "DD-MM-YYYY"
    :return: total number of days from full years only
"""

def days_since_birthday(birthday):
    year = int(birthday[-4:])
    current_year = 2026  # must match actual current year

    total_days = 0

    # exclude birth year and current year
    for y in range(year + 1, current_year):
        total_days += 365

        # leap year rule
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            total_days += 1

    return total_days

print(days_since_birthday("19-01-2005"))