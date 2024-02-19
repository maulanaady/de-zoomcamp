variable "credentials" {
  default = "./keys/service-account.json"
}

variable "project" {
  type    = string
  default = "graphite-scout-414507"
}

variable "region" {
  type    = string
  default = "asia-southeast2"
}

variable "gcs_bucket_name" {
  type    = string
  default = "terraform_zoomcamp_data"
}

variable "location" {
  type    = string
  default = "asia-southeast2"
}

variable "bq_dataset_name" {
  type    = string
  default = "zoomcamp_dataset"
}