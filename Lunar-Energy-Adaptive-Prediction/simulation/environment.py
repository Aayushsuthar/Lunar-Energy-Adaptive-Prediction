# simulation/environment.py
class LunarAsset:
    """Simulates the physical state (power and thermal) of a lunar asset."""
    def __init__(self, initial_battery_kwh=10.0, initial_temp_c=20.0):
        # Constants
        self.MMRTG_POWER_KW = 0.110
        self.MMRTG_HEAT_KW = 2.0
        self.MAX_BATTERY_KWH = initial_battery_kwh
        self.AMBIENT_DAY_TEMP = 120.0
        self.AMBIENT_NIGHT_TEMP = -173.0

        # State
        self.battery_kwh = initial_battery_kwh
        self.internal_temp_c = initial_temp_c

    def update_state(self, hour, hours_per_step, heater_power_kw):
        """Updates the asset's state over a single time step."""
        lunar_day_hours = 24 * 14.75
        is_day = (hour % (lunar_day_hours * 2)) < lunar_day_hours
        ambient_temp = self.AMBIENT_DAY_TEMP if is_day else self.AMBIENT_NIGHT_TEMP

        # Power update
        base_load_kw = 0.05
        total_power_draw_kw = heater_power_kw + base_load_kw
        net_power_kw = self.MMRTG_POWER_KW - total_power_draw_kw
        self.battery_kwh += net_power_kw * hours_per_step
        # clamp
        self.battery_kwh = max(0.0, min(self.MAX_BATTERY_KWH, self.battery_kwh))

        # Thermal update (very simplified)
        thermal_loss = (self.internal_temp_c - ambient_temp) * 0.01
        thermal_gain_from_heat_pipes = self.MMRTG_HEAT_KW * 0.1
        self.internal_temp_c += (thermal_gain_from_heat_pipes - thermal_loss) * 0.1
        self.internal_temp_c = max(-200, min(150, self.internal_temp_c))

        return {
            'battery_percent': (self.battery_kwh / self.MAX_BATTERY_KWH) * 100,
            'internal_temp_c': self.internal_temp_c
        }
