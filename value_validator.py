def validate_date(year, month, day):
    if ((len(year) == 4 and len(month) == 2 and len(day) == 2)
            and year.isdigit() and month.isdigit() and day.isdigit()):
        long_months = [1, 3, 5, 7, 8, 10, 12]
        short_months = [4, 6, 9, 11]
        is_leap_year = (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0)
        if ((1 <= int(month) <= 12 and int(day) >= 1
        and ((int(month) in long_months and int(day) <= 31) or (int(month) in short_months and int(day) <= 30)
        or (int(month) == 2 and is_leap_year and int(day) <= 29) or (int(month) == 2 and (not is_leap_year) and int(day) <= 28)))):
            return True
        else:
            return False
    else:
        return False


def validate_datetime(year, month, day, hour, minute):
    is_date_valid = validate_date(year, month, day)
    if (len(hour) == 2 and len(minute) == 2) and (hour.isdigit() and minute.isdigit()):
        if is_date_valid and (0 <= int(hour) <= 23 and 0 <= int(minute) <= 59):
            return True
        else:
            return False
    else:
        return False

