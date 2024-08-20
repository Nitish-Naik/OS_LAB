"""
The Shortest Job First (SJF) scheduling algorithm is a non-preemptive CPU scheduling algorithm that selects the process with the smallest execution time (or burst time) to execute next. This approach minimizes the average waiting time for a set of processes.

Shortest Job First (SJF) Scheduling Algorithm
Objective: To execute processes based on their burst times, with the shortest burst time being executed first. This is a non-preemptive algorithm, meaning once a process starts executing, it runs to completion before the next one begins.

Key Concepts:
Non-Preemptive: Once a process starts, it runs to completion before the next process starts.
Optimal Average Waiting Time: SJF minimizes the average waiting time for a set of processes, making it optimal in that respect.
Requires Burst Time Knowledge: The burst time (the time required for execution) for each process needs to be known in advance.


Steps to Implement SJF:


Sort Processes by Arrival Time: Start by sorting processes based on their arrival times to handle them in the order they arrive.

Use a Queue to Manage Ready Processes: Maintain a queue of processes that are ready to execute.

Select the Process with the Shortest Burst Time: From the ready queue, pick the process with the shortest burst time to execute next.

Update Execution Times: Compute the start and finish times for each process based on its burst time.

Handle Idle Time: If no process is ready, advance the time to the arrival time of the next process.

"""


def sjf(processes):
    # Sort processes by arrival time initially
    processes.sort(key=lambda x: x[1])
    
    current_time = 0
    schedule = []
    waiting_queue = []

    while processes or waiting_queue:
        # Add processes that have arrived to the waiting queue
        while processes and processes[0][1] <= current_time:
            waiting_queue.append(processes.pop(0))
        
        # Sort the waiting queue by burst time
        waiting_queue.sort(key=lambda x: x[2])
        
        if waiting_queue:
            # Pick the process with the shortest burst time
            process_id, arrival_time, burst_time = waiting_queue.pop(0)
            start_time = current_time
            finish_time = start_time + burst_time
            schedule.append([process_id, start_time, finish_time])
            current_time = finish_time
        else:
            # No process is ready to run, jump to the next arrival time
            if processes:
                current_time = processes[0][1]
    
    print("Scheduled:", schedule)

# Read the number of processes
n = int(input("Enter the number of processes: "))
processes = []

# Collect process details
for i in range(n):
    inp = input(f"Enter process_id, arrival_time, burst_time for process {i + 1} (space separated): ")
    process_id, arrival_time, burst_time = inp.split()
    process_id = str(process_id)  # Keep process_id as a string
    arrival_time = int(arrival_time)
    burst_time = int(burst_time)
    processes.append((process_id, arrival_time, burst_time))

# Call the SJF scheduling function
sjf(processes)
