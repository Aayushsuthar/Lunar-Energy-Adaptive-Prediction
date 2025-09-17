# simulation/controllers.py

class ReactiveController:
    """A simple, reactive thermostat that turns on a powerful heater
    only when a critical temperature is breached."""
    def __init__(self, critical_temp_c=-40.0):
        self.CRITICAL_TEMP_C = critical_temp_c
        self.HEATER_POWER_KW = 0.5

    def decide(self, internal_temp_c):
        if internal_temp_c < self.CRITICAL_TEMP_C:
            return self.HEATER_POWER_KW, "REACTIVE HEATING"
        return 0.0, "IDLE"

class PredictiveController:
    """A lightweight predictive-style controller (demo)."""
    def __init__(self, critical_temp_c=-40.0, safe_temp_c=10.0):
        self.CRITICAL_TEMP_C = critical_temp_c
        self.SAFE_TEMP_C = safe_temp_c
        self.HEATER_POWER_KW = 0.2

    def decide(self, internal_temp_c):
        # Basic simulated prediction: assume a drop of 15C ahead
        predicted_future_temp = internal_temp_c - 15
        if predicted_future_temp < self.CRITICAL_TEMP_C and internal_temp_c < self.SAFE_TEMP_C:
            return self.HEATER_POWER_KW, "PROACTIVE HEAT"
        return 0.0, "OPTIMIZED STANDBY"
