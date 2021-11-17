"""Dates Helper Classes and Functions"""
class TimeTracker:

    def __init__(self, time_tracker_input):
        self.username = time_tracker_input.get('username')
        self.day = time_tracker_input.get('day')
        self.hour_start = time_tracker_input.get('hour_start')
        self.minute_start = time_tracker_input.get('minute_start')
        self.hour_end = time_tracker_input.get('hour_end')        
        self.minute_end = time_tracker_input.get('minute_end')
    
    def __str__(self):
        """Returns a string formatted version of the object"""
        return '[{}] {}{}:{}-{}:{}' \
            .format(self.username, self.day, self.hour_start, self.minute_start, self.hour_end, self.minute_end)

    def is_overwritten(self, current):
        """Returns True if current overwrites existing timetracker hour and minute properties 
        and False if don't"""
        ## same day
        if current.day == self.day:
            ## same hours
            if current.hour_start == self.hour_start and current.hour_end == self.hour_end:                
                # case 1: existing (TU08:00-08:30) current (TU08:00-08:30)
                if current.minute_start == self.minute_start and current.minute_end == self.minute_end:
                    return True                               
                # case 2: existing (TU08:30-08:45) current (TU08:00-08:45)                
                elif current.minute_start <= self.minute_start and current.minute_end >= self.minute_start:
                    return True
                # case 3: existing (TU08:10-08:50) current (TU08:15-08:20)
                elif (current.minute_start >= self.minute_start and current.minute_start < self.minute_end) \
                    and (current.minute_start > self.minute_start and current.minute_start <= self.minute_end):
                    return True
                # case 4: existing (TU08:00-08:30) current (TU08:15-08:45)
                elif current.minute_start <= self.minute_end and current.minute_end >= self.minute_end:
                    return True
                # case 5: existing(TU08:10-08:50) current (TU08:00-08:59)
                elif current.minute_start < self.minute_start and current.minute_end > self.minute_end:
                    return True
                # case 6: does not overwrite within same hours
                else:
                    return False
            ## different hours
            else:
                # case 7 existing (TU08:10-08:50) current (TU07:45-08:15)
                if current.hour_start < self.hour_start \
                    and (current.hour_end == self.hour_start and current.minute_end > self.minute_start ):
                    return True
                # case 8: existing (TU08:10-08:50) current (TU08:45-09:10)
                elif current.hour_end > self.hour_end \
                    and (current.hour_start == self.hour_end and current.minute_start < self.minute_end):
                    return True
                # case 9: existing (TU08:10-08:50) current (TU07:30-09:30)
                elif current.hour_start < self.hour_start and current.hour_end > self.hour_end:
                    return True
                # case 10: does not overwrite within different hours
                else:
                    return False
        ## different days
        # case 11: does not overwrite within different days
        else:
            return False          

def load_tt(filename):
    """Returns a Timetracker Dictionary"""
    tt_dic = {}    
    file = open(filename, "r")
    for line in file:
        line = line.strip('').strip('\n').split('=')
        username = line[0]

        if username not in tt_dic:
            tt_dic[username] = []

        times = line[1].split(',')
        for time in times:
            dt = time.split('-')
            day = dt[0][:2]
            hour_start = dt[0][2:4]
            minute_start = dt[0][5:]
            hour_end = dt[1][:3]
            minute_end = dt[1][3:]

            tt_input = {
                "username": username,
                "day": day,
                "hour_start": hour_start,
                "minute_start": minute_start,
                "hour_end": hour_end,                
                "minute_end": minute_end,
            }
            timetracker = TimeTracker(tt_input)
            tt_dic[username].append(timetracker)
    return tt_dic

def combinations(arr, n):
    """Returns a list of combinations of arr grouped by n"""
    if n == 0:
        return [[]]
    l =[]
    for i in range(0, len(arr)):
        m = arr[i]
        remLst = arr[i + 1:]
        for p in combinations(remLst, n-1):
            l.append([m]+p)
    return l