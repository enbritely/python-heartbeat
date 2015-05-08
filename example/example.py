import time
import heartbeat

print("before starting heartbeat service")

heartbeat.run_heartbeat_service(8888)

print("after starting heartbeat service")

time.sleep(50)

