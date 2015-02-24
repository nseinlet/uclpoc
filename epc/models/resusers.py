# -*- coding: utf-8 -*-
from openerp import fields, models

class User(models.Model):
    _inherit = 'res.users'

    entity_id = fields.Many2one('epc.entite', string="entite")

    def get_level(self):
        import pudb
        pudb.set_trace()
        epc_centrale = self.env.ref('epc.epc_centrale')
        epc_faculte = self.env.ref('epc.epc_faculte')
        epc_profs = self.env.ref('epc.epc_profs')
        epc_assists = self.env.ref('epc.epc_assists')
        if epc_centrale.id in self.env.user.group_ids:
            return 4
        return 0
