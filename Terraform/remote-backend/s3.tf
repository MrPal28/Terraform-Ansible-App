resource "aws_s3_bucket" "terraform_state_bucket_ap_28"{
bucket = "terraform-state-bucket-ap-am-2026"
    tags = {
        Name = "terraform-state-bucket-ap-am"
        Environment = var.env
    }
}
