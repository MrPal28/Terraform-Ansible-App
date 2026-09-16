import subprocess
import sys

def run(cmd, cwd=None):
    print(f"\n>>> {cmd}\n")

    result = subprocess.run(
        cmd,
        cwd=cwd,
        shell=True
    )

    if result.returncode != 0:
        print(f"Command failed: {cmd}")
        sys.exit(1)

print("""
==========================
 Terraform-Ansible Pipeline
==========================

1. Apply
2. Destroy
""")

choice = input("Choose Action: ")

if choice == "1":

    run("terraform init", cwd="Terraform")

    run("terraform validate", cwd="Terraform")

    run("terraform apply -auto-approve", cwd="Terraform")

    run(
        "terraform output -json server_inventory > ../inventory.json",
        cwd="Terraform"
    )

    run("python script/generate_inventory.py")

    run("ssh-keygen -y -f ~/.ssh/terraform-ansible-app-key > Ansible/roles/ssh/files/ansible.pub")

    run(
        "ansible all -i Ansible/inventory/hosts.ini -m ping"
    )

    run(
        "ansible-playbook -i Ansible/inventory/hosts.ini Ansible/playbooks/site.yml"
    )

elif choice == "2":

    run("terraform init", cwd="Terraform")

    run("terraform destroy -auto-approve", cwd="Terraform")

else:
    print("Invalid Choice")