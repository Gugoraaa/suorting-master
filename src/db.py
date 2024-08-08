
import psycopg2



class Db:

    def __init__(self) -> None:

        global tablas

        try:
            self.connection = psycopg2.connect(
            dbname="Acomodo",
            user="postgres",
            password="123",
            host="localhost",
        )
        except:
            print('Hubo un error al conectar con la base de datos')



    def lista(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
        """)


        # Obtener los nombres de las tablas
        self.tablas = [registro[0] for registro in self.cursor.fetchall()]

        return self.tablas


    def hash_map(self):
        datos_tablas = {}

        for tabla in self.tablas:
            self.cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tabla}'")
            columnas = [columna[0] for columna in self.cursor.fetchall() if columna[0] != 'id']
            
            self.cursor.execute(f"SELECT * FROM {tabla}")
            datos = self.cursor.fetchall() 

            datos_columnas = {}

            for i, columna in enumerate(columnas):
                valores_columna = [fila[i] for fila in datos if fila[i] is not None]
                datos_columnas[columna] = valores_columna

            datos_tablas[tabla] = datos_columnas
        

        print(datos_tablas)
        return datos_tablas


            
    def Nuevo_mueble(self,nombre_tabla,nombre_cajones):
        self.cursor = self.connection.cursor()
        try :
            query = f'CREATE TABLE IF NOT EXISTS {nombre_tabla} ( {", ".join([f'"{nombre}" VARCHAR(100)' for nombre in nombre_cajones])})'
            
            self.cursor.execute(query)
            self.connection.commit()
            return 'Se creo con exito tu mueble'
        except:
            return 'Hubo un error al crear tu mueble'



    def Agregar_obj(self, tabla, cajon, objetos):
        self.cursor = self.connection.cursor()
        try: 
            
            query = f'INSERT INTO {tabla} ({cajon}) VALUES (%s)'
            self.cursor.execute(query, (objetos,))
            self.connection.commit()
            print('Se insertaron con éxito tus objetos')
        except :
            print('Hubo un error al encontrar tu mueble o cajón:')




    def Consultar_cajon(self,tabla,cajon):
        self.cursor = self.connection.cursor()
        try:
            query= f'SELECT {cajon} FROM {tabla} WHERE {cajon} IS NOT NULL'
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()
            self.connection.commit()
            return resultados
        except:
            print('Hubo un error al consultar tu mueble')




    def buscar_objeto(self, nombre_objeto):
        try:
            # Crear un cursor
            self.cursor = self.connection.cursor()

            # Variable para verificar si se encontró el objeto
            objeto_encontrado = False

            # Obtener todas las tablas de la base de datos
            self.cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
            """)
            tablas = self.cursor.fetchall()

            # Iterar sobre todas las tablas
            for tabla in tablas:
                tabla_nombre = tabla[0]

                # Obtener todas las columnas de la tabla actual
                self.cursor.execute(f"""
                    SELECT column_name
                    FROM information_schema.columns
                    WHERE table_name = '{tabla_nombre}'
                """)
                columnas = self.cursor.fetchall()

                # Iterar sobre todas las columnas de la tabla actual
                for columna in columnas:
                    columna_nombre = columna[0]

                    # Buscar el objeto en la columna actual
                    self.cursor.execute(f"""
                        SELECT {columna_nombre}
                        FROM {tabla_nombre}
                        WHERE CAST({columna_nombre} AS TEXT) = %s
                    """, (nombre_objeto,))
                    resultados = self.cursor.fetchall()

                    # Si se encuentran resultados, imprimir dónde está el objeto
                    if resultados:
                        objeto_encontrado = True
                        return f"El objeto {nombre_objeto} se encuentra en el mueble {tabla_nombre}, en el cajon {columna_nombre}."

            # Si el objeto no se encuentra en ninguna parte, mostrar un mensaje
            if not objeto_encontrado:
                return f"No se encontró el objeto {nombre_objeto} en ninguna tabla de la base de datos."

            # Cerrar el cursor
            self.cursor.close()
        except Exception as e:
            return f"Error: {e}"
            

