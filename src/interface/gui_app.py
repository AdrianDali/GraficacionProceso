from cmath import e
import tkinter as tk
from tkinter import ttk
import datetime
from turtle import bgcolor
#import RPi.GPIO as GPIO
import threading
#from tomlkit import value
from model.usuario import select_name_usuario_enabled, select_id_usuario
from model.pieza import select_name_piezas, select_id_pieza
from model.maquina import select_name_maquinas_enabled , select_id_maquina
from model.proceso import DBProceso, actualizar_peso_proceso,select_procesos_unfinish, insertar_monitoreo_proceso, select_id_proceso, actualizar_piezas_proceso
import time 
#import serial

from tkinter.font import BOLD
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


import numpy as np

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(10, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)


contadorM1 = 0

#ser = serial.Serial("/dev/ttyACM0" , 9600)
#ser.flushInput()




# env\Scripts\activate
print(select_name_usuario_enabled())
lista_usuarios = select_name_usuario_enabled()
lista_piezas = select_name_piezas()
lista_maquina = select_name_maquinas_enabled()
fecha_inicio = datetime.datetime.now()
fecha  = str(fecha_inicio.strftime("%Y-%m-%d"))
fecha_completa = str(fecha_inicio.strftime("%Y-%m-%d %H:%M:%S"))
print(fecha)

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu ,width =1200, height =1200)
    menu_inicio = tk.Menu(barra_menu ,tearoff= 0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Agregar Pelicula')
    menu_inicio.add_command(label='Eliminar Registro e db')
    menu_inicio.add_command(label='Salir', command=root.destroy)
    barra_menu.add_cascade(label='Inicio',  menu=menu_inicio) 
    barra_menu.add_cascade(label='Configuracion', )
    barra_menu.add_cascade(label='Ayuda', )

def listar():
    select_procesos_unfinish()
    return select_procesos_unfinish()

nombres =["Jorge", "Monica"]
piezas = [34, 40]



class Frame(tk.Frame):

    def times(self): 
        current_time = time.strftime("%H:%M:%S")
        self.clock.config(text = current_time)
        self.date.config(text = time.strftime("%d/%m/%Y"))
        self.clock.after(200, self.times)
 

    def __init__(self, root= None):
        super().__init__(root, width = 1500 , height = 1200)
        self.root = root 
        self.pack()
        self.config( bg = '#ffffff')

         #header
        #------------------------------------------------------
        frame_form_top = tk.Frame(self.root,height=50, bd = 0,padx= 10, relief=tk.SOLID, bg = "#ffffff")
        frame_form_top.pack (side = "top", fill= tk.X)
        title = tk.Label(frame_form_top, text = "Sterilization System", font = ('Times', 30 ), bg = "#ffffff", fg = "#000000", pady = 0)
        title.pack(side = "left")

        self.date =tk.Label(frame_form_top, font=('Times',15,BOLD)  ,bg = "#fcfcfc", fg = "#666a88", padx = 25)
        self.date.pack(side = "right")

        self.clock = tk.Label(frame_form_top, font = ('Times', 15, BOLD ), bg = "#6a9ff6", fg = "black", padx = 25, pady=20)
        self.clock.pack(side = "right" )
        self.times()

        text_temperatura = tk.Label(frame_form_top, text = "Temperatura: ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text_temperatura.pack(side = "left", padx=80)

        temperatura = tk.Label(frame_form_top, text = "20°C", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000", padx= 0 )
        temperatura.pack(side = "left")
        #TERMINA HEADER
        #----------------------------------------------------------------------------------------------------------------------
        frame_bottom = tk.Frame(self.root, bd= 0 ,relief= tk.SOLID, bg = "#6a9746")
        frame_bottom.pack(side= "top" ,expand= tk.YES,  fill = tk.BOTH)
        
        self.frame_graphic_process = tk.Frame(frame_bottom, bd= 0 ,relief= tk.SOLID, bg = "#6a9ff6")
        self.frame_graphic_process.pack(side= "top" ,expand= tk.YES,  fill = tk.BOTH , padx=10, pady=10)

        self.frame_phase_conditions = tk.Frame(frame_bottom, bd= 0 ,height= 250,relief= tk.SOLID, bg = "#1a6ff6")
        self.frame_phase_conditions.pack(side= "top" ,expand= tk.YES,  fill = tk.BOTH , padx=10, pady=10)


        self.campos_pelicula()
        self.deshabilitar_campos()
        fig = Figure(figsize=(6, 3), dpi=100,)
        self.axes = fig.add_subplot()
        self.axes.clear()
        self.axes.barh(nombres,piezas)
        self.figure_canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        self.figure_canvas.draw()
        toolbar = NavigationToolbar2Tk(self.figure_canvas, self.root, pack_toolbar=False)    
        toolbar.update()  
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.figure_canvas.get_tk_widget().pack(side=tk.TOP,fill = tk.BOTH,  expand=1, pady = 0)
        self.tabla_peliculas()
        

    def grafica(self,nombre,pieza):
        nombres.clear()
        piezas.clear()
        nombres.append(nombre)
        piezas.append(pieza)
        print(nombres)
        print(piezas)
        self.axes.clear()
        self.axes.barh(nombres,piezas)
        self.figure_canvas.draw()
        
    def campos_pelicula(self):
        #labels de cada campo
        self.label_nombre = tk.Label(self.frame_graphic_process, text = 'Nombre de  operador: ' , bg = '#ffffff')
        self.label_nombre.config(font=('Arial', 12, "bold"))
        self.label_nombre.grid(row = 0, column = 0,padx=5, pady=5,sticky= "E")

        self.label_proceso = tk.Label(self.frame_graphic_process, text = 'Nombre de proceso: ' , bg = '#ffffff')
        self.label_proceso.config(font=('Arial', 12, "bold"))
        self.label_proceso.grid(row = 1, column = 0, padx=5, pady=5 ,sticky= "E")  

        self.label_fecha = tk.Label(self.frame_graphic_process, text = 'Fecha: ' , bg = '#ffffff')
        self.label_fecha.config(font=('Arial', 12, "bold"))
        self.label_fecha.grid(row = 2, column = 0, padx=5, pady=5,sticky= "E")     

        self.label_pieza = tk.Label(self.frame_graphic_process, text = 'Pieza: ' , bg = '#ffffff')
        self.label_pieza.config(font=('Arial', 12, "bold"))
        self.label_pieza.grid(row = 0, column = 2, padx=10, pady=10,sticky= "E")   

        self.label_maquina = tk.Label(self.frame_graphic_process, text = 'Maquina: ' , bg = '#ffffff')
        self.label_maquina.config(font=('Arial', 12, "bold"))
        self.label_maquina.grid(row = 1, column = 2, padx=10, pady=10,sticky= "E")   

        self.label_observaciones = tk.Label(self.frame_graphic_process, text = 'Observaciones: ' , bg = '#ffffff')
        self.label_observaciones.config(font=('Arial', 12, "bold"))
        self.label_observaciones.grid(row = 2, column = 2, padx=10, pady=10,sticky= "E")   





        #Entrys de cada campo 
        self.mi_nombre = tk.StringVar()
        self.combo_nombre = ttk.Combobox(self.frame_graphic_process, values = lista_usuarios )
        self.combo_nombre.config(width= 50,font=('Arial', 12) )
        self.combo_nombre.grid(row = 0, column = 1, padx=10, pady=10, columnspan= 2,sticky= "W")

        self.mi_proceso = tk.StringVar()
        self.entry_proceso = tk.Entry(self.frame_graphic_process, textvariable = self.mi_proceso)
        self.entry_proceso.config(width= 50,font=('Arial', 12),background='#ffffff' )
        self.entry_proceso.grid(row = 1, column = 1, padx=10, pady=10 , columnspan= 2,sticky= "W")

        self.mi_fecha = tk.StringVar()
        self.entry_fecha = tk.Entry(self.frame_graphic_process, textvariable = self.mi_fecha )
        self.entry_fecha.config(width= 50,font=('Arial', 12) )
        self.entry_fecha.grid(row = 2, column = 1, padx=10, pady=10    , columnspan= 2,sticky= "W")


        self.combo_pieza = ttk.Combobox(self.frame_graphic_process, values = lista_piezas )
        self.combo_pieza.config(width= 50,font=('Arial', 12) )
        self.combo_pieza.grid(row = 0, column = 3, padx=10, pady=10, columnspan= 2,sticky= "W")
        
        self.combo_maquina = ttk.Combobox(self.frame_graphic_process, values = lista_maquina)
        self.combo_maquina.config(width= 50,font=('Arial', 12) )
        self.combo_maquina.grid(row = 1, column = 3, padx=10, pady=10, columnspan= 2,sticky= "W")

        self.mi_observaciones = tk.StringVar()
        self.text_observaciones = tk.Text(self.frame_graphic_process)
        self.text_observaciones.config(width= 50,height= 5 ,font=('Arial', 12) )
        self.text_observaciones.grid(row = 2, column = 3, padx=10, pady=10    , columnspan= 2, sticky= "W")


        

        #Botones
        self.boton_nuevo = tk.Button(self.frame_graphic_process, text = 'Nuevo', state = 'normal', command = self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, "bold"), fg = '#ffffff', bg = '#158645',
        cursor='hand2', activebackground= "#35bd6f")
        self.boton_nuevo.grid(row = 6, column = 1, padx=10, pady=10)

        self.boton_guardar = tk.Button(self.frame_graphic_process, text = 'Iniciar Proceso', state = 'normal', command = self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, "bold"), fg = '#ffffff', bg = '#1658a2',
        cursor='hand2', activebackground= "#3586df")
        self.boton_guardar.grid(row = 6, column = 2, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self.frame_graphic_process, text = 'Cancelar', state = 'normal', command = self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, "bold"), fg = '#ffffff', bg = '#bd152e',
        cursor='hand2', activebackground= "#e15370")
        self.boton_cancelar.grid(row = 6, column = 3, padx=10, pady=10)

        #Boton eliminar 
        self.boton_eliminar = tk.Button(self.frame_graphic_process, text = 'Eliminar', state = 'normal', command = self.deshabilitar_campos)
        self.boton_eliminar.config(width=20, font=('Arial', 12, "bold"), fg = '#ffffff', bg = '#bd152e',
        cursor='hand2', activebackground= "#e15370")
        self.boton_eliminar.grid(row =8, column = 2, padx=10, pady=10)

        #Botones
        self.boton_editar = tk.Button(self.frame_graphic_process, text = 'Editar', state = 'normal', command = self.editarDatos)
        self.boton_editar.config(width=20, font=('Arial', 12, "bold"), fg = '#ffffff', bg = '#158645',
        cursor='hand2', activebackground= "#35bd6f")
        self.boton_editar.grid(row = 8, column = 1, padx=10, pady=10)

        self.boton_guardar = tk.Button(self.frame_graphic_process, text = 'Terminar Proceso', state = 'normal', command = self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, "bold"), fg = '#ffffff', bg = '#1658a2',
        cursor='hand2', activebackground= "#3586df")
        self.boton_guardar.grid(row = 8, column = 3, padx=10, pady=10)

    def habilitar_campos(self):
        self.text_observaciones.config(state = 'normal')
        self.combo_nombre.config(state = 'readonly')
        self.combo_pieza.config(state = 'readonly')
        self.combo_maquina.config(state = 'readonly')
        #self.entry_duracion.config(state = 'normal')
        self.entry_fecha.config(state = 'readonly')
        self.boton_guardar.config(state = 'normal')
        self.boton_cancelar.config(state = 'normal')
        self.boton_nuevo.config(state = 'disabled')
        self.mi_fecha.set(fecha)

    def deshabilitar_campos(self):
        #borrar los campos
        self.mi_fecha.set('')
        self.mi_proceso.set('')
        self.combo_nombre.set('')
        self.combo_maquina.set('')
        self.combo_pieza.set('')
        self.mi_observaciones.set('')

        #deshabilitar los campos
        self.text_observaciones.config(state = 'disabled')
        self.combo_maquina.config(state = 'disabled')
        self.combo_pieza.config(state = 'disabled')
        self.combo_nombre.config(state = 'disabled')
        #self.entry_duracion.config(state = 'disabled')
        self.entry_fecha.config(state = 'disabled')
        self.boton_guardar.config(state = 'disabled')
        self.boton_cancelar.config(state = 'disabled')
        self.boton_nuevo.config(state = 'normal')
    
    def guardar_datos(self):
        
        nombre = self.combo_nombre.get()
        print(nombre)
        id_usuario = select_id_usuario(nombre)
        print("usuario:   ")
        print(id_usuario)
        pieza = self.combo_pieza.get()
        print(pieza)
        maquina = self.combo_maquina.get()
        print(maquina)
        observaciones = self.mi_observaciones.get()
        print(observaciones)
        fecha = self.mi_fecha.get()
        print(fecha)
        nombre_proceso = self.mi_proceso.get()
        print(nombre_proceso)
        id_maquina = select_id_maquina(maquina)
        id_pieza = select_id_pieza(pieza)
        DBProceso(id_maquina, id_pieza,id_usuario, nombre_proceso, fecha_completa,  observaciones )
        id_proceso = select_id_proceso(nombre_proceso)
        self.inicioProceso(id_usuario, id_proceso)
        print("proceso id:::  " , id_proceso)
        self.tabla_peliculas()
        self.deshabilitar_campos()
        
    def tabla_peliculas(self):

        self.lista_peliculas = listar()
        
        self.tabla = ttk.Treeview(self,
        column= ('nombre', 'proceso', 'nombre_maquina', 'nombre_pieza', 'hora_inicio','numero_piezas', 'peso_merma', 'observaciones'))
        self.tabla.grid(row = 7, column = 0, columnspan= 5)

        #scroll
        #self.scroll = ttk.Scrollbar(self,
        #orient = "vertical", command = self.tabla.yview)
        #self.scroll.grid(row = 4, column = 4, sticky = "nse")
        #self.tabla.configure(yscrollcommand= self.scroll.set)

        self.tabla.heading('#0', text = 'ID')
        self.tabla.heading('#1', text = 'NOMBRE')
        self.tabla.heading('#2', text = 'PROCESO')
        self.tabla.heading('#3', text = 'MAQUINA')
        self.tabla.heading('#4', text = 'PIEZA')
        self.tabla.heading('#5', text = 'HORA INICIO')
        self.tabla.heading('#6', text = 'NUMERO PIEZAS')
        self.tabla.heading('#7', text = 'PESO MERMA')
        self.tabla.heading('#8', text = 'OBSERVACIONES')
        #self.tabla_seleccion()
        #self.tabla.insert('',0, text = '1', values = ( 1,'Pelicula 1', '1', 'Accion'))

        #iterar lista peliculas 
        for p in self.lista_peliculas:
            self.tabla.insert('', 0, text = p[0], values = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]))
            nombres = [p[1]]
            piezas = [p[6]]
        #print("nombres para graficas")
        print(nombres)
        print(piezas)
        #self.grafica(str(input("ingresa nombre: ")),int(input("ingresa piezas : ")))
    def tabla_seleccion(self):
        select_procesos_unfinish()
        print("")
        print("PSO")
        self.tabla.insert('', 0, text = '2', values = ('peli', '4', 'Accion'))
        
    def inicioProceso(self,idUsuario,idProceso):
        #idUsuario = con.select_user_id(usuarioIniciar)
        #idProceso = con.select_proceso_id(proceso)
        thread = threading.Thread(target= self.monitoreoProceso , args=(idProceso,idUsuario))
        thread.start()
        print("HILO INICIALIZADO")

    def monitoreoProceso(self,idProceso,idUsuario):
        while(True):
            if GPIO.input(10) == GPIO.HIGH:
                lineBytes = ser.readline()
                print("LINE ")
                line = lineBytes.decode("utf-8").strip()
                print("LINEEEEEEE ")
                print(line)

                global contadorM1 
                contadorM1 = contadorM1 + 1 
                insertar_monitoreo_proceso(idProceso,idUsuario)
                print("monitoreo_proceos")
                actualizar_piezas_proceso(contadorM1, idProceso)
                actualizar_peso_proceso(line, idProceso)
                self.tabla_peliculas()
                time.sleep(2)

    def editarDatos(self):
        try: 
            proceso = self.tabla.item(self.tabla.selection())["values"][1]
            print(proceso)
        except: 
            pass


   

