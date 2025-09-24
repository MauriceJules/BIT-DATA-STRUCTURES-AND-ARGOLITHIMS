import numpy as np

# Sample data for the Ambulance Dispatch Log
dispatch_log = [
    {"id": 1, "name": "Station 1", "value": 45},
    {"id": 2, "name": "Station 2", "value": 60},
    {"id": 3, "name": "Station 3", "value": 30},
    {"id": 4, "name": "Station 4", "value": 75},
    {"id": 5, "name": "Station 5", "value": 50}
]

# Integers - Compute total, average, minimum, and maximum values
values = [entry['value'] for entry in dispatch_log]
total = sum(values)
average = np.mean(values)
minimum = np.min(values)
maximum = np.max(values)

# Strings - Create a formatted string report
report = f"Ambulance Dispatch Log Summary:\nTotal: {total}\nAverage: {average:.2f}\nMinimum: {minimum}\nMaximum: {maximum}"

# Booleans - Apply a threshold condition
threshold = 50
average_status = "Above Standard" if average > threshold else "Below Standard"

# Lists - Maintain a list of items and sort them
sorted_dispatch_log = sorted(dispatch_log, key=lambda x: x['value'])

# Arrays - Using numpy to create an array and compute sum
array_values = np.array(values)
array_sum = np.sum(array_values)

# Dictionaries - Update and delete records
dispatch_log[2]['value'] = 55  # Updating the record for Station 3
del dispatch_log[4]  # Deleting the record for Station 5

# Compute the 'value' field across records
value_sum = sum([entry['value'] for entry in dispatch_log])

# Displaying the results
print(report)
print(f"Average status: {average_status}")
print(f"Sorted Dispatch Log: {sorted_dispatch_log}")
print(f"Array Sum: {array_sum}")
print(f"Updated Dispatch Log: {dispatch_log}")
print(f"Total 'value' sum after update: {value_sum}")
