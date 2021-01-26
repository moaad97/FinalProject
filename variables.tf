variable "image_id" {
  type        = string
  description = "The id of the machine image (AMI) to use for the server." 

  validation {
    condition     = length(var.image_id) > 4 && substr(var.image_id, 0, 4) == "ami-"
    error_message = "The image_id value must be a valid AMI id, starting with \"ami-\"."
  }
}

variable "access_key_var" {
  type        = string
  default = "AKIAVI7ZKT6NGOXZZE7V"
}

variable "secret_key_var" {
  type        = string
  default = "0ezZ8xyISVeIGk332g9foAetb9JwGVT3ThmnJVAL"
}

variable "subnets" {
    type = list
    default = ["10.30.1.0/24", "10.30.10.0/24"]
}

