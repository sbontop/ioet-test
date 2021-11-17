import unittest

from helpers import TimeTracker

class TimeTrackerTest(unittest.TestCase):

    def test_coincidence_1_success(self):
        tt_existing_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '00', 'hour_end': '08', 'minute_end': '30' }
        tt_current_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '00', 'hour_end': '08', 'minute_end': '30' }

        tt_existing = TimeTracker(tt_existing_input)
        tt_current = TimeTracker(tt_current_input)

        self.assertTrue(tt_existing.is_overwritten(tt_current))
    
    def test_coincidence_2_success(self):
        tt_existing_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '30', 'hour_end': '08', 'minute_end': '45' }
        tt_current_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '00', 'hour_end': '08', 'minute_end': '45' }

        tt_existing = TimeTracker(tt_existing_input)
        tt_current = TimeTracker(tt_current_input)

        self.assertTrue(tt_existing.is_overwritten(tt_current))
    
    def test_coincidence_3_success(self):
        tt_existing_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '10', 'hour_end': '08', 'minute_end': '50' }
        tt_current_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '15', 'hour_end': '08', 'minute_end': '20' }

        tt_existing = TimeTracker(tt_existing_input)
        tt_current = TimeTracker(tt_current_input)

        self.assertTrue(tt_existing.is_overwritten(tt_current))
    
    def test_coincidence_4_success(self):
        tt_existing_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '00', 'hour_end': '08', 'minute_end': '30' }
        tt_current_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '15', 'hour_end': '08', 'minute_end': '45' }

        tt_existing = TimeTracker(tt_existing_input)
        tt_current = TimeTracker(tt_current_input)

        self.assertTrue(tt_existing.is_overwritten(tt_current))
    
    def test_coincidence_5_success(self):
        tt_existing_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '10', 'hour_end': '08', 'minute_end': '50' }
        tt_current_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '00', 'hour_end': '08', 'minute_end': '59' }

        tt_existing = TimeTracker(tt_existing_input)
        tt_current = TimeTracker(tt_current_input)

        self.assertTrue(tt_existing.is_overwritten(tt_current))
    
    def test_coincidence_7_does_not_overwrite_within_same_hours_success(self):
        tt_existing_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '10', 'hour_end': '08', 'minute_end': '50' }
        tt_current_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '51', 'hour_end': '08', 'minute_end': '59' }

        tt_existing = TimeTracker(tt_existing_input)
        tt_current = TimeTracker(tt_current_input)

        self.assertFalse(tt_existing.is_overwritten(tt_current))
    
    def test_coincidence_7_success(self):
        tt_existing_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '10', 'hour_end': '08', 'minute_end': '50' }
        tt_current_input = { 'day': 'TU', 'hour_start': '07', 'minute_start': '45', 'hour_end': '08', 'minute_end': '15' }

        tt_existing = TimeTracker(tt_existing_input)
        tt_current = TimeTracker(tt_current_input)

        self.assertTrue(tt_existing.is_overwritten(tt_current))
    
    def test_coincidence_8_success(self):
        tt_existing_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '10', 'hour_end': '08', 'minute_end': '50' }
        tt_current_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '45', 'hour_end': '09', 'minute_end': '10' }

        tt_existing = TimeTracker(tt_existing_input)
        tt_current = TimeTracker(tt_current_input)

        self.assertTrue(tt_existing.is_overwritten(tt_current))
    
    def test_coincidence_9_success(self):
        tt_existing_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '10', 'hour_end': '08', 'minute_end': '50' }
        tt_current_input = { 'day': 'TU', 'hour_start': '07', 'minute_start': '30', 'hour_end': '09', 'minute_end': '30' }

        tt_existing = TimeTracker(tt_existing_input)
        tt_current = TimeTracker(tt_current_input)

        self.assertTrue(tt_existing.is_overwritten(tt_current))
    
    def test_coincidence_does_not_overwrite_within_different_hours_10_success(self):
        tt_existing_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '10', 'hour_end': '09', 'minute_end': '10' }
        tt_current_input = { 'day': 'TU', 'hour_start': '10', 'minute_start': '10', 'hour_end': '11', 'minute_end': '10' }

        tt_existing = TimeTracker(tt_existing_input)
        tt_current = TimeTracker(tt_current_input)

        self.assertFalse(tt_existing.is_overwritten(tt_current))
    
    def test_coincidence_11_does_not_overwrite_within_different_days_success(self):
        tt_existing_input = { 'day': 'MO', 'hour_start': '08', 'minute_start': '10', 'hour_end': '09', 'minute_end': '10' }
        tt_current_input = { 'day': 'TU', 'hour_start': '08', 'minute_start': '10', 'hour_end': '09', 'minute_end': '10' }

        tt_existing = TimeTracker(tt_existing_input)
        tt_current = TimeTracker(tt_current_input)

        self.assertFalse(tt_existing.is_overwritten(tt_current))

if __name__ == '__main__':
    unittest.main()