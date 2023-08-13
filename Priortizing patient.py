import heapq
import time

class Patient:
    def __init__(self, name, priority, treatment_time):
        self.name = name
        self.priority = priority
        self.treatment_time = treatment_time

# Priority queue to simulate patient arrivals
patient_queue = []

# Simulated patient arrivals (name, priority, treatment_time)
patients = [
    Patient("Patient A", 2, 20),
    Patient("Patient B", 1, 30),
    Patient("Patient C", 3, 15),
    # Add more patient arrivals as needed
]

# Add patients to the priority queue
for patient in patients:
    heapq.heappush(patient_queue, (patient.priority, patient))

# Simulate resource allocation and treatment
while patient_queue:
    _, patient = heapq.heappop(patient_queue)
    print(f"Treating {patient.name} (Priority: {patient.priority})")
    time.sleep(patient.treatment_time)
    print(f"{patient.name} treatment complete")

print("All patients treated.")
