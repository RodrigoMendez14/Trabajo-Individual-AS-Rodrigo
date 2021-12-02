import mysql.connector
import time

def iniciarDockerAS():
    time.sleep(10) #Se esperan 10 segundos para que arranque MariaDB
    conec = mysql.connector.connect(user='usuarioAS', password='asUSERdb', host='mariadb-part', database='MariaDBAS') #Se establece la conexión con MariaDB con el usuario creado en el docker-compose
    cursor = conec.cursor() #Se crea un cursor para enviar queries a MariaDB
    cursor.execute("CREATE TABLE tableEX (dataEX int)") #Se crea la tabla "tableEX"
    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall()) #Se comprueba que se ha creado la base de datos "MariaDBAS"
    cursor.execute("SHOW TABLES")
    print(cursor.fetchall()) #Se comprueba que se ha creado la tabla "tableEX"
    cursor.execute("DESCRIBE tableEX")
    print(cursor.fetchall()) #Se comprueba que la tabla "tableEX" tiene el dato "dataEX"
    conec.close()

if __name__ == '__main__':
    iniciarDockerAS()
