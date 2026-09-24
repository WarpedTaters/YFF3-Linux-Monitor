import socket
import psutil

host=socket.gethostname()

print(host, psutil.cpu_percent(interval=1.0), psutil.disk_usage('/').percent, psutil.virtual_memory().percent, len(psutil.pids()))