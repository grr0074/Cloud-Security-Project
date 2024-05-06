import dns.message
import dns.query
import random
import time

def send_dns_queries(target_ip, no_of_queries, interval=0.01):
    query = dns.message.make_query('example.com', dns.rdatatype.A)
    for _ in range(no_of_queries):
        try:
            dns.query.udp(query, target_ip, port=53, source_port=random.randint(1024, 65535), timeout=2)
            print("Query sent")
        except Exception as e:
            print("Failed to send query:", e)
        time.sleep(interval)

if __name__ == "__main__":
    target_ip = '10.0.2.15'
    number_of_queries = 10000 
    send_dns_queries(target_ip, no_of_queries)
