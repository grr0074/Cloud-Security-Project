import psutil

def monitor_disk_io():
  """
  Monitors disk I/O and logs potential anomalies.
  """
  disk_io_stats = psutil.disk_io_counters(perdisk=True)  # Get disk I/O stats for all disks

  # Define baseline I/O values (adjust based on your system)
  baseline_read_bytes = 1024 * 1024  # 1 MB per second
  baseline_write_bytes = 1024 * 512   # 512 KB per second

  for disk, stats in disk_io_stats.items():
    read_bytes = stats.read_bytes
    write_bytes = stats.write_bytes

    if read_bytes > baseline_read_bytes * 5 or write_bytes > baseline_write_bytes * 5:
      print(f"WARNING: High Disk I/O on {disk} - Potential Checkpointing Activity")

# Run the monitoring function in a loop
while True:
  monitor_disk_io()
  time.sleep(10)  # Check disk I/O every 10 seconds
