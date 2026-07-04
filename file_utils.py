import json
from datetime import datetime

history_file = "history.json"

"""
New Angular .py functions
Functions Dedicated to Touching Files
"""
def load_history():
    try:
        with open(history_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Warning: {history_file} contains invalid JSON. Resetting history.")
        return []
    
def save_history(history):
    with open(history_file, "w") as file:
        json.dump(history, file, indent=4)


def log_history(algorithm, inputs, result, timestamp):
    history = load_history()

    if isinstance(timestamp, datetime):
        timestamp = timestamp.isoformat()

    history.append({
        "algorithm": algorithm,
        "inputs": inputs,
        "result": result,
        "timestamp": timestamp
    })

    save_history(history)


def print_history():
    history = load_history()

    if not history:
        print("No history found.")
        return

    print("=" * 40)
    print("\tHISTORY")
    print("=" * 40)
    for entry in history:
        print(json.dumps(entry, indent=4))
        print("-" * 40)


if __name__ == "__main__":
    log_history()

# """
# Legary CLI Functions
# Functions Dedicated to Touching Files
# """        
# def save_results(
#         user_name,
#         algorithm,
#         result):

#     with open(
#             "results.txt",
#             "a") as file:

#         timestamp = datetime.now()

#         file.write(
#             f"Date: {timestamp} | "
#             f"User: {user_name} | "
#             f"Algo: {algorithm} | "
#             f"Result: {result}\n"
#         )

# def read_results():
#     file = open("results.txt", "r")
#     print("=" * 40)
#     print("\t\tHISTORY")
#     print("=" * 40)
#     for line in file:
#         print(line.strip())
           
#     file.close()

# def return_latest():
#     file = open("results.txt", "r")
#     latest_entry = file.readlines()
#     print("=" * 30)
#     print("\tLATEST ENTRY...")
#     print("=" * 30)
#     if latest_entry:
#         print(latest_entry[-1].strip())
#     else:
#         print("No history found.")