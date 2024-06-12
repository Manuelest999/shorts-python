from tkinter import*
from tkinter import ttk,messagebox
import ttkbootstrap as tb
import sqlite3

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
        self.frame_left.grid(row=0,column=0,sticky=NS)
        self.frame_center=Frame(self)
        self.frame_center.grid(row=0,column=1,sticky=NSEW)
        self.frame_rigth=Frame(self,width=400)
        self.frame_rigth.grid(row=0,column=2,sticky=NSEW)

        btn_productos=ttk.Button(self.frame_left,text='Productos',bootstyle='info',width=15,command=self.ventana_lista_productos)
        btn_productos.grid(row=0,column=0,padx=10,pady=10)
        btn_ventas=ttk.Button(self.frame_left,text='Ventas',bootstyle='info',width=15)
        btn_ventas.grid(row=1,column=0,padx=10,pady=10)
        btn_clientes=ttk.Button(self.frame_left,text='Clientes',bootstyle='info',width=15)
        btn_clientes.grid(row=2,column=0,padx=10,pady=10)
        #btn_compras=ttk.Button(self.frame_left,text='Compras',bootstyle='info',width=15)
        #btn_compras.grid(row=3,column=0,padx=10,pady=10)
        btn_usuarios=ttk.Button(self.frame_left,text='Usuarios',bootstyle='info',width=15,command=self.ventana_lista_usuarios)
        btn_usuarios.grid(row=4,column=0,padx=10,pady=10)
        #btn_reportes=ttk.Button(self.frame_left,text='Reportes',bootstyle='info',width=15)
        #btn_reportes.grid(row=5,column=0,padx=10,pady=10)
        #btn_backup=ttk.Button(self.frame_left,text='Backup',bootstyle='info',width=15)
        #btn_backup.grid(row=6,column=0,padx=10,pady=10)
        #btn_restaurabd=ttk.Button(self.frame_left,text='Restaurar BD',bootstyle='info',width=15)
        #btn_restaurabd.grid(row=7,column=0,padx=10,pady=10)

        
        lbl2=Label(self.frame_center)
        lbl2.grid(row=0,column=0,padx=10,pady=10)

        lbl3=Label(self.frame_rigth)
        lbl3.grid(row=0,column=0,padx=10,pady=10)
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
                    cod_usu=row[0]
                    nom_usu=row[1]
                    cla_usu=row[2]
                    rol_usu=row[3]
                if(nom_usu==self.txt_usuario.get() and cla_usu==self.txt_clave.get()):
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
        pantalla_ancho=self.frame_rigth.winfo_screenwidth()
        pantalla_alto=self.frame_rigth.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.frame_nuevo_usuario.geometry("{}x{}+{}+{}".format(ventana_ancho,ventana_alto,coordenadas_x,coordenadas_y))
    def centrar_ventana_modificar_usuario(self,ancho,alto):
        ventana_ancho=ancho
        ventana_alto=alto
        pantalla_ancho=self.frame_rigth.winfo_screenwidth()
        pantalla_alto=self.frame_rigth.winfo_screenheight()
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
        self.frame_lista_productos=Frame(self.frame_center)
        self.frame_lista_productos.grid(row=0,column=0,columnspan=2,sticky=NSEW)

        self.lblframe_botones_listprod=LabelFrame(self.frame_lista_productos)
        self.lblframe_botones_listprod.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        btn_nuevo_producto=tb.Button(self.lblframe_botones_listprod,text='Nuevo',width=21
                                    ,bootstyle="success",command=self.ventana_nuevo_producto)
        btn_nuevo_producto.grid(row=0,column=0,padx=5,pady=5)
        btn_modificar_producto=tb.Button(self.lblframe_botones_listprod,text='Modificar',width=21,bootstyle="warning")
        btn_modificar_producto.grid(row=0,column=1,padx=5,pady=5)
        btn_eliminar_producto=tb.Button(self.lblframe_botones_listprod,text='Eliminar',width=21,bootstyle="danger",command=self.eliminar_producto)
        btn_eliminar_producto.grid(row=0,column=2,padx=5,pady=5)   

        self.lblframe_busqueda_listprod=LabelFrame(self.frame_lista_productos)
        self.lblframe_busqueda_listprod.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW) 

        self.txt_busqueda_producto=ttk.Entry(self.lblframe_busqueda_listprod,width=172)
        self.txt_busqueda_producto.grid(row=0,column=0,padx=5,pady=5)  
        self.txt_busqueda_producto.bind('<Key>',self.buscar_producto)                       

        #========================Treeview=====================================
        
        self.lblframe_tree_listprod=LabelFrame(self.frame_lista_productos)
        self.lblframe_tree_listprod.grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)

        columnas=("codigo","nombre","cantidad","talla","proveedor","preciodecosto","fechaderecepcion","preciodeventa")

        self.tree_lista_productos=tb.Treeview(self.lblframe_tree_listprod,columns=columnas,
                                         height=17,show='headings',bootstyle="dark")
        self.tree_lista_productos.grid(row=0,column=0)
        
        self.tree_lista_productos.heading("codigo",text="Codigo",anchor=W)
        self.tree_lista_productos.heading("nombre",text="Nombre",anchor=W)
        self.tree_lista_productos.heading("cantidad",text="Clave",anchor=W)
        self.tree_lista_productos.heading("talla",text="Talla",anchor=W) 
        self.tree_lista_productos.heading("proveedor",text="Proovedor",anchor=W)
        self.tree_lista_productos.heading("preciodecosto",text="Precio de costo",anchor=W)
        self.tree_lista_productos.heading("fechaderecepcion",text="Fecha de recepcion",anchor=W)
        self.tree_lista_productos.heading("preciodeventa",text="Precio de venta",anchor=W)

        self.tree_lista_productos['displaycolumns']=("codigo","nombre","talla","proveedor","preciodecosto","fechaderecepcion","preciodeventa")#esto es para ocultar la clave

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

        lbl_cantidad_nuevo_producto=Label(lblframe_nuevo_producto,text='Cantidad')
        lbl_cantidad_nuevo_producto.grid(row=2,column=0,padx=10,pady=10)
        self.txt_cantidad_nuevo_producto=Entry(lblframe_nuevo_producto,width=40)
        self.txt_cantidad_nuevo_producto.grid(row=2,column=1,padx=10,pady=10)

        lbl_talla_nuevo_producto=Label(lblframe_nuevo_producto,text='Talla')
        lbl_talla_nuevo_producto.grid(row=7,column=0,padx=10,pady=10)
        self.txt_talla_nuevo_producto=ttk.Combobox(lblframe_nuevo_producto,values=('2','4','6','8','10','12','14','16','18','S','M','L','XL','XXL'),width=38,state='readonly')
        self.txt_talla_nuevo_producto.grid(row=7,column=1,padx=10,pady=10)
        self.txt_talla_nuevo_producto.current(0)

        lbl_proveedor_nuevo_producto=Label(lblframe_nuevo_producto,text='Proveedor')
        lbl_proveedor_nuevo_producto.grid(row=3,column=0,padx=10,pady=10)
        self.txt_proveedor_nuevo_producto=Entry(lblframe_nuevo_producto,width=40)
        self.txt_proveedor_nuevo_producto.grid(row=3,column=1,padx=10,pady=10)

        lbl_preciodecosto_nuevo_producto=Label(lblframe_nuevo_producto,text='Precio de Costo')
        lbl_preciodecosto_nuevo_producto.grid(row=4,column=0,padx=10,pady=10)
        self.txt_preciodecosto_nuevo_producto=Entry(lblframe_nuevo_producto,width=40)
        self.txt_preciodecosto_nuevo_producto.grid(row=4,column=1,padx=10,pady=10)

        lbl_fechaderecepcion_nuevo_producto=Label(lblframe_nuevo_producto,text='Fecha de Recepcion')
        lbl_fechaderecepcion_nuevo_producto.grid(row=5,column=0,padx=10,pady=10)
        self.txt_fechaderecepcion_nuevo_producto=Entry(lblframe_nuevo_producto,width=40)
        self.txt_fechaderecepcion_nuevo_producto.grid(row=5,column=1,padx=10,pady=10)

        lbl_preciodeventa_nuevo_producto=Label(lblframe_nuevo_producto,text='Precio de Venta')
        lbl_preciodeventa_nuevo_producto.grid(row=6,column=0,padx=10,pady=10)
        self.txt_preciodeventa_nuevo_producto=Entry(lblframe_nuevo_producto,width=40)
        self.txt_preciodeventa_nuevo_producto.grid(row=6,column=1,padx=10,pady=10)


        btn_guardar_nuevo_producto=ttk.Button(lblframe_nuevo_producto,text='Guardar',width=38,bootstyle='success',command=self.guardar_producto)
        btn_guardar_nuevo_producto.grid(row=8,column=1,padx=10,pady=10)
    def centrar_ventana_nuevo_producto(self,ancho,alto):
        ventana_ancho=ancho
        ventana_alto=alto
        pantalla_ancho=self.frame_rigth.winfo_screenwidth()
        pantalla_alto=self.frame_rigth.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.frame_nuevo_producto.geometry("{}x{}+{}+{}".format(ventana_ancho,ventana_alto,coordenadas_x,coordenadas_y))
    def guardar_producto(self):
        #Valida que no queden vacios los campos
        if self.txt_codigo_nuevo_producto.get()=="" or self.txt_nombre_nuevo_producto.get()=="" or self.txt_cantidad_nuevo_producto.get()=="" or self.txt_proveedor_nuevo_producto.get()=="" or self.txt_preciodecosto_nuevo_producto.get()=="" or self.txt_fechaderecepcion_nuevo_producto.get()=="" or self.txt_preciodeventa_nuevo_producto.get()=="":
            messagebox.showwarning("Guardando Producto","Algun campo no es valido, por favor revise")
            return
        #Capturador de errores
        try:
            #Se establece la conexion
            miConexion=sqlite3.connect('Ventas.db')
            #Se crea el cursor
            miCursor=miConexion.cursor()
            
            datos_guardar_producto=self.txt_codigo_nuevo_producto.get(),self.txt_nombre_nuevo_producto.get(),self.txt_cantidad_nuevo_producto.get(),self.txt_talla_nuevo_producto.get(),self.txt_proveedor_nuevo_producto.get(),self.txt_preciodecosto_nuevo_producto.get(),self.txt_fechaderecepcion_nuevo_producto.get(),self.txt_preciodeventa_nuevo_producto.get()
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
            datos=miCursor.fetchall()
            #Se recorre cada fila encontrada
            for row in datos:
                #Se llena el treeview
                self.tree_lista_productos.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],))
            #se aplicand cambios
            miConexion.commit()
            #Se cierra la conexion
            miConexion.close()

        except:
            #Mensaje si ocurre algun error
            messagebox.showerror("Busqueda de productos", "Ocurrio un error al buscar en la lista de productos")




def main():
    app=Ventana()
    app.title('Sistema de Ventas')
    app.state('zoomed')
    tb.Style('morph')
    app.mainloop()

if __name__=='__main__':
    main()