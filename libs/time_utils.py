import datetime


def time_slots():
    times = []
    start_time = datetime.time(00, 00)
    end_time = datetime.time(23, 44)
    t = start_time
    while t <= end_time:
        t = (datetime.datetime.combine(datetime.date.today(), t) +
             datetime.timedelta(minutes=15)).time()
        times.append(t)

    return times
