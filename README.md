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
## System Architecture & Control Loop

L.E.A.P. uses a closed-loop feedback mechanism to maintain the internal lunar lander temperature and prevent battery depletion during the 14-day lunar night simulation.

* **State Space Inputs:** Telemetry captures the current internal temperature ($T_{int}$), external environmental temperature ($T_{ext}$), Battery State-of-Charge ($SoC$), and active payload power draw.
* **Predictive Layer (LSTM):** Forecasts the next 6 to 12 hours of thermal stress and energy availability based on historical environmental patterns.
* **Control Execution:** The Rule-Based Controller balances power allocation between survival heaters and essential systems using the following threshold matrix:

| System State | Battery SoC Range | Thermal Condition | Controller Action |
| :--- | :--- | :--- | :--- |
| **Nominal** | $70\% - 100\%$ | $T_{int} \ge 15^\circ\text{C}$ | Full payload operations enabled; nominal heating active. |
| **Degraded** | $30\% - 70\%$ | $0^\circ\text{C} \le T_{int} < 15^\circ\text{C}$ | Non-essential payloads shed; pulse-width modulated heating. |
| **Critical** | $< 30\%$ | $T_{int} < 0^\circ\text{C}$ | Emergency power save mode; deep sleep with survival-only heating. |

---

## Technical Specifications & Mathematical Formulation

### 1. Thermal Equilibrium Model
The internal temperature dynamics are modeled using a simplified lumped-parameter thermal mass equation:

$$C_{th} \frac{dT_{int}}{dt} = Q_{gen} + Q_{heater} - \frac{T_{int} - T_{ext}}{R_{th}}$$

Where:
* $C_{th}$: Thermal capacitance of the lander core ($\text{J/K}$).
* $Q_{gen}$: Internal heat generation from active electronics ($\text{W}$).
* $Q_{heater}$: Heat injected by the survival heaters ($\text{W}$).
* $R_{th}$: Thermal resistance of the multi-layer insulation (MLI) shell ($\text{K/W}$).

### 2. Battery State-of-Charge (SoC) Dynamics
The battery capacity integrates net power consumption over time:

$$SoC(t + \Delta t) = SoC(t) - \frac{\int_{t}^{t+\Delta t} (P_{payload} + P_{heater} - P_{solar}) \, dt}{E_{max}} \times 100$$

Where:
* $E_{max}$: Total battery capacity ($\text{Wh}$).
* $P_{solar}$: Solar array output power ($\text{W}$), which drops to zero during the lunar night.

---

## Evaluation Metrics

To verify the performance of both rule-based and predictive models, the framework tracks three critical metrics:

* **Survival Window Time ($t_{surv}$):** The consecutive number of hours the system maintains $T_{int} > -20^\circ\text{C}$ without dropping $SoC$ below $10\%$.
* **Thermal Root Mean Squared Error (RMSE):** Evaluates LSTM prediction accuracy against actual simulated trajectories:
    $$RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (T_{pred, i} - T_{actual, i})^2}$$
* **Energy Efficiency Ratio (EER):** Ratio of total system utility achieved relative to total battery energy expended.
