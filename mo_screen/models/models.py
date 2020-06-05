# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mo_screen(models.Model):
    
    _inherit = 'mrp.product.produce'
    
    size_of_pieces = fields.Char(string='Size of Pieces', readonly=False)