# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BillCount(models.Model):
    _name = 'bill.count'
    _description = "账单"

    sale_man = fields.Char('业务员')
    company_name = fields.Char('客户名称')
    name = fields.Char('做账日期')
    duty_num = fields.Char('税号个数')
    total_sum = fields.Char('总金额')
    tips = fields.Char('备注')
    lines_ids = fields.One2many('bill.lines', 'bill_lines', string=u"明细项")
    
      
#    bill_id = fields.Many2one('bill.line',string='分类')
# value = fields.Integer()
# value2 = fields.Float(compute="_value_pc", store=True)
#    description = fields.Text()

#    @api.depends('value')
#    def _value_pc(self):
#        self.value2 = float(self.value) / 100
#    bill_ids = fields.One2many('bill.line','bill_id','datetime')
class agent_bill(models.Model):
    _name = 'agent.bill'
    _description = '代理记账公司'
    
    company_id = fields.Char('公司税号')
    company_name = fields.Char('公司名称')
    coop_mode = fields.Char('合作模式')
    name = fields.Char('做账日期')
    cost = fields.Char('费用')
    tips = fields.Char('备注')

class invoice_sum(models.Model):
    _name = 'invoice.sum'
    _description = "单据汇总"

    company_id = fields.Char('公司税号')
    name = fields.Char('账期')
    company_name = fields.Char('公司名称')
    company_type = fields.Selection([('generalpay',u'一般纳税人'),
    ('smallscale',u'小规模纳税人')],string=u'纳税人类型',required=True)
    company_belong = fields.Char('代理记账公司')
    invoice_num = fields.Char('扫描票据总数')
    ocr_done = fields.Char('ocr处理完成')
    account_done = fields.Char('已做账')

class bill_lines(models.Model):
    _name = 'bill.lines'
    _description = "账单明细项"

    company_id = fields.Char('税号')
    company_name = fields.Char('公司名称')
    coop_id = fields.Char('合作模式')
    name = fields.Char('账期')
    cost = fields.Char('费用')
    tips = fields.Char('备注')
    lines_id = fields.Many2one('bill.count', string=u"明细项",index=True)

class coop_type(models.Model):
    _name = 'coop.type'
    _description = "合作类型"

    coop_id = fields.Char('合作模式')


#class CreateBillWizard(models.TransientModel):
#    _name = "create.bill.wizard"
#    _description = '账单的创建向导'

#    @api.model
#    def _default_period_id(self):
#        return self._default_period_id_impl()
    
#    @api.model
#    def _default_period_id_impl(self):
#        return self.env[]