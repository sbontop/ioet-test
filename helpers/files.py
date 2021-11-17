"""Input Helper Classes and Functions"""

from helpers.timetracker import TimeTracker

def load_tt(filename):
    timetracker_dic = {}
    """Returns a Timetracker Dictionary"""
    file = open(filename, "r")
    for line in file:
        line = line.strip('').strip('\n').split('=')
        username = line[0]

        if username not in timetracker_dic:
            timetracker_dic[username] = []

        times = line[1].split(',')
        for time in times:
            dt = time.split('-')
            day = dt[0][:2]
            hour_start = dt[0][2:4]
            minute_start = dt[0][5:]
            hour_end = dt[1][:3]
            minute_end = dt[1][3:]

            timetracker_input = {
                "username": username,
                "day": day,
                "hour_start": hour_start,
                "minute_start": minute_start,
                "hour_end": hour_end,                
                "minute_end": minute_end,
            }
            print(timetracker_input)
            timetracker = TimeTracker(timetracker_input)
            timetracker_dic[username].append(timetracker)
    return timetracker_dic
