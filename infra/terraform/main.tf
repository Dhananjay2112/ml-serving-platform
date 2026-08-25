terraform {
  required_version = ">= 1.7"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  # Remote state - create the S3 bucket + DynamoDB lock table once,
  # then uncomment this block and `terraform init -migrate-state`.
  # backend "s3" {
  #   bucket         = "your-tfstate-bucket"
  #   key            = "model-serving-platform/terraform.tfstate"
  #   region         = "ap-south-1"
  #   dynamodb_table = "terraform-locks"
  #   encrypt        = true
  # }
}

provider "aws" {
  region = var.aws_region
}
