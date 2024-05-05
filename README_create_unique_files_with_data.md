## README: create_unique_files_with_data.py

This Python script generates a specified number of unique files filled with random data, simulating resource-intensive tasks like creating snapshots.

**Requirements:**

* Python 3.x

**How to Run:**

1. Save the script as a Python file (**create_unique_files_with_data.py**).
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:

```bash
python create_unique_files_with_data.py
```

**Expected Output:**

The script will:

* Create a user-defined number of files (default: 20) with unique names.
* Fill each file with a configurable amount of random data (default: 4096 bytes). Adjust this value within the script for desired resource usage (higher value = more resource consumption).
* Print the path to each created file.
* Print a message indicating the completion of creating the desired number of files.

**Notes:**

* Creating a large number of files with significant data size might impact your system's performance.
* This script simulates the resource usage of tasks that generate data files, not actual data backup or management.

**Customization:**

* You can modify the `number_of_snapshots` variable at the beginning of the script to control the number of files created.
* Change the `data_size` argument passed to the `create_resource_intensive_snapshot` function within the loop to adjust the amount of random data written to each file.
