import psutil
import time

print("AstraShield.ai | Real-Time Traffic Monitor")

net1 = psutil.net_io_counters()
time.sleep(3)
net2 = psutil.net_io_counters()

bytes_sent = net2.bytes_sent - net1.bytes_sent
bytes_recv = net2.bytes_recv - net1.bytes_recv

traffic_rate = (bytes_sent + bytes_recv) / 3

print(f"Real Traffic Rate: {traffic_rate:.2f} bytes/sec")

if traffic_rate > 50000:
    print("Traffic Pattern: Abnormal")
    anomaly = True
else:
    print("Traffic Pattern: Normal")
    anomaly = False
