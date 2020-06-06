# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mo_screen(models.Model):
    _inherit = 'mrp.production'
    
    size_of_pieces = fields.Char(string='Size of Pieces', store=True, readonly=False)
    

    
class inv_screen(models.Model):
    _inherit = 'stock.picking'
    
    size_of_pieces_inv = fields.Many2one('mo.screen', string='Size of Pieces', store=True, readonly=False)