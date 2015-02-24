# -*- coding: utf-8 -*-
from openerp import fields, models

class PersonneAcademique(models.Model):
    _inherit = 'res.partner'

    is_personnelacademique = fields.Boolean(string="Personnel academique")
    datenaissance = fields.Date(string="Date de naissance")
