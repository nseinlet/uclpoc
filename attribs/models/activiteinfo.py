# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ActiviteInfo(models.Model):
    _inherit = 'epc.activiteinfo'
    
    attribution_ids = fields.One2many(related=('activity_id', 'attribution_ids'), string="attributions")
