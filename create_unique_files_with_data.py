import os
import random

def generate_random_data(size):
  """
  Generates a random string of the specified size filled with characters.
  """
  chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
  return ''.join(random.choice(chars) for i in range(size))

def create_resource_intensive_snapshot(prefix="snapshot", data_size=1024):
  """
  This function creates a file with a unique name based on the provided prefix and fills it with random data.

  Args:
      prefix (str, optional): The prefix to use for the filename (default: "snapshot").
      data_size (int, optional): The amount of random data to write to the file (default: 1024 bytes).

  Returns:
      str: The path to the created file.
  """
  # Generate a unique suffix using a random number.
  unique_suffix = f"{os.urandom(4).hex()}"
  filename = f"{prefix}_{unique_suffix}.txt"

  # Check if the file already exists (unlikely due to random suffix).
  while os.path.exists(filename):
    unique_suffix = f"{os.urandom(4).hex()}"
    filename = f"{prefix}_{unique_suffix}.txt"

  # Generate random data
  random_data = generate_random_data(data_size)

  # Create the file and write data
  with open(filename, 'w') as f:
    f.write(random_data)

  return filename

number_of_snapshots = 20000

# Create dummy files with unique names and random data
for i in range(number_of_snapshots):
  snapshot_file = create_resource_intensive_snapshot(f"snapshot_{i}", 4096)  # Adjust data_size for desired resource usage
  print(f"Created snapshot file: {snapshot_file}")

print(f"Created {number_of_snapshots} dummy files with random data to simulate snapshots.")
