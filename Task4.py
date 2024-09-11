def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def date_check(date: str) -> bool:
    day, month, year = (int(item) for item in date.split('.'))
    if not (1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if is_leap(year) and month == 2 and day > 29:
        return False
    if not is_leap(year) and month == 2 and day > 28:
        return False
    return True


if __name__ == '__main__':
    print(date_check('29.02.2020'))


__all__ = ['date_check', 'is_leap']