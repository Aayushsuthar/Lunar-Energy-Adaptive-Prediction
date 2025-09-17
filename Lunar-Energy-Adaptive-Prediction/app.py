import streamlit as st
import plotly.graph_objects as go
from simulation.environment import LunarAsset
from simulation.controllers import ReactiveController, PredictiveController

def run_full_simulation(controller, initial_battery_kwh=10.0, hours_per_step=12):
    asset = LunarAsset(initial_battery_kwh=initial_battery_kwh)
    history = {'hour': [], 'battery': [], 'temp': []}
    total_sim_hours = int(24 * 14.75 * 2)  # two lunar cycles ~28 days
    for hour in range(0, total_sim_hours, hours_per_step):
        heater_power, mode = controller.decide(asset.internal_temp_c)
        state = asset.update_state(hour, hours_per_step, heater_power)
        history['hour'].append(hour)
        history['battery'].append(state['battery_percent'])
        history['temp'].append(state['internal_temp_c'])
    return history

st.set_page_config(page_title="Project L.E.A.P. Dashboard", layout="wide")
st.title("🚀 Project L.E.A.P. - Lunar Night Survival Simulation")
st.markdown("**Team: The Night Watchers**")

st.sidebar.header("Simulation settings")
initial_batt = st.sidebar.number_input("Initial battery (kWh)", value=10.0, min_value=1.0, step=1.0)
step_hours = st.sidebar.selectbox("Hours per simulation step", options=[1, 6, 12, 24], index=2)

if st.button("▶️ Run Simulation"):
    with st.spinner("Simulating..."):
        control_history = run_full_simulation(ReactiveController(), initial_battery_kwh=initial_batt, hours_per_step=step_hours)
        leap_history = run_full_simulation(PredictiveController(), initial_battery_kwh=initial_batt, hours_per_step=step_hours)

    st.success("✅ Simulation Complete!")

    col1, col2 = st.columns(2)
    with col1:
        st.header("Control Case (Reactive)")
        final_bat_control = control_history['battery'][-1]
        st.metric(label="Final Battery Reserve", value=f"{final_bat_control:.1f}%")
        if final_bat_control < 10:
            st.error("Status: CRITICAL POWER FAILURE")
        else:
            st.warning("Status: SURVIVAL MARGIN LOW")

    with col2:
        st.header("Project L.E.A.P. (Predictive)")
        final_bat_leap = leap_history['battery'][-1]
        st.metric(label="Final Battery Reserve", value=f"{final_bat_leap:.1f}%")
        st.success("Status: NOMINAL SURVIVAL")

    st.markdown("---")
    st.header("Performance Comparison Over Time")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=control_history['hour'], y=control_history['battery'], mode='lines', name='Control Case Battery'))
    fig.add_trace(go.Scatter(x=leap_history['hour'], y=leap_history['battery'], mode='lines', name='L.E.A.P. System Battery'))
    fig.update_layout(title='Battery State of Charge (%)', xaxis_title='Mission Hour', yaxis_title='Battery %')
    st.plotly_chart(fig, use_container_width=True)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=control_history['hour'], y=control_history['temp'], mode='lines', name='Control Case Temperature'))
    fig2.add_trace(go.Scatter(x=leap_history['hour'], y=leap_history['temp'], mode='lines', name='L.E.A.P. System Temperature'))
    fig2.add_hline(y=-40.0, line_dash='dot', annotation_text='Critical Temp')
    fig2.update_layout(title='Internal System Temperature (°C)', xaxis_title='Mission Hour', yaxis_title='Temperature °C')
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")
    st.write("**Notes:** This is a demonstrative simulator. For higher-fidelity results, increase resolution (smaller step size) and/or integrate trained predictive model from `models/train_model.py`.")
