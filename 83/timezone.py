from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    utc_dt = utc.localize(naive_utc_dt)
    return utc_dt.astimezone(AUSTRALIA), utc_dt.astimezone(SPAIN)
