# Find and fix all errors
instance_count = "10"
cost_per_instance = 15.5

# This line has an error - fix it
instance_count_int = float(instance_count)
total_cost = instance_count_int * cost_per_instance

print(f"Total cost: {total_cost}")

# Another error here

status_message = 'Running'
print(f"Server status: {status_message}")