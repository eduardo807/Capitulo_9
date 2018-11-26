3)-Usar un editor de texto Linux:

Tarde o temprano, será necesario editar archivos desde la línea de comandos. 
En muchos sistemas Debian el editor de texto predeterminado es vi. Si no se 
siente a gusto con éste, puede usar una alternativa más amigable. En sistemas 
Ubuntu el editor de texto predeterminado es nano. Puede que prefiera usar éste 
ya que es más fácil de usar. En caso que no esté disponible en su servidor, puede 
instalarlo con:

$ sudo apt-get install nano

En las siguientes secciones se asumirá como el editor de preferencia. Si prefiere 
cualquier otro editor, siéntase libre de adaptar los comandos de acuerdo a su elección.

3.1)-Instalar y configurar Samba:

El proyecto Samba proporciona a Linux servicios para compartir archivos compatibles con 
sistemas Microsoft Windows. Se puede instalar en el servidor Debian/Ubuntu con:

$ sudo apt-get install samba samba-common-bin

3.2)-Habilitar las herramientas técnicas:

Odoo incluye algunas herramientas que son muy útiles para las personas que desarrollan, y 
haremos uso de estas a lo largo del libro. Estas son las Características Técnicas y el Modo de Desarrollo.

Estas están deshabilitadas de forma predeterminada, así que aprenderemos como habilitarlas.

3.3)-Activar las Características Técnicas
Las Características Técnicas proporcionan herramientas avanzadas de configuración del servidor.

Estas están deshabilitadas de forma predeterminada, y para habilitarlas, es necesario acceder con el 
usuario Administrador. En el menú Configuración, seleccione Usuarios y edite el usuario Administrador. 
En la pestaña Derechos de Acceso, encontrará una casilla de selección de Características Técnicas. 
Seleccione esa casilla y guarde los cambios.

Ahora es necesario recargar la página en el navegador web. Deberá poder ver en el menú Configuraciones 
una nueva sección Técnico que da acceso a lo interno del servidor Odoo

3.4)-Activar el modo de Desarrollo:

Para habilitarlo, abra el menú desplegable en la esquina superior derecha de la ventana del navegador, 
en el nombre de usuario, y seleccione la opción Acerca de Odoo. En la ventana de dialogo Acerca de, haga 
clic sobre el botón Activar modo desarrollador en la esquina superior derecha.
