output "ec2_public_ips" {
  value = aws_instance.infra_app_server[*].public_ip
}

output "ec2_private_ips" {
  value = aws_instance.infra_app_server[*].private_ip
}

output "ec2_instance_ids" {
  value = aws_instance.infra_app_server[*].id
}