# Dojo: Adaptive, Injury-Preventive Half Marathon Trainer

**Dojo** is a half marathon training app focused on mindful, adaptive training.

The goal is to reduce the risk of overuse injuries—which are especially common in novice runners—by generating personalized training plans that adjust dynamically based on:

- **Injury status**
- **Weekly energy levels**

Beginner runners are particularly vulnerable to injuries such as shin splints, often caused by rapid increases in training volume or intensity. Dojo helps runners build up gradually and safely by tailoring their training to how their body feels each week.

The user interface is currently being developed using the **Kivy** framework in Python.

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
- Injury status  
- Energy level for the current week  

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
- Cut back every 4th week by ~20% (recovery week)  
- Taper in final 2 weeks (reduce mileage by 30–50%)  

---

## References 

1. **Hal Higdon Half Marathon Novice 1 Plan**  
   A 12-week beginner plan featuring 3–4 runs per week, rest days, cross-training, and gradual long-run progression.  
   https://www.halhigdon.com/training-programs/half-marathon-training/novice-1-half-marathon/

2. **Santos-Lozano et al., 2020 – Predicting Race Performance in Recreational Half-Marathon Runners**  
   Found that training volume, longest run distance, and training duration significantly affect race outcomes.  
   https://pubmed.ncbi.nlm.nih.gov/32421886/

3. **Videbæk et al., 2015 – Incidence of Running-Related Injuries in Different Types of Runners: A Systematic Review and Meta-Analysis**  
   Novice runners have a higher injury rate compared to recreational and experienced runners.  
   https://bjsm.bmj.com/content/49/8/511
