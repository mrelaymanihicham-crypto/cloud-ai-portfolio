""""
CLOUD COST CALCULATOR
Practice variables, types, and basic operations
"""

# Cloud instance specifications
instance_name = "c5.xlarge"
vcpus = 4
memory_gb = 8.0
price_per_hour = 0.17
is_spot_instance = True  # Cheaper, can be terminated
region = "us-east-1"

# Calculations
hours_per_day = 24
days_per_month = 30

# Monthly cost calculation
monthly_cost = price_per_hour * hours_per_day * days_per_month

# Output report
print("=== CLOUD INSTANCE REPORT ===")
print(f"Instance: {instance_name}")
print(f"vCPUs: {vcpus} ({type(vcpus)})")
print(f"Memory: {memory_gb} GB ({type(memory_gb)})")
print(f"Region: {region}")
print(f"Spot Instance: {is_spot_instance}")
print(f"Hourly Rate: ${price_per_hour}")
print(f"Monthly Cost: ${monthly_cost:.2f}")  # Format to 2 decimals

# Bonus: Convert to different units
price_per_minute = price_per_hour / 60
print("\nAlternative Units:")
print(f"Price per minute: ${price_per_minute:.4f}")
print(f"Price per second: ${price_per_minute / 60:.6f}")