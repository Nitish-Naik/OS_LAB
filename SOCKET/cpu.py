def rr(p, bt, q):
    n, rem_bt, wt, tat, ct, rt, t = len(p), bt[:], [0]*n, [0]*n, [0]*n, [-1]*n, 0
    gantt = []
    while any(rem_bt):
        for i in range(n):
            if rem_bt[i] > 0:
                if rt[i] == -1: rt[i] = t
                exec_time = min(rem_bt[i], q)
                t += exec_time
                rem_bt[i] -= exec_time
                gantt.append((p[i], t))
                if rem_bt[i] == 0: ct[i], tat[i], wt[i] = t, t, t - bt[i]
    return p, wt, tat, ct, rt, gantt

# Input
p, bt, q = ['P1', 'P2', 'P3', 'P4'], [10, 5, 8, 6], 3
p, wt, tat, ct, rt, gantt = rr(p, bt, q)

# Output
print("P\tBT\tWT\tTAT\tCT\tRT")
for i in range(len(p)): print(f"{p[i]}\t{bt[i]}\t{wt[i]}\t{tat[i]}\t{ct[i]}\t{rt[i]}")

# Gantt Chart
print("\nGantt Chart:")
for g in gantt: print(f"| {g[0]} ", end="")
print("|\n0", end="")
for g in gantt: print(f"   {g[1]}", end="")





































def sjf(p, bt):
    n, wt, tat, ct, rt = len(p), [0]*len(p), [0]*len(p), [0]*len(p), [0]*len(p)
    p, bt = zip(*sorted(zip(p, bt), key=lambda x: x[1]))  # Sort by burst time
    for i in range(1, n): 
        wt[i] = wt[i-1] + bt[i-1]  # Calculate waiting time
    for i in range(n): 
        tat[i] = wt[i] + bt[i]      # Calculate turnaround time
        ct[i] = tat[i]              # Completion time is same as TAT for non-preemptive SJF
        rt[i] = wt[i]               # Response time is same as waiting time in non-preemptive scheduling
    return p, wt, tat, ct, rt

# Input
p, bt = ['P1', 'P2', 'P3', 'P4'], [6, 2, 8, 3]
p, wt, tat, ct, rt = sjf(p, bt)

# Output
print("P\tBT\tWT\tTAT\tCT\tRT")
for i in range(len(p)): 
    print(f"{p[i]}\t{bt[i]}\t{wt[i]}\t{tat[i]}\t{ct[i]}\t{rt[i]}")

# Gantt Chart
print("\nGantt Chart:")
time = 0
for i in range(len(p)): 
    time += bt[i]
    print(f"| {p[i]} ", end="")
print(f"|\n0", end="")

time = 0
for i in range(len(p)): 
    time += bt[i]
    print(f"   {time}", end="")































































# Function to implement FCFS scheduling
def fcfs_scheduling(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Waiting time calculation
    for i in range(1, n):
        waiting_time[i] = burst_time[i-1] + waiting_time[i-1]

    # Turnaround time calculation
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    return waiting_time, turnaround_time

# Function to display Gantt chart in text format
def gantt_chart(processes, burst_time):
    print("\nGantt Chart:")
    print("|", end="")
    
    start_time = 0
    for i in range(len(processes)):
        # Print process execution as part of the Gantt chart
        print(f" {processes[i]} |", end="")
        start_time += burst_time[i]
    
    # Print the time line
    print("\n0", end="")
    start_time = 0
    for i in range(len(processes)):
        start_time += burst_time[i]
        print(f"   {start_time}", end="")

# Input: Process names and burst times
processes = ['P1', 'P2', 'P3', 'P4']
burst_time = [5, 3, 8, 6]

# Call the FCFS scheduling function
waiting_time, turnaround_time = fcfs_scheduling(processes, burst_time)

# Output waiting and turnaround times
print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(len(processes)):
    print(f"{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

# Display Gantt chart
gantt_chart(processes, burst_time)
