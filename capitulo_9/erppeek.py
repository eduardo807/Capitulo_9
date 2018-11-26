# -*- coding: utf-8 -*-


import  erppeek
api = erppeek.Client('http://192.168.1.110:8069', 'odoo', 'admin', 'admin')
api.common.version()
api.count('res.partner', [])
api.search('res.partner', [('country_id', '=', 'be'), ('parent_id', '!=', False)])
api.read('res.partner', [43], ['id',  'name', 'parent_id'])

#~ Tenemos las siguientes dos formas alternativas de obtener una instancia para un modelo,
#~ ya sea utilizando el método model () o accediendo a un atributo en el caso de camello
m = api.model('res.partner')
m = api.ResPartner

#~ Ahora podemos realizar acciones en ese modelo
m.count([('name', 'like', 'Packt%')])
m.search([('name', 'like', 'Packt%')])

#~ También proporciona representación de objetos del lado del cliente para los registros 
recs = m.browse([('name', 'like', 'Packt%')])
recs <RecordList 'res.partner,[76]'>
recs.name ['Packt']

#~ Al abrir una línea de comando, podemos echar un vistazo a las opciones disponibles
erppeek --help

#~ sesión de muestra:
#~ se realizó una conexión con el servidor y el contexto de ejecución proporcionó una referencia al método model()
#~ para obtener instancias del modelo y realizar acciones en ellas
erppeek --server='http://192.168.1.110:8069' -d odoo -u admin
Usage (some commands): models(name)
# List models matching pattern model(name)
# Return a Model instance (...)
Password for 'admin':
Logged in as 'admin' odoo
model('res.users').count()
rec = model('res.partner').browse(43)
rec.name 'Michel Fletcher'
