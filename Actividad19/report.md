# Reporte - Actividad 19

## Fases y Conceptos:

### Fase 0: Preparación e introducción:

1. ¿ Qué



### Fase 1: Fundamentos de terraform y primer recurso local

Después de haber ejecutado `terraform init`, se tuvo que modificar la ruta de ejecución de Python en `main.tf` de acuerdo al sistema operativo actual: EndeavourOS (ArchLinux Based) 



Ejecutamos `terraform apply` (sin parámetros), y se ejecuta directamente nuestro `main.tf` en el cual se intentará la creación de varios archivos. Lo que no sinteresa ahora es la creación de un directorio y un archivo .txt dentro de este: `./generated_environment/bienvenida.txt`:
```bash
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

random_id.entorno_id: Creating...
module.simulated_apps["app2"].data.template_file.app_config: Reading...
module.simulated_apps["app1"].data.template_file.app_config: Reading...
module.simulated_apps["app2"].data.template_file.app_config: Read complete after 0s [id=d878d3d4604c852e2a0a314ab697f727ebafe5d548d91feaa0b4e9ae469ba48e]
module.simulated_apps["app2"].null_resource.crear_directorio_app: Creating...
module.simulated_apps["app1"].null_resource.crear_directorio_app: Creating...
module.simulated_apps["app1"].data.template_file.app_config: Read complete after 0s [id=56be291dafa49a1b15250fb99db0c59fc4d49842ed0d7ed463eb608bd25bf975]
local_file.bienvenida: Creating...
local_file.bienvenida: Creation complete after 0s [id=e1c520d520bedc55e0bdb4f2806561b4fff3bd2c]
random_id.entorno_id: Creation complete after 0s [id=iTbLyui2ldc]
module.simulated_apps["app2"].null_resource.crear_directorio_app: Provisioning with 'local-exec'...
module.simulated_apps["app1"].null_resource.crear_directorio_app: Provisioning with 'local-exec'...
module.simulated_apps["app2"].null_resource.crear_directorio_app (local-exec): Executing: ["/bin/sh" "-c" "mkdir \"/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app2_v0.5.0/logs\""]
module.simulated_apps["app1"].null_resource.crear_directorio_app (local-exec): Executing: ["/bin/sh" "-c" "mkdir \"/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app1_v1.0.2/logs\""]
module.simulated_apps["app1"].null_resource.crear_directorio_app (local-exec): mkdir: cannot create directory ‘/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app1_v1.0.2/logs’: No such file or directory
module.simulated_apps["app2"].null_resource.crear_directorio_app (local-exec): mkdir: cannot create directory ‘/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app2_v0.5.0/logs’: No such file or directory
╷
│ Error: local-exec provisioner error
│ 
│   with module.simulated_apps["app1"].null_resource.crear_directorio_app,
│   on modules/application_service/main.tf line 13, in resource "null_resource" "crear_directorio_app":
│   13:   provisioner "local-exec" {
│ 
│ Error running command 'mkdir "/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app1_v1.0.2/logs"': exit status 1.
│ Output: mkdir: cannot create directory ‘/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app1_v1.0.2/logs’: No such
│ file or directory
│ 
╵
╷
│ Error: local-exec provisioner error
│ 
│   with module.simulated_apps["app2"].null_resource.crear_directorio_app,
│   on modules/application_service/main.tf line 13, in resource "null_resource" "crear_directorio_app":
│   13:   provisioner "local-exec" {
│ 
│ Error running command 'mkdir "/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app2_v0.5.0/logs"': exit status 1.
│ Output: mkdir: cannot create directory ‘/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app2_v0.5.0/logs’: No such
│ file or directory
│ 
╵

```

Notamos que, a pesar de algunos errores, ha creado satisfactoriamente `./generated_environment/bienvenida.txt` y lo verificamos con el comando `tree`:

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local(main)$ tree
.
├── generated_environment
│   └── bienvenida.txt
├── Instrucciones.md
├── main.tf
├── modules
│   ├── application_service
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   ├── templates
│   │   │   └── config.json.tpl
│   │   └── variables.tf
│   └── environment_setup
│       ├── main.tf
│       ├── scripts
│       │   └── initial_setup.sh
│       └── variables.tf
├── outputs.tf
├── scripts
│   ├── bash
│   │   ├── check_simulated_health.sh
│   │   └── start_simulated_service.sh
│   └── python
│       ├── generate_app_metadata.py
│       └── validate_config.py
├── terraform.tfstate
├── terraform.tfstate.backup
├── terraform.tfvars.example
├── variables.tf
└── versions.tf

10 directories, 20 files

```

### Fase 2:  Variables, archivos de configuración y scripts Bash

Como existen cambios que no debemos implementar, pues ya estaban implementados al haber clonado el proyecto, procedemos a modificar los necesarios: `./modules/environment_setup/variables.tf`:

```
variable "base_path" {
  description = "Ruta base para el entorno."
  type        = string
}

variable "nombre_entorno_modulo" {
  description = "Nombre del entorno para este módulo."
  type        = string
}
```

Esto se hace con el proposito de eliminar duplicados.
También debemos modificar `./variables.tf` para indicar la ruta del ejecutable de python.

Estos cambios implican que se deben de eliminar de los archivos que los contenían originalmente, sino aparecerá un error de variables duplicadas, similar al siguiente:
```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local(main)$ terraform validate
╷
│ Error: Duplicate variable declaration
│ 
│   on modules/application_service/variables.tf line 1:
│    1: variable "app_name" {
│ 
│ A variable named "app_name" was already declared at modules/application_service/main.tf:1,1-20. Variable names must be unique within a module.
╵

```

Como realizamos de manera apropiada, no aparece el error:

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local(main)$ terraform validate
Success! The configuration is valid.

```

### Fase 3: Módulos, plantillas y scripts Python

Hemos de realizar la ejecución:
```bash
  Enter a value: yes

module.simulated_apps["app2"].null_resource.crear_directorio_app: Destroying... [id=3182310132418018070]
module.simulated_apps["app1"].null_resource.crear_directorio_app: Destroying... [id=5835763325415123625]
local_file.bienvenida: Destroying... [id=e436565478c1f5f831abdaaffcef50ce003bf22d]
module.simulated_apps["app1"].data.template_file.app_config: Reading...
module.simulated_apps["app1"].null_resource.crear_directorio_app: Destruction complete after 0s
module.simulated_apps["app2"].data.template_file.app_config: Reading...
module.simulated_apps["app1"].data.template_file.app_config: Read complete after 0s [id=3b37df862d9907940f817df87f594bf3cd3eecbefc0104d74e4bcfb77129a7d2]
module.simulated_apps["app2"].data.template_file.app_config: Read complete after 0s [id=dbcc055623ddb577bcb3b700f8fa9ca7cff599641e66274e5c153a803b8f2f3e]
module.simulated_apps["app2"].null_resource.crear_directorio_app: Destruction complete after 0s
local_file.bienvenida: Destruction complete after 0s
module.simulated_apps["app1"].null_resource.crear_directorio_app: Creating...
module.simulated_apps["app2"].null_resource.crear_directorio_app: Creating...
module.simulated_apps["app1"].null_resource.crear_directorio_app: Provisioning with 'local-exec'...
module.simulated_apps["app2"].null_resource.crear_directorio_app: Provisioning with 'local-exec'...
module.simulated_apps["app1"].null_resource.crear_directorio_app (local-exec): Executing: ["/bin/sh" "-c" "mkdir -p \"/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app1_v1.0.2/logs\""]
module.simulated_apps["app2"].null_resource.crear_directorio_app (local-exec): Executing: ["/bin/sh" "-c" "mkdir -p \"/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app2_v0.5.0/logs\""]
module.simulated_apps["app2"].null_resource.crear_directorio_app: Creation complete after 0s [id=6138180089982325982]
module.simulated_apps["app1"].null_resource.crear_directorio_app: Creation complete after 0s [id=448741119112227064]
local_file.bienvenida: Creating...
local_file.bienvenida: Creation complete after 0s [id=2f7a1adc3f56856e09b93e7d530164d08e36519b]
module.simulated_apps["app1"].local_file.config_json: Creating...
module.simulated_apps["app1"].local_file.metadata_json: Creating...
module.simulated_apps["app2"].local_file.config_json: Creating...
module.simulated_apps["app2"].local_file.metadata_json: Creating...
module.simulated_apps["app1"].local_file.metadata_json: Creation complete after 0s [id=8cd8cf950696efab0dc7580ecb7fc26c4e56a610]
module.simulated_apps["app2"].local_file.config_json: Creation complete after 0s [id=05b9a225f1273d582cbe34862688c2ca7dfb09a6]
module.simulated_apps["app1"].local_file.config_json: Creation complete after 0s [id=debf115fda947edd4bd2ad15f0dae88ecf629b96]
module.simulated_apps["app2"].local_file.metadata_json: Creation complete after 0s [id=7040772f456c083d19709b03d4de2798381b5a19]
module.simulated_apps["app2"].null_resource.start_service_sh: Creating...
module.simulated_apps["app1"].null_resource.start_service_sh: Creating...
module.simulated_apps["app1"].null_resource.start_service_sh: Provisioning with 'local-exec'...
module.simulated_apps["app1"].null_resource.start_service_sh (local-exec): Executing: ["/bin/sh" "-c" "bash ./scripts/bash/start_simulated_service.sh 'app1' '/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app1_v1.0.2' '/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app1_v1.0.2/config.json'"]
module.simulated_apps["app2"].null_resource.start_service_sh: Provisioning with 'local-exec'...
module.simulated_apps["app2"].null_resource.start_service_sh (local-exec): Executing: ["/bin/sh" "-c" "bash ./scripts/bash/start_simulated_service.sh 'app2' '/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app2_v0.5.0' '/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app2_v0.5.0/config.json'"]
module.simulated_apps["app1"].null_resource.start_service_sh (local-exec): --- Iniciando servicio simulado: app1 ---
module.simulated_apps["app2"].null_resource.start_service_sh (local-exec): --- Iniciando servicio simulado: app2 ---
module.simulated_apps["app1"].null_resource.start_service_sh (local-exec): Ruta de instalación: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app1_v1.0.2
module.simulated_apps["app2"].null_resource.start_service_sh (local-exec): Ruta de instalación: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app2_v0.5.0
module.simulated_apps["app1"].null_resource.start_service_sh (local-exec): Archivo de configuración: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app1_v1.0.2/config.json
module.simulated_apps["app2"].null_resource.start_service_sh (local-exec): Archivo de configuración: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app2_v0.5.0/config.json
module.simulated_apps["app1"].null_resource.start_service_sh (local-exec): Servicio app1 'iniciado'. PID: 96571
module.simulated_apps["app2"].null_resource.start_service_sh (local-exec): Servicio app2 'iniciado'. PID: 96572
module.simulated_apps["app1"].null_resource.start_service_sh (local-exec): --- Fin inicio servicio app1 ---
module.simulated_apps["app2"].null_resource.start_service_sh (local-exec): --- Fin inicio servicio app2 ---
module.simulated_apps["app1"].null_resource.start_service_sh: Creation complete after 0s [id=1901191438832539047]
module.simulated_apps["app2"].null_resource.start_service_sh: Creation complete after 0s [id=4491449119680015808]
null_resource.validate_all_configs: Creating...
null_resource.validate_all_configs: Provisioning with 'local-exec'...
null_resource.validate_all_configs (local-exec): Executing: ["/bin/sh" "-c" "/usr/bin/python /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/scripts/python/validate_config.py /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services"]
null_resource.validate_all_configs (local-exec): {"validation_summary": "Validados 0 archivos de configuraci\u00f3n.", "errors_found": ["[/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app2_v0.5.0/config.json] Error al decodificar JSON.", "[/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app1_v1.0.2/config.json] Error al decodificar JSON."], "warnings_found": [], "detailed_report_lines": ["Archivo de resumen de validaci\u00f3n generado el 2025-05-28 06:47:24.777133", "L\u00ednea de sumario 0", "L\u00ednea de sumario 1", "L\u00ednea de sumario 2", "L\u00ednea de sumario 3", "L\u00ednea de sumario 4", "L\u00ednea de sumario 5", "L\u00ednea de sumario 6", "L\u00ednea de sumario 7", "L\u00ednea de sumario 8", "L\u00ednea de sumario 9", "L\u00ednea de sumario 10", "L\u00ednea de sumario 11", "L\u00ednea de sumario 12", "L\u00ednea de sumario 13", "L\u00ednea de sumario 14", "L\u00ednea de sumario 15", "L\u00ednea de sumario 16", "L\u00ednea de sumario 17", "L\u00ednea de sumario 18"]}
null_resource.validate_all_configs: Creation complete after 0s [id=4196198489395093146]
null_resource.check_all_healths: Creating...
null_resource.check_all_healths: Provisioning with 'local-exec'...
null_resource.check_all_healths (local-exec): Executing: ["bash" "-c" "      for service_dir in $(ls -d /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/*/); do\n        bash /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/scripts/bash/check_simulated_health.sh \"$service_dir\"\n      done\n"]
null_resource.check_all_healths (local-exec): --- Comprobando salud de: app1_v1.0.2 en /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app1_v1.0.2/ ---
null_resource.check_all_healths (local-exec): Servicio app1 (PID 96571) parece estar 'corriendo'.
null_resource.check_all_healths (local-exec): --- Salud OK para app1_v1.0.2 ---
null_resource.check_all_healths (local-exec): --- Comprobando salud de: app2_v0.5.0 en /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/services/app2_v0.5.0/ ---
null_resource.check_all_healths (local-exec): Servicio app2 (PID 96572) parece estar 'corriendo'.
null_resource.check_all_healths (local-exec): --- Salud OK para app2_v0.5.0 ---
null_resource.check_all_healths: Creation complete after 0s [id=4559886256812735467]

Apply complete! Resources: 11 added, 0 changed, 3 destroyed.

Outputs:

detalles_apps_simuladas = <sensitive>
id_entorno = "8936cbcae8b695d7"
ruta_bienvenida = "/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local/generated_environment/bienvenida.txt"
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local(main)$ 

```

Y podemos verificar que se ha creado el nuevo directorio y archivo

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local(main)$ tree ./generated_environment/
./generated_environment/
├── bienvenida.txt
└── services
    ├── app1_v1.0.2
    │   ├── app1.pid
    │   ├── config.json
    │   ├── logs
    │   │   ├── app1_startup.log
    │   │   └── app1_v1.0.2_health.log
    │   └── metadata_generated.json
    └── app2_v0.5.0
        ├── app2.pid
        ├── config.json
        ├── logs
        │   ├── app2_startup.log
        │   └── app2_v0.5.0_health.log
        └── metadata_generated.json

6 directories, 11 files
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local(main)$ 

```

### Fase 4: Validación y reportes (Python y Bash)

En el paso anterior hemos verificado que no se presentan errores, pero volvemos a ejecutar:

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local(main)$ terraform validate
Success! The configuration is valid.

amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local(main)$ 

```



## Ejercicios

### Ejercicio 3:

Modificamos el archivo `modules/environment_setup/scripts/initial_setup.sh` para tener la idempotencia y el contador de ejecuciones (reto adicional), implementandolos en el 

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local(main)$ cat modules/environment_setup/scripts/initial_setup.sh 
#!/bin/bash
# Script: initial_setup.sh
# Uso: initial_setup.sh <ENV_NAME> <README_PATH>

ENV_NAME=$1
README_PATH=$2

CONTROL_FILE="placeholder_control.txt"
COUNTER_FILE="setup_run_count.txt"

echo "Ejecutando setup inicial para entorno: $ENV_NAME"

# Si el control ya existe, salimos silenciosamente (idempotencia)
if [[ -f "$CONTROL_FILE" ]]; then
  echo "Encontrado $CONTROL_FILE → nada que hacer."
  exit 0
fi

echo "Control no encontrado; ejecutando acciones iniciales…"

# Acción real solo la primera vez
echo "Creando $CONTROL_FILE y placeholder_*.txt"
touch "$CONTROL_FILE"
touch "placeholder_$(date +%s).txt"

# Registrar en log estándar
echo "Fecha de setup: $(date)" > setup_log.txt
echo "README se encuentra en: $README_PATH"  >> setup_log.txt

# Algoritmo: incrementar contador de ejecuciones
if [[ -f "$COUNTER_FILE" ]]; then
  count=$(<"$COUNTER_FILE")
  ((count++))
else
  count=1
fi
echo "$count" > "$COUNTER_FILE"
echo "Ejecuciones acumuladas: $count" >> setup_log.txt

# Simular pasos extra
for i in {1..20}; do
  echo "Paso simulado $i…" >> setup_log.txt
done

echo "Setup inicial COMPLETADO."

amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad19/Proyecto_iac_local(main)$ 

```

