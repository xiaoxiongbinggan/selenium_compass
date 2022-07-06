# coding:utf-8

"""
creatime:2021-08-19
creatby:meilulin@yeah.net
"""


from faker import Faker
import random
import os
import openpyxl

header = ['报备人', '招聘渠道', '管道名称', '市场属性',
          '用工类型', '身份证号码', '手机号', '面试时间', '姓名', '性别']
channel = ['院校', '供应商','自主招聘']
yuanxiao = ['院校12','二级院校']
conduit = ['测试11', '上线前最后的供应商1126']
neijian = ['身份证号码1', '身份证号码2', '身份证号码2', '身份证号码3', '身份证号码4']
market = ['本地市场', '外地市场']
em_type = ['劳动合同','兼职协议','实习协议','劳务协议']
creatby = ['仵鹏',  '李勇', '仇洪伟', '管小芳', '战丽梅', '朱继梅']
eger = ['男', '女']


def nor_creat_report(number):
    filepath = r'D:\auto_test\script\正常报备测试数据{0}条.xlsx'.format(number)
    fake = Faker('zh_CN')
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(header)
    for _ in range(number):
        a1 = random.choice(channel)
        if a1 == '院校':
            a2 = random.choice(yuanxiao)
        elif a1 == '供应商':
            a2 = random.choice(conduit)
        elif a1 == '内荐':
            a2 = random.choice(neijian)
        else:
            a2 = random.choice(creatby)
        test_lst = [random.choice(creatby), a1, a2, random.choice(
            market), random.choice(em_type), fake.ssn(min_age=18, max_age=35), fake.phone_number(),
            fake.date_time_between(start_date='-1d',end_date='now'), fake.name(), random.choice(eger)]
        ws.append(test_lst)
    wb.save(filepath)
    print('创建成功:', filepath)
    wb.close()

def abnor_creat_report(number):
    filepath = r'D:\auto_test\script\异常报备测试数据{0}条.xlsx'.format(number)
    fake = Faker('zh_CN')
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(header)
    for _ in range(number):
        a1 = random.choice(channel)
        if a1 == '院校':
            a2 = random.choice(yuanxiao)
        elif a1 == '供应商':
            a2 = random.choice(conduit)
        elif a1 == '内荐':
            a2 = random.choice(neijian)
        else:
            a2 = random.choice(creatby)
        test_lst = [random.choice(creatby), a1, a2, random.choice(
            market), random.choice(em_type), fake.ssn(min_age=18, max_age=35), fake.phone_number(),
            fake.date_time_between(start_date='-10d',end_date='-3d'), fake.name(), random.choice(eger)]
        ws.append(test_lst)
    wb.save(filepath)
    print('创建成功:', filepath)
    wb.close()

if __name__ == '__main__':

    choice=input('正常报备输入1   |   异常报备输入2\n')
    if choice=='1':
        number=input('输入报备人数\n')
        nor_creat_report(int(number))
    elif choice=='2':
        number=input('输入报备人数\n')
        abnor_creat_report(int(number))



    # number = 5
    # try:
    #     nor_creat_report(int(number))
    # except Exception as e:
    #     print('创建失败:', e)


# fake = Faker('zh_TW')
# print(fake.profile(fields=None, sex=None))
