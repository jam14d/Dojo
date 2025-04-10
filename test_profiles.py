import json
from datetime import datetime

"""
Loads and parses dummy data
"""


# Load JSON file
with open("test_profiles.json", "r") as file:
    raw_profiles = json.load(file)

# Convert race_date strings to datetime objects
def parse_profile(profile):
    profile["race_date"] = datetime.strptime(profile["race_date"], "%Y-%m-%d")
    return profile

# Parse individual profiles
test_profile_basic = parse_profile(raw_profiles["basic_profile"])
test_profile_advanced = parse_profile(raw_profiles["advanced_profile"])
