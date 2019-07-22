'''
Utils functions
'''

import datetime


def add_ms_to_datetime(timestamp, ms):
    '''
    Arguments:
        timestamp: base datetime
        ms: ms to add

    Returns: addition of timestamp and ms

    Add ms milliseconds to timestamps
    '''
    return timestamp + datetime.timedelta(milliseconds=int(ms))


def datetime_to_print(timestamp):
    '''
    Arguments:
        timestamp: datetime object

    Returns: date, time in a printable format

    Transforms datetime into a date and a time in a printable format
    '''
    date = timestamp.strftime('%d of %B, %Y')
    time = timestamp.strftime('%H::%M::%S')
    return date, time
