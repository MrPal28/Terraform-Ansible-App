resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-ansible-dynamodb-state-table"
  billing_mode = "PAY_PER_REQUEST"

  hash_key = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Name        = "terraform-ansible-dynamodb-state-table"
    Environment = var.env
  }
}