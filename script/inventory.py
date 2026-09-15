import json

with open("inventory.json") as f:
    data = json.load(f)

with open("Ansible/inventory/hosts.ini", "w") as inv:

    inv.write("[prod]\n")
    for ip in data["prod"]:
        inv.write(f"{ip}\n")

    inv.write("\n[dev]\n")
    for ip in data["dev"]:
        inv.write(f"{ip}\n")

    inv.write("\n[stg]\n")
    for ip in data["stg"]:
        inv.write(f"{ip}\n")

print("Inventory generated successfully")