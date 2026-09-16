resource "tls_private_key" "ansible_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "local_file" "ansible_private_key" {
  content         = tls_private_key.ansible_key.private_key_pem
  filename        = "terraform-ansible-app.pem"
  file_permission = "0600"
}

resource "aws_key_pair" "ansible_key" {
  key_name   = "terraform-ansible-app-key"
  public_key = tls_private_key.ansible_key.public_key_openssh
}