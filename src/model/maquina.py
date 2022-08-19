
from model.DBmysql import DataBase

def select_name_maquinas_enabled():
        sql = 'SELECT nombre_maquina from maquina where disponible = 1 '
        try:
            connection = DataBase().connection
            cursor = connection.cursor()
            cursor.execute(sql)
            maquinas = cursor.fetchall()
            lista  = []
            for maquina in maquinas:
                lista.append(maquina[0])
                cursor.close()
            return lista
        except Exception as e:
            print(e)
            raise
    
def select_id_maquina(nombre):
    sql = 'SELECT id_maquina from maquina where nombre_maquina = "{}"'.format(nombre)
    try:
        connection = DataBase().connection
        cursor = connection.cursor()
        cursor.execute(sql)
        id_maquina = cursor.fetchone()
        cursor.close()
        return id_maquina[0]
    except Exception as e: 
        print(e)
        raise

class DBMaquina():
    def __init__(self, id):
        self.connection = DataBase().connection
        self.cursor = self.connection.cursor()
        maquina = self.select_maquina(id)
        self.id_maquina = maquina[0]
        self.nombre_maquina = maquina[1]
        self.disponible = maquina[2]
        print('id: ', self.id_maquina)
        print('nombre: ', self.nombre_maquina)
        print('disponible: ', self.disponible)
        print('\n')



    def select_maquina(self,id):
        sql = 'SELECT id_maquina, nombre_maquina, disponible from maquina where id_maquina = {}'.format(id)
        objeto_maquina = []
        try: 
            self.cursor.execute(sql)
            maquina = self.cursor.fetchone()
            objeto_maquina = [maquina[0],maquina[1],maquina[2]]
            self.cursor.close()
            return objeto_maquina
        except Exception as e:
            print(e)
            raise
            

    

#maquina  = DBMaquina(1)
#list = maquina.select_name_maquinas_enabled()
#print(list)