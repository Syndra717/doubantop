# *-* coding = utf-8 *-*
# @Time : 2020/7/23 上午1:44
# @Author : 杨欣
# @File : testSqlite.py
# @Software : PyCharm
import sqlite3

# 1.连接数据库
conn = sqlite3.connect("test.db")       #打开或创建数据库文件

print("Opened database successfully")