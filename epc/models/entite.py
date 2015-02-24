# -*- coding: utf-8 -*-

from openerp import models, fields, api

class entite(models.Model):
    _name = 'epc.entite'
    _inherit = 'mail.thread'
    
    name = fields.Char(required=True)
    validity_start = fields.Datetime()
    validity_end = fields.Datetime()
    parent_id = fields.Many2one('epc.entite', string='Parent entity', select=True, ondelete='restrict')
    child_ids = fields.One2many('epc.entite', 'parent_id', string='Child Entities')
    parent_left = fields.Integer('Left Parent', select=1)
    parent_right = fields.Integer('Right Parent', select=1)
    activites_charge_ids = fields.One2many('epc.activiteinfo', 'entity_id', string='Cours en charge')
    activites_attrib_ids = fields.One2many('epc.activiteinfo', 'entity_attrib_id', string='Cours en charge')
    
    _parent_name = "parent_id"
    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'
    
    #name_abrege = fields.Char()
    
