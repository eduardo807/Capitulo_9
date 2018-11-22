# -*- coding: utf-8 -*-

import  xmlrpclib

#~ Crearemos una clase para configurar la conexión y almacenar su información.
#~ Aquí almacenamos en el objeto creado toda la información necesaria para ejecutar llamadas en un modelo
class NoteAPI():

    def __init__(self, srv, db, user, pwd):

        common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % srv)
        self.api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % srv)
        self.uid = common.authenticate(db, user, pwd, {})
        self.pwd = pwd
        self.db = db
        self.model = 'todo.task'
        
    def execute(self, method, arg_list, kwarg_dict=None):
        return self.api.execute_kw(
                               self.db,
                               self.uid,
                               self.pwd,
                               self.model,
                               method,
                               arg_list,
                               kwarg_dict or {})
 
#~ El método get() aceptará una lista opcional de ID para recuperar.
    def get(self, ids=None):
        domain = []
        if ids:
            domain = [('id', 'in', ids)]
        fields = ['id', 'name']
        return  self.execute('search_read', [domain, fields])
  
#~ El método set () tendrá como argumentos el texto de la tarea para escribir y una identificación opcional.
#~ Si no se proporciona la identificación, se creará un nuevo registro.
    def set(self, text, id=None):
        if id:
            self.execute('write', [[id], {'name': text}])
        else:
            vals = {'name': text, 'user_id': self.uid}
            id = self.execute('create', [vals])

#~ Terminemos el archivo con un pequeño fragmento de código de prueba que se ejecutará si ejecutamos el archivo Python
if  __name__    ==  '__main__':
    srv, db = 'http://192.168.1.106:8069', 'odoo'
    user, pwd = 'admin', 'admin'
    api =  NoteAPI(srv, db, user, pwd)
    from pprint import pprint
    pprint(api.get())
        
