import unittest

def convert_date_format(date_str):
    # Expect input in "YYYY-MM-DD"; validate structure and numeric parts
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Input must be in 'YYYY-MM-DD' format")
    yyyy, mm, dd = parts
    if not (yyyy.isdigit() and len(yyyy) == 4 and mm.isdigit() and dd.isdigit()):
        raise ValueError("Input must be in 'YYYY-MM-DD' format with numeric parts")
    return f"{dd}-{mm}-{yyyy}"

