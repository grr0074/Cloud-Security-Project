import socket
import time

def monitor_dns_queries(port=53, host='0.0.0.0'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    print(f"Listening for DNS queries on {host}:{port}")
    while True:
        data, addr = sock.recvfrom(1024)
	print(f"recieved query from {addr}")
        yield data, addr

def detect_dns_amplification():
    query_count = {}
    threshold = 4 
    time_window = 15 
    start_time = time.time()
    alert_detected = False

    while True:
        for data, addr in monitor_dns_queries():
            if alert_detected:
                print("Alert has been detected. stopping recieving packets.")
                return

            current_time = time.time()
            ip = addr[0]

            if current_time - start_time > time_window:
                print("Resetting counts.")
                query_count = {}
                start_time = current_time

            query_count[ip] = query_count.get(ip, 0) +1
            print(f"IP {ip} has {query_count[ip]} queries.")

            if query_count[ip] > threshold:
                print(f"Potential DNS Amplification attack detected from {ip}")
                alert_admin(ip)
                alert_detected = True

def alert_admin(ip):
    print(f"Alert: High volume of DNS queries detected from IP: {ip}. Possible DNS amplification attack.")

if __name__ == "__main__":
    try:
        detect_dns_amplification()
    except KeyboardInterrupt:
        print("monitoring stopped by user.")
    except Exception as e:
        print(f"an error occurred: {e}")
