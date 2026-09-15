resource "tls_private_key" "terraform_key"{
    algorithm = "RSA"
    rsa_bits =2048
}
resource "local_file" "private_key"{
    content = tls_private_key.terraform_key.private_key_pem
    filename = "${var.env}-infra-app-key.pem"
    file_permission = "0600"
}
resource "aws_key_pair" "terraform_key"{
    key_name = "${var.env}-infra-app-key"
    public_key = tls_private_key.terraform_key.public_key_openssh

    tags = {
      Environment = var.env
    }
}