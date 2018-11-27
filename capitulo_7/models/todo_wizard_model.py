# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import exceptions # will be used in the code
import logging

class   TodoWizard(models.TransientModel):
    _name = 'todo.wizard'
    
    # ~ definirá los tres campos que necesitamos
    
    task_ids = fields.Many2many('todo.task', string='Tasks')
    new_deadline = fields.Date(string='Deadline to Set')
    new_user_id  = fields.Many2one('res.users',string='Responsible to Set')
    
    # ~ Luego necesitamos implementar las acciones ejecutadas al hacer clic en el botón “Mass Update”
    
    @api.multi 
    def do_mass_update(self):
        self.ensure_one()
        if not (self.new_deadline   or self.new_user_id):
            raise  exceptions.ValidationError('No data to    update!') #
        else:
            _logger.debug('Mass update on Todo Tasks %s',self.task_ids.ids)
            if self.new_deadline:
                self.task_ids.write({'date_deadline': self.new_deadline})
                if self.new_user_id:
                    self.task_ids.write({'user_id': self.new_user_id.id})
                    return True
    
     # ~ Aunque no es la mejor interfaz, nos aprovechamos de esto para mostrar un mensaje en el botón “Count”:
    @api.multi
    def do_count_tasks(self):
        Task  = self.env['todo.task']
        count = Task.search_count([])
        raise exceptions.Warning('There are %d active tasks.' % count)
        
    @api.multi
    def do_populate_tasks(self):
        self.ensure_one()
        Task = self.env['todo.task']
        all_tasks = Task.search([])
        self.task_ids   = all_tasks       # reopen wizard form on same wizard record
        return self.do_reopen_form()
