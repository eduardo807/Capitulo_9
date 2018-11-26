#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessDenied, AccessError, UserError, ValidationError

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread'] # El atributo _inherit le dice a Odoo que esta clase hereda el modelo todo.task y mail.thread, el modelo mail.thread es un modelo abstracto. 
    
    # ~ El user_id representa un usuario desde el modelo Users, res.users
    user_id = fields.Many2one('res.users', string= 'Responsible')
    # ~ El date_deadline es un simple campo de fecha
    date_deadline = fields.Date(string= 'Deadline')
    # ~ para agregar un comentario de ayuda al campo name
    name = fields.Char(help="What needs to be done?")
    
    @api.multi
    def do_clear_done(self):
        domain = [('is_done', '=', True), '|', ('user_id', '=', self.env.uid), ('user_id', '=', False)] #El filtro de búsqueda sigue una sintaxis especial de Odoo referida como domain.
        done_recs = self.search(domain)
        done_recs.write({'active': False})
        return True
        # ~ Se modifico para que borre solo las tareas del usuario actual.

    @api.one
    def do_toggle_done(self):
        if self.user_id != self.env.user:
            raise UserError('Only the responsible can do this!')
        else:
            return super(TodoTask, self).do_toggle_done()
        # ~ Ahora solo ejecuta la acción sobre las Tareas asignadas a nuestro usuario.


