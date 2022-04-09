# check weather the 13th friday exists in given month and year

import datetime
def has_friday_13(month, year):
    return datetime.date(year, month, 13).strftime("%A") == "Friday"

print(has_friday_13(5, 2001))