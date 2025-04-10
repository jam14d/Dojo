# Dojo: Training Plan App

## Goal

_Dojo_ is a half marathon training app being built in Python. It's designed for runners like me who want to train smarter—not harder.

I'm working to generate a personalized training plan that adjusts the training schedule based on:

- Injury status (starting with shin splints)
- Weekly energy levels

The initial version will run as a script. Future versions may include a GUI or web interface.

---

## Phase 1: Core Functionality 

### User Inputs

- Target race date
- Current weekly mileage or running experience
- Days per week available to run
- Injury status (yes/no for shin splints)
- Energy level for the current week (low / normal / high)

### Training Plan Generator

- Base 12-week half marathon plan structure
- Gradual weekly mileage increase with cutback weeks and tapering

**Adjustments based on user input:**

**Shin splints:**
- Reduce mileage and/or intensity
- Increase rest days
- Optionally substitute cross-training


**Low energy week:**
- Decrease volume
- Replace some runs with easy runs or rest

### Output

- Display weekly or daily schedule in terminal
- Optionally save to a `.txt` or `.csv` file

### Python Features to Use

- `datetime` module for calculating weeks
- Lists/dictionaries for schedule management
- Conditional logic for plan adjustments
- File writing for exporting plans

---

## Phase 2: Enhanced Features

- Include pace recommendations based on user input (e.g., recent race times)
- Track persistent injuries and suggest rest if not improving
- Save and reload user data or training progress

---

## Phase 3: Interface Development

Once the logic is solid, explore building a user interface:

- Desktop GUI using Tkinter
- Web interface using Flask or FastAPI
- (Advanced/future) Mobile app using React Native, Flutter, or Swift

---

 ## Baseline Training Structure (According to Refs)
 - Start at 10–15 miles/week (beginner level)
 - Increase mileage by ~10% each week
 - Cutback every 4th week by ~20% (recovery week)
 - Taper in final 2 weeks (reduce mileage by 30–50%)

---
## References 

1. **Hal Higdon Half Marathon Novice 1 Plan**  
   A 12-week beginner plan designed for new runners, featuring 3–4 runs per week, rest days, cross-training, and a gradual build-up of long runs.  
   https://www.halhigdon.com/training-programs/half-marathon-training/novice-1-half-marathon/

2. **Santos-Lozano et al., 2020 – Predicting Race Performance in Recreational Half-Marathon Runners**  
   Found that training volume, longest run distance, and training duration significantly affect race outcomes.  
   https://pubmed.ncbi.nlm.nih.gov/32421886/
