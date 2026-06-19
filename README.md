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
- 
## Future Roadmap & Planned Issues

### 1. Machine Learning & Predictive Modeling
* **Real Dataset Integration (`models/train_model.py`):** Replace the current template script with a robust data preprocessing and training pipeline. Target datasets include MMRTG power decay metrics, battery state-of-charge (SoC) profiles, and extreme external thermal fluctuations.
* **LSTM Architecture Optimization:** Implement sequential data formatting to handle multi-step ahead predictions for autonomous decision-making during the 14-day lunar night.

### 2. Simulation Engine Enhancements
* **Stochastic Environmental Fluctuations (`simulation/environment.py`):** Transition the simulation from a deterministic model to a stochastic one by introducing random variables for unpredictable surface events, sudden albedo variations, and solar radiation anomalies.
* **Multi-Agent Control Telemetry:** Expand the controllers to handle concurrent sub-system tasks, balancing payload heating priorities against critical communication link power reserves.

### 3. Code Quality & Infrastructure
* **CI/CD Integration:** Set up GitHub Actions to enforce automated testing for controller logic and static code analysis (`pylint`/`black`) across Python 3.9+.
* **Unit Testing:** Implement automated test suites for the rule-based and predictive controllers in `simulation/controllers.py` to ensure boundary-case safety compliance.
