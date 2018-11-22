# -*- coding: utf-8 -*-

#~ Aquí, importamos la biblioteca xmlrpclib
import xmlrpclib

#~ Configuramos algunas variables con la información para la ubicación del servidor y las credenciales de conexión
srv, db = 'http://192.168.1.106:8069', 'odoo'
user, pwd = 'admin', 'admin'

#~ configuramos el acceso a los servicios públicos del servidor, expuestos en /xmlrpc/2/common.
common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % srv)

#~ Lo usamos para confirmar que podemos comunicarnos con el servidor.
print common.version()

#~ Este método confirma que el nombre de usuario y la contraseña son aceptados y devuelve el ID de usuario que debe usarse en las solicitudes
uid = common.authenticate(db, user, pwd, {})
print uid
