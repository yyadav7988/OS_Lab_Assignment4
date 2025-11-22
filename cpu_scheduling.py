from lab3.priority_roundrobin import priority_scheduling, round_robin  # (import your Lab 3 code)
# If not modular, just paste same Lab 3 scheduling code here

def fcfs():
    n = int(input("Enter number of processes: "))
    burst = list(map(int, input("Enter burst times: ").split()))
    wt, tat = [0]*n, [0]*n
    for i in range(1, n):
        wt[i] = wt[i-1] + burst[i-1]
    for i in range(n):
        tat[i] = wt[i] + burst[i]
    print(f"Waiting Time: {wt}\nTurnaround Time: {tat}")

def sjf():
    n = int(input("Enter number of processes: "))
    burst = list(map(int, input("Enter burst times: ").split()))
    sorted_order = sorted(range(n), key=lambda x: burst[x])
    wt, tat = [0]*n, [0]*n
    time = 0
    for i in sorted_order:
        wt[i] = time
        time += burst[i]
        tat[i] = time
    print(f"Waiting Time: {wt}\nTurnaround Time: {tat}")

def main():
    while True:
        print("\n=== CPU Scheduling ===")
        print("1. FCFS\n2. SJF\n3. Round Robin\n4. Priority\n5. Exit")
        ch = input("Choice: ")
        if ch == '1': fcfs()
        elif ch == '2': sjf()
        elif ch == '3': round_robin()
        elif ch == '4': priority_scheduling()
        elif ch == '5': break
        else: print("Invalid!")

if __name__ == "__main__":
    main()
