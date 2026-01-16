# Just create the list - you decide what's in it
servers = []

# Add your first server manually
servers.append({
    "name": "wb-01",
    "type": "t2.micro",
    "status": "running",
    "region": "us-east-1"})
servers.append({
    "name": "db-01",
    "type": "t3.medium",
    "status": "running",
    "region": "us-east-1"})
servers.append({
    "name": "hy-09",
    "type": "c5.large",
    "status": "stopped",
    "region": "eu-west-1"})


#print (servers)
valid_types = {"t2.micro", "t3.medium", "c5.large", "r5.large", "m5.large"}
valid_regions = {"us-east-1","us-west-2","eu-west-1","ap-southeast-1"}

def add_server(server_name,server_type,status,region_type):
    if server_type not in valid_types:
        print(f"❌Server type {server_type} is : Invalid.")
        return
    if region_type not in valid_regions:
        print(f"❌Server region {region_type} is : Invalid.")
        return
    server = {
        "name": server_name,
        "type": server_type,
        "status": status,
        "region": region_type
    }
    servers.append(server)
    print(f"✅ Server : {server_name} was added successfully.")
#add_server("Clouding","m5.large","stopped","ap-southeast-1")
#add_server("monitoring","m5.large","stopped","af-south-5")


def list_servers():
    for servers_available in servers:
        print(f"{servers_available}\n")
#list_servers()

def find_servers_by_region(region_name):
    print(f"Servers in {region_name}")
    found = False
    for server in servers:
        if region_name == server["region"]:
            print(f"- {server['name']} {server['type']} - {server['status']}")
            found = True
    if not found:
        print("No Servers were Found.")
        
        

#find_servers_by_region("us-east-1")

def count_servers_by_status():
    running = 0
    stopped = 0
    print("\nServer status count:")
    for server in servers:
        if server["status"] == "running":
            running += 1
        elif server["status"] == "stopped":
            stopped += 1
    print(f"Running : {running}")
    print(f"Stopped : {stopped}")
#count_servers_by_status()



def show_menu():
    print("\n=== CLOUD INVENTORY SYSTEM ===")
    print("1. List all servers")
    print("2. Add new server")
    print("3. Find servers by region")
    print("4. Count servers by status")
    print("5. Exit")


import json
def save_to_file():
    with open("servers.json", "w") as f:
        json.dump(servers, f)
    print("✅ Data saved to servers.json")

def load_from_file():
    global servers
    try:
        with open("servers.json", "r") as f:
            servers = json.load(f)
        print("✅ Data loaded from servers.json")
    except FileNotFoundError:
        print("ℹ️  No save file found, starting fresh")
def main():
    load_from_file()
    while True:
        show_menu()
        choice = input("Enter choice (1-5): ")
        
        if choice == "1":
            list_servers()
        elif choice == "2":
            addname = input("Enter The name of the server : ")
            addtype = input("Enter the type : ")
            addstatus = input("Enter the status : ")
            addregion = input("Enter the region : ")
            add_server(addname,addtype,addstatus,addregion)
        elif choice == "3":
            region = input("Enter the Region : ")
            find_servers_by_region(region)
        elif choice =="4":
            count_servers_by_status()
        elif choice == "5":
            print("Goodbye!")
            save_to_file()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()