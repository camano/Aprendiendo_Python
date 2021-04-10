import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aldebaran28@",
  database="master_python"
)

cursor= mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
""" cursor.execute("show databases")

for bd in cursor:
  print(bd) """

#crear tablas
cursor.execute("""
  create table if not exists vehiculo(
  id int(10) auto_increment not null,
  marca varchar(40) not null,
  modelo varchar(40) not null,
  precio float(10,2) not null,
  constraint pk_vehiculo primary key(id)
)
""")

#insertar tabla
#cursor.execute("insert into vehiculo values(null,'Opel','Astra',18500)")

coches=[
  ('set','ibiza',32788),
  ('Renault','Clio',37892),
  ('Citroen','Saxo',32732),
  ('Mercedez','Clase C',33444)
]

#cursor.executemany("insert into vehiculo values(null,%s,%s,%s)",coches)

mydb.commit()

cursor.execute("select * from vehiculo where precio <=32000")
result=cursor.fetchall()
print("-----Mis coches-----")
print(result)
for coches in result:
  print(coches)
