2)-Instalar Odoo desde el código fuente:

Primero, asegúrese que ha accedido con el usuario creado anteriormente, o
durante el proceso de instalación, y no como root.

Ahora es posible usar este script. Muestra como instalar Odoo :

$ sudo apt-get update & sudo apt-get upgrade # Instala las actualizaciones del sistema
$ sudo apt-get install git # Instala Git
$ mkdir ~/libro_odoo # Crear el directorio de trabajo
$ cd ~/libro_odoo # Ingresar en el directorio de trabajo
$ git clone https://github.com/odoo/odoo.git -b 10.0 # Obtiene el código fuente de Odoo
$ sudo apt-get install postgres# Instala PostgreSQL y el usuario administrador para un usuario Unix

Al finalizar, Odoo estará listo para ser usado. El símbolo ~ es un atajo para su directorio 
raíz (por ejemplo, /home/odoo). La opción git -b 10.0 explícitamente solicita descargar la rama 10.0 
de Odoo. En el momento de escribir éste libro se utilizo odoo 8,pero ésto puede cambiar, lo que hará 
más flexible lo aquí descrito.

2.1)-Inicializar una base de datos nueva en Odoo:

Para poder crear una base de datos nueva, su usuario debe ser un superusuario de PostgreSQL

$ sudo postgres

Para crear una base de datos nueva use el comando createdb. Cree la base de datos v8dev:

$ createdb v8dev

2.2)-Gestionar la base de datos:

Ya sabe como usar el comando createdb para crear una base de datos vacía, pero también puede crear 
una base de datos copiando una existente, usando la opción --template.

Asegúrese que su instancia de Odoo este detenida y no tenga otra conexión abierta con la base 
de datos v8dev creada anteriormente, y ejecute:

$ createdb --template = v8dev v8test

Para listar las bases de datos existentes en su sistema use la utilidad psql de PostgreSQL con la opción -l:

$ psql -l

Para eliminar una base de datos que ya no necesite (o necesita crear nuevamente), use el comando dropdb:

$ dropdb v8test

Ahora ya conoce lo básico para trabajar con varias bases de datos.

2.3)-Unas palabras sobre las versiones de Odoo:

A la fecha de publicación, la última versión estable de Odoo es la 8, marcada en GitHub como branch 8.0. Ésta 
es la versión con la que se trabajará a lo largo de éste libro.

Es importante saber que las bases de datos de Odoo son incompatibles entre versiones principales de Odoo. Esto 
significa que si ejecuta un servidor Odoo 8 contra una base de datos Odoo/OpenERP 7, no funcionará. Es necesario 
un trabajo de migración significativo para que una base de datos pueda ser usada con una versión más reciente del producto.

2.4)-Cambiar el puerto de escucha:

El comando --xmlrpc-server=<port> permite cambiar el puerto predeterminado 8069 desde donde la instancia del 
servidor escucha las peticiones. Esto puede ser usado para ejecutar más de una instancia al mismo tiempo, en el mismo servidor.

Intentemos esto. Abra dos ventanas de la terminal. En la primera ejecute:

$ ~ / odoo-dev / odoo.py --xmlrpc-port = 8070

y en la otra ejecute:

$ ~ / odoo-dev / odoo.py --xmlrpc-port = 8071

Y allí lo tiene: dos instancias de Odoo en el mismo servidor escuchando a través de diferentes puertos

