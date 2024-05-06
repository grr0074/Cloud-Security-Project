from scapy.all import sniff, TCP, IP
from collections import defaultdict
import time
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SynFloodDetector:
    def __init__(self):
        self.THRESHOLD = 100
        self.TIME_WINDOW = 10
        self.syn_counter = defaultdict(int)
        self.start_time = time.time()

    def alert_flood_detection(self, ip, count):
        """Alerts when a potential SYN flood attack is detected."""
        logging.warning(f"Potential TCP flood attack detected from {ip}: {count} SYN packets")
        # Here you can add additional actions such as sending an alert email or executing a network script.

    def detect_flood(self, packet):
        """Function to detect SYN flood attacks based on packet data."""
        if TCP in packet and packet[TCP].flags & 0x02:  # Check for SYN flag
            src_ip = packet[IP].src
            self.syn_counter[src_ip] += 1

        # Handling the timing and reporting
        current_time = time.time()
        if current_time - self.start_time > self.TIME_WINDOW:
            for ip, count in self.syn_counter.items():
                if count > self.THRESHOLD:
                    self.alert_flood_detection(ip, count)
            self.syn_counter.clear()
            self.start_time = current_time

def main():
    detector = SynFloodDetector()
    logging.info("Monitoring for TCP flood attacks...")
    sniff(filter="tcp", prn=detector.detect_flood)

if __name__ == "__main__":
    main()
