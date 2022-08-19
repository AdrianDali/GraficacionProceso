import tkinter as tk # Importa la libreria tkinter
import interface.gui_app as gui_app



def main():
    root = tk.Tk() # Crea una ventana
    
    root.title('catalogo de peliculas') # Le pone un titulo a la ventana    
    #root.iconbitmap('img/grafico.ico') # Le pone un icono a la ventana 
    #root.resizable(False, False) # No se puede cambiar el tamaño de la ventana  
    root.config(bg='#f2f2f2') # Le pone un color de fondo a la ventana  
    #root.geometry('1000x800') # Le pone un tamaño a la ventana   
    gui_app.barra_menu(root)
    app = gui_app.Frame(root = root) # Crea una instancia de la clase Frame

    root.mainloop() # Muestra la ventana

if __name__ == '__main__':
    main()