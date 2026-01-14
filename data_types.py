# STRINGS - Text data
name = "Cloud Engineer"
project = 'AI Pipeline'
print("String Examples:")
print(f"Career: {name}")
print(f"Project: {project}")
print(f"Length of name: {len(name)}")
print("---")

# INTEGERS - Whole numbers
age_years = 5  # Years of experience
server_count = 100
print("Integer Examples:")
print(f"Experience: {age_years} years")
print(f"Servers: {server_count}")
print(f"Total capacity: {server_count * 64} GB RAM")  # Assuming 64GB each
print("---")

# FLOATS - Decimal numbers
cpu_utilization = 87.5  # Percentage
cost_per_hour = 0.065  # Dollars
print("Float Examples:")
print(f"CPU: {cpu_utilization}%")
print(f"Cost: ${cost_per_hour}/hour")
print(f"Daily cost: ${cost_per_hour * 24:.2f}")  # .2f means 2 decimal places
print("---")

# BOOLEANS - True/False
is_scalable = True
needs_maintenance = False
print("Boolean Examples:")
print(f"Scalable: {is_scalable}")
print(f"Maintenance needed: {needs_maintenance}")
print(f"Opposite of scalable: {not is_scalable}")
print("---")
# Type checking
print("Type Checking:")
print(f"Type of name: {type(name)}")
print(f"Type of server_count: {type(server_count)}")
print(f"Type of cpu_utilization: {type(cpu_utilization)}")
print(f"Type of is_scalable: {type(is_scalable)}")
# Type conversion - CRITICAL for data pipelines
print("\nType Conversion:")
users = "1500"  # String that looks like number
print(f"Users as string: {users}, type: {type(users)}")

users_int = int(users)  # Convert to integer
print(f"Users as integer: {users_int}, type: {type(users_int)}")

users_float = float(users)  # Convert to float
print(f"Users as float: {users_float}, type: {type(users_float)}")

cpu_string = str(cpu_utilization)  # Convert to string
print(f"CPU as string: '{cpu_string}', type: {type(cpu_string)}")