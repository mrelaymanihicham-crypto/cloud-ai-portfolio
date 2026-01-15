instances = [
    {"name": "web-server", "cost_per_hour": 0.10},
    {"name": "database", "cost_per_hour": 0.25},
    {"name": "cache", "cost_per_hour": 0.05},
    {"name": "analytics", "cost_per_hour": 0.35},
    {"name": "backup", "cost_per_hour": 0.08}
]

total_daily_cost = 0
most_expensive_name = ""
most_expensive_cost = 0
cheapest_name = ""
cheapest_cost = float('inf')
expensive_instances = []

for instance in instances:
    name = instance["name"]
    hourly_cost = instance["cost_per_hour"]
    daily_cost = hourly_cost * 24
    total_daily_cost += daily_cost
    if most_expensive_cost < daily_cost:
        most_expensive_cost = daily_cost
        most_expensive_name = name
    if cheapest_cost > daily_cost:
        cheapest_cost = daily_cost
        cheapest_name = name
    if daily_cost > 1:
        expensive_instances.append(name)
    
print(f"Total daily cost: ${total_daily_cost:.2f}") 
print(f"Most expensive: {most_expensive_name} (${most_expensive_cost:.2f}/day)") 
print(f"Cheapest: {cheapest_name} (${cheapest_cost:.2f}/day)") 
print(f"Instances > $1/day: {expensive_instances}")