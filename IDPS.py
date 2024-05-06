import psutil
import subprocess
import time
import collections

callForRestart = 20  # Threshold for reset intiation
timesLooped = 0  # Counter for amount of times the detecttion system has looped

# Thresholds for CPU, Memory, and Process Count
CPU_THRESHOLD = 85
MEM_THRESHOLD = 60
MAX_PROCESSES = 300 

# Dictionary to store process names and their counts
process_counts = collections.defaultdict(int)
bombProcesses = set()  # Set to store names of bomb processes

# Detection System that tracks if CPU , mem or Preocesses cross thresholds
def DetectionSystem(cpu_percent, mem_percent, num_processes):
    global timesLooped
    if cpu_percent > CPU_THRESHOLD or mem_percent > MEM_THRESHOLD or num_processes > MAX_PROCESSES:
        print("Bomb detected! Taking action...")
        PreventionSystem()
        timesLooped += 1
        if timesLooped >= callForRestart:
            choice = input("You are being attacked! Do you want to restart your VM? (yes/no): ").lower()
            if choice == 'yes':
                restart_vm()
            else:
                timesLooped = 0
                print("VM restart declined.")

def PreventionSystem():
    global bombProcesses

    # Identify and add processes with counts exceeding the threshold to the bombProcesses set
    for process in psutil.process_iter(['pid', 'name']):
        process_name = process.info['name']
        process_counts[process_name] += 1
        if process_counts[process_name] > 120 and process_counts[process_name] != "VBoxClient":
            bombProcesses.add(process_name)

    # Kill processes with Bomb relation
    for name in bombProcesses:
            subprocess.run(['pkill', '-9', name])
            print(f"Killed bomb processes with name: {name}")
def restart_vm():
    print("Restarting the VM...")
    subprocess.run(['sudo', 'shutdown', '-r', 'now'])
# Monitoring tool that continously tracks the CPU, Memory and Process precentages // counts
def MonitoringTool():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)  # Check CPU every second
        mem_percent = psutil.virtual_memory().percent  # Get memory usage
        num_processes = len(psutil.pids())  # Get the number of processes
        print(f"CPU: {cpu_percent}% | Memory: {mem_percent}% | Processes: {num_processes}")

        DetectionSystem(cpu_percent, mem_percent, num_processes)

        time.sleep(1)

if __name__ == "__main__":
    MonitoringTool()


