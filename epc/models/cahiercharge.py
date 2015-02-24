# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError

class CahierCharge(models.Model):
    _name = 'epc.cahiercharge'
    _inherit = 'mail.thread'
    _description = "Cahier de charge"
    
    validite = fields.Integer('Validite')
    activity_id = fields.Many2one('epc.activite', string="Activite")
    langue = fields.Char()
    competences = fields.Html("Compétence à aquérir")
    theme_ids = fields.Many2many('epc.theme')
    prerequis = fields.Html("Prérequis")
    
    _sql_constraints = [('activlang_uniq', 'unique(activity_id,langue)', 'Cahier de charge must be unique by language-activity!')]
