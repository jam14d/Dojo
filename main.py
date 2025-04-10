from training_data import training_plan
from datetime import datetime

def get_user_input():
    print("Welcome to Dojo – your personal half-marathon coach!\n")

    name = input("What's your name? ")

    # Get and parse race date
    while True:
        race_date_input = input("Enter your target race date (YYYY-MM-DD): ")
        try:
            race_date = datetime.strptime(race_date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter the date in the correct format: YYYY-MM-DD")

    # Get current weekly mileage
    while True:
        try:
            mileage = float(input("What's your current weekly mileage (in miles)? "))
            break
        except ValueError:
            print("Please enter a number.")

    # Experience level
    levels = ['beginner', 'intermediate', 'advanced']
    while True:
        level = input("What's your running level (beginner/intermediate/advanced)? ").lower()
        if level in levels:
            break
        print("Please choose from: beginner, intermediate, or advanced.")

    # Injury history
    injuries = input("List any current or past injuries (comma-separated, or type 'none'): ")
    injury_list = [inj.strip().lower() for inj in injuries.split(",")] if injuries.lower() != 'none' else []

    # Preferred running days
    preferred_days = input("Preferred days to run (e.g., Mon,Wed,Fri): ")
    preferred_days = [day.strip().capitalize() for day in preferred_days.split(",")]

    user_profile = {
        "name": name,
        "race_date": race_date,
        "weekly_mileage": mileage,
        "level": level,
        "injuries": injury_list,
        "preferred_days": preferred_days,
    }

    return user_profile


def calculate_weeks_until_race(race_date):
    # Determine how long the training plan should be
    pass

def generate_training_plan(user_profile):
    # Build a personalized training schedule
    pass

def adjust_for_injuries(training_plan, injury_history):
    # Modify training for injuries
    pass

def display_plan(training_plan):
    # Print or export the plan
    pass

def main():
    user_profile = get_user_input()
    training_plan = generate_training_plan(user_profile)
    training_plan = adjust_for_injuries(training_plan, user_profile['injuries'])
    display_plan(training_plan)

if __name__ == "__main__":
    main()
