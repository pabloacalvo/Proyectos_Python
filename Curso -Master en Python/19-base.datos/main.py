import mysql.connector
 
# Conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)
 
#print(database)
 
# Cursor
cursor = database.cursor(buffered=True)
 
# Crear base de datos
 
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
"""
cursor.execute("SHOW DATABASES")
 
for bd in cursor:
    print(bd)
"""
# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculo(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")
 
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

# Insertar datos 

#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
coches = [
    ('Seat','Ibiza',5000),
    ('Fiat','Palio',15000),
    ('Mercedes','Clase C',85000),
    ('Renault','Clio',12500),
]


#cursor.executemany("INSERT INTO vehiculos VALUES (null,%s,%s,%s)",coches)

database.commit()

# Mostrar datos

cursor.execute("SELECT  * FROM vehiculos WHERE precio <= 5000")
result = cursor.fetchall()


for coche in result:
    print(coche[1],coche[3])

#Primer registro
cursor.execute("SELECT  * FROM vehiculos")
coche = cursor.fetchone()
print(coche)

# Borrar registro
cursor.execute("DELETE FROM vehiculos where id=2")
database.commit()

print(cursor.rowcount,"borrados!!")

# Actualizar datos

cursor.execute("UPDATE vehiculos SET modelo='Uno' WHERE marca='Fiat'")
database.commit()
print(cursor.rowcount,"Actualizados")