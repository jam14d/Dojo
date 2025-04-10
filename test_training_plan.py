import unittest
from test_profiles import test_profile_basic
from main import calculate_weeks_until_race

"""
Runs  unit tests using dummy data

"""

class TestTrainingPlan(unittest.TestCase):
    def test_weeks_calculation(self):
        weeks = calculate_weeks_until_race(test_profile_basic["race_date"])
        self.assertGreaterEqual(weeks, 0)

if __name__ == "__main__":
    unittest.main()
