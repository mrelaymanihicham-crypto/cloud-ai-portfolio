from learn_functions import server_name
from learn_functions import calculate_cost
from learn_functions import check_health

def generate_report(server_name,cpu,memory,hourly_rate):
    status = check_health(cpu, memory)
    cost = float(calculate_cost(hourly_rate))
    report = (
        f"SERVER : {server_name}\n"
        f"Status : {status}\n"
        f"Daily cost : ${cost:.2f}"
    )
    return report
print (generate_report("web-01",65,60,0.1))