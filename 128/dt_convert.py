from datetime import datetime

THIS_YEAR = 2018


def years_ago(date):
    year = datetime.strptime(date, '%d %b, %Y')
    return THIS_YEAR - year.year


def convert_eu_to_us_date(date):
    eu_date = datetime.strptime(date, '%d/%m/%Y')
    return eu_date.strftime('%m/%d/%Y')
