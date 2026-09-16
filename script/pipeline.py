import subprocess
import sys
import time


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

def wait_for_ansible(max_retries=10, delay=10):

    for attempt in range(max_retries):

        print(
            f"\n>>> Checking Ansible connectivity "
            f"({attempt + 1}/{max_retries})\n"
        )

        result = subprocess.run(
            "ansible all -m ping",
            cwd="Ansible",
            shell=True
        )

        if result.returncode == 0:
            print("\nAll hosts reachable.\n")
            return

        print(
            f"\nHosts not ready yet. "
            f"Retrying in {delay} seconds...\n"
        )

        time.sleep(delay)

    print("\nERROR: Hosts never became reachable.\n")
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

    print("\nCreating/Updating Remote Backend...\n")

    run("terraform init", cwd="Terraform/remote-backend")

    run(
        "terraform apply -auto-approve",
        cwd="Terraform/remote-backend"
    )

    print("\nDeploying Infrastructure...\n")

    run("terraform init", cwd="Terraform")

    run("terraform validate", cwd="Terraform")

    run("terraform apply -auto-approve", cwd="Terraform")

    run(
        "terraform output -json server_inventory > ../inventory.json",
        cwd="Terraform"
    )

    run("python3 script/inventory.py")

    run(
        "ssh-keygen -y -f ~/.ssh/terraform-ansible-app-key > "
        "Ansible/roles/ssh/files/ansible.pub"
    )

    wait_for_ansible()

    run(
        "ansible-playbook playbooks/site.yml",
        cwd="Ansible"
    )

elif choice == "2":

    print("\nDestroying Infrastructure...\n")

    run("terraform init", cwd="Terraform")

    run("terraform destroy -auto-approve", cwd="Terraform")

    destroy_backend = input(
        "\nDestroy Remote Backend Too? (yes/no): "
    ).lower()

    if destroy_backend == "yes":

        run(
            "terraform init",
            cwd="Terraform/remote-backend"
        )

        run(
            "aws s3 rm s3://terraform-state-bucket-ap-am-2026 --recursive",
            cwd="Terraform/remote-backend"
        )

        run(
            "terraform destroy -auto-approve",
            cwd="Terraform/remote-backend"
        )

else:
    print("Invalid Choice")