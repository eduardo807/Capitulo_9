#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.base.res import res_request
from odoo.exceptions import ValidationError

class Tags(models.Model):
    _name= 'todo.task.tag'
    _parent_store = True
    #_parent_name  = 'parent_id'
    
    name = fields.Char(string= 'Name')
    parent_id     = fields.Many2one('todo.task.tag', string= 'Parent Tag', ondelete='restrict')
    parent_left   = fields.Integer(string= 'Parent Left', index=True)
    parent_right  = fields.Integer(string= 'Parent  Right', index=True)
    tag_ids = fields.Many2many( 'todo.task', # modelo relacionado
                            'todo_task_tag_rel', # nombre de la tabla de relación
                            'task_id', # campo para "este" registro
                            'tag_id', # campo para "otro" registro
                             string='Tasks')
    child_ids = fields.One2many('todo.task.tag', 'parent_id', string='Child Tags')
                             
class Stage(models.Model):
    _name = 'todo.task.stage'
    _order = 'sequence,name'
   
   # Campos de cadena de caracteres:
    name  = fields.Char(string= 'Name', size=40)
    desc  = fields.Text(string='Description')
    state = fields.Selection([('draft','New'),('open','Started'), ('done','Closed')], string='State')
    docs  = fields.Html(string= 'Documentation')

    # Campos numéricos:
    sequence = fields.Integer(string='Sequence')
    perc_complete = fields.Float(string= '% Complete', digits=(3,2))

    # Campos de fecha:
    date_effective = fields.Date(string='Effective Date')
    date_changed   = fields.Datetime(string='Last Changed')

    # Otros campos:
    fold  = fields.Boolean(string='Folded?')
    image = fields.Binary(string='Image')
    
    #Stage class relación con Tasks:
    tasks = fields.One2many('todo.task',# modelo relacionado
                            'stage_id',# campo para "este" en el modelo relacionado
                            string='Tasks in this stage')

class TodoTask(models.Model):
    _inherit = 'todo.task'
    
    stage_id = fields.Many2one('todo.task.stage', string='Stage')
    tag_ids = fields.Many2many('todo.task.tag', string='Tags')
    refers_to = fields.Reference([('res.user', 'User'),('res.partner', 'Partner')], string='Refers to')
    # ~ refers_to = fields.Reference(referencable_models, string='Refers to')
    
    def referencable_models(self):
        return res_request.referencable_model(self, self.env.cr, self.env.uid, context=self.env.context)
    
    stage_fold = fields.Boolean(
        string   = 'Stage Folded?',
        compute  ='_compute_stage_fold',
        search   ='_search_stage_fold',
        inverse  ='_write_stage_fold')
    
    def _search_stage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]

    def _write_stage_fold(self):
        self.stage_id.fold = self.stage_fold
        
        
    stage_state = fields.Selection(related='stage_id.state', string='Stage State')
    _sql_constraints = [
        ('todo_task_name_uniq',
         'UNIQUE (name, user_id, active)',
         'Task title must be unique!')]

    @api.one
    @api.constrains('name')
    def _check_name_size(self):
        if len(self.name) < 5:
            raise ValidationError('Must have 5 chars!')
            
    # ~ agregar el campo calculado correspondiente
    @api.one 
    def compute_user_todo_count(self):
        self.user_todo_count = self.search_count([('user_id', '=', self.user_id.id)])
        
    user_todo_count= fields.Integer(string='User To-Do   Count', compute='compute_user_todo_count')
    
    # ~ Esta vista presenta los datos en un gráfico de Gantt
    effort_estimate = fields.Integer('Effort Estimate')
