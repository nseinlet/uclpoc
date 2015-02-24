# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError

class ActiviteInfo(models.Model):
    _name = 'epc.activiteinfo'
    _inherit = 'mail.thread'
    _description = "Activite Info"
    
    name = fields.Char('Intitulé abrégé')
    intitulecomplet = fields.Char('Intitulé complet')
    code = fields.Char(compute='_compute_code',store=True,select=1)
    site = fields.Char(compute='_compute_site')
    validite = fields.Integer('Validity')
    sigle = fields.Char('Sigle', required=True)
    cnum = fields.Integer('CNum', required=True)
    subdivision = fields.Char('Subdivision')
    type_activite = fields.Selection([('COURS', 'Cours'), ('PARTIM', 'Partim'), ('THESE', 'Thèse'), ('CLASSE', 'Classe')])
    active = fields.Boolean(default=True)
    entity_id = fields.Many2one('epc.entite', string='Entite Charge', ondelete="restrict")
    entity_attrib_id = fields.Many2one('epc.entite', string="Entite attribution", ondelete="restrict")
    validity_start = fields.Datetime(related=('entity_id', 'validity_start'), string="Debut de validite")
    validity_end = fields.Datetime(related=('entity_id', 'validity_end'), string="fin de validite")
    poids = fields.Float()
    langue = fields.Char()
    vol1_total = fields.Float(default=0)
    vol1_q1 = fields.Float(default=0)
    vol1_q2 = fields.Float(default=0)
    vol1_coeff = fields.Integer(default=0)
    vol2_total = fields.Float(default=0)
    vol2_q1 = fields.Float(default=0)
    vol2_q2 = fields.Float(default=0)
    vol2_coeff = fields.Integer(default=0)
    cahiercharge_ids = fields.One2many(related=('activity_id', 'cahiercharge_ids'), string="Cahiers de charge")
    activity_id = fields.Many2one('epc.activite',string="Activite")
    ens_debut = fields.Integer(related=('activity_id', 'ens_debut'))
    ens_fin = fields.Integer(related=('activity_id', 'ens_fin'))
    
    @api.constrains('vol1_total')
    def _check_total_q1(self):
        for record in self:
            if round(record.vol1_q1 + record.vol1_q2 - record.vol1_total,2)!=0 and (record.vol1_q1!=0 or record.vol1_q2!=0):
                raise ValidationError("Your total is not equal to the sum of the 2 quarters : %s + %s != %s" % (record.vol1_q1, record.vol1_q2,  record.vol1_total))

    @api.one
    @api.depends('sigle', 'cnum', 'subdivision')
    def _compute_code(self):
        self.code = "%s%s" % (self.sigle, self.cnum)
        if self.subdivision:
            self.code = "%s%s" % (self.code, self.subdivision)
            
    @api.one
    @api.depends('sigle')
    def _compute_site(self):
        self.site = self.sigle[0] if self.sigle else ""

    @api.multi
    def write(self, vals):
        write_res = super(ActiviteInfo, self).write(vals)
        return write_res
        
        
