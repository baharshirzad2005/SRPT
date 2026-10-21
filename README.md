

# 1. Introduction

CPU scheduling is an important function of an operating system. It determines which process or task should use the CPU at a particular time.

Different scheduling algorithms use different rules to select processes. Some algorithms focus on reducing waiting time, while others focus on meeting deadlines in real-time systems.

This report compares three scheduling algorithms: Shortest Remaining Processing Time (SRPT), Rate Monotonic (RM), and Earliest Deadline First (EDF).

# 2. SRPT Scheduling Algorithm

## 2.1 Definition

SRPT stands for Shortest Remaining Processing Time. It is a preemptive scheduling algorithm that selects the process with the shortest remaining execution time.

If a new process arrives with a shorter remaining processing time than the currently running process, the CPU can interrupt the current process and execute the new one.

## 2.2 How SRPT Works

1. Check which processes have arrived.
2. Calculate the remaining execution time of each available process.
3. Select the process with the shortest remaining time.
4. Execute the selected process.
5. Reconsider the selection when a new process arrives or the current process finishes.
6. Continue until all processes are completed.

## 2.3 Advantages of SRPT

* It can minimize average turnaround time when processing requirements are known.
* Short processes can finish quickly.
* It adapts to the arrival of new processes.

## 2.4 Disadvantages of SRPT

* Long processes may experience starvation.
* The remaining processing time must be known or estimated.
* Frequent preemption can increase context-switching overhead.

# 3. Rate Monotonic Scheduling (RM)

## 3.1 Definition

Rate Monotonic (RM) is a fixed-priority scheduling algorithm commonly used for periodic tasks in real-time systems.

In RM, tasks with shorter periods receive higher priorities. Priorities remain fixed during execution.

## 3.2 How RM Works

1. Identify the period of each periodic task.
2. Assign higher priority to the task with the shorter period.
3. Execute the highest-priority ready task.
4. Preempt a lower-priority task if a higher-priority task becomes ready.
5. Repeat the scheduling process.

## 3.3 Advantages of RM

* It is relatively simple to implement.
* Task priorities are fixed and predictable.
* It is suitable for many periodic real-time systems.

## 3.4 Disadvantages of RM

* A task with a longer period receives lower priority.
* Some task sets may miss their deadlines.
* Under standard assumptions, its utilization bound can be lower than EDF's.

# 4. Earliest Deadline First Scheduling (EDF)

## 4.1 Definition

Earliest Deadline First (EDF) is a dynamic-priority scheduling algorithm used in real-time systems.

EDF selects the ready task whose absolute deadline is closest. A task with an earlier deadline receives priority over a task with a later deadline.

## 4.2 How EDF Works

1. Identify all ready tasks.
2. Determine the absolute deadline of each ready task.
3. Select the task with the earliest deadline.
4. Execute that task.
5. Reconsider the selection when necessary.
6. Continue until the tasks finish or their deadlines are reached.

## 4.3 Advantages of EDF

* Priorities change according to task deadlines.
* It can achieve high processor utilization.
* Under ideal preemptive uniprocessor assumptions, EDF can schedule a feasible task set when total utilization does not exceed 100%.

## 4.4 Disadvantages of EDF

* Dynamic priority management can be more complex than RM.
* Overload can cause multiple deadline misses.
* Scheduling decisions require deadline information.

# 5. Comparison Table

| Feature          | SRPT                               | RM                                               | EDF                                          |
| ---------------- | ---------------------------------- | ------------------------------------------------ | -------------------------------------------- |
| Full name        | Shortest Remaining Processing Time | Rate Monotonic                                   | Earliest Deadline First                      |
| Priority basis   | Remaining execution time           | Task period                                      | Absolute deadline                            |
| Priority type    | Dynamic                            | Fixed                                            | Dynamic                                      |
| Preemptive       | Yes                                | Usually yes                                      | Usually yes                                  |
| Main application | General process scheduling         | Real-time periodic tasks                         | Real-time tasks                              |
| Main objective   | Reduce turnaround time             | Meet periodic task deadlines                     | Meet task deadlines                          |
| Starvation       | Possible                           | Possible for lower-priority tasks under overload | Not inherent under feasible ideal conditions |
| Complexity       | Moderate                           | Relatively simple                                | Moderate                                     |

# 6. Pseudocode

## 6.1 SRPT Pseudocode

Start

While unfinished processes exist:

* Find all arrived processes.
* Select the process with the shortest remaining time.
* Execute the selected process.
* Update its remaining time.
* If it finishes, record its completion time.
* Repeat.

Stop

## 6.2 RM Pseudocode

Start

Assign fixed priorities according to task periods.

While tasks remain:

* Find all ready tasks.
* Select the ready task with the highest RM priority.
* Execute the selected task.
* Update its remaining execution time.
* Check for new releases and completed tasks.

Stop

## 6.3 EDF Pseudocode

Start

While unfinished tasks exist:

* Find all ready tasks.
* Select the task with the earliest absolute deadline.
* Execute the selected task.
* Update its remaining execution time.
* Check for new arrivals and completed tasks.

Stop

# 7. SRPT Example and Gantt Chart

Consider three processes with the following arrival times and burst times.

| Process | Arrival Time | Burst Time |
| ------- | -----------: | ---------: |
| P1      |            0 |          7 |
| P2      |            2 |          4 |
| P3      |            4 |          1 |

SRPT always chooses the available process with the shortest remaining processing time.

At time 0, P1 starts execution. At time 2, P2 arrives with a burst time of 4, which is less than the remaining time of P1. Therefore, P2 preempts P1.

At time 4, P3 arrives with a burst time of 1. It preempts P2 because its remaining processing time is shorter.

## Gantt Chart

0 — P1 — 2 — P2 — 4 — P3 — 5 — P2 — 7 — P1 — 12

## Calculations

Turnaround Time = Completion Time − Arrival Time

Waiting Time = Turnaround Time − Burst Time

| Process | Completion Time | Turnaround Time | Waiting Time |
| ------- | --------------: | --------------: | -----------: |
| P1      |              12 |              12 |            5 |
| P2      |               7 |               5 |            1 |
| P3      |               5 |               1 |            0 |

Average Waiting Time = (5 + 1 + 0) / 3 = 2

Average Turnaround Time = (12 + 5 + 1) / 3 = 6

# 8. Gantt Charts for RM and EDF

RM and EDF are designed primarily for real-time tasks, so their Gantt charts should be constructed using periodic tasks and their deadlines.

For RM, assign a fixed priority to each task according to its period. The task with the shortest period has the highest priority.

For EDF, compare the absolute deadlines of the ready tasks at each scheduling decision. The task with the earliest deadline is selected.

The same periodic task set should be used for both charts to make the comparison fair. Each chart should mark task releases, execution intervals, preemptions, idle intervals, and deadlines.

# 9. Deadlock and Starvation

## 9.1 Deadlock

Deadlock occurs when processes wait indefinitely for resources held by one another.

Deadlock is not an inherent property of SRPT, RM, or EDF. It depends on resource allocation and synchronization. A scheduling algorithm alone does not guarantee deadlock prevention.

## 9.2 Starvation

Starvation occurs when a process waits for a very long time because other processes continue to receive CPU time.

* **SRPT:** Long processes can starve if short processes continually arrive.
* **RM:** Lower-priority tasks may miss deadlines or wait under heavy load.
* **EDF:** Starvation is not inherent in a feasible ideal task set, but overload can cause deadline misses.

# 10. Conclusion

SRPT, RM, and EDF use different rules to select processes or tasks.

SRPT focuses on the shortest remaining processing time and can reduce average turnaround time. RM assigns fixed priorities according to task periods and is relatively simple to implement. EDF assigns priorities dynamically according to absolute deadlines and can achieve high processor utilization under ideal real-time scheduling assumptions.

The best algorithm depends on the system requirements. SRPT is useful for minimizing turnaround time, while RM and EDF are particularly relevant when real-time deadlines must be satisfied.
