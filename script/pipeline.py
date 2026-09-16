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

    run(
        "ansible all -m ping",
        cwd="Ansible"
    )

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
            "terraform destroy -auto-approve",
            cwd="Terraform/remote-backend"
        )

else:
    print("Invalid Choice")