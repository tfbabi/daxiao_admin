# -*- coding: utf-8 -*-
# @Time : 2022/1/2 7:59 PM
# @Author : mos
# @Email : tfbabi@163.com
# @File : DbUtils.py


import pymysql

class Model(object):

    def __init__(self, username='xxxx', password='xxxx', database='xxxx',port=xxxx, host='xxxx'):
        # 创建连接
        self.connection = pymysql.connect(user=username, password=password, database=database,port=port, host=host, cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.connection.cursor()
        # 查询所有数据
    def fetchall(self, sql):
        try:
            self.__execute(sql)
            return self.cursor.fetchall()
        except Exception as error:
            print(error)
     # 查询多条数据
    def fetchmany(self, sql, size=1):
        try:
             self.__execute(sql)
             return self.cursor.fetchmany(size)
        except Exception as error:
             print(error)
     # 查询一条数据
    def fetchone(self, sql):
        try:
             self.__execute(sql)
             return self.cursor.fetchone()
        except Exception as error:
             print(error)
     # 增删改的方法
    def change(self, sql):
        try:
            self.__execute(sql)
            self.connection.commit()
        except Exception as error:
             print(error)
     # 执行的私有方法
    def __execute(self, sql):
        self.cursor.execute(sql)
     # 关闭连接和游标
    def __del__(self):
        self.connection.close()
        self.cursor.close()


if __name__ == '__main__':

    employee = Model()
    res = employee.fetchall('select * from auth_user')
    res = employee.fetchall('select nickname from employee where job="头领"')[0]
    res1 = employee.fetchmany('select nickname from employee where job="头领"', 2)
    res2 = employee.fetchone('select nickname from employee where name = "宋江"')
     # 插入一条语句
    employee.change('insert into employee (name)values ("关羽")')
     # 删除一条语句
    employee.change('delete from employee where name="关羽"')
    # 更新一条语句
   # obj.change('update employee set name="张飞"where id=8004')
