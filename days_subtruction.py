from value_validator import validate_date

def subtract_days(date, days): # Вычитает дни через цикл с условиями (учитывает количество дней в каждом месяце и високосные года)
    try:
        year, month, day = date.split('-')
    except:
        raise ValueError("Неправильный формат даты")
    if validate_date(year, month, day):
        year, month, day = int(year), int(month), int(day)
        long_months = [1,3,5,7,8,10,12]
        short_months = [4,6,9,11]
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        for i in range(days):
            day -= 1
            if day == 0:
                month -= 1

                if month == 0:
                    month = 12
                    year -= 1
                    is_leap_year = year % 4 == 0 and year % 100 != 0

                if month in long_months:
                    day = 31
                elif month in short_months:
                    day = 30
                elif is_leap_year:
                    day = 29
                else:
                    day = 28

        return f"{year:04d}-{month:02d}-{day:02d}"
    else:
        raise ValueError("Неправильный формат даты")