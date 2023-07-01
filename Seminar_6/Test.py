def _is_valid_date(data_str):
    day, month, year = map(int, data_str.split('.'))
    print(year)
    if not 1 <= year <= 9999:
        return False
    else:
        return True


print(_is_valid_date('0.0.25000'))