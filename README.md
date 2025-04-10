# Dojo: Training Plan App

## Goal

Dojo is a half marathon training app focused on mindful, adaptive training.

It generates personalized training plans that dynamically adjust based on:

- Injury status
- Weekly energy levels

The user interface is currently being developed with the Kivy framework in Python.

---
## Environment Setup

```bash
python3 -m venv dojo-kivy
source dojo-kivy/bin/activate
```
---

## Core Functionality 

### User Inputs

- Target race date
- Current weekly mileage or running experience
- Days per week available to run
- Injury status (yes/no for shin splints)
- Energy level for the current week (low / normal / high)

### Training Plan Generator

- Base 12-week half marathon plan structure
- Gradual weekly mileage increase with cutback weeks and tapering

#### Adjustments based on user input:

**Shin splints:**
- Reduce mileage and/or intensity
- Increase rest days
- Optionally substitute cross-training


**Low energy week:**
- Decrease volume
- Replace some runs with easy runs or rest

### Output

- Display a weekly training schedule 

---

 ## Baseline Training Structure 
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
