import sqlite3 

#Conexion
conexion=sqlite3.connect('prueba.db')

#Crear Cursor
cursor=conexion.cursor()

#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id integer primary key autoincrement,"+
"titulo varchar(255),"+
"desripcion TEXT,"+
"precio int(255)"+
")")

#Guardar cambios
conexion.commit()

#Insertar datos
cursor.execute("insert into productos values(null,'producto3','descripcion3',550)")
conexion.commit()


#listar datos
cursor.execute("select * from productos")
producto=cursor.fetchall()

for productos in producto:
    print(productos)


#Cerrar conexion
conexion.close()