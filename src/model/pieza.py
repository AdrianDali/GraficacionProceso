from model.DBmysql import DataBase

def select_name_piezas():
        sql = 'SELECT nombre_pieza from pieza '
        try:
            connection = DataBase().connection
            cursor = connection.cursor()
            cursor.execute(sql)
            piezas = cursor.fetchall()
            lista  = []
            for pieza in piezas:
                lista.append(pieza[0])
            cursor.close()
            return lista
        except Exception as e:
            print(e)
            raise


def select_id_pieza(nombre):
    sql = 'SELECT id_pieza from pieza where nombre_pieza = "{}"'.format(nombre)
    try:
        connection = DataBase().connection
        cursor = connection.cursor()
        cursor.execute(sql)
        id_pieza = cursor.fetchone()
        cursor.close()
        return id_pieza[0]
    except Exception as e: 
        print(e)
        raise

class DBPieza():
    def __init__(self, id):
        self.connection = DataBase().connection
        self.cursor = self.connection.cursor()
        pieza = self.select_pieza(id)
        self.id_pieza = pieza[0]
        self.nombre_pieza = pieza[1]
        #self.disponible = pieza[2]
        print('id: ', self.id_pieza)
        print('nombre: ', self.nombre_pieza)
        #print('disponible: ', self.disponible)
        print('\n')



    def select_pieza(self,id):
        sql = 'SELECT id_pieza, nombre_pieza from pieza where id_pieza = {}'.format(id)
        objeto_pieza = []
        try: 
            self.cursor.execute(sql)
            pieza = self.cursor.fetchone()
            objeto_pieza = [pieza[0],pieza[1]]
            self.cursor.close()
            return objeto_pieza
        except Exception as e:
            print(e)
            raise
            

    

#maquina  = DBPieza(1)
#list = maquina.select_name_piezas()
#print(list)