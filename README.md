# Working in project

![Esta es una imagen de ejemplo](assets/remote-working.png)

# RUN DOCKER

Para ingresar a la terminal del contenedor, puedes usar el siguiente comando:

docker run -it <nombre_imagen> /bin/bash
Por ejemplo, si el nombre de la imagen es python-project, puedes usar el siguiente comando para ingresar a la terminal:

docker run -it python-project /bin/bash
Una vez que estés en la terminal del contenedor, podrás ejecutar los comandos de Python como lo harías en una máquina local.

Aquí hay un ejemplo de cómo usar este Dockerfile:

Crea un nuevo directorio para tu proyecto y crea un archivo Dockerfile con el contenido anterior.
Copia tu código Python al directorio del proyecto.
Ejecuta el siguiente comando para crear la imagen:
docker build -t python-project .
Ejecuta el siguiente comando para iniciar un contenedor de la imagen:
docker run -it python-project
Ingresa a la terminal del contenedor usando el comando /bin/bash.
Ejecuta tu código Python usando el comando python3 main.py.

docker run -it <image>:<image_tag> <command>
