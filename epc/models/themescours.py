# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError

class ThemeCours(models.Model):
    _name = 'epc.theme'
    _description = "Theme"
    
    name = fields.Char()
