
def srpt_scheduling(processes):
    n = len(processes)

    remaining = [p[2] for p in processes]
    completion = [0] * n
    gantt = []

    time = 0
    completed = 0
    current_process = -1
    segment_start = 0

    while completed < n:
        available = [
            i for i in range(n)
            if processes[i][1] <= time and remaining[i] > 0
        ]

        if not available:
            if current_process != -1:
                gantt.append(
                    (current_process, segment_start, time)
                )
                current_process = -1

            time += 1
            continue

        # Select the process with the shortest remaining time
        selected = min(
            available,
            key=lambda i: (remaining[i], processes[i][1], i)
        )

        # Record a context switch in the Gantt chart
        if selected != current_process:
            if current_process != -1:
                gantt.append(
                    (current_process, segment_start, time)
                )

            current_process = selected
            segment_start = time

        remaining[selected] -= 1
        time += 1

        if remaining[selected] == 0:
            completion[selected] = time
            completed += 1

    if current_process != -1:
        gantt.append((current_process, segment_start, time))

    print("\nGantt Chart:")
    for pid, start, end in gantt:
        print(f"P{pid + 1} ({start}-{end})", end=" | ")

    print("\n\nProcess Results:")
    print("PID\tAT\tBT\tCT\tTAT\tWT")

    total_waiting = 0
    total_turnaround = 0

    for i in range(n):
        arrival = processes[i][1]
        burst = processes[i][2]

        turnaround = completion[i] - arrival
        waiting = turnaround - burst

        total_waiting += waiting
        total_turnaround += turnaround

        print(
            f"P{i + 1}\t{arrival}\t{burst}\t"
            f"{completion[i]}\t{turnaround}\t{waiting}"
        )

    print(f"\nAverage Waiting Time: {total_waiting / n:.2f}")
    print(f"Average Turnaround Time: {total_turnaround / n:.2f}")


def main():
    print("SRPT CPU Scheduling Algorithm")

    n = int(input("Enter number of processes: "))

    if n <= 0:
        print("Number of processes must be positive.")
        return

    processes = []

    for i in range(n):
        print(f"\nProcess P{i + 1}")
        arrival = int(input("Arrival Time: "))
        burst = int(input("Burst Time: "))

        if arrival < 0 or burst <= 0:
            print("Arrival must be >= 0 and burst must be > 0.")
            return

        processes.append((i + 1, arrival, burst))

    srpt_scheduling(processes)