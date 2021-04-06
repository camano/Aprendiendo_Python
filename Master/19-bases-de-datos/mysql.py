import pymysql

conn=pymysql.connect(host="localhost",user="jonathan",passwd="Aldebaran28@")
cursor=conn
cursor.execute("create database hola")
conn.commit()