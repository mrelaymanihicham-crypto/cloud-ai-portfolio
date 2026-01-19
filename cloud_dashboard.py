"""
CLOUD DASHBOARD - Consolidation Project
Combines all learned concepts into one system
"""

# Core data structure
servers = [
    {
        "name": "web-01",
        "type": "t2.micro", 
        "region": "us-east-1",
        "status": "stopped",
        "hourly_cost": 0.16,
        "metrics": {"cpu": 90, "memory": 90, "disk": 45}
    },
    {
        "name": "web-02",
        "type": "t3.micro", 
        "region": "us-west-2",
        "status": "running",
        "hourly_cost": 0.0254,
        "metrics": {"cpu": 95, "memory": 70, "disk": 45}
    },
    {
        "name": "web-03",
        "type": "t3.small", 
        "region": "eu-west-1",
        "status": "stopped",
        "hourly_cost": 0.176,
        "metrics": {"cpu": 70, "memory": 60, "disk": 45}
    }
]

valid_names = {"web-01","web-02","web-03","db-01","db-02","app-01","app-02","lb-01","proxy-01","bastion-01","vpn-01","api-01","cache-01","worker-01"}
valid_types = {"t2.micro","t3.micro","t3.small","t3.medium","m5.large","c5.large","r5.large","g5.xlarge"}
valid_regions = {"us-east-1","us-west-2","eu-west-1","eu-central-1","ap-south-1","ap-northeast-1"}
valid_statuses = {"pending","running","stopped","terminated"}

def calculate_total_cost():
    hourly_cost = sum(server["hourly_cost"] for server in servers)
    daily_totals = hourly_cost * 24
    monthly_totals = daily_totals * 30

    return daily_totals, monthly_totals, hourly_cost

def generate_health_report():
    report = []
    for server in servers:
        name = server.get("name")
        cpu = server["metrics"]["cpu"]
        memory = server["metrics"]["memory"]
        issues = []

        if cpu > 80:
            issues.append(f"CPU at {cpu}%")
        if memory > 80:
            issues.append(f"Memory at {memory}%")

        status = "UNHEALTHY" if issues else "HEALTHY"
        issue = " | ".join(issues)
        report.append((name,status,issue))
    return report

def check_alerts():
    alerts = []
    health_data = {
        name : issue for name,status,issue in generate_health_report() if status == "UNHEALTHY"}

    for server in servers:
        name = server.get("name")
        daily_cost = server.get("hourly_cost") * 24
        

        if daily_cost > 1:
            alerts.append(f"COST ALERT : {name} costs ${daily_cost:.2f}/day")
        
        if name in health_data:
            alerts.append(f"HEALTH ALERT : {name} {health_data.get(name)}")

        if server.get("status") == "stopped" and daily_cost > 0:
            alerts.append(f"WASTE ALERT : {name} is stopped but still costs ${daily_cost:.2f}/day")
    return alerts


def generate_dashboard():
    print("=== CLOUD DASHBOARD ===\n")
    total_servers = len(servers)
    total_running_servers = sum(1 for server in servers if server.get("status") == "running")
    total_stopped_servers = sum(1 for server in servers if server.get("status") == "stopped")
    print(f"📊 SERVERS: {total_servers} total | {total_running_servers} running | {total_stopped_servers} stopped")
    health_reports = generate_health_report()
    healthy_servers = sum(1 for _,status,_ in health_reports if status == "HEALTHY")
    unhealthy_servers = sum(1 for _,status,_ in health_reports if status == "UNHEALTHY")
    print(f"💚 HEALTH: {healthy_servers} healthy | {unhealthy_servers} unhealthy ")
    daily_costs,monthly_costs,hourly_costs = calculate_total_cost()
    print(f"💰 COST: ${daily_costs:.2f}/day | ${monthly_costs:.2f}/month\n")
    total_alerts = check_alerts()
    
    print(f"🚨 ALERTS ({len(total_alerts)}):")
    for alert in total_alerts:
        print(f"  • {alert}")

generate_dashboard()