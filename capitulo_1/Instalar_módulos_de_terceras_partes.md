4)-Instalar módulos de terceras partes:

Hacer que nuevos módulos estén disponibles en una instancia de Odoo para que puedan 
ser instalados es algo que puede resultar confuso para las personas nuevas. Pero no 
necesariamente tiene que ser así, así que a continuación se desmitificará esta suposición.

4.1)-Encontrar módulos de la comunidad:

Existen muchos módulos para Odoo disponibles en Internet. El sitio web https://www.odoo.com/apps 
es un catalogo de módulos que pueden ser descargados e instalados. La Odoo Community Association (OCA) 
coordina las contribuciones de la comunidad y mantiene unos pocos repositorios en GitHub, en https://github.com/OCA.

4.2)-Configurar la ruta de complementos:

El servidor Odoo tiene una opción llamada addons-path que define donde buscar los módulo. De forma 
predeterminada este apunta al directorio /addons del servidor Odoo que se esta ejecutando.

Afortunadamente, es posible asignar no uno, sino una lista de directorios donde se pueden encontrar 
los módulos. Esto permite mantener los módulos personalizados en un directorio diferente, sin mezclarlos 
con los complementos oficiales. Se ejecutará el servidor con una ruta de complemento incluyendo el nuevo directorio de módulos:

$ cd ~ / odoo-dev / odoo
$ ./odoo.py -d v8dev --addons-path = ”/ department,. / addons”

4.3)Actualizar la lista de módulos:

Es necesario pedirle a Odoo que actualice su lista de módulos antes que estos módulos 
nuevos estén disponibles para ser instalados.

Para esto es necesario habilitar el menú Técnico, debido a que esta provee la opción de 
menú Actualizar Lista de Módulos. Esta puede ser encontrada en la sección Módulos en el menú Configuración.

Luego de ejecutar la actualización de la lista de módulos se puede confirmar que los módulos 
nuevos están disponibles para ser instalados. En la lista de Módulos Locales, quite el filtro 
de Aplicaciones en línea y busque department. Debería poder ver los nuevos módulos disponibles.
