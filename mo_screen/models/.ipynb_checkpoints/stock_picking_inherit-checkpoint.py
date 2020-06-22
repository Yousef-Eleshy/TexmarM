# -*- coding: utf-8 -*-
from odoo import models, fields, api
from itertools import groupby


class StockPicking(models.Model):
    _inherit = 'stock.picking'


class StockMove(models.Model):
    _inherit = 'stock.move'

    size_of_pieces = fields.Char(string='Size of Pieces', readonly=1)
