# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mo_screen(models.Model):
    _inherit = 'mrp.production'
    
    size_of_pieces = fields.Char(string='Size of Pieces', store=True, readonly=False)
    
    #api.onchange('size_of_pieces')
    #def _onchange_size(self):
        # set auto-changing field
     #   self.size_of_pieces_inv = self.size_of_pieces

    
class inv_screen(models.Model):
    _inherit = 'stock.picking'
    
    # size_of_pieces_inv = fields.Char(string='Size of Pieces', readonly=False)
    # size_of_pieces_inv = fields.Many2one('mrp.production', string='Size of Pieces', store=True, readonly=False)
    
    size_of_pieces_inv = fields.Many2one(string='Size of Pieces', related='mo_screen.size_of_pieces', store=True)
    
    
