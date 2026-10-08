import socket
import psutil
import json
import time
import subprocess


try:
    while True:
        # array ={
        #     "hostname": socket.gethostname(),
        #     "kernel": subprocess.run(["uname", "-r"], capture_output=True, text=True).stdout, 
        #     "CPU_percent": psutil.cpu_percent(interval=1.0),
        #     "disk_usage_percent": psutil.disk_usage('/').percent, 
        #     "RAM": psutil.virtual_memory().percent, 
        #     "process_amount": len(psutil.pids())
        # }
        array = [            
            f"hostname: {socket.gethostname()}",
            f"kernel: {subprocess.run(["uname", "-r"], capture_output=True, text=True).stdout}", 
            f"CPU percent: {psutil.cpu_percent(interval=1.0)}%",
            f"disk usage percent: {psutil.disk_usage('/').percent}%", 
            f"RAM: {psutil.virtual_memory().percent}%", 
            f"process amount: {len(psutil.pids())}"]
        with open("systemdata.json", "w") as file:
            json.dump(array, file, indent=4)
        time.sleep(5)
except KeyboardInterrupt:
    pass