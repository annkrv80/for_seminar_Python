import sys

def _leap_year(year):
    return (year % 4 == 0 or year % 100 != 0 and year % 400 == 0)


def _is_valid_date(data_str):
    data_str_list = data_str.split('.')
    if len(data_str_list) > 3:
        return False
    day, month, year = map(int, data_str.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    if month in[4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if _leap_year(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False

    return True
    

#print(_is_valid_date('12.12.2005'))


__all__ = ['_is_valid_date']  


if __name__ == '__main__':
    _, date = sys.argv
    print(_is_valid_date(date))