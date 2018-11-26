1)-Configurar una computadora como servidor Odoo:

Preferimos usar sistemas Debian/Ubuntu para el servidor Odoo, aunque puede trabajar
desde el sistema operativo de su preferencia, sea Windows, Macintosh, o Linux.

En este capítulo, se aprenderá a configurar y trabajar con Odoo sobre un sistema Ubuntu

Nota

Tenga en cuenta que estas instrucciones tienen como objetivo configurar un nuevo sistema
para desarrollo. Si desea probarlas en un sistema existente, haga un respaldo a tiempo 
que le permita recuperar el sistema en caso de algún problema.


1.1)-Disposiciones para un equipo Debian:

Si ingresa usado root, su primera tarea será crear un usuario para ser usado en el trabajo 
cotidiano, ya que es considerada una mala práctica trabajar como root. Particularmente, el 
servidor Odoo se rehusará a ejecutarse si está usando root.

Si está usando Ubuntu, probablemente no necesite esto ya que el proceso de instalación le 
habrá guiado en la creación de un usuario personal.

1.2)-Creando una cuenta de usuario para Odoo:

Primero, asegúrese que sudo este instalado. Su usuario de trabajo lo necesitará. Si ha 
accedido como root ejecute los siguientes comandos:

$ apt-get update & apt-get upgrade # Instalar actualizaciones del sistema
$ apt-get install sudo # Asegurarse que 'sudo' esta instalada

Los siguientes comandos crearán un usuario odoo:

$ useradd -m -g sudo -s / bin / bash odoo # Crea un usuario 'Odoo' con poderes sudo
$ passwd odoo # Solicita y configura una contraseña para el nuevo usuario

Puede cambiar odoo por cualquier nombre que desee. La opción -m crea el directorio home. 
El -g sudo agrega al nuevo usuario a la lista de usuarios sudo, por lo tanto podrá ejecutar 
comandos como root, y -s /bin/bash configura la línea de comando predeterminada a bash, la 
cual es mas amigable de usar que la fijada por omisión estándar sh.
