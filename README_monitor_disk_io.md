# Disk I/O Monitor

This Python script monitors disk I/O activity on a system and logs potential anomalies that may indicate checkpointing activity.

## Requirements

- Python 3.x
- `psutil` library (install with `pip install psutil`)

## Usage

1. Save the provided code in a file named `idps_monitor_disk_io.py`.
2. Run the script with `python idps_monitor_disk_io.py`.
3. The script will continuously monitor disk I/O for all disks and print warnings if the read or write activity exceeds the defined baselines.

## How It Works

The script uses the `psutil` library to retrieve disk I/O statistics for all disks on the system. It defines baseline values for read and write activity (1 MB/s and 512 KB/s, respectively) and checks if the current activity exceeds five times the baseline values.

If a disk's read or write activity exceeds the defined thresholds, the script prints a warning message indicating potential checkpointing activity on that disk.

The monitoring loop runs indefinitely, checking disk I/O every 10 seconds. You can adjust the sleep time or baselines according to your system's requirements.

## Customization

- Adjust the `baseline_read_bytes` and `baseline_write_bytes` values to suit your system's normal disk I/O activity.
- Modify the warning message or add additional logging/notification mechanisms as per your requirements.
- Implement more sophisticated anomaly detection algorithms based on your specific use case.
