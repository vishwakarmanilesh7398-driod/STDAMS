import time
import random
import csv
import os
import math # Wave ke liye zaroori hai
from datetime import datetime

DATA_FILE = 'data/satellite.csv'

# Base values
ALTITUDE_BASE = 400.0
VELOCITY_BASE = 7.8
SIGNAL_BASE = 90.0
counter = 0 # Time constant for waves

def generate_telemetry():
    global counter
    counter += 0.2 # Isse wave ki frequency control hogi

    # 1. Frequency/Wave Logic (Sine Wave)
    # Altitude 400 ke upar-neeche wave banayega
    altitude = ALTITUDE_BASE + (math.sin(counter) * 15) 
    # Velocity thoda alag frequency par chalega
    velocity = VELOCITY_BASE + (math.cos(counter * 0.5) * 0.2)
    # Signal strength random rahegi
    signal = SIGNAL_BASE + random.uniform(-2, 2)

    # 2. Inject Anomaly (Wahi purana logic)
    if random.random() < 0.15:
        event = random.choice(['drop', 'jam'])
        if event == 'drop':
            altitude -= 30 # Sudden drop in wave
        elif event == 'jam':
            signal -= 40

    return {
        'timestamp': datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + 'Z',
        'altitude': round(altitude, 2),
        'velocity': round(velocity, 2),
        'signal_strength': round(signal, 2),
        'proximity_km': round(random.uniform(50, 100), 2)
    }

def write_telemetry(row):
    file_exists = os.path.isfile(DATA_FILE)
    with open(DATA_FILE, 'a', newline='') as f:
        # Fieldnames updated with proximity_km
        fieldnames = ['timestamp', 'altitude', 'velocity', 'signal_strength', 'proximity_km']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

if __name__ == '__main__':
    # File saaf karke start karein taaki purana junk data na ho
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
        
    print('Starting STDAMS Telemetry Simulator...')
    while True:
        data = generate_telemetry()
        write_telemetry(data)
        print(f"Data Sent: Alt: {data['altitude']} | Signal: {data['signal_strength']} | Prox: {data['proximity_km']}")
        time.sleep(2) # Refresh rate fast