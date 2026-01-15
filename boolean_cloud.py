"""
BOOLEAN LOGIC IN CLOUD OPERATIONS
Understanding AND, OR, NOT for infrastructure decisions
"""

print("=== BOOLEAN LOGIC DEMO ===\n")

# Cloud deployment conditions
has_backup = True
has_monitoring = False
is_encrypted = True
in_eu_region = False

print("Initial Conditions:")
print(f"Has backup: {has_backup}")
print(f"Has monitoring: {has_monitoring}")
print(f"Is encrypted: {is_encrypted}")
print(f"In EU region: {in_eu_region}")

print("\n=== LOGICAL OPERATIONS ===")

# AND: All conditions must be True
production_ready = has_backup and has_monitoring and is_encrypted
print(f"Production ready (AND all): {production_ready}")

# OR: At least one condition must be True
has_security = is_encrypted or in_eu_region
print(f"Has security feature (OR): {has_security}")

# NOT: Inverts the value
needs_monitoring = not has_monitoring
print(f"Needs monitoring (NOT): {needs_monitoring}")

# Complex combination
gdpr_compliant = is_encrypted and (in_eu_region or has_backup)
print(f"GDPR compliant (complex): {gdpr_compliant}")

print("\n=== REAL CLOUD SCENARIO ===")

# Simulating auto-healing logic
cpu_high = True
memory_ok = False
disk_space_low = True
network_ok = True

print(f"CPU high: {cpu_high}")
print(f"Memory OK: {memory_ok}")
print(f"Disk space low: {disk_space_low}")
print(f"Network OK: {network_ok}")

# Decision logic
needs_restart = cpu_high and not memory_ok
needs_cleanup = disk_space_low and network_ok
critical_issue = (cpu_high and disk_space_low) or (not memory_ok and not network_ok)

print(f"\nNeeds restart: {needs_restart}")
print(f"Needs cleanup: {needs_cleanup}")
print(f"Critical issue: {critical_issue}")