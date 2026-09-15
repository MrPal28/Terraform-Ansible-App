resource "aws_s3_bucket" "infra_app_bucket"{
  bucket  = "${var.env}-${var.bucket_name}"
  tags = {
    Name = "${var.env}-aws-s3-infra-app-bucket"
    Environment = var.env
  }
}