# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError

class Activite(models.Model):
    _name = 'epc.activite'
    _inherit = 'mail.thread'
    _description = "Activite"
    
    name = fields.Char(compute='_compute_name', store=True)
    activity_ids = fields.One2many('epc.activiteinfo', 'activity_id')
    ens_debut = fields.Integer()
    ens_fin = fields.Integer()
    cahiercharge_ids = fields.One2many('epc.cahiercharge', 'activity_id', string="Cahiers de charge")
    
    @api.one
    @api.depends('ens_debut','ens_fin')
    def _compute_name(self):
        self.name = "%s-%s" % (self.ens_debut if self.ens_debut else "", self.ens_fin if self.ens_fin else "")
