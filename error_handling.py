import json
with open("config.json", "w") as f:
    json.dump({"threshold": 90}, f)

error_count = 0
def calculate_cpu_utilization(total, used):
    global error_count
    try:
        return f"{(used / total) * 100:.1f}%"
    except ZeroDivisionError:
        error_count += 1
        return "ERROR: Cannot calculate - total is 0%"
    except TypeError:
        error_count += 1
        return "ERROR: Invalid data types"
    
print("=== CLOUD MONITORING WITH ERROR HANDLING ===\n")
print("1. CPU Utilization Calculation:")
print(f"Normal case : {calculate_cpu_utilization(100,75)}")
print(f"Zero division case : {calculate_cpu_utilization(0,75)}")
print(f"Invalid type case : {calculate_cpu_utilization('100',75)}")

def load_monitoring_config(filename):
    global error_count
    try:
        with open(filename,"r") as file:
            config = json.load(file)
            print(f"Loading '{filename}': ✅ Success")
            return config
    except FileNotFoundError:
        error_count += 1
        print(f"Loading '{filename}': ❌ File not found, using defaults")
        return {}
    except PermissionError:
        error_count += 1
        return {}

print("\n2. Configuration Loading:")
load_monitoring_config("config.json")
load_monitoring_config("missing.json")


def parse_cloud_response(response_string):
    global error_count
    try:
        data = json.loads(response_string)
        servers = data["servers"]
        status = data["status"]
        return f"Server count: {servers}, Status: {status}"

    except json.JSONDecodeError:
        error_count += 1
        return "ERROR: Invalid response format"

    except KeyError as e:
        error_count += 1
        return f"ERROR: '{e.args[0]}' key missing"

print("\n3. API Response Parsing:")
valid_json = '{"servers":"5","status":"healthy"}'
print(f"Valid JSON : {parse_cloud_response(valid_json)}")
missing_key_json = '{"server":"5","status":"healthy"}'
print(f"Missing Key : {parse_cloud_response(missing_key_json)}")
invalid_json ='{"servers":"5","status":"healthy"'
print(f"Invalid JSON : {parse_cloud_response(invalid_json)}")
print("\n=== SUMMARY ===")
print(f"System handled {error_count} errors gracefully")
print("Monitoring continues despite failures")
