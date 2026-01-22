import random
import time
from datetime import datetime

def call_cloud_api(api_url):
    chance = random.random()
    if chance < 0.4:
        return(True,"SUCCESS")
    elif chance < 0.9:
        return (False, "Rate Limited")
    else:
        return (False, "Permanent Error")

def monitor_service(service_name,service_url):
    print(f"Service: {service_name}")
    print(f"Calling cloud API: {service_url}")
    for attempt_number in range(1,4):
        success,message = call_cloud_api(service_url)

        if success:
            print(f"Attempt {attempt_number}: ✅ Success!\n")
            return (True,attempt_number,message)
        elif message == "Rate Limited":
            print(f"Attempt {attempt_number}: Failed (rate limited) - Retrying...")
            time.sleep(1)
            if attempt_number == 3:
                print(f"Failed! (retries exhausted)\n")
                return (False, attempt_number,message)
        elif message == "Permanent Error":
            print(f"Attempt {attempt_number}: ❌ Failed! (permanent error)\n")
            return(False, attempt_number,message)
    return (False,3)

def log_results(results):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("monitoring_log2.txt","a") as f:
            f.write(f"\n[{timestamp}] MONITORING REPORT\n")
            for result in results:
                f.write(f"{result}\n")
    except IOError as e:
        print(f"Error writing log: {e}")

def main():
    services = [
        {"name": "Compute API", "url": "https://api.cloud.com/compute"},
        {"name": "Database API", "url": "https://api.cloud.com/database"},
        {"name": "Storage API", "url": "https://api.cloud.com/storage"}
    ]
    results = []
    health_count = 0
    total_servers = len(services)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=== CLOUD PRODUCTION MONITOR ===")
    print(f"[{timestamp}] Starting Monitoring cycle...\n")
    for service in services:
        success,attempt,message = monitor_service(service["name"],service["url"])
        if success and attempt == 1:
            health_count += 1
            log_msg = f"{service['name']}: SUCCESS!"
        elif success and attempt > 1:
            health_count += 1
            log_msg = f"{service['name']}: SUCCESS! (after {attempt} attempts)"
        elif message == "Permanent Error":
            log_msg = f"{service['name']}: FAILED! (permanent error)"
        else:
            log_msg = f"{service['name']}: FAILED! (after {attempt} attempts)"
        results.append(log_msg)
    log_results(results)
    print(f"[{timestamp}] Summary: {health_count}/{total_servers} servers healthy")
    print("Results saved to monitoring_log2.txt")

if __name__ == "__main__":
    main()