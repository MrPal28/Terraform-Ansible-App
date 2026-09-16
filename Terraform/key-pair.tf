resource "aws_key_pair" "ansible_key" {
  key_name   = "terraform-ansible-app-key"
  public_key = file("${path.module}/keys/terraform-ansible-app-key.pub")
}
