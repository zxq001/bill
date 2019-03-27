# -*- coding: utf-8 -*-
from odoo import http

class Bill(http.Controller):
    @http.route('/bill/bill/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/bill/bill/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('bill.listing', {
            'root': '/bill/bill',
            'objects': http.request.env['bill.count'].search([]),
        })

    @http.route('/bill/bill/objects/<model("bill.count"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('bill.object', {
            'object': obj
        })