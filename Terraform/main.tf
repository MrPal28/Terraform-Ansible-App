module "dev-infra" {
  source = "./infra-app"
  env = "dev"
  bucket_name = "zone1"
  ec2_instance_count = 1
  ec2_instance_type = "t2.micro"
  ec2_ami = "ami-01a00762f46d584a1"
  ec2_default_storage_size = 8
  ec2_storage_type = "gp3"
  hash_key = "studentID"
}

module "prod-infra" {
  source = "./infra-app"
  env = "prod"
  bucket_name = "zone2"
  ec2_instance_count = 2
  ec2_instance_type = "t3.micro"
  ec2_ami = "ami-01a00762f46d584a1"
  ec2_default_storage_size = 8
  ec2_storage_type = "gp3"
  hash_key = "studentID"
}

module "stg-infra" {
  source = "./infra-app"
  env = "stg"
  bucket_name = "zone3"
  ec2_instance_count = 1
  ec2_instance_type = "t2.small"
  ec2_ami = "ami-01a00762f46d584a1"
  ec2_default_storage_size = 8
  ec2_storage_type = "gp3"
  hash_key = "studentID"
}

