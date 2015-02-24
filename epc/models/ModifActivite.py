# -*- coding: utf-8 -*-
from openerp import fields, models, api

class ModifActivite(models.Model):
    _name = 'epc.modifactivite'

    activity_id = fields.Many2one('epc.activiteinfo', string="activite")
    state = fields.Selection([
         ('draft', "Draft"),
         ('canceled', "Canceled"),
         ('done', "Done"),
    ], default='draft')
    vol1_total = fields.Float(default=0)
    vol1_q1 = fields.Float(default=0)
    vol1_q2 = fields.Float(default=0)
    vol1_coeff = fields.Integer(default=0)
    vol2_total = fields.Float(default=0)
    vol2_q1 = fields.Float(default=0)
    vol2_q2 = fields.Float(default=0)
    vol2_coeff = fields.Integer(default=0)

    @api.one
    def action_cancel(self):
        self.state = 'canceled'
        
    @api.one
    def action_done(self):
        self.activity_id.vol2_coeff = self.vol1_total
        self.activity_id.vol2_q2 = self.vol1_q1
        self.activity_id.vol2_q1 = self.vol1_q2
        self.activity_id.vol2_total = self.vol1_coeff
        self.activity_id.vol1_coeff = self.vol2_total
        self.activity_id.vol1_q2 = self.vol2_q1
        self.activity_id.vol1_q1 = self.vol2_q2
        self.activity_id.vol1_total = self.vol2_coeff
        self.state = 'done'
