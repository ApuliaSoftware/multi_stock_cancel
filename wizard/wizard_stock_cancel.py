# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Andre@ (<a.gallina@cgsoftware.it>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from osv import fields, osv
from tools.translate import _


class multi_stockcancel(osv.osv_memory):

    _name = "wizard.multistockcancel"


    def start_cancel(self, cr, uid, ids, context={}):
        stock_ids = context.get('active_ids', False)
        if not stock_ids:
            return {'type': 'ir.actions.act_window_close'}
        stock_obj = self.pool.get('stock.move')
        res = stock_obj.action_cancel(cr, uid, stock_ids, context)
        if res:
            return {'type': 'ir.actions.act_window_close'}


