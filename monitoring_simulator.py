"""
MONITORING SYSTEM SIMULATOR
Using loops for continuous monitoring and automation
"""

print("=== SERVER MONITORING SIMULATION ===\n")

# Simulated server metrics (CPU % for 10 servers)
server_cpus = [45, 80, 30, 90, 65, 75, 40, 85, 50, 95]

print("Initial scan of 10 servers:")
print(f"All CPU values: {server_cpus}")

print("\n=== FOR LOOP: INDIVIDUAL SERVER CHECK ===")
high_load_servers = 0

# for loop: check each server individually
for cpu in server_cpus:
    if cpu > 80:
        print(f"🚨 Server with {cpu}% CPU - CRITICAL")
        high_load_servers += 1
    elif cpu > 70:
        print(f"⚠️  Server with {cpu}% CPU - HIGH")
    else:
        print(f"✅ Server with {cpu}% CPU - NORMAL")

print(f"\nTotal critical servers: {high_load_servers}")

print("\n=== WHILE LOOP: CONTINUOUS MONITORING ===")
# Simulate monitoring until all servers are healthy
print("Starting continuous monitoring...")

minutes = 0
unhealthy_servers = high_load_servers

while unhealthy_servers > 0:
    minutes += 1
    # Simulate fixing one server each minute
    unhealthy_servers -= 1
    print(f"Minute {minutes}: Fixed 1 server. {unhealthy_servers} remaining.")
    
    if minutes >= 5 and unhealthy_servers > 0:
        print("⚠️  Warning: Taking too long to fix all servers")
        break  # Emergency break from loop

print("\n✅ All servers now healthy or escalation triggered")

print("\n=== ENUMERATE: SERVER ID TRACKING ===")
# enumerate gives both index and value
for server_id, cpu in enumerate(server_cpus):
    print(f"Server #{server_id + 1}: {cpu}% CPU", end="")
    if cpu > 80:
        print(" [REBOOT SCHEDULED]")
    else:
        print(" [OK]")