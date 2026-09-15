variable "env" {
  description = "Environment name"
  type = string
}

variable "bucket_name"{
  description = "Bucket name"
  type = string
}

variable "ec2_instance_count" {
  description = "Number of EC2 instances to create"
  type = number
}

variable "ec2_instance_type" {
  description = "Type of EC2 instance"
  type = string
}

variable "ec2_ami" {
  description = "AMI ID for the EC2 instance"
  type = string
}

variable "ec2_default_storage_size" {
  description = "Default storage size for EC2 instance in GB"
  type = number
}

variable "ec2_storage_type" {
  description = "Storage type for EC2 instance"
  type = string
}

variable "hash_key" {
  description = "Hash key for DynamoDB table"
  type = string
}