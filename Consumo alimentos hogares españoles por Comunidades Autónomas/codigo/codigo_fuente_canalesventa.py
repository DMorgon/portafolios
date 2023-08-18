"""
1) Importo las librerías que se van a utilizar
2) Cargaré los documentos .xlsx en marcos de datos de Pandas.
3) Realizaré un EDA de cada marco de datos para detectar las transformaciones a realizar
4) Realizaré las trasformaciones que son necesarios.
5) Cargaré el marco de datos resultante en un archivo .csv en la carpeta datos_preprocesados que se encuentra en el
espacio dedicado a este proyecto en el repositorio de GitHub
"""

# Importo las librerías que voy a utilizar en este proyecto

import pandas as pd
import requests as rq
import os


"""
2) CARGA DE ARCHIVO

En este apartado procederé a cargar los archivos excel, alojados en el repositorio de GitHub en marcos de datos de 
Pandas. Para ello sigo el siguiente plan de trabajo:

1) Creo la lista con el nombre de los documentos .xlsx.
2) Creo las funciones para cargar cada documento en un marco de datos de Pandas.
3) Realizo la llamada de cada una de las funciones para cargar los datos.
4) Uno los marcos de datos según corresponda a los años. 

Antes que nada, hay que tener en cuenta que las hojas de los archivos 2020, 2021 y 2022 etan colocadas de forma
diferente a las demás. Con lo que habría que tenerlo en cuenta a la hora de crear las funciones.
"""

# Creo las listas con el nombre de los documentos

lista_archivos = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011",
                  "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]


# Creo las funciones que me permitirá cargar los datos de los archivos alojados en el repositorio de GitHub


def carga_valor(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/Consumo alimentos hogares españoles por Comunidades Autónomas/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{nombre_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    df_valor = pd.read_excel(response.content, sheet_name=7, header=2, engine="openpyxl")
    df_valor["ANALISIS"] = "Valor (miles de euros)"
    return df_valor


def carga_volumen(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/Consumo alimentos hogares españoles por Comunidades Autónomas/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{nombre_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    df_volumen = pd.read_excel(response.content, sheet_name=8, header=2, engine="openpyxl")
    df_volumen["ANALISIS"] = "Volumen (miles de kg o litros)"
    return df_volumen

# Cargo los datos correspondientes con las hojas valor de cada archivo


lista_df_valor = []

for archivo in lista_archivos:
    df = carga_valor(archivo)
    lista_df_valor.append(df)

# Cargo los datos correspondientes con las hojas volumen de cada archivo


lista_df_volumen = []

for archivo in lista_archivos:
    df = carga_volumen(archivo)
    lista_df_volumen.append(df)

# Uno los marcos de datos según el año y los incluyo en la lista_df

lista_df = []

for i in range(0, 23, 1):
    df = pd.concat([lista_df_valor[i], lista_df_volumen[i]], ignore_index=True)
    lista_df.append(df)

"""
3. ANÁLISIS EXPLORATORIO DE DATOS

A continuación realizó un Análisis Exploratorio de Datos (EDA) en cada marco de datos de la lista_df, para obtener
información y anomalías de las mismas.

"""

# Realizo EDA en cada marco de datos

for i, df in enumerate(lista_df):
    tabla_nombre = f"df_{2000 + i}"
    print("Nombre de la tabla de datos:", tabla_nombre)
    print(df.info())
    if df.isna().any().any():
        print("Hay valores NA en la tabla de datos" + "\n")
    else:
        print("No hay valores NA en la tabla de datos" + "\n")

"""
Revisando la información de cada marco de datos, encontramos las siguientes anomalías:

1) Los marcos de datos df_2000, df_2001, df_2002, df_2003, df_2004, df_2005, df_2006, df_2007 tienen 23 variables.

2) Los marcos de datos df_2008, df_2009, df_2010, df_2011, df_2012 tienen 24 variables.
"""

"""
4. TRANSFORMACIÓN DE LOS DATOS

Conforme a los resultados obtenidos del EDA, procedo a continuación a realizar las siguientes transformaciones en los
datos:

1) Elimino las variables correspondientes a los territorios que no voy a utilizar.

2) Corrijo el nombre de las variables correspondientes a las comunidades autónomas.

3) Añado la columna AÑO con los valores correspondiente al año del marco de datos.

4) Uno todas las tablas en una sola df_total

5) Modifico el nombre de la variable Unnamed: 0 a CATEGORIAS

5) Realizó un filtro en df_total para sólo quedarme con las categorías de alimentos que voy a utilizar.

6) Corrijo el nombre de la categoría de los alimentos.

7) Transformo el formato de ancho a largo, manteniendo las columnas "AÑO", "CATEGORIA" y "ANALISIS" como
 identificadores
"""

# Añado la columna AÑO con los valores correspondiente al año del marco de datos

for i, df in enumerate(lista_df):
    df["AÑO"] = int(lista_archivos[i])

# Corrijo el nombre de las variables correspondientes a las comunidades autónomas.

for df in lista_df:
    df.columns = df.columns.str.replace("SUPER/AUTOS/G.AL", "SUPER/AUTOS/G.ALM.", regex=False)
    df.columns = df.columns.str.replace("SUPER/AUTOS/G.ALM.M.", "SUPER/AUTOS/G.ALM.", regex=False)
    df.columns = df.columns.str.replace("HEBORISTERIA", "HERBORISTERIA", regex=False)
    df.columns = df.columns.str.replace("CARNICERIA/CHARC", "CARNICERIA/CHARC.", regex=False)
    df.columns = df.columns.str.replace("CARNICERIA/CHARC..", "CARNICERIA/CHARC.", regex=False)
    df.columns = df.columns.str.replace("MERCADOS/AMBULAN", "MERCADOS/AMBULANT.", regex=False)
    df.columns = df.columns.str.replace("MERCADOS/AMBULANT.T.", "MERCADOS/AMBULANT.", regex=False)
    df.columns = df.columns.str.replace("MERCADOS Y PLAZA", "MERCADOS Y PLAZAS", regex=False)
    df.columns = df.columns.str.replace("MERCADOS Y PLAZASS", "MERCADOS Y PLAZAS", regex=False)
    df.loc[:, sorted(df.columns)] = df.loc[:, df.columns]


# Creo la variable Tda.tradicional y les añado los valores de la suma de las variables correspondiente.

columnas_sumar = ["TDA.TRADICIONAL", "PESCADERIA", "TDA.CONGELADOS", "HERBORISTERIA", "FARMACIA",
                  "CARNICERIA/CHARC.", "MERCADOS Y PLAZAS", "LECHERIA", "PANADERIA", "BAR-BODEGA"]

for df in lista_df:
    df["Tda.tradicional"] = df[columnas_sumar].sum(axis=1)

# Creo la variable Distr Orga/Plataforma y les añado los valores de la suma de las variables correspondiente.

columnas_sumar = ["HIPERMERCADOS", "SUPER/AUTOS/G.ALM.", "SUPER+AUTOS", "DISCOUNTS"]

for df in lista_df:
    df["Distr Orga/Plataforma"] = df[columnas_sumar].sum(axis=1)

# Uno todas las tablas en una sola df_total

df_total = pd.concat(objs=lista_df, axis=0)

# Elimino las variables que no voy a utilizar

columnas_eliminar = [".TOTAL ESPAÑA", "T.ESPAÑA", "HIPERMERCADOS", "SUPER/AUTOS/G.ALM.", "SUPER+AUTOS", "DISCOUNTS",
                     "TDA.TRADICIONAL", "PESCADERIA", "TDA.CONGELADOS", "HERBORISTERIA", "FARMACIA",
                     "CARNICERIA/CHARC.", "MERCADOS Y PLAZAS", "LECHERIA", "PANADERIA", "BAR-BODEGA", "MERCADOS/AMBULANT."]

df_total.drop(columns=columnas_eliminar, errors="ignore", inplace=True)

# Modifico el nombre de la variable Unamed: 0 a CATEGORIAS.

df_total.rename(columns={"Unnamed: 0": "CATEGORIAS"}, inplace=True)

# Realizó un filtro en df_total para sólo quedarme con las categorías de alimentos que voy a utilizar

lista_categoria = ["T.HUEVOS KGS", "MIEL", "TOTAL CARNE", "TOTAL PESCA", "TOTAL LECHE LIQUIDA", "TOTAL OTRAS LECHES",
                   "DERIVADOS LACTEOS", "PAN", "BOLL.PAST.GALLET.CERE", "PRODUCTOS NAVIDEÑOS",
                   "CHOCOLATES/CACAOS/SUC", "ARROZ", "TOTAL PASTAS", "AZUCAR", "EDULCORANTES", "LEGUMBRES",
                   "TOTAL ACEITE", "MARGARINA", "ACEITUNAS", "BEBIDAS DERIVADAS VI", "TOTAL VINOS", "CERVEZAS",
                   "SIDRAS", "T.BEBIDAS ESPIRITUOSA", "VINAGRE", "TOTAL ZOMO Y NECTAR", "TOTAL PATATAS",
                   "T.HORTALIZAS FRESCAS", "T.FRUTAS FRESCAS", "FRUTOS SECOS", "T.FRUTA&HORTA.TRANSF",
                   "PLATOS PREPARADOS", "CAFES E INFUSIONES", "CALDOS", "SALSAS", "AGUA DE BEBIDA ENVAS.",
                   "GASEOSAS Y BEBID.REFR", "BASES PIZZAS&MASAS HO", "HARINAS Y SEMOLAS", "ENCURTIDOS",
                   "ESPECIAS Y CONDIMENTO", "SAL", "OTROS PROD.EN PESO", "OTROS PROD.EN VOLUMEN", "ALGAS"]

df_total = df_total[df_total["CATEGORIAS"].isin(lista_categoria)]


# Corrijo el nombre de la categoría de los alimentos


nuevas_categorias = {"T.HUEVOS KGS": "Huevos", "MIEL": "Miel", "TOTAL CARNE": "Carne",
                     "TOTAL PESCA": "Pescados y mariscos", "TOTAL LECHE LIQUIDA": "Leche líquida",
                     "TOTAL OTRAS LECHES": "Otras leches", "DERIVADOS LACTEOS": "Derivados lacteos", "PAN": "Pan",
                     "BOLL.PAST.GALLET.CERE": "Bolleria, pastelería, galletas y cereales",
                     "PRODUCTOS NAVIDEÑOS": "Productos navideños", "CHOCOLATES/CACAOS/SUC": "Chocolates",
                     "ARROZ": "Arroz", "TOTAL PASTAS": "Pastas", "AZUCAR": "Azucar", "EDULCORANTES": "Edulcorante",
                     "LEGUMBRES": "Legumbres", "TOTAL ACEITE": "Aceites", "MARGARINA": "Margarinas",
                     "ACEITUNAS": "Aceitunas", "BEBIDAS DERIVADAS VI": "Bebidas derivadas del vino",
                     "TOTAL VINOS": "Vinos", "CERVEZAS": "Cervezas", "SIDRAS": "Sidras",
                     "T.BEBIDAS ESPIRITUOSA": "Bebidas espirituosas", "VINAGRE": "Vinagres",
                     "TOTAL ZOMO Y NECTAR": "Zumos y nectares", "TOTAL PATATAS": "Patatas",
                     "T.HORTALIZAS FRESCAS": "Hortalizas frescas", "T.FRUTAS FRESCAS": "Frutas frescas",
                     "FRUTOS SECOS": "Frutos secos", "T.FRUTA&HORTA.TRANSF": "Frutas y hortalizas transformadas",
                     "PLATOS PREPARADOS": "Platos preparados", "CAFES E INFUSIONES": "Cafes e infusiones",
                     "CALDOS": "Caldos", "SALSAS": "Salsas", "AGUA DE BEBIDA ENVAS.": "Aguas envasadas",
                     "GASEOSAS Y BEBID.REFR": "Gaseosas y bebidas refrescantes", "BASES PIZZAS&MASAS HO": "Masas",
                     "HARINAS Y SEMOLAS": "Harinas y semolas", "ENCURTIDOS": "Encurtidos",
                     "ESPECIAS Y CONDIMENTO": "Especias", "SAL": "Sal", "OTROS PROD.EN PESO": "Otros productos en peso",
                     "OTROS PROD.EN VOLUMEN": "Otros productos en volumen"}

df_total["CATEGORIAS"] = df_total["CATEGORIAS"].replace(nuevas_categorias)

# Transformo el formato de ancho a largo, manteniendo las columnas "AÑO", "CATEGORIAS" y "ANALISIS" como identificadores


df_total = df_total.melt(id_vars=["AÑO", "CATEGORIAS", "ANALISIS"], var_name="CANALES DE VENTA",
                         value_name="CANTIDAD")

"""
5) EXPORTACIÓN DEL MARCO RESULTANTE

Finalmente, del marco de datos resultantes, creo un documento con extensión .csv, que, posteriormente, voy a guardar en
la carpeta de descarga de la máquina local
"""

# Convierto df_total  a un archivo CSV
csv_content = df_total.to_csv(index=False)

# Obtengo la ruta de la carpeta de descargas del usuario
download_folder = os.path.expanduser("~")
csv_filename = "tabla_procesada_canalesventa.csv"
csv_path = os.path.join(download_folder, csv_filename)

# Guardo el contenido del archivo CSV en la ubicación deseada
with open(csv_path, "w", encoding="utf-8") as f:
    f.write(csv_content)

print(f'Archivo CSV guardado en: {csv_path}')

