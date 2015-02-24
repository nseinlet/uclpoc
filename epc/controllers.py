# -*- coding: utf-8 -*-
from openerp import http

class Webserv(http.Controller):
    @http.route('/epc/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('epc.listing', {
            'root': '/epc',
            'objects': http.request.env['epc.activite'].search([]),
        })

    @http.route('/epc/objects/<model("epc.activite"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('epc.object', {
            'object': obj
        })
