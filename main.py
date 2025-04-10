from training_data import training_plan
from visualization import plot_week_range_mileage

def adjust_mileage(miles, adjust):
    if isinstance(miles, (int, float)) and adjust:
        return round(miles * 0.5, 1)
    return miles

def print_plan(adjust=False):
    for week in training_plan:
        print(f"Week {week['week']}:")
        for day in ["tue", "wed", "thu", "sun"]:
            miles = adjust_mileage(week.get(day), adjust)
            print(f"  {day.capitalize()}: {miles} mi")
        print()

def get_range():
    kind = input("View a week, range, or all? (single/range/all): ").strip().lower()
    if kind == "all":
        return None
    if kind == "range":
        start = int(input("Start week: "))
        end = int(input("End week: "))
        return (start, end)
    if kind == "single":
        week = int(input("Week: "))
        return (week, week)
    return get_range()

if __name__ == "__main__":
    adjust = input("Shin splints? (yes/no): ").strip().lower() == "yes"
    print_plan(adjust)

    show = input("Visualize? (yes/no): ").strip().lower() == "yes"
    if show:
        week_range = get_range()
        plot_week_range_mileage(training_plan, week_range, adjust)
