from datetime import datetime, timedelta

def calculate_sat(times):
    week_day = times.weekday()
    if week_day in [5,6]:
        different = 5-week_day
    else:
        different = -2-week_day
    week_sat = times + timedelta(days = different)
    return week_sat