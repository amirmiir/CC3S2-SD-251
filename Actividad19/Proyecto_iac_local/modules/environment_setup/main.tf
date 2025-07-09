resource "null_resource" "crear_directorio_base" {
  provisioner "local-exec" {
    command = "mkdir -p ${var.base_path}/${var.nombre_entorno_modulo}_data"
  }
  triggers = {
    dir_name = "${var.base_path}/${var.nombre_entorno_modulo}_data"
  }
}

resource "local_file" "readme_entorno" {
  depends_on = [null_resource.crear_directorio_base]
  content    = "Este es el entorno ${var.nombre_entorno_modulo}. ID: ${random_id.entorno_id_modulo.hex}"
  filename   = "${var.base_path}/${var.nombre_entorno_modulo}_data/README.md"
}

resource "random_id" "entorno_id_modulo" {
  byte_length = 4
}

resource "null_resource" "ejecutar_setup_inicial" {
  depends_on = [local_file.readme_entorno]

  triggers = {
    readme_md5     = local_file.readme_entorno.content_md5
    setup_revision = var.setup_revision # ← nuevo
    script_sha256  = filesha256("${path.module}/scripts/initial_setup.sh")
  }

  provisioner "local-exec" {
    command     = "bash ${abspath("${path.module}/scripts/initial_setup.sh")} '${var.nombre_entorno_modulo}' '${local_file.readme_entorno.filename}'"
    interpreter = ["bash", "-c"]
    working_dir = "${var.base_path}/${var.nombre_entorno_modulo}_data"
  }
}


output "ruta_readme_modulo" {
  value = local_file.readme_entorno.filename
}
