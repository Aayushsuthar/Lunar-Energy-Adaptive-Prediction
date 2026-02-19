# Project L.E.A.P. (Lunar Energy Autonomous Platform)
ASTRA 2025 Hackathon Submission by Team "The Night Watchers"

## Overview
Project L.E.A.P. is a simulation & predictive controller prototype built to demonstrate autonomous thermal and power management for lunar night survival.

## How to run locally
1. Create and activate a virtual environment (recommended).
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit UI:
   ```
   streamlit run app.py
   ```


## Project structure
├── models/
│   └── train_model.py
├── simulation/
│   ├── controllers.py
│   └── environment.py
├── app.py
├── README.md
└── requirements.txt

## Notes
- The `models/train_model.py` is a template that requires a real dataset to train an LSTM.
- This prototype is deterministic and designed for demo/hackathon use.
