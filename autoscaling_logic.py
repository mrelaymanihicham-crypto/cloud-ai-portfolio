"""
CLOUD AUTOSCALING DECISION ENGINE
Using if/elif/else for infrastructure decisions
"""

print("=== CLOUD AUTOSCALING SYSTEM ===\n")

# Get current metrics
cpu_utilization = float(input("Enter current CPU utilization (%): "))
memory_utilization = float(input("Enter current Memory utilization (%): "))
active_users = int(input("Enter number of active users: "))

print("\n=== ANALYSIS ===")

# Rule 1: CPU-based scaling
print("CPU Decision: ", end="")
if cpu_utilization > 80:
    print("🚨 Scale UP - CPU critical")
elif cpu_utilization > 60:
    print("⚠️  Monitor - CPU high")
elif cpu_utilization < 20:
    print("💡 Scale DOWN - CPU low")
else:
    print("✅ Stable - CPU normal")

# Rule 2: Memory-based scaling
print("Memory Decision: ", end="")
if memory_utilization > 85:
    print("🚨 Scale UP - Memory critical")
elif memory_utilization > 70:
    print("⚠️  Monitor - Memory high")
else:
    print("✅ Stable - Memory normal")

# Rule 3: User load-based scaling
print("User Load Decision: ", end="")
if active_users > 10000:
    print("🚨 Scale UP - Heavy load")
elif active_users > 5000:
    print("⚠️  Add standby instances")
elif active_users < 1000:
    print("💡 Reduce instances")
else:
    print("✅ Normal operations")

# Combined decision
print("\n=== FINAL DECISION ===")
if cpu_utilization > 80 or memory_utilization > 85 or active_users > 10000:
    print("🚨 IMMEDIATE SCALE UP REQUIRED")
elif (cpu_utilization > 60 and memory_utilization > 70) or active_users > 5000:
    print("⚠️  SCHEDULE SCALE UP")
elif cpu_utilization < 20 and memory_utilization < 50 and active_users < 1000:
    print("💡 SCALE DOWN TO SAVE COSTS")
else:
    print("✅ MAINTAIN CURRENT CAPACITY")