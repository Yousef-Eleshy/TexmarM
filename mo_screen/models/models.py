# -*- coding: utf-8 -*-

from odoo import models, fields, api
from itertools import groupby


class mo_screen(models.Model):
    _inherit = 'mrp.production'

    size_of_pieces = fields.Char(string='Size of Pieces', store=True, readonly=False)


class StockMoveExt(models.Model):
    _inherit = "stock.move"

    def _assign_picking(self):
        """
        Size of Pieces field from MO is linked with Transfer Size of Pieces field
        :return:
        """
        Picking = self.env['stock.picking']
        grouped_moves = groupby(sorted(self, key=lambda m: [f.id for f in m._key_assign_picking()]), key=lambda m: [m._key_assign_picking()])
        
        for group, moves in grouped_moves:
            moves = self.env['stock.move'].concat(*list(moves))
            new_picking = False
            # Could pass the arguments contained in group but they are the same
            # for each move that why moves[0] is acceptable
            picking = moves[0]._search_picking_for_assignation()
            if picking:
                if any(picking.partner_id.id != m.partner_id.id or picking.origin != m.origin for m in moves):
                    # If a picking is found, we'll append `move` to its move list and thus its
                    # `partner_id` and `ref` field will refer to multiple records. In this
                    # case, we chose to  wipe them.
                    picking.write({
                        'partner_id': False,
                        'origin': False,
                    })
            else:
                new_picking = True
                picking = Picking.create(moves._get_new_picking_values())
                picking.size_of_pieces_inv = self.env['mrp.production'].search([('name', '=', self.origin)],limit=1).size_of_pieces
            moves.write({'picking_id': picking.id})
            moves._assign_picking_post_process(new=new_picking)
        return True


class inv_screen(models.Model):
    _inherit = 'stock.picking'

    size_of_pieces_inv = fields.Char(string='Size of Pieces', store=True)
