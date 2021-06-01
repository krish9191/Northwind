def to_str_date(model_date):
    str_date = model_date.strftime('%Y/%m/%d')
    return str_date


def byte_array_to_json(byte_array):
    new_array = byte_array.decode('utf8')
    return new_array


def to_year(model_date):
    year = model_date.strftime('%Y')
    return year
