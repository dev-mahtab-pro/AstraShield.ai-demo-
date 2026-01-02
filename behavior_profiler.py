print("AstraShield.ai | Behavior Profiler")

traffic_rate = 60000  # value passed logically from monitor

baseline = 30000

if traffic_rate > baseline:
    print("Behavior Deviation Detected")
    anomaly = True
else:
    print("Behavior Normal")
    anomaly = False
