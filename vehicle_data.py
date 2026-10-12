import random

vehicle_data = {
    "rpm": 800,
    "speed": 0,
    "coolant_temp": 80,
    "engine_load": 20,
    "throttle_position": 0,
    "state": "idle",
    "state_timer": 0
}

def set_vehicle_state():
     
    # Stays idle for 5 seconds before accelerating
    if vehicle_data["state"] == "idle":
        if vehicle_data["state_timer"] >= 5:
            vehicle_data["state"] = "accelerating"
            vehicle_data["state_timer"] = 0
    
    # Accelerates until it reaches 40mph
    elif vehicle_data["state"] == "accelerating":
        if vehicle_data["speed"] >= 40:
            vehicle_data["state"] = "cruising"
            vehicle_data["state_timer"] = 0

    # Cruises for 8 seconds and starts slowing
    elif vehicle_data["state"] == "cruising":
        if vehicle_data["state_timer"] >= 8:
            vehicle_data["state"] = "slowing"
            vehicle_data["state_timer"] = 0

    # Slows down until 0mph then idles
    elif vehicle_data["state"] == "slowing":
        if vehicle_data["speed"] <= 0:
            vehicle_data["speed"] = 0
            vehicle_data["state"] = "idle"
            vehicle_data["state_timer"] = 0


def get_vehicle_data():

    # Increase the amount of time spent in the current state
    vehicle_data["state_timer"] += 1

    set_vehicle_state()

    if vehicle_data["state"] == "idle":
        vehicle_data["speed"] = 0
        vehicle_data["rpm"] = 800
        vehicle_data["throttle_position"] = 0
        vehicle_data["engine_load"] = 20

    elif vehicle_data["state"] == "accelerating":
        vehicle_data["speed"] += random.randint(1, 4)
        vehicle_data["rpm"] += random.randint(100, 250)
        vehicle_data["throttle_position"] = random.randint(50, 80)
        vehicle_data["engine_load"] = random.randint(60, 90)

    elif vehicle_data["state"] == "cruising":
        vehicle_data["speed"] += random.randint(-1, 1)
        vehicle_data["rpm"] += random.randint(-50, 50)
        vehicle_data["throttle_position"] = random.randint(20, 40)
        vehicle_data["engine_load"] = random.randint(30, 50)

    elif vehicle_data["state"] == "slowing":
        vehicle_data["speed"] -= random.randint(1, 4)
        vehicle_data["rpm"] -= random.randint(50, 150)
        vehicle_data["throttle_position"] = random.randint(0, 15)
        vehicle_data["engine_load"] = random.randint(10, 30)

        if vehicle_data["speed"] <=0:
            vehicle_data["speed"] = 0
            vehicle_data["state"] = 'idle'
            vehicle_data["state_timer"] = 0
 

    # Simulate small coolant temperature changes
    vehicle_data["coolant_temp"] += random.randint(-1, 1)

    # Prevent impossible values
    if vehicle_data["rpm"] < 800:
        vehicle_data["rpm"] = 800

    if vehicle_data["speed"] < 0:
        vehicle_data["speed"] = 0

    if vehicle_data["throttle_position"] < 0:
        vehicle_data["throttle_position"] = 0

    if vehicle_data["throttle_position"] > 100:
        vehicle_data["throttle_position"] = 100

    if vehicle_data["engine_load"] < 0:
        vehicle_data["engine_load"] = 0

    if vehicle_data["engine_load"] > 100:
        vehicle_data["engine_load"] = 100


    return vehicle_data