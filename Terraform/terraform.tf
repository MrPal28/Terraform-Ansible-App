terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

    backend "s3" {
      bucket         = "terraform-state-bucket-ap-am-2026"
      key            = "terraform.tfstate"
      region         = "ap-south-1"
      dynamodb_table = "terraform-ansible-dynamodb-state-table"
    }
}