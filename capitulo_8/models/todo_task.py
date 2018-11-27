# -*- coding: utf-8 -*-

from odoo import models, fields

class TodoTask(models.Model):
    _inherit = 'todo.task'
    
    # ~ Los dos campos que son frecuentemente usados en las vistas kanban son: priority y kanban state
    
    priority = fields.Selection([
                                ('0','Low'),
                                ('1','Normal'),
                                ('2','High')],
                                string= 'Priority',default='1')
                                
    kanban_state = fields.Selection([
                                    ('normal', 'In Progress'),
                                    ('blocked', 'Blocked'),
                                    ('done', 'Ready for next stage')],
                                    string='Kanban State', default='normal')
