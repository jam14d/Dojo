from training_data import training_plan
from datetime import datetime

def main(use_test_profile=False):
    if use_test_profile:
        from test_profiles import test_profile_basic
        user_profile = test_profile_basic
    else:
        user_profile = get_user_input()

    training_plan = generate_training_plan(user_profile)
    training_plan = adjust_for_injuries(training_plan, user_profile['injuries'])
    display_plan(training_plan)


def get_user_input():
    print("Welcome to Dojo – your personal half-marathon coach!\n")
    name = input("What's your name? ")

    while True:
        race_date_input = input("Enter your target race date (YYYY-MM-DD): ")
        try:
            race_date = datetime.strptime(race_date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter the date in the correct format: YYYY-MM-DD")

    while True:
        try:
            mileage = float(input("What's your current weekly mileage (in miles)? "))
            break
        except ValueError:
            print("Please enter a number.")

    levels = ['beginner', 'intermediate', 'advanced']
    while True:
        level = input("What's your running level (beginner/intermediate/advanced)? ").lower()
        if level in levels:
            break
        print("Please choose from: beginner, intermediate, or advanced.")

    injuries = input("List any current or past injuries (comma-separated, or type 'none'): ")
    injury_list = [inj.strip().lower() for inj in injuries.split(",")] if injuries.lower() != 'none' else []

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
    today_date = datetime.today()
    delta = race_date - today_date
    weeks = delta.days // 7
    return weeks

def generate_training_plan(user_profile):
    race_date = user_profile["race_date"]
    weeks = calculate_weeks_until_race(race_date)
    
    # Temporary print just to confirm
    print(f"Generating plan for {weeks} weeks...")

    # Placeholder for now
    return {"weeks": weeks, "plan": []}


def adjust_for_injuries(training_plan, injury_history):
    pass

def display_plan(training_plan):
    pass

if __name__ == "__main__":
    main(use_test_profile=True)  # Flip this when you're developing
