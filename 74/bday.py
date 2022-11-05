from calendar import day_name, weekday
import datetime


def weekday_of_birth_date(date: datetime.date):
    """Takes a date object and returns the corresponding weekday string"""
    return day_name[weekday(date.year, date.month, date.day)]
