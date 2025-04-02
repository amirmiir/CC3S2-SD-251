### Estructura de archivos y directorios para proyecto hipotético
Fuente de referencia: https://developer.hashicorp.com/terraform/language/modules/develop/structure 

$ tree complete-module/
.
├── README.md
├── main.tf
├── variables.tf
├── outputs.tf
├── ...
├── modules/
│   ├── network/
│   │   ├── README.md
│   │   ├── ...
│   ├── database/
│   │   ├── README.md
│   │   ├── ...
│   ├── application/
│   │   ├── README.md
│   │   ├── ...
│   ├── .../
├── examples/
│   ├── exampleA/
│   │   ├── main.tf
│   ├── exampleB/
│   ├── .../

