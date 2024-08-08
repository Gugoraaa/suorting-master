import customtkinter
from db import Db
from tkinter import messagebox

class GUI():

    def __init__(self, map,list):
        self.x = False
        self.combo_box1 = None
        self.DB=Db()


        self.h_map= map
        self.lista=list


        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.root = customtkinter.CTk()
        self.root.title("Ordenador")
        self.root.geometry("500x300")

        label_bienvenido = customtkinter.CTkLabel(self.root, text="Bienvenido")
        label_bienvenido.pack()

        boton1 = customtkinter.CTkButton(self.root, text="Consultar", command=lambda: self.consultar(map,list))
        boton1.pack(side='top', pady=5)

        boton2 = customtkinter.CTkButton(self.root, text="Agregar",command=lambda: self.agregar(map,list))
        boton2.pack(side='top', pady=5)

        boton3 = customtkinter.CTkButton(self.root, text="Nuevo Mueble", command=lambda: self.nuevo())
        boton3.pack(side='top', pady=5)

        boton4 = customtkinter.CTkButton(self.root, text="Buscar objeto",command=lambda: self.buscar_objeto())
        boton4.pack(side='top', pady=5)

    def loop(self):
        self.root.mainloop()

    def back_btn (self):
        for widget in self.root.winfo_children():
            widget.pack_forget()



        self.root.geometry("500x300")

        label_bienvenido = customtkinter.CTkLabel(self.root, text="Bienvenido")
        label_bienvenido.pack()

        boton1 = customtkinter.CTkButton(self.root, text="Consultar", command=lambda: self.consultar(self.h_map,self.lista))
        boton1.pack(side='top', pady=5)

        boton2 = customtkinter.CTkButton(self.root, text="Agregar",command=lambda: self.agregar(map=self.h_map,table_list=self.lista))
        boton2.pack(side='top', pady=5)

        boton3 = customtkinter.CTkButton(self.root, text="Nuevo Mueble", command=lambda: self.nuevo())
        boton3.pack(side='top', pady=5)

        boton4 = customtkinter.CTkButton(self.root, text="Buscar objeto",command=lambda: self.buscar_objeto())
        boton4.pack(side='top', pady=5)

    

    def consultar(self, map, table_list):
        tabla = ''


    
            
        def entrar_mueble(mueble):

            def resultados(cajon):
                messagebox.showinfo('Informacion',self.DB.Consultar_cajon(tabla=mueble, cajon=cajon))



            for widget in self.root.winfo_children():
                widget.pack_forget()
            columnas = self.h_map[mueble]
            nombres_columnas = list(columnas.keys())
            

            
            label_consultar = customtkinter.CTkLabel(self.root, text="Selecciona cajon")
            label_consultar.pack()

            self.combo_box_cajones = customtkinter.CTkComboBox(self.root, values=nombres_columnas)  
            self.combo_box_cajones.pack()


            boton4 = customtkinter.CTkButton(self.root, text="Buscar", command=lambda: resultados(cajon= self.combo_box_cajones.get()))
            boton4.pack(side='top', pady=5) 


            back_btn = customtkinter.CTkButton(self.root, text="Atras", command=lambda: self.back_btn())
            back_btn.pack(side='right', anchor='se', pady=5)

            

        for widget in self.root.winfo_children():
            widget.pack_forget()

        label_consultar = customtkinter.CTkLabel(self.root, text="Consultar")
        label_consultar.pack()

        self.combo_box1 = customtkinter.CTkComboBox(self.root, values=table_list, variable=tabla)  
        self.combo_box1.pack()

        boton4 = customtkinter.CTkButton(self.root, text="Entrar", command=lambda: entrar_mueble(mueble=self.combo_box1.get()))
        boton4.pack(side='top', pady=5)  


        back_btn = customtkinter.CTkButton(self.root, text="Atras", command=lambda: self.back_btn())
        back_btn.pack(side='right', anchor='se', pady=5)


    def agregar (self,map, table_list):

        def dentro_cajon(selected_table,map):


            def tomar ():
                self.tabla = selected_table
                self.mueble = self.combo_box_cajones.get()
                self.objeto= self.entry_objeto.get()

                self.DB.Agregar_obj(tabla=self.tabla,cajon=self.mueble,objetos=self.objeto)
                mensaje= messagebox.showinfo('Informacion','Se insertaron con éxito tus objetos')


        
            for widget in self.root.winfo_children():
                widget.pack_forget()

            columnas = map[selected_table]
            nombres_columnas = list(columnas.keys())
            

            
            label_consultar = customtkinter.CTkLabel(self.root, text="Selecciona cajon")
            label_consultar.pack()

            self.combo_box_cajones = customtkinter.CTkComboBox(self.root, values=nombres_columnas)  
            self.combo_box_cajones.pack()


            label_agregar= customtkinter.CTkLabel(self.root, text="Escribe el nombre de tu objeto ")
            label_agregar.pack()


            self.entry_objeto = customtkinter.CTkEntry (self.root, placeholder_text="")
            self.entry_objeto.pack(pady=20, padx=20)


            boton4 = customtkinter.CTkButton(self.root, text="agregar",command=lambda: tomar())
            boton4.pack(side='top', pady=5)  


            back_btn = customtkinter.CTkButton(self.root, text="Atras", command=lambda: self.back_btn())
            back_btn.pack(side='right', anchor='se', pady=5)

        
        for widget in self.root.winfo_children():
            widget.pack_forget()

        tabla = ''

        label_consultar = customtkinter.CTkLabel(self.root, text="Agregar")
        label_consultar.pack()  

        self.combo_box1 = customtkinter.CTkComboBox(self.root, values=table_list, variable=tabla)  
        self.combo_box1.pack()

        boton4 = customtkinter.CTkButton(self.root, text="Entrar",command=lambda: dentro_cajon(selected_table=self.combo_box1.get(), map=self.h_map))
        boton4.pack(side='top', pady=5)  


        back_btn = customtkinter.CTkButton(self.root, text="Atras", command=lambda: self.back_btn())
        back_btn.pack(side='right', anchor='se', pady=5)

                                

    def buscar_objeto (self):
        def buscar():
            obj= entry_1.get()
            mensaje= messagebox.showinfo('Informacion',self.DB.buscar_objeto(nombre_objeto=obj))

        for widget in self.root.winfo_children():
            widget.pack_forget()

        label_agregar= customtkinter.CTkLabel(self.root, text="Escribe el nombre de tu objeto ")
        label_agregar.pack()

        entry_text_1 = customtkinter.StringVar()

        entry_1 = customtkinter.CTkEntry (self.root,textvariable=entry_text_1, placeholder_text="")
        entry_1.pack(pady=20, padx=20)

        boton4 = customtkinter.CTkButton(self.root, text="Buscarlo", command=lambda: buscar())
        boton4.pack(side='top', pady=5) 

        back_btn = customtkinter.CTkButton(self.root, text="Atras", command=lambda: self.back_btn())
        back_btn.pack(side='right', anchor='se', pady=5)




    def nuevo (self):

        def crearlo():
            nombre=entry_1.get()
            cajones=entry_3.get()

            nombre_cajones= cajones.split(',')

            print(f'nombre {nombre}')
            print(f'nombre {cajones}')


            
            messagebox.showinfo('Información',self.DB.Nuevo_mueble(nombre_tabla=nombre,nombre_cajones=nombre_cajones))
            


        for widget in self.root.winfo_children():
            widget.pack_forget()

        label_agregar= customtkinter.CTkLabel(self.root, text="Escribe el nombre de tu mueble")
        label_agregar.pack()

        entry_text_1 = customtkinter.StringVar()

        entry_1 = customtkinter.CTkEntry (self.root,textvariable=entry_text_1, placeholder_text="")
        entry_1.pack(pady=20, padx=20)


        label_agregar= customtkinter.CTkLabel(self.root, text="Escribe el nombre de tus cajones")
        label_agregar.pack()

        entry_text_3 = customtkinter.StringVar()

        entry_3 = customtkinter.CTkEntry (self.root,textvariable=entry_text_3, placeholder_text="")
        entry_3.pack(pady=20, padx=20)

        

        boton4 = customtkinter.CTkButton(self.root, text="Crear", command=lambda: crearlo())
        boton4.pack(side='top', pady=5)  

        back_btn = customtkinter.CTkButton(self.root, text="Atras", command=lambda: self.back_btn())
        back_btn.pack(side='right', anchor='se', pady=5)
