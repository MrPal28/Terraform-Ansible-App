output "server_inventory" {
  value = {
    prod = module.prod-infra.ec2_public_ips
    dev  = module.dev-infra.ec2_public_ips
    stg  = module.stg-infra.ec2_public_ips
  }
}