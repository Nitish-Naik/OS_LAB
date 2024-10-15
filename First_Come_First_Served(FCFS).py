def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    # Initialize the current time
    current_time = 0
    # Calculate waiting time, turnaround time, and completion time
    for i in range(n):
        if current_time < processes[i]['arrival_time']:
            current_time = processes[i]['arrival_time']
        # Completion Time for the process
        completion_time[i] = current_time + processes[i]['burst_time']
        # Turnaround Time for the process
        turnaround_time[i] = completion_time[i] - processes[i]['arrival_time']
        # Waiting Time for the process
        waiting_time[i] = turnaround_time[i] - processes[i]['burst_time']
        # Update current time to the end of this process
        current_time = completion_time[i]
    # Calculate total waiting time and turnaround time
    total_wt = sum(waiting_time)
    total_tt = sum(turnaround_time)

    print("Process ID | Arrival Time | Burst Time | Completion Time(sum(BT)) | Turnaround Time(CT-AT) | Waiting Time(TAT-BT)")
    for i in range(n):
        print(f"{processes[i]['id']:>10} | {processes[i]['arrival_time']:>12} | {processes[i]['burst_time']:>10} | {completion_time[i]:>24} | {turnaround_time[i]:>22} | {waiting_time[i]:>15}")

    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tt / n:.2f}")

# Example usage with arrival times
processes = [
    {'id': 1, 'arrival_time': 0, 'burst_time': 6},
    {'id': 2, 'arrival_time': 1, 'burst_time': 8},
    {'id': 3, 'arrival_time': 2, 'burst_time': 7},
    {'id': 4, 'arrival_time': 3, 'burst_time': 3}
]

fcfs(processes)


# method 2 
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    start_time = 0
    schedule = []
    for process_id, arrival_time, burst_time in processes:
        start_time = max(start_time, arrival_time)
        finish_time = start_time + burst_time
        schedule.append((process_id, start_time, finish_time))
        start_time = finish_time
    return schedule

# Example usage
processes = [(1, 0, 3), (2, 2, 6), (3, 4, 4)]
schedule = fcfs_scheduling(processes)
print("FCFS Schedule:", schedule)








def fcfs(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda x: x[1])

    start_time = 0
    schedule = []

    for process_id, arrival_time, burst_time in processes:
        # Determine the start time for the process
        start_time = max(start_time, arrival_time)
        # Calculate finish time
        finish_time = start_time + burst_time
        # Append process details to the schedule
        schedule.append([process_id, start_time, finish_time])
        # Update start time for the next process
        start_time = finish_time

    print("Scheduled:", schedule)
        
# Read the number of processes
n = int(input("Enter the number of processes: "))
processes = []

# Collect process details
for i in range(n):
    inp = input(f"Enter process_id, arrival_time, burst_time for process {i + 1} (space separated): ")
    process_id, arrival_time, burst_time = inp.split()
    arrival_time = int(arrival_time)
    burst_time = int(burst_time)
    process = (process_id, arrival_time, burst_time)
    # Add the process to the list
    processes.append(process)

# Call the FCFS scheduling function
fcfs(processes)
