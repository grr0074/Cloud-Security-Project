import time

def perform_workload_task():
  # Simulate workload by performing a time-consuming task (replace with your actual workload)
  for i in range(100000):  # Adjust loop iterations for desired workload
    pass

def simulate_checkpointing_overhead(checkpoint_time):
  """
  Simulates the overhead associated with taking checkpoints.

  Args:
      checkpoint_time (float): The time delay between simulated checkpoints in seconds.
  """
  while True:
    # Simulate checkpointing overhead
    time.sleep(checkpoint_time)  # Delay between simulated checkpoints

    # Perform workload within the container
    perform_workload_task()

# Example usage (adjust checkpoint_time for desired impact)
simulate_checkpointing_overhead(0.1)  # Simulates checkpoint every 0.1 seconds
