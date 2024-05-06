from scapy.all import sniff, TCP, IP
from collections import defaultdict
import time
import subprocess


THRESHOLD = 100
TIME_WINDOW = 10


syn_counter = defaultdict(int)
start_time = time.time()


container_stopped = False

def stop_docker_container(container_name):
    """Stops a Docker container by name using the Docker CLI."""
    global container_stopped
    if not container_stopped:
        command = ["docker", "stop", container_name]
        try:
            subprocess.run(command, check=True)
            print(f"Docker container {container_name} stopped successfully.")
            container_stopped = True  # Set the flag to True after stopping the container
        except subprocess.CalledProcessError as e:
            print(f"Failed to stop Docker container {container_name}: {str(e)}")

def detect_flood(packet):
    """Function to detect SYN flood attacks based on packet data."""
    global start_time
    global container_stopped
    if TCP in packet and packet[TCP].flags & 0x02:  # TCP SYN flag
        src_ip = packet[IP].src
        syn_counter[src_ip] += 1

        current_time = time.time()
        if current_time - start_time > TIME_WINDOW:
            for ip, count in syn_counter.items():
                if count > THRESHOLD and not container_stopped:
                    print(f"Potential TCP flood attack detected from {ip}: {count} SYN packets")
                    stop_docker_container("my_server")  # Replace with your actual container name
                    return  
            syn_counter.clear()
            start_time = current_time

def main():
    """Main function to start monitoring TCP traffic for SYN flood detection."""
    print("Monitoring for TCP flood attacks...")
    sniff(filter="tcp", prn=detect_flood)

if __name__ == "__main__":
    main()
