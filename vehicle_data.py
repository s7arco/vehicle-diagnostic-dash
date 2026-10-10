import random

def get_vehicle_data():
    vehicle_data = {
        "rpm": random.randint(600,3000),
        "speed": random.randint(0,100),
        "engine_load": random.randint(10,90),
        "coolant_temp": random.randint(75,100),
        "throttle_position": random.randint(0,100)
    } # Generates random values for vehicle info.

    return vehicle_data

print(get_vehicle_data(get_vehicle_data["rpm"]))