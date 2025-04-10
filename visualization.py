import matplotlib.pyplot as plt

def adjust_miles(m, adjust):
    return round(m * 0.5, 1) if isinstance(m, (int, float)) and adjust else 0 if isinstance(m, str) else m

def plot_week_range_mileage(plan, week_range=None, adjust=False):
    data = plan if week_range is None else [w for w in plan if week_range[0] <= w["week"] <= week_range[1]]
    rows = len(data)

    fig, axs = plt.subplots(rows, 1, figsize=(8, 4 * rows))
    axs = [axs] if rows == 1 else axs

    for ax, week in zip(axs, data):
        days = ["tue", "wed", "thu", "sun"]
        miles = [adjust_miles(week.get(d), adjust) for d in days]
        ax.bar([d.capitalize() for d in days], miles)
        ax.set_title(f"Week {week['week']}")
        ax.set_ylim(0, max(miles) + 2)

    plt.tight_layout()
    plt.show()
