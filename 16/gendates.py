from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    pybites_born_plus_100_days = PYBITES_BORN
    while True:
        pybites_born_plus_100_days = pybites_born_plus_100_days + timedelta(days=100)
        yield pybites_born_plus_100_days