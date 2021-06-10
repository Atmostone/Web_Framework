import quopri


def decode_data(data):
    """
    decode string to readable text
    :param data:
    :return:
    """
    new_data = {}
    for k, v in data.items():
        val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = quopri.decodestring(val).decode('UTF-8')
        new_data[k] = val_decode_str
    return new_data


def parse_data(data):
    """
    parse parameters from request
    :param data:
    :return:
    """
    result = {}
    if data:
        params = data.split('&')
        for item in params:
            key, value = item.split('=')
            result[key] = value
    return decode_data(result)
