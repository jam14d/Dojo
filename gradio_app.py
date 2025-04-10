import gradio as gr
from datetime import datetime
import re

def process_user_input(name, race_date, mileage, level, injuries, preferred_days):
    # Clean up input values
    try:
        race_date = datetime.strptime(race_date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    try:
        mileage = float(mileage)
    except ValueError:
        return "Mileage must be a number."

    
    injury_list = [inj.strip().lower() for inj in injuries.split(",")] if injuries.lower() != 'none' else []
    preferred_day_list = [day.strip().capitalize() for day in preferred_days.split(",")]

    user_profile = {
        "name": name,
        "race_date": race_date.strftime("%Y-%m-%d"),
        "weekly_mileage": mileage,
        "level": level.lower(),
        "injuries": injury_list,
        "preferred_days": preferred_day_list
    }

    return user_profile

# Gradio UI
inputs = [
    gr.Textbox(label="Name"),
    gr.Textbox(label="Race Date (YYYY-MM-DD)"),
    gr.Textbox(label="Current Weekly Mileage"),
    gr.Radio(choices=["beginner", "intermediate", "advanced"], label="Experience Level"),
    gr.Textbox(label="Injuries (comma-separated or type 'none')"),
    gr.Textbox(label="Preferred Run Days (comma-separated, e.g. Mon,Wed,Fri)")
]


output = gr.JSON(label="Parsed User Profile")

app = gr.Interface(fn=process_user_input, inputs=inputs, outputs=output, title="Dojo Training Planner")

app.launch()
