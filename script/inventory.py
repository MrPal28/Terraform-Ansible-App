import json
import os

key_path = os.getenv(
    "ANSIBLE_KEY_PATH",
    "/home/ubuntu/.ssh/terraform-ansible-app-key"
)

with open("inventory.json") as f:
    data = json.load(f)

with open("Ansible/inventory/hosts.ini", "w") as inv:

    inv.write("[production]\n")

    for index, ip in enumerate(data["prod"], start=1):
        inv.write(f"prod0{index} ansible_host={ip}\n")

    inv.write("\n[staging]\n")

    for index, ip in enumerate(data["stg"], start=1):
        inv.write(f"stage0{index} ansible_host={ip}\n")

    inv.write("\n[development]\n")

    for index, ip in enumerate(data["dev"], start=1):
        inv.write(f"dev0{index} ansible_host={ip}\n")

    inv.write("\n[all:vars]\n")
    inv.write("ansible_user=ubuntu\n")
    inv.write(
        f"ansible_ssh_private_key_file={key_path}\n"
    )

print("Inventory generated successfully")
