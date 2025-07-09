variable "base_path" {
  description = "Ruta base para el entorno."
  type        = string
}

variable "nombre_entorno_modulo" {
  description = "Nombre del entorno para este módulo."
  type        = string
}

# modules/environment_setup/variables.tf
variable "setup_revision" {
  description = "Valor que, al cambiar, vuelve a ejecutar initial_setup.sh."
  type        = string
}
