import random
import time

# starting numbers
telemetry_state = {
    'altitude': 100.0,
    'latitude': 34.0522,
    'longitude': -118.2437,
    'speed': 15.0,
    'battery': 100.0,
}


def update_telemetry(state):

    # altitude drift
    state['altitude'] += random.uniform(-1.5, 1.5)
    state['altitude'] = max(0, min(500, state['altitude']))

    # speed drift
    state['speed'] += random.uniform(-0.5, 0.5)
    state['speed'] = max(0, min(60, state['speed']))

    # position drift
    state['latitude'] += random.uniform(-0.0001, 0.0001)
    state['longitude'] += random.uniform(-0.0001, 0.0001)

    # battery
    state['battery'] -= 0.02
    state['battery'] = max(0, state['battery'])

    return state


# flight loop
print("--- DRONE TELEMETRY STARTING ---")

while True:
    data = update_telemetry(telemetry_state)

    # print with formatting
    print(f"Altitude:  {data['altitude']:.1f}m")
    print(f"Latitude:  {data['latitude']:.6f}")
    print(f"Longitude: {data['longitude']:.6f}")
    print(f"Speed:     {data['speed']:.1f}m/s")
    print(f"Battery:   {data['battery']:.1f}%")
    print("----------------------------")

    time.sleep(1)
