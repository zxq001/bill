# -*- coding: utf-8 -*-
{
    'name': "bill",

    'summary': """
        账单""",

    'description': """
    账单流程：
    1.登陆ocr管理员账号按期间导出票据汇总、费用类小票信息
    2.在拉取的表格中按照代理记账公司筛选旗下公司
    3.在每家公司中将最新数据替换原先的数据（表格中数据与总账
    jst管理员账号下比对，如有出入以总账为准）
    4.按照收费标准记录收费金额 有补账的备注补账
    5.将税号总数与收费金额填入收费总表
    6.将收费金额填入市场部税号汇总    
    """,

    'author': "嘉商通",
    'website': "http://www.cicjust.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}