# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Activite(models.Model):
    _inherit = 'epc.activite'
    
    attribution_ids = fields.One2many('attribs.attribs', 'activity_id', string="attributions")
