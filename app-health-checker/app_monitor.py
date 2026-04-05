# Simple App Health Check (DevOps-style thinking)
# Author: Amsu Madhu Deepika Oruganti

import requests
import time

# This is the application URL we want to monitor
url = "https://jsonplaceholder.typicode.com/posts/1"

print("Starting application health check...\n")

# We’ll check the app status 3 times (like periodic monitoring)
for attempt in range(1, 4):
    print(f"Checking attempt {attempt}...")

    try:
        response = requests.get(url)

        # If everything is working fine
        if response.status_code == 200:
            print("Application is running smoothly.\n")
        
        # If something is off
        else:
            print(f" Unexpected response! Status code: {response.status_code}\n")

    except Exception as error:
        print(f"Something went wrong: {error}\n")

    # Wait for 2 seconds before next check (simulating real monitoring interval)
    time.sleep(2)

print("Health check process completed.\n")

# Final simple alert logic
if response.status_code != 200:
    print("ALERT: Application might be down. Please investigate.")
else:
    print("All good! No issues detected.")
