###Шиянова Катерина
variable "architecture" {
  type        = string
  default     = "x86_64"
  description = "Architecture of your AMI: can be arm64, or x86_64"
}

variable "manifest_file_name" {
  type        = string
  default     = "manifest.json"
  description = "Manifest file name"
}

variable "http_port" {
  type        = string
  default     = "8081"
  description = "Default port for nginx docker"
}
locals {
  tags = {
    Name   = "packer-${var.architecture}"
    Hillel = "Lesson 20"
  }

  timestamp = formatdate("YYYYMMDDhhmm", timestamp())
}
