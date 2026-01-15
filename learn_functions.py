def server_name(name):
    return(f"Checking server: {name}")
messages = [
    server_name("web-01"),
    server_name("db-01")
]
for message in messages:
    print(message)


def calculate_cost(hourly_rate,hours=24):
    return(f"${hourly_rate * hours:.1f}")
daily = calculate_cost(0.10)
hourly = calculate_cost(0.10,8)

print(f"Daily cost: {daily}")
print(f"8-hour cost: {hourly}")



def calculate_cost(hourly_rate,hours=24):
    return(f"{hourly_rate * hours:.1f}")
costs = [
    ("Daily cost: ", calculate_cost(0.10)),
    ("8-hour cost: ", calculate_cost(0.10,8))
]

for type,cost in costs:
    print(f"{type}${cost}")


def check_health(cpu_usage ,memory_usage):
    if cpu_usage > 90 or memory_usage > 85:
        return "CRITICAL"
    elif cpu_usage > 75 or memory_usage > 70:
        return "WARNING"
    else:
        return "HEALTHY"
    
print(check_health(65, 60))  # Should be "HEALTHY"
print(check_health(80, 65))  # Should be "WARNING"
print(check_health(95, 70))  # Should be "CRITICAL"