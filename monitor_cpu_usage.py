import psutil

def monitor_cpu_usage():
  """
  Monitors CPU usage and logs potential anomalies.
  """
  cpu_usage = psutil.cpu_percent(interval=1)  # Monitor CPU usage every second
  threshold = 80  # Set a CPU usage threshold (adjust based on your system)

  if cpu_usage > threshold:
    print(f"WARNING: High CPU Usage ({cpu_usage}%) - Potential Checkpointing Activity")

# Run the monitoring function in a loop
while True:
  monitor_cpu_usage()
  time.sleep(5)  # Check CPU usage every 5 seconds
