# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BillCount(models.Model):
    _name = 'bill.count'
    _description = "账单"

    name = fields.Char(string="Title",required=True)
      
#    bill_id = fields.Many2one('bill.line',string='分类')
# value = fields.Integer()
# value2 = fields.Float(compute="_value_pc", store=True)
#    description = fields.Text()

#    @api.depends('value')
#    def _value_pc(self):
#        self.value2 = float(self.value) / 100
#    bill_ids = fields.One2many('bill.line','bill_id','datetime')
class BillDetial(models.Model):
    _name = 'bill.detial'
    _description = '账套信息明细'

    name = fields.Char('test')

#class agent_account(models.Model):
#    _name = 'agent.account'
#    _description = "代理记账公司"
    
#    name = fields.Char('代理记账公司')

#class duty_num(models.Model):
#    _name = 'duty.num'
#    _description = "税号"

#    name = fields.Char()

class invoice_sum(models.Model):
    _name = 'invoice.sum'
    _description = "单据汇总"

    company_id = fields.Char('公司税号')
    name = fields.Char('账期')
    company_name = fields.Char('公司名称')
    company_type = fields.Selection([('generalpay','一般纳税人'),
    ('smallscale','小规模纳税人')],string='纳税人类型',required=True)
    company_belong = fields.Char('代理记账公司')
    invoice_num = fields.Char('扫描票据总数')
    ocr_done = fields.Char('ocr处理完成')
    account_done = fields.Char('已做账')
