import functools
import xmlrpc.client
username = '2270155887@qq.com'
pwd = '111111'
db = 'test'

# 1. Login
common = xmlrpc.client.ServerProxy('http://127.0.0.1:8069/xmlrpc/common')
uid = common.login(db,username,pwd)

# 2. Read the sessions
models = xmlrpc.client.ServerProxy('http://127.0.0.1:8069/xmlrpc/object')

#partner = { 'name': '测试', 'lang': 'zh_CN', }
#partner_id = models.execute(db, uid, pwd, 'res.partner', 'create',partner)

for session in sessions:
    print("Session %s "(session['company_id'], session['company_name']))
# 3.create a new session
session_id = call('bill.lines', 'create', {
    'name' : 'My session',
    'course_id' : 2,
})

partner = { 'sale_man': '徐', 'company_name': '卡歆', 'account_date': '12',
            'duty_num': '100', 'total_sum': '500', 'tips': '补账', 'lines_ids':
                [
                (0, False, {'company_id': '33330000F077696552', 
                            'company_name': '宁波市江北区致成法律服务所', 
                            'coop_id': '8元/月/税号  自行扫描 装订', 
                            'name': '12', 
                            'cost': '8', 
                            'tips': '补账', 
                            }
                ),
                ]}
models.execute(db, uid, pwd, 'bill.count', 'create',partner)