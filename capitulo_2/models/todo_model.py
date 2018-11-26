#-*- coding: utf-8 -*-
# ~ La primera línea le dice al interprete de Python que ese archivo es UTF-8, por lo que puede manejar y esperarse caracteres non-ASCII

# ~hace que estén disponibles los modelos y campos del núcleo de Odoo.
from odoo import models, fields, api

# ~ Es una clase derivada de models.Model
class TodoTask(models.Model):
    _name = 'todo.task'  # definiendo el identificador que será usado por Odoo para referirse a este modelo
    
     # ~ los campos del modelo. Vale la pena señalar que name y active son nombres de campos especiales
    name = fields.Char(string= 'Description', required=True)
    is_done = fields.Boolean(string= 'Done?')
    active = fields.Boolean(string= 'Active?', default=True)
    
    # ~ usamos el decorador @api.one, Aquí self representara un registro
    @api.one 
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True
    # ~ Como puede observar, simplemente modifica el campo is_done, invirtiendo su valor

    # ~ usamos el decorador @api.multi el self representa un conjunto de registros
    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True
    # ~ Este debe buscar todos los registros activos que estén finalizados, y desactivarlos
