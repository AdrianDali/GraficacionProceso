from cmath import e
from model.DBmysql import DataBase
import numpy as np
import datetime 



def select_procesos_unfinish():
        sql = 'SELECT p.id_proceso, u.nombre as nombre_usuario,p.nombre, m.nombre_maquina, i.nombre_pieza, p.hora_inicio,p.numero_piezas , p.peso_merma,p.observaciones FROM proceso as p join maquina as m on m.id_maquina = p.id_maquina  join pieza as i on p.id_pieza = i.id_pieza join usuarios as u on u.id_usuario = p.id_nombre  where p.proceso_terminado = 1;'
        try:
            connection = DataBase().connection
            cursor = connection.cursor()
            cursor.execute(sql)
            procesos = cursor.fetchall()
            cursor.close()
            return procesos
        
        except Exception as e:
            print(e)
            raise


def insertar_monitoreo_proceso(idProceso,idUsuario):
    fecha= datetime.datetime.now()
    print(idProceso)
    print(str(fecha.strftime("%Y-%m-%d %H:%M:%S")))
    sql = "insert into proceso_usuario(id_proceso, id_usuario,hora) values({},{},'{}')".format(idProceso,idUsuario, str(fecha.strftime("%H:%M:%S")))
    try:
        connection = DataBase().connection 
        cursor = connection.cursor() 
        cursor.execute(sql)
        connection.commit()
        print("logrado")
        cursor.close()
    except Exception as e: 
        raise 


def actualizar_piezas_proceso(contador, idProceso):
    sql = "update proceso set numero_piezas = {} where id_proceso = {}".format(contador, idProceso)
    try:
        connection = DataBase().connection 
        cursor = connection.cursor() 
        cursor.execute(sql)
        connection.commit()
        print("logrado")
        cursor.close()
    except Exception as e: 
        raise 

def actualizar_peso_proceso(contador, idProceso):
    sql = "update proceso set peso_merma = {} where id_proceso = {}".format(contador, idProceso)
    try:
        connection = DataBase().connection 
        cursor = connection.cursor() 
        cursor.execute(sql)
        connection.commit()
        print("logrado")
        cursor.close()
    except Exception as e: 
        raise 


def select_id_proceso(proceso):
    sql = 'SELECT id_proceso from proceso where nombre = "{}" '.format(proceso)
    objeto_usuario = []
    try: 
        connection = DataBase().connection
        cursor = connection.cursor()
        cursor.execute(sql)
        proceso = cursor.fetchone()
        user = proceso[0]
        print(user)
        cursor.close()
        return user
    except Exception as e:
        print(e)
        raise


class DBProceso():
    def __init__(self, id_maquina,id_pieza,id_nombre , nombre, hora_inicio, observaciones ):
        self.connection = DataBase().connection
        self.cursor = self.connection.cursor()
        id_nombre = int(id_nombre)
        sql = 'INSERT INTO proceso(id_maquina,id_pieza,id_nombre ,nombre,hora_inicio,observaciones)VALUES({},{},{},"{}","{}","{}")'.format(id_maquina,id_pieza,id_nombre,nombre,hora_inicio,observaciones)
        try :
            self.cursor.execute(sql)
            self.connection.commit()
            print("logrado") 
            self.cursor.close()
        except Exception as e:
            print(e)
            raise

        self.id_maquina = id_maquina 
        self.id_pieza = id_pieza
        self.nombre_proceso = nombre
        self.hora_inicio = hora_inicio
        self.observaciones = observaciones




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
            

    def select_name_maquinas_enabled(self):
        sql = 'SELECT nombre_maquina from maquina where disponible = 1 '
        try:
            self.cursor.execute(sql)
            maquinas = self.cursor.fetchall()
            lista  = []
            for maquina in maquinas:
                lista.append(maquina[0])
            self.cursor.close()
            return lista
        except Exception as e:
            print(e)
            raise

#maquina  = DBMaquina(1)
#list = maquina.select_name_maquinas_enabled()
#print(list)




