#!/usr/bin/env python3

import psutil
import shutil
import time
import datetime

# Thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

LOG_FILE = "/var/log/system_health.log"

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")

def check_system():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = shutil.disk_usage("/").used / shutil.disk_usage("/").total * 100
    processes = len(psutil.pids())

    log(f"CPU: {cpu}%, MEM: {mem}%, DISK: {disk:.2f}%, PROCESSES: {processes}")

    if cpu > CPU_THRESHOLD:
        log("[ALERT] HIGH CPU USAGE!")
    if mem > MEM_THRESHOLD:
        log("[ALERT] HIGH MEMORY USAGE!")
    if disk > DISK_THRESHOLD:
        log("[ALERT] LOW DISK SPACE!")

if __name__ == "__main__":
    log("=== System Health Monitor Started ===")
    while True:
        check_system()
        time.sleep(5)
