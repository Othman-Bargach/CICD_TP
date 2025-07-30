//--- Providers ---
terraform {
    backend "s3" {
        bucket = "terraform-tp-devops"
        key = "terraform/terraform.tfstate"
        region = "eu-west-1"
    }
}