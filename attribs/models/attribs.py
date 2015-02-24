# -*- coding: utf-8 -*-

from openerp import models, fields, api

class attribs(models.Model):
    _name = 'attribs.attribs'

    personne_id = fields.Many2one('res.partner', string="Attribue à", domain="[('is_personnelacademique', '=', True)]")
    activity_id = fields.Many2one('epc.activite')
    fonction = fields.Selection([('COORD','Coordinateur'), ('COTIT','Cotitulaire')])
    attrib_start = fields.Date(string="Date debut")
    attrib_end = fields.Date(string="Date fin")
    vol1 = fields.Integer(string = "Heures de cours magistraux")
    vol2 = fields.Integer(string = "Heures de cours TP")
