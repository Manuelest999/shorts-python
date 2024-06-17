from tkinter import*
from tkinter import ttk,messagebox
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame
import sqlite3
from datetime import datetime

class Ventana(tb.Window):
    def __init__(self):
        super().__init__()
        self.ventana_login()

    def ventana_login(self):

        self.frame_login=Frame(self)
        self.frame_login.pack()

        self.lblframe_login=LabelFrame(self.frame_login,text='Acceso', font=('Arial', 14))
        self.lblframe_login.pack(padx=10,pady=10)

        lbltitulo=ttk.Label(self.lblframe_login,text='Inicio de sesion', font=('Arial',18))
        lbltitulo.pack(padx=10,pady=35)

        self.txt_usuario=ttk.Entry(self.lblframe_login,width=40,justify=CENTER)
        self.txt_usuario.pack(padx=10,pady=10)
        self.txt_clave=ttk.Entry(self.lblframe_login,width=40,justify=CENTER)
        self.txt_clave.pack(padx=10,pady=10)
        self.txt_clave.configure(show='*')
        btn_acceso=ttk.Button(self.lblframe_login,text='Log in',width=38,bootstyle='info',command=self.logueo)
        btn_acceso.pack(padx=10,pady=10)
    def ventana_menu(self):
        self.frame_left=Frame(self,width=200)
        self.frame_left.grid(row=0,column=0,sticky=NSEW)

        self.frame_center=Frame(self)
        self.frame_center.grid(row=0,column=1,sticky=NSEW)
        #self.frame_rigth=Frame(self,width=400)
        #self.frame_rigth.grid(row=0,column=2,sticky=NSEW)
        
        self.ventana_busqueda_detalle_venta()

        btn_productos=ttk.Button(self.frame_left,text='Productos',bootstyle='info',width=17,command=self.ventana_lista_productos)
        btn_productos.grid(row=0,column=0,padx=10,pady=10)
        btn_ventas=ttk.Button(self.frame_left,text='Ventas',bootstyle='info',width=17,command=self.ventana_detalle_ventas)
        btn_ventas.grid(row=1,column=0,padx=10,pady=10)
        btn_clientes=ttk.Button(self.frame_left,text='Clientes',bootstyle='info',width=17)
        btn_clientes.grid(row=2,column=0,padx=10,pady=10)
        #btn_compras=ttk.Button(self.frame_left,text='Compras',bootstyle='info',width=15)
        #btn_compras.grid(row=3,column=0,padx=10,pady=10)
        btn_usuarios=ttk.Button(self.frame_left,text='Usuarios',bootstyle='info',width=17,command=self.ventana_lista_usuarios)
        btn_usuarios.grid(row=4,column=0,padx=10,pady=10)
        #btn_reportes=ttk.Button(self.frame_left,text='Reportes',bootstyle='info',width=15)
        #btn_reportes.grid(row=5,column=0,padx=10,pady=10)
        #btn_backup=ttk.Button(self.frame_left,text='Backup',bootstyle='info',width=15)
        #btn_backup.grid(row=6,column=0,padx=10,pady=10)
        #btn_restaurabd=ttk.Button(self.frame_left,text='Restaurar BD',bootstyle='info',width=15)
        #btn_restaurabd.grid(row=7,column=0,padx=10,pady=10)

        
        #lbl2=Label(self.frame_center)
        #lbl2.grid(row=0,column=0,padx=10,pady=10)

        #lbl3=Label(self.frame_rigth)
        #lbl3.grid(row=0,column=0,padx=10,pady=10)
    def logueo(self):
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            
            nombre_usuario=self.txt_usuario.get()
            clave_usuario=self.txt_clave.get()

            #Se consulta la base de datos
            miCursor.execute("SELECT * FROM Usuarios WHERE Nombre=? AND Clave=?",(nombre_usuario,clave_usuario))
            #Con esto se traen todos los registros y se guardan en "datos"
            datos_logueo=miCursor.fetchall()
            if datos_logueo!="":
                for row in datos_logueo:
                    self.cod_usu=row[0]
                    self.nom_usu=row[1]
                    cla_usu=row[2]
                    rol_usu=row[3]
                if(self.nom_usu==self.txt_usuario.get() and cla_usu==self.txt_clave.get()):
                    self.frame_login.pack_forget()#Aqui se oculta la ventana login
                    self.ventana_menu()#Aqui se abre la nueva ventana menu

            #Se aplican los cambios
            miConexion.commit()
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Acceso", "El usuario o clave son incorrectos")
    def ventana_lista_usuarios(self):
        self.borrar_frames()
        self.frame_lista_usuarios=Frame(self.frame_center)
        self.frame_lista_usuarios.grid(row=0,column=0,columnspan=2,sticky=NSEW)

        self.lblframe_botones_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_botones_listusu.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        btn_nuevo_usuario=tb.Button(self.lblframe_botones_listusu,text='Nuevo',width=21
                                    ,bootstyle="success",command=self.ventana_nuevo_usuario)
        btn_nuevo_usuario.grid(row=0,column=0,padx=5,pady=5)
        btn_modificar_usuario=tb.Button(self.lblframe_botones_listusu,text='Modificar',width=21,bootstyle="warning",command=self.ventana_modificar_usuario)
        btn_modificar_usuario.grid(row=0,column=1,padx=5,pady=5)
        btn_eliminar_usuario=tb.Button(self.lblframe_botones_listusu,text='Eliminar',width=21,bootstyle="danger",command=self.eliminar_usuario)
        btn_eliminar_usuario.grid(row=0,column=2,padx=5,pady=5)   

        self.lblframe_busqueda_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_busqueda_listusu.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW) 

        self.txt_busqueda_usuario=ttk.Entry(self.lblframe_busqueda_listusu,width=73)
        self.txt_busqueda_usuario.grid(row=0,column=0,padx=5,pady=5)  
        self.txt_busqueda_usuario.bind('<Key>',self.buscar_usuarios)                       

        #========================Treeview=====================================
        
        self.lblframe_tree_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_tree_listusu.grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)

        columnas=("codigo","nombre","clave","rol")

        self.tree_lista_usuarios=tb.Treeview(self.lblframe_tree_listusu,columns=columnas,
                                         height=17,show='headings',bootstyle="dark")
        self.tree_lista_usuarios.grid(row=0,column=0)
        
        self.tree_lista_usuarios.heading("codigo",text="Codigo",anchor=W)
        self.tree_lista_usuarios.heading("nombre",text="Nombre",anchor=W)
        self.tree_lista_usuarios.heading("clave",text="Clave",anchor=W)
        self.tree_lista_usuarios.heading("rol",text="Rol",anchor=W) 
        self.tree_lista_usuarios['displaycolumns']=("codigo","nombre","rol")#esto es para ocultar la clave

        #scrollbar
        tree_scroll_listausu=tb.Scrollbar(self.frame_lista_usuarios,bootstyle='round-success')
        tree_scroll_listausu.grid(row=2,column=1)
        #Configuracion del scrollbar
        tree_scroll_listausu.config(command=self.tree_lista_usuarios.yview)

        #Se llama a la funcion mostrar usuarios
        self.mostrar_usuarios()      
    def mostrar_usuarios(self):
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            #Se limpia el treeview
            registros=self.tree_lista_usuarios.get_children()
            #Se recorre cada regristro
            for elementos in registros:
                self.tree_lista_usuarios.delete(elementos)
            #Se consulta la base de datos
            miCursor.execute("SELECT * FROM Usuarios")
            #Con esto se traen todos los registros y se guardan en "datos"
            datos=miCursor.fetchall()
            #Se recorre cada fila encontrada
            for row in datos:
                #Se llena el treeview
                self.tree_lista_usuarios.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3],))
            #se aplicand cambios
            miConexion.commit()
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Lista de Usuarios", "Ocurrio un error al mostrar la lista de usuarios")
    def ventana_nuevo_usuario(self):

        self.frame_nuevo_usuario=Toplevel(self)#Ventana que va encima de la lista de usuarios
        self.frame_nuevo_usuario.title('Nuevo Usuario')#titulo de la ventana
        self.centrar_ventana_nuevo_usuario(450,260)#Tamaño de la ventana
        self.frame_nuevo_usuario.resizable(0,0)#Para que no se pueda maximixar ni minimizar
        self.frame_nuevo_usuario.grab_set()#Para que no permita ninguna otra accion hasa que se cierre la ventana

        lblframe_nuevo_usuario=LabelFrame(self.frame_nuevo_usuario)
        lblframe_nuevo_usuario.grid(row=0,column=0,sticky=NSEW,padx=10,pady=10)

        lbl_codigo_nuevo_usuario=Label(lblframe_nuevo_usuario,text='Codigo')
        lbl_codigo_nuevo_usuario.grid(row=0,column=0,padx=10,pady=10)
        self.txt_codigo_nuevo_usuario=Entry(lblframe_nuevo_usuario,width=40)
        self.txt_codigo_nuevo_usuario.grid(row=0,column=1,padx=10,pady=10)

        lbl_nombre_nuevo_usuario=Label(lblframe_nuevo_usuario,text='Nombre')
        lbl_nombre_nuevo_usuario.grid(row=1,column=0,padx=10,pady=10)
        self.txt_nombre_nuevo_usuario=Entry(lblframe_nuevo_usuario,width=40)
        self.txt_nombre_nuevo_usuario.grid(row=1,column=1,padx=10,pady=10)

        lbl_clave_nuevo_usuario=Label(lblframe_nuevo_usuario,text='Clave')
        lbl_clave_nuevo_usuario.grid(row=2,column=0,padx=10,pady=10)
        self.txt_clave_nuevo_usuario=Entry(lblframe_nuevo_usuario,width=40)
        self.txt_clave_nuevo_usuario.grid(row=2,column=1,padx=10,pady=10)

        lbl_rol_nuevo_usuario=Label(lblframe_nuevo_usuario,text='Rol')
        lbl_rol_nuevo_usuario.grid(row=3,column=0,padx=10,pady=10)
        self.txt_rol_nuevo_usuario=ttk.Combobox(lblframe_nuevo_usuario,values=('Administrador','Bodega','Vendedor'),width=38,state='readonly')
        self.txt_rol_nuevo_usuario.grid(row=3,column=1,padx=10,pady=10)
        self.txt_rol_nuevo_usuario.current(0)

        btn_guardar_nuevo_usuario=ttk.Button(lblframe_nuevo_usuario,text='Guardar',width=38,bootstyle='success',command=self.guardar_usuario)
        btn_guardar_nuevo_usuario.grid(row=4,column=1,padx=10,pady=10)
        self.correlativo_usuarios()
        self.txt_nombre_nuevo_usuario.focus()

        #Se llama a la funcion ultimo usuario
        #self.ultimo_usuario()
    def guardar_usuario(self):
        #Valida que no queden vacios los campos
        if self.txt_codigo_nuevo_usuario.get()=="" or self.txt_nombre_nuevo_usuario.get()=="" or self.txt_clave_nuevo_usuario.get()=="":
            messagebox.showwarning("Guardando Usuarios","Algun campo no es valido, por favor revise")
            return
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            
            datos_guardar_usuario=self.txt_codigo_nuevo_usuario.get(),self.txt_nombre_nuevo_usuario.get(),self.txt_clave_nuevo_usuario.get(),self.txt_rol_nuevo_usuario.get()
            #Se consulta la base de datos
            miCursor.execute("INSERT INTO Usuarios VALUES(?,?,?,?)",(datos_guardar_usuario))
            messagebox.showinfo('Guardando Usuarios',"Usuario Guardado Correctamente")
            #se aplican cambios
            miConexion.commit()
            self.frame_nuevo_usuario.destroy()#Se cierra la ventana guardar nuevo usuario
            self.ventana_lista_usuarios()#Se carga nuevamente la ventana de usuarios para ver los cambios
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Guardando Usuarios", "Ocurrio un error al Guardar Usuario")
    def centrar_ventana_nuevo_usuario(self,ancho,alto):
        ventana_ancho=ancho
        ventana_alto=alto
        pantalla_ancho=self.winfo_screenwidth()
        pantalla_alto=self.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.frame_nuevo_usuario.geometry("{}x{}+{}+{}".format(ventana_ancho,ventana_alto,coordenadas_x,coordenadas_y))
    def centrar_ventana_modificar_usuario(self,ancho,alto):
        ventana_ancho=ancho
        ventana_alto=alto
        pantalla_ancho=self.winfo_screenwidth()
        pantalla_alto=self.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.frame_modificar_usuario.geometry("{}x{}+{}+{}".format(ventana_ancho,ventana_alto,coordenadas_x,coordenadas_y))
    def buscar_usuarios(self,event):
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            #Se limpia el treeview
            registros=self.tree_lista_usuarios.get_children()
            #Se recorre cada regristro
            for elementos in registros:
                self.tree_lista_usuarios.delete(elementos)
            #Se consulta la base de datos
            miCursor.execute("SELECT * FROM Usuarios WHERE Nombre LIKE ?",(self.txt_busqueda_usuario.get() + '%',) )
            #Con esto se traen todos los registros y se guardan en "datos"
            datos=miCursor.fetchall()
            #Se recorre cada fila encontrada
            for row in datos:
                #Se llena el treeview
                self.tree_lista_usuarios.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3],))
            #se aplicand cambios
            miConexion.commit()
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Busqueda de usuarios", "Ocurrio un error al buscar en la lista de usuarios")
    def ventana_modificar_usuario(self):
        #Con esto se valida que se abra la ventana si solamentente hay algun valor seleccionado
        self.usuario_seleccionado=self.tree_lista_usuarios.focus()
        self.val_mod_usu=self.tree_lista_usuarios.item(self.usuario_seleccionado,'values')
        if self.val_mod_usu!='':
            
        
           self.frame_modificar_usuario=Toplevel(self)#Ventana que va encima de la lista de usuarios
           self.frame_modificar_usuario.title('Modificar Usuario')#titulo de la ventana
           self.centrar_ventana_modificar_usuario(450,260)
           self.frame_modificar_usuario.resizable(0,0)#Para que no se pueda maximixar ni minimizar
           self.frame_modificar_usuario.grab_set()#Para que no permita ninguna otra accion hasa que se cierre la ventana

           lblframe_modificar_usuario=LabelFrame(self.frame_modificar_usuario)
           lblframe_modificar_usuario.grid(row=0,column=0,sticky=NSEW,padx=10,pady=10)

           lbl_codigo_modificar_usuario=Label(lblframe_modificar_usuario,text='Codigo')
           lbl_codigo_modificar_usuario.grid(row=0,column=0,padx=10,pady=10)
           self.txt_codigo_modificar_usuario=Entry(lblframe_modificar_usuario,width=40)
           self.txt_codigo_modificar_usuario.grid(row=0,column=1,padx=10,pady=10)

           lbl_nombre_modificar_usuario=Label(lblframe_modificar_usuario,text='Nombre')
           lbl_nombre_modificar_usuario.grid(row=1,column=0,padx=10,pady=10)
           self.txt_nombre_modificar_usuario=Entry(lblframe_modificar_usuario,width=40)
           self.txt_nombre_modificar_usuario.grid(row=1,column=1,padx=10,pady=10)

           lbl_clave_modificar_usuario=Label(lblframe_modificar_usuario,text='Clave')
           lbl_clave_modificar_usuario.grid(row=2,column=0,padx=10,pady=10)
           self.txt_clave_modificar_usuario=Entry(lblframe_modificar_usuario,width=40)
           self.txt_clave_modificar_usuario.grid(row=2,column=1,padx=10,pady=10)

           lbl_rol_modificar_usuario=Label(lblframe_modificar_usuario,text='Rol')
           lbl_rol_modificar_usuario.grid(row=3,column=0,padx=10,pady=10)
           self.txt_rol_modificar_usuario=ttk.Combobox(lblframe_modificar_usuario,values=('Administrador','Bodega','Vendedor'),width=38)
           self.txt_rol_modificar_usuario.grid(row=3,column=1,padx=10,pady=10)


           btn_modificar_usuario=ttk.Button(lblframe_modificar_usuario,text='Guardar',width=38,bootstyle='warning',command=self.modificar_usuario)
           btn_modificar_usuario.grid(row=4,column=1,padx=10,pady=10)
           self.llenar_entrys_modificar_usuario()
    def llenar_entrys_modificar_usuario(self):
        #Se limpian todos los entrys
        self.txt_codigo_modificar_usuario.delete(0,END)
        self.txt_nombre_modificar_usuario.delete(0,END)
        self.txt_clave_modificar_usuario.delete(0,END)
        self.txt_rol_modificar_usuario.delete(0,END)
        #Se llenan los entrys
        self.txt_codigo_modificar_usuario.insert(0,self.val_mod_usu[0])
        self.txt_nombre_modificar_usuario.insert(0,self.val_mod_usu[1])
        self.txt_clave_modificar_usuario.insert(0,self.val_mod_usu[2])
        self.txt_rol_modificar_usuario.insert(0,self.val_mod_usu[3])
    def modificar_usuario(self):
        #Valida que no queden vacios los campos
        if self.txt_codigo_modificar_usuario.get()=="" or self.txt_nombre_modificar_usuario.get()=="" or self.txt_clave_modificar_usuario.get()=="":
            messagebox.showwarning("Modificar Usuarios","Algun campo no es valido, por favor revise")
            return
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            
            datos_modificar_usuario=self.txt_nombre_modificar_usuario.get(),self.txt_clave_modificar_usuario.get(),self.txt_rol_modificar_usuario.get()
            #Se consulta la base de datos
            miCursor.execute("UPDATE Usuarios SET Nombre=?,Clave=?,Rol=? WHERE Codigo="+self.txt_codigo_modificar_usuario.get(),(datos_modificar_usuario))
            messagebox.showinfo('Modificar Usuarios',"Usuario Modificado Correctamente")
            #se aplican cambios
            miConexion.commit()
            self.val_mod_usu=self.tree_lista_usuarios.item(self.usuario_seleccionado,text='',values=(self.txt_codigo_modificar_usuario.get(),self.txt_nombre_modificar_usuario.get(),self.txt_clave_modificar_usuario.get(),self.txt_rol_modificar_usuario.get(),))
            self.frame_modificar_usuario.destroy()#Se cierra la ventana guardar nuevo usuario
            #self.ventana_lista_usuarios()#Se carga nuevamente la ventana de usuarios para ver los cambios
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Modificar Usuarios", "Ocurrio un error al Modificar Usuario")
    def eliminar_usuario(self):
        self.usuario_seleccionado_eliminar=self.tree_lista_usuarios.focus()
        self.val_elm_usu = self.tree_lista_usuarios.item(self.usuario_seleccionado_eliminar, 'values')

        try:
            if self.val_elm_usu!= '':
                respuesta = messagebox.askquestion('Eliminando Usuario', '¿Está seguro de eliminar el usuario seleccionado?')
                if respuesta == 'yes':
                    miConexion = sqlite3.connect('Ventas.db')
                    miCursor = miConexion.cursor()
                    miCursor.execute("DELETE FROM Usuarios WHERE Codigo="+ str(self.val_elm_usu[0]))
                    miConexion.commit()
                    messagebox.showinfo('Eliminando Usuario', 'Registro Eliminado Correctamente')
                    self.mostrar_usuarios()
                    miConexion.close()
                else:
                    messagebox.showerror('Eliminando Usuario', 'Eliminación Cancelada')
        except:
            messagebox.showerror('Eliminando Usuario','Ocurrió un error')
    def correlativo_usuarios(self):
        #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            miCursor.execute("SELECT MAX(Codigo) FROM Usuarios")
            #Con esto se traen todos los registros y se guardan en "datos"
            correlativo_usuarios=miCursor.fetchone()
            for datos in correlativo_usuarios:
                if datos==None:
                    self.nuevo_correlativo_usuario=(int(1))
                    self.txt_codigo_nuevo_usuario.config(state=NORMAL)
                    self.txt_codigo_nuevo_usuario.insert(0,self.nuevo_correlativo_usuario)
                    self.txt_codigo_nuevo_usuario.config(state='readonly')
                else:
                    self.nuevo_correlativo_usuario=(int(datos)+1)
                    self.txt_codigo_nuevo_usuario.config(state=NORMAL)
                    self.txt_codigo_nuevo_usuario.insert(0,self.nuevo_correlativo_usuario)
                    self.txt_codigo_nuevo_usuario.config(state='readonly')

            #se aplican cambios
            miConexion.commit()
            #Se cierra la conexion
            miConexion.close()

#===============================PRODUCTOS================================

    def mostrar_productos(self):
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            #Se limpia el treeview
            registros=self.tree_lista_productos.get_children()
            #Se recorre cada regristro
            for elementos in registros:
                self.tree_lista_productos.delete(elementos)
            #Se consulta la base de datos
            miCursor.execute("SELECT * FROM Productos")
            #Con esto se traen todos los registros y se guardan en "datos"
            datos=miCursor.fetchall()
            #Se recorre cada fila encontrada
            for row in datos:
                #Se llena el treeview
                self.tree_lista_productos.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
            #se aplicand cambios
            miConexion.commit()
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Lista de Productos", "Ocurrio un error al mostrar la lista de productos")   
    def ventana_lista_productos(self):
        self.borrar_frames()
        self.frame_lista_productos=Frame(self.frame_center)
        self.frame_lista_productos.grid(row=0,column=0,columnspan=2,sticky=NSEW)

        self.lblframe_botones_listprod=LabelFrame(self.frame_lista_productos)
        self.lblframe_botones_listprod.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        btn_nuevo_producto=tb.Button(self.lblframe_botones_listprod,text='Nuevo',width=21
                                    ,bootstyle="success",command=self.ventana_nuevo_producto)
        btn_nuevo_producto.grid(row=0,column=0,padx=5,pady=5)
        btn_modificar_producto=tb.Button(self.lblframe_botones_listprod,text='Modificar',width=21,bootstyle="warning",command=self.ventana_modificar_producto)
        btn_modificar_producto.grid(row=0,column=1,padx=5,pady=5)
        btn_eliminar_producto=tb.Button(self.lblframe_botones_listprod,text='Eliminar',width=21,bootstyle="danger",command=self.eliminar_producto)
        btn_eliminar_producto.grid(row=0,column=2,padx=5,pady=5)   

        self.lblframe_busqueda_listprod=LabelFrame(self.frame_lista_productos)
        self.lblframe_busqueda_listprod.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW) 

        self.txt_busqueda_producto=ttk.Entry(self.lblframe_busqueda_listprod,width=172)
        self.txt_busqueda_producto.grid(row=0,column=0,padx=5,pady=5)  
        self.txt_busqueda_producto.bind('<KeyRelease>',self.buscar_producto)                       

        #========================Treeview=====================================
        
        self.lblframe_tree_listprod=LabelFrame(self.frame_lista_productos)
        self.lblframe_tree_listprod.grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)

        columnas=("codigo","nombre","proveedor","costo","precio","stock","talla","fechaderecepcion")

        self.tree_lista_productos=tb.Treeview(self.lblframe_tree_listprod,columns=columnas,
                                         height=17,show='headings',bootstyle="dark")
        self.tree_lista_productos.grid(row=0,column=0)
        
        self.tree_lista_productos.heading("codigo",text="Codigo",anchor=W)
        self.tree_lista_productos.heading("nombre",text="Nombre",anchor=W)
        self.tree_lista_productos.heading("proveedor",text="Proveedor",anchor=W)
        self.tree_lista_productos.heading("costo",text="Costo",anchor=W) 
        self.tree_lista_productos.heading("precio",text="Precio",anchor=W)
        self.tree_lista_productos.heading("stock",text="Stock",anchor=W)
        self.tree_lista_productos.heading("talla",text="Talla",anchor=W)
        self.tree_lista_productos.heading("fechaderecepcion",text="Fecha de recepcion",anchor=W)

        self.tree_lista_productos['displaycolumns']=("codigo","nombre","proveedor","costo","precio","stock","talla","fechaderecepcion")

        #scrollbar
        tree_scroll_listaprod=tb.Scrollbar(self.frame_lista_productos,bootstyle='round-success')
        tree_scroll_listaprod.grid(row=2,column=1,padx=5,pady=10)
        #Configuracion del scrollbar
        tree_scroll_listaprod.config(command=self.tree_lista_productos.yview)

        #Se llama a la funcion mostrar usuarios
        self.mostrar_productos()      
    def ventana_nuevo_producto(self):

        self.frame_nuevo_producto=Toplevel(self)
        self.frame_nuevo_producto.title('Nuevo Producto')
        self.centrar_ventana_nuevo_producto(542,450)
        self.frame_nuevo_producto.resizable(0,0)
        self.frame_nuevo_producto.grab_set()

        lblframe_nuevo_producto=LabelFrame(self.frame_nuevo_producto)
        lblframe_nuevo_producto.grid(row=0,column=0,sticky=NSEW,padx=10,pady=10)

        lbl_codigo_nuevo_producto=Label(lblframe_nuevo_producto,text='Codigo')
        lbl_codigo_nuevo_producto.grid(row=0,column=0,padx=10,pady=10)
        self.txt_codigo_nuevo_producto=Entry(lblframe_nuevo_producto,width=40)
        self.txt_codigo_nuevo_producto.grid(row=0,column=1,padx=10,pady=10)

        lbl_nombre_nuevo_producto=Label(lblframe_nuevo_producto,text='Nombre')
        lbl_nombre_nuevo_producto.grid(row=1,column=0,padx=10,pady=10)
        self.txt_nombre_nuevo_producto=Entry(lblframe_nuevo_producto,width=40)
        self.txt_nombre_nuevo_producto.grid(row=1,column=1,padx=10,pady=10)

        lbl_proveedor_nuevo_producto=Label(lblframe_nuevo_producto,text='Proveedor')
        lbl_proveedor_nuevo_producto.grid(row=2,column=0,padx=10,pady=10)
        self.txt_proveedor_nuevo_producto=Entry(lblframe_nuevo_producto,width=40)
        self.txt_proveedor_nuevo_producto.grid(row=2,column=1,padx=10,pady=10)

        lbl_costo_nuevo_producto=Label(lblframe_nuevo_producto,text='Costo')
        lbl_costo_nuevo_producto.grid(row=3,column=0,padx=10,pady=10)
        self.txt_costo_nuevo_producto=Entry(lblframe_nuevo_producto,width=40)
        self.txt_costo_nuevo_producto.grid(row=3,column=1,padx=10,pady=10)

        lbl_precio_nuevo_producto=Label(lblframe_nuevo_producto,text='Precio')
        lbl_precio_nuevo_producto.grid(row=4,column=0,padx=10,pady=10)
        self.txt_precio_nuevo_producto=Entry(lblframe_nuevo_producto,width=40)
        self.txt_precio_nuevo_producto.grid(row=4,column=1,padx=10,pady=10)

        lbl_stock_nuevo_producto=Label(lblframe_nuevo_producto,text='Stock')
        lbl_stock_nuevo_producto.grid(row=5,column=0,padx=10,pady=10)
        self.txt_stock_nuevo_producto=Entry(lblframe_nuevo_producto,width=40)
        self.txt_stock_nuevo_producto.grid(row=5,column=1,padx=10,pady=10)
        
        lbl_talla_nuevo_producto=Label(lblframe_nuevo_producto,text='Talla')
        lbl_talla_nuevo_producto.grid(row=7,column=0,padx=10,pady=10)
        self.txt_talla_nuevo_producto=ttk.Combobox(lblframe_nuevo_producto,values=('2','4','6','8','10','12','14','16','18','S','M','L','XL','XXL'),width=38,state='readonly')
        self.txt_talla_nuevo_producto.grid(row=7,column=1,padx=10,pady=10)
        self.txt_talla_nuevo_producto.current(0)
        
        lbl_fechaderecepcion_nuevo_producto=Label(lblframe_nuevo_producto,text='Fecha de Recepcion')
        lbl_fechaderecepcion_nuevo_producto.grid(row=6,column=0,padx=10,pady=10)
        self.txt_fechaderecepcion_nuevo_producto=Entry(lblframe_nuevo_producto,width=40)
        self.txt_fechaderecepcion_nuevo_producto.grid(row=6,column=1,padx=10,pady=10)


        btn_guardar_nuevo_producto=ttk.Button(lblframe_nuevo_producto,text='Guardar',width=38,bootstyle='success',command=self.guardar_producto)
        btn_guardar_nuevo_producto.grid(row=8,column=1,padx=10,pady=10)
    def centrar_ventana_nuevo_producto(self,ancho,alto):
        ventana_ancho=ancho
        ventana_alto=alto
        pantalla_ancho=self.winfo_screenwidth()
        pantalla_alto=self.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.frame_nuevo_producto.geometry("{}x{}+{}+{}".format(ventana_ancho,ventana_alto,coordenadas_x,coordenadas_y))
    def centrar_ventana_modificar_producto(self,ancho,alto):
        ventana_ancho=ancho
        ventana_alto=alto
        pantalla_ancho=self.winfo_screenwidth()
        pantalla_alto=self.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.frame_modificar_producto.geometry("{}x{}+{}+{}".format(ventana_ancho,ventana_alto,coordenadas_x,coordenadas_y))
    def guardar_producto(self):
        #Valida que no queden vacios los campos
        if self.txt_codigo_nuevo_producto.get()=="" or self.txt_nombre_nuevo_producto.get()=="" or self.txt_proveedor_nuevo_producto.get()=="" or self.txt_precio_nuevo_producto.get()=="" or self.txt_stock_nuevo_producto.get()=="" or self.txt_talla_nuevo_producto.get()=="" or self.txt_fechaderecepcion_nuevo_producto.get()=="":
            messagebox.showwarning("Guardando Producto","Algun campo no es valido, por favor revise")
            return
        #Capturador de errores
        try:
            float(self.txt_costo_nuevo_producto.get())
            float(self.txt_precio_nuevo_producto.get())
            int(self.txt_stock_nuevo_producto.get())
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            
            datos_guardar_producto=self.txt_codigo_nuevo_producto.get(),self.txt_nombre_nuevo_producto.get(),self.txt_proveedor_nuevo_producto.get(),self.txt_costo_nuevo_producto.get(),self.txt_precio_nuevo_producto.get(),self.txt_stock_nuevo_producto.get(),self.txt_talla_nuevo_producto.get(),self.txt_fechaderecepcion_nuevo_producto.get()
            #Se consulta la base de datos
            miCursor.execute("INSERT INTO Productos VALUES(?,?,?,?,?,?,?,?)",(datos_guardar_producto))
            messagebox.showinfo('Guardando Producto',"Producto Guardado Correctamente")
            #se aplican cambios
            miConexion.commit()
            self.frame_nuevo_producto.destroy()
            self.ventana_lista_productos()
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Guardando Productos", "Ocurrio un error al Guardar el Producto")
    def eliminar_producto(self):
        self.producto_seleccionado_eliminar=self.tree_lista_productos.focus()
        self.val_elm_prod = self.tree_lista_productos.item(self.producto_seleccionado_eliminar, 'values')

        try:
            if self.val_elm_prod!= '':
                respuesta = messagebox.askquestion('Eliminando Producto', '¿Está seguro de eliminar el producto seleccionado?')
                if respuesta == 'yes':
                    miConexion = sqlite3.connect('Ventas.db')
                    miCursor = miConexion.cursor()
                    miCursor.execute("DELETE FROM Productos WHERE Codigo="+ str(self.val_elm_prod[0]))
                    miConexion.commit()
                    messagebox.showinfo('Eliminando Producto', 'Registro Eliminado Correctamente')
                    self.mostrar_productos()
                    miConexion.close()
                else:
                    messagebox.showerror('Eliminando Producto', 'Eliminación Cancelada')
        except:
            messagebox.showerror('Eliminando Producto','Ocurrió un error')
    def buscar_producto(self,event):
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            #Se limpia el treeview
            registros=self.tree_lista_productos.get_children()
            #Se recorre cada regristro
            for elementos in registros:
                self.tree_lista_productos.delete(elementos)
            #Se consulta la base de datos
            miCursor.execute("SELECT * FROM Productos WHERE Nombre LIKE ?",(self.txt_busqueda_producto.get() + '%',) )
            #Con esto se traen todos los registros y se guardan en "datos"
            datos_productos=miCursor.fetchall()
            #Se recorre cada fila encontrada
            for row in datos_productos:
                #Se llena el treeview
                self.tree_lista_productos.insert('',0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],))
            #se aplicand cambios
            miConexion.commit()
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Busqueda de productos", "Ocurrio un error al buscar en la lista de productos")
    def ventana_modificar_producto(self):

        self.producto_seleccionado=self.tree_lista_productos.focus()
        self.val_mod_prod=self.tree_lista_productos.item(self.producto_seleccionado,'values')
        if self.val_mod_prod!='':

           self.frame_modificar_producto=Toplevel(self)
           self.frame_modificar_producto.title('Modificar Producto')
           self.centrar_ventana_modificar_producto(542,450)
           self.frame_modificar_producto.resizable(0,0)
           self.frame_modificar_producto.grab_set()

           lblframe_modificar_producto=LabelFrame(self.frame_modificar_producto)
           lblframe_modificar_producto.grid(row=0,column=0,sticky=NSEW,padx=10,pady=10)

           lbl_codigo_modificar_producto=Label(lblframe_modificar_producto,text='Codigo')
           lbl_codigo_modificar_producto.grid(row=0,column=0,padx=10,pady=10)
           self.txt_codigo_modificar_producto=Entry(lblframe_modificar_producto,width=40,state='readonly')
           self.txt_codigo_modificar_producto.grid(row=0,column=1,padx=10,pady=10)

           lbl_nombre_modificar_producto=Label(lblframe_modificar_producto,text='Nombre')
           lbl_nombre_modificar_producto.grid(row=1,column=0,padx=10,pady=10)
           self.txt_nombre_modificar_producto=Entry(lblframe_modificar_producto,width=40)
           self.txt_nombre_modificar_producto.grid(row=1,column=1,padx=10,pady=10)

           lbl_proveedor_modificar_producto=Label(lblframe_modificar_producto,text='Proveedor')
           lbl_proveedor_modificar_producto.grid(row=2,column=0,padx=10,pady=10)
           self.txt_proveedor_modificar_producto=Entry(lblframe_modificar_producto,width=40)
           self.txt_proveedor_modificar_producto.grid(row=2,column=1,padx=10,pady=10)

           lbl_costo_modificar_producto=Label(lblframe_modificar_producto,text='Costo')
           lbl_costo_modificar_producto.grid(row=3,column=0,padx=10,pady=10)
           self.txt_costo_modificar_producto=Entry(lblframe_modificar_producto,width=40)
           self.txt_costo_modificar_producto.grid(row=3,column=1,padx=10,pady=10)

           lbl_precio_modificar_producto=Label(lblframe_modificar_producto,text='Precio')
           lbl_precio_modificar_producto.grid(row=4,column=0,padx=10,pady=10)
           self.txt_precio_modificar_producto=Entry(lblframe_modificar_producto,width=40)
           self.txt_precio_modificar_producto.grid(row=4,column=1,padx=10,pady=10)

           lbl_stock_modificar_producto=Label(lblframe_modificar_producto,text='Stock')
           lbl_stock_modificar_producto.grid(row=5,column=0,padx=10,pady=10)
           self.txt_stock_modificar_producto=Entry(lblframe_modificar_producto,width=40)
           self.txt_stock_modificar_producto.grid(row=5,column=1,padx=10,pady=10)
        
           lbl_talla_modificar_producto=Label(lblframe_modificar_producto,text='Talla')
           lbl_talla_modificar_producto.grid(row=7,column=0,padx=10,pady=10)
           self.txt_talla_modificar_producto=ttk.Combobox(lblframe_modificar_producto,values=('2','4','6','8','10','12','14','16','18','S','M','L','XL','XXL'),width=38,state='readonly')
           self.txt_talla_modificar_producto.grid(row=7,column=1,padx=10,pady=10)
           self.txt_talla_modificar_producto.current(0)
        
           lbl_fechaderecepcion_modificar_producto=Label(lblframe_modificar_producto,text='Fecha de Recepcion')
           lbl_fechaderecepcion_modificar_producto.grid(row=6,column=0,padx=10,pady=10)
           self.txt_fechaderecepcion_modificar_producto=Entry(lblframe_modificar_producto,width=40)
           self.txt_fechaderecepcion_modificar_producto.grid(row=6,column=1,padx=10,pady=10)

           btn_guardar_modificar_producto=ttk.Button(lblframe_modificar_producto,text='Modificar',width=38,bootstyle='warning',command=self.modificar_producto)
           btn_guardar_modificar_producto.grid(row=8,column=1,padx=10,pady=10)

           self.llenar_entrys_modificar_producto()     
    def llenar_entrys_modificar_producto(self):
        #Se limpian todos los entrys
        self.txt_codigo_modificar_producto.delete(0,END)
        self.txt_nombre_modificar_producto.delete(0,END)
        self.txt_proveedor_modificar_producto.delete(0,END)
        self.txt_costo_modificar_producto.delete(0,END)
        self.txt_precio_modificar_producto.delete(0,END)
        self.txt_stock_modificar_producto.delete(0,END)
        self.txt_talla_modificar_producto.delete(0,END)
        self.txt_fechaderecepcion_modificar_producto.delete(0,END)
        #Se llenan los entrys
        self.txt_codigo_modificar_producto.insert(0,self.val_mod_prod[0])
        self.txt_nombre_modificar_producto.insert(0,self.val_mod_prod[1])
        self.txt_proveedor_modificar_producto.insert(0,self.val_mod_prod[2])
        self.txt_costo_modificar_producto.insert(0,self.val_mod_prod[3])
        self.txt_precio_modificar_producto.insert(0,self.val_mod_prod[4])
        self.txt_stock_modificar_producto.insert(0,self.val_mod_prod[5])
        self.txt_talla_modificar_producto.insert(0,self.val_mod_prod[6])
        self.txt_fechaderecepcion_modificar_producto.insert(0,self.val_mod_prod[7])
    def modificar_producto(self):
        #Valida que no queden vacios los campos
       if self.txt_codigo_modificar_producto.get()=="" or self.txt_nombre_modificar_producto.get()=="" or self.txt_proveedor_modificar_producto.get()=="" or self.txt_precio_modificar_producto.get()=="" or self.txt_stock_modificar_producto.get()=="" or self.txt_talla_modificar_producto.get()=="" or self.txt_fechaderecepcion_modificar_producto.get()=="":
            messagebox.showwarning("Modificando Producto","Algun campo no es valido, por favor revise")
            return
        #Capturador de errores
       try:
            float(self.txt_costo_modificar_producto.get())
            float(self.txt_precio_modificar_producto.get())
            int(self.txt_stock_modificar_producto.get())
             #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            
            modificar_datos_producto=(self.txt_nombre_modificar_producto.get(),self.txt_proveedor_modificar_producto.get(),self.txt_costo_modificar_producto.get(),self.txt_precio_modificar_producto.get(),self.txt_stock_modificar_producto.get(),self.txt_talla_modificar_producto.get(),self.txt_fechaderecepcion_modificar_producto.get())
            #Se consulta la base de datos
            miCursor.execute("UPDATE Productos SET Nombre=?,Proveedor=?,Costo=?,Precio=?,Stock=?,Talla=?,Fechaderecepcion=? WHERE Codigo="+self.txt_codigo_modificar_producto.get(),(modificar_datos_producto))
            messagebox.showinfo('Modificar Productos',"Producto Modificado Correctamente")
            #se aplican cambios
            miConexion.commit()
            self.valores_producto_seleccionado=self.tree_lista_productos.item(self.producto_seleccionado,text='',values=(self.txt_codigo_modificar_producto.get(),self.txt_nombre_modificar_producto.get(),self.txt_proveedor_modificar_producto.get(),self.txt_costo_modificar_producto.get(),self.txt_precio_modificar_producto.get(),self.txt_stock_modificar_producto.get(),self.txt_talla_modificar_producto.get(),self.txt_fechaderecepcion_modificar_producto.get()))
            self.frame_modificar_producto.destroy()
            #Se cierra la conexion
            miConexion.close()
       except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Modificar Productos","Ocurrio un error al Modificar Producto")
    
#===============================VENTAS====================================

    def ventana_detalle_ventas(self):
        self.borrar_frames()
        self.frame_detalle_venta=tb.Frame(self.frame_center)
        self.frame_detalle_venta.grid(row=0,column=1,sticky=NSEW)

        self.lblframe_botones_detalle_venta=tb.LabelFrame(self.frame_detalle_venta)
        self.lblframe_botones_detalle_venta.grid(row=0,column=0,sticky=NSEW)

        btn_detalle=tb.Button(self.lblframe_botones_detalle_venta,text='Detalle',width=12,command=self.ventana_listado_ventas)
        btn_detalle.grid(row=0,column=0,padx=5)

        btn_cantidad=tb.Button(self.lblframe_botones_detalle_venta,text='Cantidad',width=12,command=self.ventana_modificar_cantidad)
        btn_cantidad.grid(row=0,column=1,padx=5)

        btn_borrar=tb.Button(self.lblframe_botones_detalle_venta,text='Borrar',width=12,command=self.borrar_producto_detalle_venta)
        btn_borrar.grid(row=0,column=2,padx=4)   

        btn_descuento=tb.Button(self.lblframe_botones_detalle_venta,text='Descuento',width=12,command=self.ventana_descuento)
        btn_descuento.grid(row=0,column=3,padx=5)

        btn_cobrar=tb.Button(self.lblframe_botones_detalle_venta,text='Cobrar',width=12,command=self.ventana_contado)
        btn_cobrar.grid(row=0,column=4,padx=5)


        self.busqueda_codigo()
        self.busqueda_nombre()               

        #========================Treeview=====================================
        
        self.lblframe_tree_lista_detalle_venta=LabelFrame(self.frame_detalle_venta)
        self.lblframe_tree_lista_detalle_venta.grid(row=2,column=0,sticky=NSEW)

        columnas=("no","codigo","nombre","costo","precio","cantidad","stock","descuento","subtotal","existencia")

        self.tree_detalle_venta=tb.Treeview(self.lblframe_tree_lista_detalle_venta,columns=columnas,
                                         height=34,show='headings',bootstyle="dark")
        self.tree_detalle_venta.grid(row=0,column=0)
        
        self.tree_detalle_venta.heading("no",text="No",anchor=W)
        self.tree_detalle_venta.heading("codigo",text="Codigo",anchor=W)
        self.tree_detalle_venta.heading("nombre",text="Nombre",anchor=W)
        self.tree_detalle_venta.heading("costo",text="Costo",anchor=W) 
        self.tree_detalle_venta.heading("precio",text="Precio",anchor=W)
        self.tree_detalle_venta.heading("cantidad",text="Cantidad",anchor=W)
        self.tree_detalle_venta.heading("stock",text="Stock",anchor=W)
        self.tree_detalle_venta.heading("descuento",text="Descuento",anchor=W)
        self.tree_detalle_venta.heading("subtotal",text="Subtotal",anchor=W)
        self.tree_detalle_venta.heading("existencia",text="Existencia",anchor=W)
  
        self.tree_detalle_venta['displaycolumns']=("codigo","nombre","precio","cantidad","subtotal","existencia")

        #scrollbar
        tree_scroll=tb.Scrollbar(self.frame_detalle_venta,bootstyle='round-success')
        tree_scroll.grid(row=2,column=2,pady=10)
        #Configuracion del scrollbar
        tree_scroll.config(command=self.tree_detalle_venta.yview)

        self.lblframe_total_detalle_venta=tb.LabelFrame(self.frame_detalle_venta)
        self.lblframe_total_detalle_venta.grid(row=3,column=0,sticky=NSEW)

        self.txt_total_detalle_venta=tb.Entry(self.lblframe_total_detalle_venta,width=59,font=('calibri',24),justify=CENTER)
        self.txt_total_detalle_venta.grid(row=0,column=0)

        self.ent_busqueda_detalle_venta.focus()
        self.ventana_busqueda_detalle_venta()
        self.buscar_productos_detalle_venta('')
        self.mostrar_productos_detalle_venta()
        self.total_detalle_venta()
        self.correlativo_ventas()
    def busqueda_nombre(self):
        self.lblframe_busqueda_detalle_venta=tb.LabelFrame(self.frame_detalle_venta)
        self.lblframe_busqueda_detalle_venta.grid(row=1,column=0,sticky=NSEW) 
        
        self.btn_busqueda_nombre=tb.Button(self.lblframe_busqueda_detalle_venta,text='abc',bootstyle='success-outline',command=self.busqueda_codigo)
        self.btn_busqueda_nombre.grid(row=0,column=0)
       
        self.ent_busqueda_detalle_venta=ttk.Entry(self.lblframe_busqueda_detalle_venta,font=14,width=64,bootstyle='info')
        self.ent_busqueda_detalle_venta.grid(row=0,column=1)  
        self.ent_busqueda_detalle_venta.bind('<KeyRelease>',self.buscar_productos_detalle_venta)
    def busqueda_codigo(self):
        self.lblframe_busqueda_detalle_venta=tb.LabelFrame(self.frame_detalle_venta)
        self.lblframe_busqueda_detalle_venta.grid(row=1,column=0,sticky=NSEW) 
        
        self.btn_busqueda_codigo=tb.Button(self.lblframe_busqueda_detalle_venta,text=' # ',bootstyle='success-outline',command=self.busqueda_nombre)
        self.btn_busqueda_codigo.grid(row=0,column=0)
       
        self.txt_busqueda_codigo_detalle_venta=ttk.Entry(self.lblframe_busqueda_detalle_venta,font=14,width=64,bootstyle='info')
        self.txt_busqueda_codigo_detalle_venta.grid(row=0,column=1)  
        self.txt_busqueda_codigo_detalle_venta.bind('<Return>',self.producto_encontrado_detalle_venta)    
    def ventana_busqueda_detalle_venta(self):
        self.frame_busqueda_detalle_venta=ScrolledFrame(self,width=517,autohide=True)
        self.frame_busqueda_detalle_venta.grid(row=0,column=2,sticky=NSEW)
    def buscar_productos_detalle_venta(self,event):
        try:
            
            miConexion=sqlite3.connect('Ventas.db')
            
            miCursor=miConexion.cursor()
            
            for wid in self.frame_busqueda_detalle_venta.winfo_children():
                wid.destroy()
            
            miCursor.execute("SELECT * FROM Productos WHERE Nombre LIKE ?",(self.ent_busqueda_detalle_venta.get() + '%',) )
            
            datos_productos_detalle_venta=miCursor.fetchall()

            codigo_busqueda_detalle_venta=StringVar()
            contador=0
            filas=2
            
            for row in datos_productos_detalle_venta:

                radbutton=Radiobutton(self.frame_busqueda_detalle_venta,text=row[1]+'\n'+row[2]+'\n' '\n'+str(f'${row[4]:,.2f}'),value=row[0],variable=codigo_busqueda_detalle_venta,indicatoron=0,width=30,height=5,command=lambda:self.pasar_codigo_detalle_venta(codigo_busqueda_detalle_venta.get()))
                radbutton.grid(row=contador//filas,column=contador%filas)
                contador+=1
                
            
            miConexion.commit()
            
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Busqueda de productos", "Ocurrio un error al buscar en la lista de productos")
    def pasar_codigo_detalle_venta(self,codigo_seleccionado_detalle_venta):
        self.txt_busqueda_codigo_detalle_venta.insert(0,codigo_seleccionado_detalle_venta)
        self.producto_encontrado_detalle_venta('')
    def producto_seleccionado_detalle_venta(self):
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            
            miCursor.execute("SELECT * FROM Productos WHERE Codigo="+self.txt_busqueda_codigo_detalle_venta.get())
            #Con esto se traen todos los registros y se guardan en "datos"
            datos_producto_seleccionado=miCursor.fetchall()

            if datos_producto_seleccionado!=None:
                for row in datos_producto_seleccionado:
                    self.datos_guardar_producto_detalle_venta=(int(self.nuevo_correlativo_ventas),row[0],row[1],row[3],row[4],'1',row[5],'0')
            
            

            miConexion.commit()

            self.mostrar_productos_detalle_venta() 
            self.agregar_producto_detalle_venta()

            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Producto Seleccionado", "Ocurrio un error al buscar en la lista de productos")
    def agregar_producto_detalle_venta(self):

        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()  
            miCursor.execute("INSERT INTO DetalleVentaT VALUES(?,?,?,?,?,?,?,?)",(self.datos_guardar_producto_detalle_venta))
            messagebox.showinfo('Agregando Productos Detalle Venta',"Registro Agregado Correctamente")
            #se aplican cambios
            miConexion.commit()
            self.frame_nuevo_producto.destroy()
            self.ventana_lista_productos()
            #Se cierra la conexion
            miConexion.close()

        except:
             #Mensaje si ocurre algun error
            messagebox.showerror("Agregando Productos Detalle Venta", "Ocurrio un error al Agregar el Producto")
    def mostrar_productos_detalle_venta(self):
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            #Se limpia el treeview
            registros=self.tree_detalle_venta.get_children()
            #Se recorre cada regristro
            for elementos in registros:
                self.tree_detalle_venta.delete(elementos)
            #Se consulta la base de datos
            miCursor.execute("SELECT * FROM DetalleVentaT")
            #Con esto se traen todos los registros y se guardan en "datos"
            self.datos_productos_detalle_venta=miCursor.fetchall()
            #Se recorre cada fila encontrada
            for row in self.datos_productos_detalle_venta:
                #Calcular el subtotal y la existencia

                subtotal=float(row[4]*row[5])
                existencia=int(row[6]-row[5])
                self.tree_detalle_venta.insert('',0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],subtotal,existencia))
            #se aplicand cambios
            miConexion.commit()
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Busqueda de productos detalle venta", "Ocurrio un error al buscar en la lista de productos")
    def producto_encontrado_detalle_venta(self,event):
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            
            miCursor.execute("SELECT * FROM DetalleVentaT WHERE Codigo="+self.txt_busqueda_codigo_detalle_venta.get())
            producto_entontrado=miCursor.fetchall()
            for row in producto_entontrado:
                cantidad_actual=row[5]
                stock_actual=row[6]
                existencia=int(stock_actual-cantidad_actual)
                if existencia==0:
                    messagebox.showwarning('Existencia','Producto sin existencia')
                    self.txt_busqueda_codigo_detalle_venta.delete(0,END)
                    return
            if producto_entontrado==[]:
                miCursor.execute("SELECT Stock FROM Productos WHERE Codigo="+self.txt_busqueda_codigo_detalle_venta.get())
                producto_no_entontrado=miCursor.fetchall()
                for row in producto_no_entontrado:
                    stock=row[0]
                    if stock==0:
                        messagebox.showwarning('Existencia','Producto sin existencia')
                        self.txt_busqueda_codigo_detalle_venta.delete(0,END)
                        return
                    else:
                       self.producto_seleccionado_detalle_venta()
                       self.txt_busqueda_codigo_detalle_venta.delete(0,END)
                       self.total_detalle_venta()
            else:
                self.sumar_uno_detalle_venta()
                self.txt_busqueda_codigo_detalle_venta.delete(0,END)
                self.total_detalle_venta()
                
            #se aplicand cambios
            miConexion.commit()
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Productos", "Producto no encontrado")
    def sumar_uno_detalle_venta(self):
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()

            miCursor.execute("UPDATE DetalleVentaT SET Cantidad=Cantidad + 1 WHERE Codigo="+self.txt_busqueda_codigo_detalle_venta.get())
            #se aplican cambios
            miConexion.commit()
            self.mostrar_productos_detalle_venta()

            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Sumar uno detalle venta", "Ocurrio un error al Modificar Usuario")
    def borrar_producto_detalle_venta(self):
        self.producto_seleccionado_eliminar=self.tree_detalle_venta.focus()
        self.valor_producto_seleccionado_eliminar = self.tree_detalle_venta.item(self.producto_seleccionado_eliminar, 'values')
        if self.valor_producto_seleccionado_eliminar!='':
            
            try:
                    miConexion = sqlite3.connect('Ventas.db')
                    miCursor = miConexion.cursor()
                    miCursor.execute("DELETE FROM DetalleVentaT WHERE Codigo="+ str(self.valor_producto_seleccionado_eliminar[1]))

                    miConexion.commit()
                    messagebox.showinfo('Eliminando Producto Detalle Venta', 'Registro Eliminado Correctamente')
                    self.mostrar_productos_detalle_venta()
                    self.total_detalle_venta()
                    miConexion.close()
            except:
                messagebox.showerror('Eliminando Producto Detalle venta','Ocurrió un error')
    def total_detalle_venta(self):
        self.total=0
        for row in self.tree_detalle_venta.get_children():
            self.total+=float(self.tree_detalle_venta.item(row,'values')[8])

        self.txt_total_detalle_venta.config(state=NORMAL)
        self.txt_total_detalle_venta.delete(0,END)
        self.txt_total_detalle_venta.insert(0,f'${self.total:,.2f}')
        self.txt_total_detalle_venta.config(state='readonly')
    def ventana_modificar_cantidad(self):
        #Con esto se valida que se abra la ventana si solamentente hay algun valor seleccionado
        self.cantidad_seleccionada=self.tree_detalle_venta.focus()
        self.val_can_sel=self.tree_detalle_venta.item(self.cantidad_seleccionada,'values')
        if self.val_can_sel!='':
            
        
           self.frame_modificar_cantidad=Toplevel(self)#Ventana que va encima de la lista de usuarios
           self.frame_modificar_cantidad.title('Modificar Cantidad')#titulo de la ventana
           self.centrar_ventana_modificar_cantidad(400,250)
           self.frame_modificar_cantidad.resizable(0,0)#Para que no se pueda maximixar ni minimizar
           self.frame_modificar_cantidad.grab_set()#Para que no permita ninguna otra accion hasa que se cierre la ventana
           
           variable_nombre=(self.val_can_sel[2])

           lbl_nombre_cantidad=tb.Label(self.frame_modificar_cantidad,text='Producto',font=('Calibri',16),bootstyle='info')
           lbl_nombre_cantidad.pack(padx=10,pady=35)
           lbl_nombre_cantidad.config(text=variable_nombre)

           lbl_cantidad_modificar=Label(self.frame_modificar_cantidad,text='Cantidad',font=14)
           lbl_cantidad_modificar.pack(padx=10,pady=5)
           self.txt_cantidad_modificar_detalle=Entry(self.frame_modificar_cantidad,justify=CENTER,font=14)
           self.txt_cantidad_modificar_detalle.pack(padx=10,pady=15)
           self.txt_cantidad_modificar_detalle.insert(0,self.val_can_sel[5])
           self.txt_cantidad_modificar_detalle.focus()
           self.txt_cantidad_modificar_detalle.bind('<Return>',self.modificar_cantidad)
    def centrar_ventana_modificar_cantidad(self,ancho,alto):
        ventana_ancho=ancho
        ventana_alto=alto
        pantalla_ancho=self.winfo_screenwidth()
        pantalla_alto=self.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.frame_modificar_cantidad.geometry("{}x{}+{}+{}".format(ventana_ancho,ventana_alto,coordenadas_x,coordenadas_y))
    def modificar_cantidad(self,event):
        #Valida que no queden vacios los campos
        if self.txt_cantidad_modificar_detalle.get()=='0':
            messagebox.showwarning("Modificar Cantidad","La cantidad no es valida")
            return
        if int(self.txt_cantidad_modificar_detalle.get())>int(self.val_can_sel[6]):
            messagebox.showerror('Modificando Cantidad','Existencia insuficiente')
            return
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()

            codigo=self.val_can_sel[1]
            cantidad=self.txt_cantidad_modificar_detalle.get()
            
            miCursor.execute("UPDATE DetalleVentaT SET Cantidad=? WHERE Codigo = ?",(cantidad,codigo))
            
            miConexion.commit()

            subtotal=float(self.val_can_sel[4])*float(self.txt_cantidad_modificar_detalle.get())
            existencia=int(self.val_can_sel[6])-int(self.txt_cantidad_modificar_detalle.get())

            self.val_can_sel=self.tree_detalle_venta.item(self.cantidad_seleccionada,text='',values=(self.val_can_sel[0],self.val_can_sel[1],self.val_can_sel[2],self.val_can_sel[3],self.val_can_sel[4],self.txt_cantidad_modificar_detalle.get(),self.val_can_sel[6],self.val_can_sel[7],subtotal,existencia))
            self.frame_modificar_cantidad.destroy()
            self.total_detalle_venta()
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Modificar Cantidad Detalle Venta", "Ocurrio un error")
    def ventana_descuento(self):
        #Con esto se valida que se abra la ventana si solamentente hay algun valor seleccionado
        self.descuento_seleccionado=self.tree_detalle_venta.focus()
        self.valor_descuento_seleccionado=self.tree_detalle_venta.item(self.descuento_seleccionado,'values')
        if self.valor_descuento_seleccionado!='':
            
           self.buscar_precio_descuento()
        
           self.frame_descuento=Toplevel(self)#Ventana que va encima de la lista de usuarios
           self.frame_descuento.title('Aplicar Descuento')#titulo de la ventana
           self.centrar_ventana_descuento(400,350)
           self.frame_descuento.resizable(0,0)#Para que no se pueda maximixar ni minimizar
           self.frame_descuento.grab_set()#Para que no permita ninguna otra accion hasa que se cierre la ventana
           
           nombre_descuento=(self.valor_descuento_seleccionado[2])
           costo_descuento=(self.valor_descuento_seleccionado[3])
           #precio_descuento=(self.valor_descuento_seleccionado[4])
           precio_descuento=(self.precio_aplicar_descuento)

           lbl_nombre_descuento=tb.Label(self.frame_descuento,text='Producto',font=('Calibri',16),bootstyle='info')
           lbl_nombre_descuento.pack(padx=10,pady=15)
           lbl_nombre_descuento.config(text=nombre_descuento)

           lbl_costo_descuento=tb.Label(self.frame_descuento,text='Costo',font=('Calibri',16))
           lbl_costo_descuento.pack(padx=10,pady=5)
           lbl_costo_descuento.config(text=f'Costo: {costo_descuento}')

           lbl_precio_descuento=tb.Label(self.frame_descuento,text='Precio',font=('Calibri',16))
           lbl_precio_descuento.pack(padx=10,pady=5)
           lbl_precio_descuento.config(text=f'Precio: {precio_descuento}')

           lbl_nuevo_precio=tb.Label(self.frame_descuento,text='Nuevo Precio',font=('Calibri',16),bootstyle='warning')
           lbl_nuevo_precio.pack(padx=10,pady=5)
           self.txt_nuevo_precio=Entry(self.frame_descuento,justify=CENTER,font=14)
           self.txt_nuevo_precio.pack(padx=10,pady=15)
           self.txt_nuevo_precio.insert(0,self.valor_descuento_seleccionado[4])
           self.txt_nuevo_precio.focus_set()
           self.txt_nuevo_precio.bind('<Return>',self.aplicar_descuento)        
    def centrar_ventana_descuento(self,ancho,alto):
        ventana_ancho=ancho
        ventana_alto=alto
        pantalla_ancho=self.winfo_screenwidth()
        pantalla_alto=self.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.frame_descuento.geometry("{}x{}+{}+{}".format(ventana_ancho,ventana_alto,coordenadas_x,coordenadas_y))
    def aplicar_descuento(self,event):
        try:
            float(self.txt_nuevo_precio.get())

            if float(self.txt_nuevo_precio.get())<float(self.valor_descuento_seleccionado[3]):
                messagebox.showerror("Aplicando Descuento","La nuevo precio esta por debajo del costo")
                return
            if float(self.txt_nuevo_precio.get())>float(self.precio_aplicar_descuento):
                messagebox.showerror("Aplicando Descuento","No está aplicando ningun descuento, el nuevo precio es mayor al precio actual")
                return
            #Calcular descuento
            descuento_unitario=float(self.precio_aplicar_descuento)-float(self.txt_nuevo_precio.get())
        
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()

            codigo=self.valor_descuento_seleccionado[1]
            precio=self.txt_nuevo_precio.get()
            
            miCursor.execute("UPDATE DetalleVentaT SET Precio=?, Descuento=? WHERE Codigo = ?",(precio,descuento_unitario,codigo))
            
            miConexion.commit()

            subtotal=float(self.valor_descuento_seleccionado[5])*float(self.txt_nuevo_precio.get())
            existencia=int(self.valor_descuento_seleccionado[6])-int(self.valor_descuento_seleccionado[5])

            self.valor_descuento_seleccionado=self.tree_detalle_venta.item(self.descuento_seleccionado,text='',values=(self.valor_descuento_seleccionado[0],self.valor_descuento_seleccionado[1],self.valor_descuento_seleccionado[2],self.valor_descuento_seleccionado[3],self.txt_nuevo_precio.get(),self.valor_descuento_seleccionado[5],self.valor_descuento_seleccionado[6],descuento_unitario,subtotal,existencia))
            self.frame_descuento.destroy()
            self.total_detalle_venta()
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Aplicando descuento", "Ocurrio un error")
    def buscar_precio_descuento(self):
        try:
            
            miConexion=sqlite3.connect('Ventas.db')
            
            miCursor=miConexion.cursor()
            
            miCursor.execute("SELECT Precio FROM Productos WHERE Codigo="+self.valor_descuento_seleccionado[1])
            
            datos_precio_descuento=miCursor.fetchall()

            for row in datos_precio_descuento:
                self.precio_aplicar_descuento=row[0]


            miConexion.commit()
            
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Busqueda de productos", "Ocurrio un error al buscar en la lista de productos")
    def ventana_contado(self):
        

            fecha_actual=datetime.now()

            self.fecha_venta_contado=(fecha_actual.strftime('%d/%m/%Y'))
            self.hora_venta_contado=(fecha_actual.strftime('%H:%M:%S'))

            self.frame_contado=Toplevel(self)
            self.frame_contado.title('Cobrar Venta de Contado')
            self.centrar_ventana_contado(580,380)
            self.frame_contado.grab_set()

            self.lblframe_total=tb.LabelFrame(self.frame_contado)
            self.lblframe_total.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

            lbl_total_contado=tb.Label(self.lblframe_total,text='Total Venta',font=('Calibri',22),bootstyle='info')
            lbl_total_contado.pack()
            lbl_total_venta=tb.Label(self.lblframe_total,text='Total',font=('Calibri',22))
            lbl_total_venta.pack()
            lbl_total_venta.config(text=f'${self.total:,.2f}')

            self.lblframe_cambio=tb.LabelFrame(self.frame_contado)
            self.lblframe_cambio.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)

            lbl_efectivo=tb.Label(self.lblframe_cambio,text='Efectivo',font=('Calibri',22),bootstyle='warning')
            lbl_efectivo.grid(row=0,column=0,padx=10,pady=10)
            
            self.ent_efectivo=tb.Entry(self.lblframe_cambio,justify=CENTER,font=('Calibri',22))
            self.ent_efectivo.grid(row=0,column=1,padx=10,pady=10)
            self.ent_efectivo.insert(0,self.total)
            self.ent_efectivo.bind('<KeyRelease>',self.calcular_cambio)

            lbl_cambio=tb.Label(self.lblframe_cambio,text='Cambio',font=('Calibri',22),bootstyle='warning')
            lbl_cambio.grid(row=1,column=0,padx=10,pady=10)

            self.lbl_calculo_cambio=tb.Label(self.lblframe_cambio,text='$0,00',font=('Calibri',22))
            self.lbl_calculo_cambio.grid(row=1,column=1,padx=10,pady=10)

            btn_cobro_contado=tb.Button(self.lblframe_cambio,text='Cobrar',width=45,bootstyle='success',command=self.guardar_ventas)
            btn_cobro_contado.grid(row=2,column=1,padx=10,pady=10)

            self.ent_efectivo.focus()
    def calcular_cambio(self,event):
        if self.ent_efectivo.get()=='':
            self.lbl_calculo_cambio.config(text='$0.00')
            return
        try:
            float(self.ent_efectivo.get())
            cambio=0
            venta=(self.total)
            efectivo=(self.ent_efectivo.get())

            cambio=float(efectivo)-float(venta)
            self.lbl_calculo_cambio.config(text=f'${cambio:,.2f}')

        except:
            messagebox.showerror('Calcular Cambio','Algun dato no es valido')
    def centrar_ventana_contado(self,ancho,alto):
        ventana_ancho=ancho
        ventana_alto=alto
        pantalla_ancho=self.winfo_screenwidth()
        pantalla_alto=self.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.frame_contado.geometry("{}x{}+{}+{}".format(ventana_ancho,ventana_alto,coordenadas_x,coordenadas_y))
    def correlativo_ventas(self):
        try:

            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            miCursor.execute("SELECT MAX(No) FROM Ventas")
            #Con esto se traen todos los registros y se guardan en "datos"
            correlativo_ventas=miCursor.fetchone()
            for datos in correlativo_ventas:
                if datos==None:
                    self.nuevo_correlativo_ventas=(int(1))
                   
                else:
                    self.nuevo_correlativo_ventas=(int(datos)+1)
                    
            #se aplican cambios
            miConexion.commit()
            #Se cierra la conexion
            miConexion.close()

        except:
            messagebox.showerror('Correlativo Ventas','Ocurrio un error')
    def guardar_ventas(self):

        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor() 

            datos_ventas=self.nuevo_correlativo_ventas,self.fecha_venta_contado,self.hora_venta_contado,self.cod_usu,self.nom_usu,'1','CONSUMIDOR FINAL',self.total,'Emitido','Contado'
            miCursor.execute("INSERT INTO Ventas VALUES(?,?,?,?,?,?,?,?,?,?)",(datos_ventas))
            #se aplican cambios
            miConexion.commit()
            messagebox.showinfo('Guardando Venta',"Venta agregada correctamente")
            self.guardar_detalle_ventas()
            self.eliminar_detalle_ventaT()
            self.frame_contado.destroy()
            self.ventana_detalle_ventas()
            #Se cierra la conexion
            miConexion.close()

        except:
             #Mensaje si ocurre algun error
            messagebox.showerror("Guardndo Venta", "Ocurrio un error")
    def guardar_detalle_ventas(self):
        self.mostrar_productos_detalle_venta()
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()

            datos_detalle_venta=self.datos_productos_detalle_venta
            for elementos in datos_detalle_venta:  

                miCursor.execute("INSERT INTO DetalleVenta VALUES(?,?,?,?,?,?,?,?)",(elementos))
            #se aplican cambios
            miConexion.commit()
            self.actualizar_stock()
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Guardando Productos Detalle Venta", "Ocurrio un error al Agregar el Producto")
    def eliminar_detalle_ventaT(self):
            try:
                    miConexion = sqlite3.connect('Ventas.db')
                    miCursor = miConexion.cursor()
                    miCursor.execute("DELETE FROM DetalleVentaT")

                    miConexion.commit()
                    miConexion.close()
            except:
                messagebox.showerror('Eliminando Detalle VentaT','Ocurrió un error')
    def actualizar_stock(self):
        self.mostrar_productos_detalle_venta()
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()

            datos_stock=self.datos_productos_detalle_venta
            for row in datos_stock:  
                codigo=str(row[1])
                cantidad=str(row[5])

                miCursor.execute("UPDATE Productos SET Stock=Stock-? WHERE Codigo= ?",(cantidad,codigo))
            #se aplican cambios
            miConexion.commit()
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Actualizando Stock", "Ocurrio un error al Agregar el Producto")
    def ventana_listado_ventas(self):
        self.borrar_frames()

        self.frame_listado_venta=Frame(self.frame_center)
        self.frame_listado_venta.grid(row=0,column=1,sticky=NSEW)

        lblframe_busqueda_listado_venta=tb.LabelFrame(self.frame_listado_venta)
        lblframe_busqueda_listado_venta.grid(row=0,column=0,sticky=NSEW)

        lbl_fecha_listado_venta=tb.Label(lblframe_busqueda_listado_venta,bootstyle='info',text='Ventas de Fecha:',font=('Calibri',14))
        lbl_fecha_listado_venta.grid(row=0,column=1,padx=5,pady=5)
        self.ent_fecha_listado_venta=tb.DateEntry(lblframe_busqueda_listado_venta)
        self.ent_fecha_listado_venta.grid(row=0,column=1,padx=5,pady=5)
        btn_buscar_venta_fecha=tb.Button(lblframe_busqueda_listado_venta,text='Buscar',width=20,bootstyle='success',command=self.mostrar_listado_ventas)
        btn_buscar_venta_fecha.grid(row=0,column=2,padx=5,pady=10)

        lblframe_titulo_listado_venta=tb.LabelFrame(self.frame_listado_venta)
        lblframe_titulo_listado_venta.grid(row=1,column=0,sticky=NSEW)
        lbl_titulo_listado_venta=tb.Label(lblframe_titulo_listado_venta,bootstyle='dark',text='LISTA DE VENTAS DEL DIA DE JOTTA`S STORE',font=('Calibri',14))
        lbl_titulo_listado_venta.grid(row=0,column=0)

        #============================Treeview==============================
        lblframe_tree_listado_venta=tb.LabelFrame(self.frame_listado_venta)
        lblframe_tree_listado_venta.grid(row=2,column=0,sticky=NSEW)

        columnas=("no","fecha","hora","codusu","usuario","codcli","cliente","monto","estado","tipo")

        self.tree_listado_venta=tb.Treeview(lblframe_tree_listado_venta,height=30,columns=columnas,show='headings',bootstyle='dark')
        self.tree_listado_venta.grid(row=0,column=0)

        self.tree_listado_venta.heading("no",text="No",anchor=W)
        self.tree_listado_venta.heading("fecha",text="Fecha",anchor=W)
        self.tree_listado_venta.heading("hora",text="Hora",anchor=W)
        self.tree_listado_venta.heading("codusu",text="Codigo Usuario",anchor=W)
        self.tree_listado_venta.heading("usuario",text="Usuario",anchor=W)
        self.tree_listado_venta.heading("codcli",text="Codigo Cliente",anchor=W)
        self.tree_listado_venta.heading("cliente",text="Cliente",anchor=W)
        self.tree_listado_venta.heading("monto",text="Monto",anchor=W)
        self.tree_listado_venta.heading("estado",text="Estado",anchor=W)
        self.tree_listado_venta.heading("tipo",text="Tipo",anchor=W)

        self.tree_listado_venta['displaycolumns']=("no","fecha","hora","cliente","monto","tipo")

        self.tree_listado_venta.column("no",width=50)
        self.tree_listado_venta.column("fecha",width=100)
        self.tree_listado_venta.column("hora",width=100)
        self.tree_listado_venta.column("cliente",width=200)
        self.tree_listado_venta.column("monto",width=75)
        self.tree_listado_venta.column("tipo",width=75)

        tree_croll=tb.Scrollbar(self.frame_listado_venta,bootstyle='succes-round')
        tree_croll.grid(row=2,column=2,pady=10)

        tree_croll.config(command=self.tree_listado_venta.yview)

        #total de ventas del dia
        self.lbl_total_listado_venta=tb.Label(self.frame_listado_venta,font=('Calibri',24),justify=RIGHT)
        self.lbl_total_listado_venta.grid(row=3,column=0,sticky=E)

        #=======================LISTADO DETALLE DE VENTAS============================

        lblframe_datos_detalle_venta=tb.LabelFrame(self.frame_listado_venta)
        lblframe_datos_detalle_venta.grid(row=0,column=3,sticky=NSEW)

        lbl_numero=tb.Label(lblframe_datos_detalle_venta,text='Venta:',bootstyle='info',font=('Calibri',14))
        lbl_numero.grid(row=0,column=0,padx=5,pady=5)
        self.lbl_no_venta=Label(lblframe_datos_detalle_venta,text='')
        self.lbl_no_venta.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        lbl_cliente=tb.Label(lblframe_datos_detalle_venta,text='Cliente:',bootstyle='info',font=('Calibri',14))
        lbl_cliente.grid(row=1,column=0,padx=5,pady=5)
        self.lbl_cliente_venta=Label(lblframe_datos_detalle_venta,text='')
        self.lbl_cliente_venta.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        lblframe_botones_listado_detalle_venta=tb.LabelFrame(self.frame_listado_venta)
        lblframe_botones_listado_detalle_venta.grid(row=1,column=1,sticky=NSEW)

        self.btn_devolucion_contado=tb.Button(lblframe_botones_listado_detalle_venta,text='Devolucion',width=30,bootstyle='danger')
        self.btn_devolucion_contado.grid(row=0,column=0,padx=5,pady=2)
        self.btn_imprimir_venta=tb.Button(lblframe_botones_listado_detalle_venta,text='Imprimir Venta',width=30,bootstyle='info')
        self.btn_imprimir_venta.grid(row=0,column=1,padx=5,pady=2)

        lblframe_tree_listado_detalle_venta=tb.LabelFrame(self.frame_listado_venta)
        lblframe_tree_listado_detalle_venta.grid(row=2,column=1,sticky=NSEW)

        columnas=("no","codigo","nombre","costo","precio","cantidad","stock","descuento","subtotal")

        self.tree_listado_detalle_venta=tb.Treeview(lblframe_tree_listado_detalle_venta,height=30,columns=columnas,show='headings',bootstyle='dark')
        self.tree_listado_detalle_venta.grid(row=0,column=0)

        self.tree_listado_detalle_venta.heading('no',text='No',anchor=W)
        self.tree_listado_detalle_venta.heading('codigo',text='Codigo',anchor=W)
        self.tree_listado_detalle_venta.heading('nombre',text='Nombre',anchor=W)
        self.tree_listado_detalle_venta.heading('costo',text='Costo',anchor=W)
        self.tree_listado_detalle_venta.heading('precio',text='Precio',anchor=W)
        self.tree_listado_detalle_venta.heading('cantidad',text='Cantidad',anchor=W)
        self.tree_listado_detalle_venta.heading('stock',text='Stocl',anchor=W)
        self.tree_listado_detalle_venta.heading('descuento',text='Descuento',anchor=W)
        self.tree_listado_detalle_venta.heading('subtotal',text='Subtotal',anchor=W)

        self.tree_listado_detalle_venta['displaycolumns']=('codigo','nombre','precio','cantidad','subtotal')

        self.tree_listado_detalle_venta.column('codidgo',width=75)
        self.tree_listado_detalle_venta.column('nombre',width=200)
        self.tree_listado_detalle_venta.column('precio',width=75)
        self.tree_listado_detalle_venta.column('cantidad',width=75)
        self.tree_listado_detalle_venta.column('subtotal',width=75)

        tree_croll_detalle=tb.Scrollbar(self.frame_listado_venta,bootstyle='succes-round')
        tree_croll_detalle.grid(row=2,column=4,pady=10)

        tree_croll_detalle.config(command=self.tree_listado_detalle_venta.yview)

        self.lbl_total_listado_detalle_venta=tb.Label(self.frame_listado_venta,font=('Calibri',24))
        self.lbl_total_listado_detalle_venta.grid(row=3,column=3,sticky=E)
        self.mostrar_listado_ventas()
    def mostrar_listado_ventas(self):
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            #Se limpia el treeview
            registros=self.tree_listado_venta.get_children()
            #Se recorre cada regristro
            for elementos in registros:
                self.tree_listado_venta.delete(elementos)

            patron=self.ent_fecha_listado_venta.entry.get()
            #Se consulta la base de datos
            miCursor.execute("SELECT * FROM Ventas WHERE Fecha LIKE ?",('%'+patron+'%',) )
            #Con esto se traen todos los registros y se guardan en "datos"
            datos_listado_ventas=miCursor.fetchall()
            print(datos_listado_ventas)
            #Se recorre cada fila encontrada
            for row in datos_listado_ventas:
                #Se llena el treeview
                self.tree_listado_venta.insert('',0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
            #se aplicand cambios
            miConexion.commit()
            #Se cierra la conexion
            miConexion.close()

        except Exception as e:
            print("Error:", e)
            #Mensaje si ocurre algun error
            messagebox.showerror("Busqueda de productos", "Ocurrio un error al buscar en la lista de productos")




#==========================ELIMINAR FRAMES================================
    def borrar_frames(self):
        for frames in self.frame_center.winfo_children():
            frames.destroy()
        self.frame_busqueda_detalle_venta.grid_forget()    

def main():
    app=Ventana()
    app.title('Sistema de Ventas')
    app.state('zoomed')
    tb.Style('morph')
    app.mainloop()

if __name__=='__main__':
    main()