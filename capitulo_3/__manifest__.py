# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Multiuser To-Do',
    'description': 'Extend the To-Do app to multiuser.',
    'author': 'Eduardo Morillo',
    'depends': ['todo_app'],
    'data': [
    'view/todo_view.xml',
    'security/todo_access_rules.xml'
             ],

}
