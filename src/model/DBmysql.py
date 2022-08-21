import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            #host='192.168.1.135',
            #host='192.168.1.145',
            host='localhost',
            #user = 'root01',
            user = 'root',
            passwd = '1234',
            db = 'monitoreo_trabajo'
            )
        self.cursor = self.connection.cursor()
        print('Conexion exitosa')
       

    

