#!/usr/bin/env python3

import requests
import datetime

URL = "http://localhost:4499"  # Change to your application's URL
TIMEOUT = 3
LOG_FILE = "/var/log/app_health.log"

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")

def check_app():
    try:
        response = requests.get(URL, timeout=TIMEOUT)

        if response.status_code == 200:
            log(f"[UP] Application is running (HTTP {response.status_code})")
        else:
            log(f"[DOWN] Application returned an error (HTTP {response.status_code})")

    except requests.exceptions.RequestException:
        log("[DOWN] Application is NOT responding!")

if __name__ == "__main__":
    log("=== Application Health Checker Started ===")
    check_app()
