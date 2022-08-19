print('USEEERRRR')
from model.DBmysql import DataBase


def select_name_usuario_enabled():
        sql = 'SELECT nombre from usuarios where disponible = 1 '
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

def select_id_usuario(usuario):
    sql = 'SELECT id_usuario from usuarios where nombre = "{}" '.format(usuario)
    objeto_usuario = []
    try: 
        connection = DataBase().connection
        cursor = connection.cursor()
        cursor.execute(sql)
        usuario = cursor.fetchone()
        user = usuario[0]
        print(user)
        cursor.close()
        return user
    except Exception as e:
        print(e)
        raise


class DBUsuario():
    def __init__(self, id):
        self.connection = DataBase().connection
        self.cursor = self.connection.cursor()
        usuario = self.select_usuario(id)
        self.id_usuario = usuario[0]
        self.nombre_usuario = usuario[1]
        self.disponible = usuario[2]
        print('id: ', self.id_usuario)
        print('nombre: ', self.nombre_usuario)
        print('disponible: ', self.disponible)
        print('\n')



    def select_usuario(self,id):
        sql = 'SELECT id_usuario, nombre, disponible from usuarios where id_usuario = {}'.format(id)
        objeto_usuario = []
        try: 
            self.cursor.execute(sql)
            usuario = self.cursor.fetchone()
            objeto_usuario = [usuario[0],usuario[1],usuario[2]]
            print(objeto_usuario)
            self.cursor.close()
            return objeto_usuario
        except Exception as e:
            print(e)
            raise
            

    

#usuario  = DBUsuario(2)
#list = usuario.select_name_usuario_enabled()
#print(list)


