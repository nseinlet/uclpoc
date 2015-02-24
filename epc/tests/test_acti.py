from openerp.tests.common import TransactionCase, SingleTransactionCase
from openerp.exceptions import Warning, ValidationError
cache = {}
from psycopg2 import IntegrityError

class TestTeacher(SingleTransactionCase):
    
    def test_01_create_course(self):
        mod_activ = self.env['epc.activite']
        mod_cc = self.env['epc.cahiercharge']
        
        acti = mod_activ.create({
            'ens_debut' : 2015,
            'ens_fin' : 2015,
        }).id
        
        cc1 = mod_cc.create({
            'activity_id': acti,
            'langue': 'FR',
        })
        excpt=0
        with self.assertRaises(IntegrityError):
            cc2 = mod_cc.create({
                'activity_id': acti,
                'langue': 'FR',
            })
        
