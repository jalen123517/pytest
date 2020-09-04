# fp = open("1.txt",mode="r")
# b = []
# for i in fp:
#     a =i.split("\t")
#     b.append(a[1].strip("\n"))
#     print(a[1].strip("\n"))
# print(b)
#
# import pandas
# # data = pandas.read_excel('C:/Users/jalen/Desktop/cases.xls')
# data = pandas.read_excel(r'c:\Users\jalen\Desktop\cases.xls')
# print(data)
# datalist = data.values.tolist()
# print(datalist)

import pymysql
conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="test",charset="utf8")
cur = conn.cursor()

#实现批量写入数据
datalist = []
for i in range(10):
    datalist.append(("zhansan%s" %i,i))


sql = "insert into user_var(username,passwd) values('u','1')"
sql = "insert into user_var values(%s,%s)"
# sql = "select * from user_var"
# data = cur.execute(sql)
cur.executemany(sql,datalist)
conn.commit()

# print(data)
conn.close()