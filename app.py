import streamlit as st
from vehicle_data import get_vehicle_data

st.title("Vehicle Diagnostics Dashboard")

@st.fragment(run_every=1) #reruns the live_dash function every 1 second
def live_dash():
    data = get_vehicle_data()

    st.write("Driving State:", data["state"].capitalize())
    col1, col2, col3 = st.columns(3) # Create 3 colums
    col1.metric("Engine RPM", f"{data['rpm']} RPM") # Displays RPM as metric
    col2.metric("Speed", f"{data['speed']} mph")
    col3.metric("Coolant Temperature", f"{data['coolant_temp']} °C")

    col4, col5 = st.columns(2)
    col4.metric("Engine Load", f"{data['engine_load']} %")
    col5.metric("Throttle Position", f"{data['throttle_position']} %")

live_dash()