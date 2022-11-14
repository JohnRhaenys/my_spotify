from datetime import datetime
import datetime as dt


def time_formatter(time_in_seconds):
    """
    Formats seconds to a string with hours, minutes and seconds
    :param time_in_seconds: the time, in seconds
    :return: a formatted string with the following style -> 23:59:59
    """
    hours, minutes, seconds = str(dt.timedelta(seconds=time_in_seconds)).split(':')
    if hours == '0':
        return f'{minutes}:{seconds}'
    else:
        return f'{hours}:{minutes}:{seconds}'


def time_formatter_extense(time_in_seconds):
    """
    Formats seconds to a string with hours, minutes and seconds
    :param time_in_seconds: the time, in seconds
    :return: a formatted string with the following style -> 23 hours 59 min 59 sec
    """
    hours, minutes, seconds = str(dt.timedelta(seconds=time_in_seconds)).split(':')
    if hours == '0':
        return f'{minutes} min {seconds} sec'
    else:
        return f'{hours} h {minutes} min {seconds} sec'


def date_formatter(date_time_string):
    year, month, day = date_time_string.split(' ')[0].split('-')
    date_time_obj = datetime(int(year), int(month), int(day))
    return date_time_obj.strftime("%b %d, %Y")


def get_duration_in_seconds(video_duration):
    if video_duration.count(':') == 1:
        video_duration = '0:' + video_duration
    ftr = [3600, 60, 1]
    return sum([a * b for a, b in zip(ftr, [int(i) for i in video_duration.split(":")])])
