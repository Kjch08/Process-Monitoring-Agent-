import psutil
import socket
import requests

# Django backend API endpoint
API_URL = "http://127.0.0.1:8000/api/process-data/"
API_KEY =  "mysecretapikey"  # Must match backend settings
headers = {"Authorization": f"Api-Key {API_KEY}"}


def collect_processes():
    hostname = socket.gethostname()
    process_list = []

    for proc in psutil.process_iter(['pid', 'ppid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info
            process_list.append({
                "hostname": hostname,
                "pid": info['pid'],
                "ppid": info['ppid'],
                "name": info['name'],
                "cpu": info['cpu_percent'],
                "memory": info['memory_percent'],
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return process_list

def send_to_backend(data):
    headers = {"Authorization": f"Api-Key {API_KEY}"}
    try:
        response = requests.post(API_URL, json=data, headers=headers)
        if response.status_code == 201:
            print(" Data sent successfully")
        else:
            print(" Error:", response.status_code, response.text)
    except Exception as e:
        print("Failed to connect:", e)

if __name__ == "__main__":
    data = collect_processes()
    print(f"Collected {len(data)} processes")
    send_to_backend(data)
