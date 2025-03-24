import mysql.connector
from mysql.connector import errorcode

import os
from dotenv import load_dotenv
load_dotenv()
# ------------------------------------------------------------------------------
def creacion_bbdd_tablas():
    try:
        # Conectar a MySQL Server
        cnx = mysql.connector.connect(
            user= os.getenv('mysql_username'),       
            password= os.getenv('mysql_password'),  
            host= os.getenv('mysql_host'),
            port= os.getenv('mysql_port'),   
        )
# ------------------------------------------------------------------------------
        if cnx.is_connected():
            print("¡Conectado!")

            mycursor = cnx.cursor()

            # Crear la base de datos si no existe
            mycursor.execute("CREATE DATABASE IF NOT EXISTS spotify")
            print("Base de datos 'spotify' creada correctamente.")

            # Usar la base de datos
            try:
                mycursor.execute("USE spotify")
                print("Base de datos seleccionada correctamente.")
            except mysql.connector.Error as err:
                print("⚠️ Error al seleccionar la base de datos.")
                print("Código de Error:", err.errno)
                print("SQLSTATE:", err.sqlstate)
                print("Mensaje:", err.msg)
# ------------------------------------------------------------------------------
        # Crear la tabla de Spotify

        # mycursor.execute("""
        #     CREATE TABLE IF NOT EXISTS songs (
        #         id INT AUTO_INCREMENT PRIMARY KEY,
        #         artist VARCHAR(255),
        #         track VARCHAR(255),
        #         album VARCHAR(255),
        #         release_date DATE,
        #         duration_ms INT
        #     );
        # """)
        # print("Tabla 'songs' creada correctamente.")
# ------------------------------------------------------------------------------
        # Confirmar los cambios
        cnx.commit()
# ------------------------------------------------------------------------------
    # except mysql.connector.Error as err:
    #     print("⚠️ Se produjo un error al crear la tabla.")
    #     print("Código de Error:", err.errno)
    #     print("SQLSTATE:", err.sqlstate)
    #     print("Mensaje:", err.msg)
# ------------------------------------------------------------------------------
    finally:
        if cnx.is_connected():
            mycursor.close()
            cnx.close()
            print("Conexión MySQL cerrada.")
# ------------------------------------------------------------------------------
# Ejecutar la función para crear la base de datos y tablas
creacion_bbdd_tablas()