import hashlib
import json
from datetime import datetime
import os

LOG_FILE = "secure_log.json"

def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as f:
        return json.load(f)
    
def save_logs(logs):
    with open(LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=4)

def add_log(event, description):
    logs = load_logs()

    index = len(logs) + 1
    timestamp = str(datetime.now())

    previous_hash = logs[-1]["current_hash"] if logs else "0"

    data = f"{index}{timestamp}{event}{description}{previous_hash}"
    current_hash = calculate_hash(data)

    log_entry = {
        "index": index,
        "timestamp": timestamp,
        "event": event,
        "description": description,
        "previous_hash": previous_hash,
        "current_hash": current_hash
    }

    logs.append(log_entry)
    save_logs(logs)

    print("Log added successfully!")

def verify_logs():
    logs = load_logs()

    for i in range(len(logs)):
        log = logs[i]

        expected_prev_hash = logs[i-1]["current_hash"] if i > 0 else "0"

        data = f"{log['index']}{log['timestamp']}{log['event']}{log['description']}{log['previous_hash']}"
        recalculated_hash = calculate_hash(data)

        if log["previous_hash"] != expected_prev_hash:
            print(f"Tampering detected at log {i+1} (Previous hash mismatch)")
            return

        if log["current_hash"] != recalculated_hash:
            print(f"Tampering detected at log {i+1} (Hash mismatch)")
            return

    print("All logs are valid. No tampering detected.")

while True:
    print("\n1. Add Log")
    print("2. Verify Logs")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        event = input("Enter event type: ")
        desc = input("Enter description: ")
        add_log(event, desc)

    elif choice == "2":
        verify_logs()

    elif choice == "3":
        break

    else:
        print("Invalid choice")