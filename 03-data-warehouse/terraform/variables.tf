variable "credentials" {
  description = "My Credentials"
  default     = "./service-account-gcp.json"
}

variable "project" {
  description = "Project"
  default     = "graphite-scout-414507"
}

variable "region" {
  type        = string
  description = "The default compute region"
  default     = "asia-southeast2"
}

variable "location" {
  type    = string
  default = "asia-southeast2"
}

variable "gcs_bucket_dir_name" {
  description = "Storage Bucket Directory Name for Week-3 Homework"
  default     = "green-taxi-data"
}


variable "bq_dataset_name" {
  type    = string
  default = "week_3_zoomcamp_dataset"
}


variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}