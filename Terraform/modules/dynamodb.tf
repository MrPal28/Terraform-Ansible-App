resource "aws_dynamodb_table" "terraform_locks" {
  name         = "${var.env}-infra-app-table"
  billing_mode = "PAY_PER_REQUEST"

  hash_key = var.hash_key

  attribute {
    name = var.hash_key
    type = "S"
  }

  tags = {
    Name        = "${var.env}-infra-app-dynamodb-table"
    Environment = var.env
  }
}