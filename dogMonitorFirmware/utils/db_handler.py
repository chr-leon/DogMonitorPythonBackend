import mysql.connector
from mysql.connector import Error

class SQLHandler:
    __dbserver__ = None
    __dbuser__ = None
    __dbpass__ = None
    __dbname__ = None
    __cursor__ = None

    def __init__(self, dbserver, dbuser, dbpass, dbname):
        self.__dbserver__ = dbserver
        self.__dbuser__ = dbuser
        self.__dbpass__ = dbpass
        self.__dbname__ = dbname
        self.__cursor__ = None

    def connect(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.__dbserver__,
                user=self.__dbuser__,
                passwd=self.__dbpass__
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection

    def execute_query(self, connection, values_to_save):
        
        query = 'INSERT INTO dogmonitor.imu (sampled_at, a_x, a_y, a_z, g_x, g_y, g_z, m_x, m_y, m_z, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        print(query)
        query2 = 'use dogmonitor;'
        cursor = connection.cursor()
        try:
            cursor.executemany(query, values_to_save)
            connection.commit() 
            print("Query successful")
        except Error as err:
       	    print(f"Error: '{err}'")
        

if __name__=='__main__':
    sql = SQLHandler('localhost', 'rafa','123456789', 'dogmonitor')
    connection = sql.connect()
    sql.execute_query(connection, 0.06, 0.05, 0.005, 0.004, 0.0005, 0.00003, 0.001,'test')