DNS Amplification Detection (dns_amplification_detector.py):

The detection code monitors incoming DNS queries, counts the number of queries from each IP address, and detects potential DNS amplification attacks.
It listens for DNS queries on a specified port and IP address, tracks the number of queries from each IP address within a time window, and triggers an alert if the query count exceeds a predefined threshold.

Running:
run python3 dns_amplification_detector.py on terminal 1



Attack Script (dns_attack.py):

The attack code simulates a DNS amplification attack by sending a large number of DNS queries to a target IP address.
It generates DNS query messages for a specified domain name and sends them to the target IP address using the DNS protocol.

running:
run python3 dns_attack.py on terminal 2

