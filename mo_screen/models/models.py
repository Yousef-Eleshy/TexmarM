# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mo_screen(models.TransientModel):
    
    _inherit = 'mrp.product.produce'
    
    size_of_pieces = fields.Char(string='Size of Pieces', store=True, readonly=False)
    

    
class inv_screen(models.TransientModel):
    
    _inherit = 'mrp.product.produce'
    
    size_of_pieces_inv = fields.Char(string='Size of Pieces', store=True, readonly=False)