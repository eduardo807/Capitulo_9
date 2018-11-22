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

#~ configuramos el acceso a los métodos del servidor que necesitan un inicio de sesión para acceder. Estos se exponen en el punto final de / xmlrpc / 2 / object
api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % srv)
print api.execute_kw(db, uid, pwd, 'res.partner', 'search_count', [[]])
print api.execute_kw(db, uid, pwd, 'res.partner', 'read', [[43]], {'fields': ['id', 'name', 'parent_id']})
print api.execute_kw(db, uid, pwd, 'res.partner', 'search_read', [[('country_id', '=',    'be'), ('parent_id', '!=', False)]], {'fields': ['id', 'name', 'parent_id']})


