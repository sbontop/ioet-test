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
