# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # ~ el atributo name es obligatorio
    'name' : 'To-do application',
    # ~ description, para una descripción más larga
    'description': 'Manage your personal Tasks with this module.',
    # ~ author: La persona creador del modulo
    'author': 'Eduardo Morillo',
    # ~ El atributo depends puede tener una lista de otros módulos requeridos
    'depends' : ['base', 'mail'],
    # ~ data. Este define la lista de archivos que son cargados por el módulo
    'data': [
             "view/todo_view.xml",
             "security/ir.model.access.csv",
             "security/todo_access_rules.xml"
             ],
             
    # ~ appilcation, la colocamos en True para indicar que nuestro modulo es una aplicacion.
    'application': True,
}
