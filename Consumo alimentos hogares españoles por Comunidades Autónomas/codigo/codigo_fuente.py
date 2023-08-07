"""

1) ImportarÉ las librerías que se van a utilizar
2) Cargaré los documentos .xlsx en marcos de datos de Pandas.
3) Realizaré un EDA de cada marco de datos para detectar las transformaciones a realizar
4) Realizaré las trasformaciones que son necesarios.
5) Cargaré el marco de datos resultante en un archivo .csv en la carpeta datos_preprocesados que se encuentra en el
espacio dedicado a este proyecto en el repositorio de GitHub
"""

# Importo las librerías que voy a utilizar en este proyecto

import pandas as pd
import requests as rq
import base64


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
    df_consumoxcapita = pd.read_excel(response.content, sheet_name=1, header=2, engine="openpyxl")
    df_consumoxcapita["ANALISIS"] = "Valor (miles de euros)"
    return df_consumoxcapita


def carga_volumen(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/Consumo alimentos hogares españoles por Comunidades Autónomas/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{nombre_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    df_consumoxcapita = pd.read_excel(response.content, sheet_name=2, header=2, engine="openpyxl")
    df_consumoxcapita["ANALISIS"] = "Volumen (miles de kg o litros)"
    return df_consumoxcapita


def carga_consumoxcapita(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/Consumo alimentos hogares españoles por Comunidades Autónomas/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{nombre_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    if int(nombre_archivo) <= 2019:
        df_consumoxcapita = pd.read_excel(response.content, sheet_name=4, header=2, engine="openpyxl")
        df_consumoxcapita["ANALISIS"] = "Consumo x cápita (miles de kg o litros)"
    else:
        df_consumoxcapita = pd.read_excel(response.content, sheet_name=5, header=2, engine="openpyxl")
        df_consumoxcapita["ANALISIS"] = "Consumo x cápita (miles de kg o litros)"
    return df_consumoxcapita


def carga_gastoxcapita(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/Consumo alimentos hogares españoles por Comunidades Autónomas/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{nombre_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    if int(nombre_archivo) <= 2019:
        df_consumoxcapita = pd.read_excel(response.content, sheet_name=5, header=2, engine="openpyxl")
        df_consumoxcapita["ANALISIS"] = "Consumo x cápita (miles de kg o litros)"
    else:
        df_consumoxcapita = pd.read_excel(response.content, sheet_name=6, header=2, engine="openpyxl")
        df_consumoxcapita["ANALISIS"] = "Consumo x cápita (miles de kg o litros)"
    return df_consumoxcapita


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

# Cargo los datos correspondientes con las hojas consumoxcapita de cada archivo.


lista_df_consumoxcapita = []

for archivo in lista_archivos:
    df = carga_consumoxcapita(archivo)
    lista_df_consumoxcapita.append(df)

# Cargo los datos correspondientes con las hojas gastoxcapita de cada archivo.


lista_df_gastoxcapita = []

for archivo in lista_archivos:
    df = carga_gastoxcapita(archivo)
    lista_df_gastoxcapita.append(df)

# uno los marcos de datos según el año y los incluyo en la lista_df

lista_df = []

for i in range(0, 23, 1):
    df = pd.concat([lista_df_valor[i], lista_df_volumen[i], lista_df_consumoxcapita[i], lista_df_gastoxcapita[i]],
                   ignore_index=True)
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

1) Los marcos de datos referentes a los años 2000, 2001, 2002, 2003, 2019, 2020, 2021 y 2022 tienen 20 columnas
 mientras que el resto de las tablas tienen 28. Hay variables que no son necesarias, para el análisis, con lo que
 pueden ser eliminadas.
 
2) Existen marcos de datos con el nombre de las variables de ciertas comunidades autónomas diferentes.

3) La variable de las categorías de los alimentos se denomina Unamed: 0.
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

# Elimino las variables correspondientes a los territorios que no voy a utilizar

columnas_eliminar = [".TOTAL ESPAÑA", "T.ESPAÑA", "NORESTE", "LEVANTE", "ANDALUCIA", "CENTRO-SUR", "CASTILLA Y LEON",
                     "NOROESTE", "NORTE", "T.CANARIAS"]

for df in lista_df:
    df.drop(columns=columnas_eliminar, errors="ignore", inplace=True)

# Corrijo el nombre de las variables correspondientes a las comunidades autónomas.

for df in lista_df:
    df.columns = df.columns.str.replace("CASTILLA LA MANCHA", "CASTILLA - LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA DE MADRID", "MADRID", regex=False)
    df.columns = df.columns.str.replace("PRINCIPADO DE ASTURIAS", "ASTURIAS", regex=False)
    df.columns = df.columns.str.replace("ILLES BALEARS", "BALEARES", regex=False)
    df.columns = df.columns.str.replace("C. FORAL DE NAVARRA", "NAVARRA", regex=False)
    df.columns = df.columns.str.replace("COMUNITAT VALENCIANA", "VALENCIA", regex=False)
    df.columns = df.columns.str.replace("ANDALUCÍA", "ANDALUCIA", regex=False)
    df.columns = df.columns.str.replace("T.ANDALUCIA", "ANDALUCIA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA Y LEÓN", "CASTILLA Y LEON", regex=False)
    df.columns = df.columns.str.replace("ARAGÓN", "ARAGON", regex=False)
    df.columns = df.columns.str.replace("REGIÓN DE MURCIA", "MURCIA", regex=False)
    df.columns = df.columns.str.replace("COMUNIDAD DE MADRID", "MADRID", regex=False)
    df.loc[:, sorted(df.columns)] = df.loc[:, df.columns]

# Añado la columna AÑO con los valores correspondiente al año del marco de datos

for i, df in enumerate(lista_df):
    df["AÑO"] = int(lista_archivos[i])

# Uno todas las tablas en una sola df_total

df_total = pd.concat(objs=lista_df, axis=0)

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

df_total_filtrado = df_total[df_total["CATEGORIAS"].isin(lista_categoria)]


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


df_total = df_total.melt(id_vars=["AÑO", "CATEGORIAS", "ANALISIS"], var_name="COMUNIDAD AUTONOMA",
                         value_name="CANTIDAD")


"""
5) EXPORTACIÓN DEL MARCO RESULTANTE
 
Finalmente, del marco de datos resultantes, creo un documento con extensión .csv, que, posteriormente, voy a cargar
en la carpeta del repositorio de GitHub habilitada para ello.
"""

# Definir las variables
username = "DMorgon"
reponame = "portafolios/main/Consumo alimentos hogares españoles por Comunidades Autónomas/datos_preprocesados"
access_token = "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"

# Convertir el DataFrame en contenido CSV

csv_content = df_total.to_csv(index=False)

# Codificar el contenido en base64
encoded_content = base64.b64encode(csv_content.encode("utf-8")).decode("utf-8")

# URL de la API para crear un archivo en GitHub
url = f"https://api.github.com/repos/{username}/{reponame}/contents/Consumo alimentos hogares españoles por Comunidades Autónomas/datos_preprocesados/tabla_procesada.csv"

# Encabezados de autenticación
headers = {
    'Authorization': f'token {access_token}'
}

# Datos para la solicitud POST

data = {
    'path': "https://api.github.com/repos/DMorgon/portafolios/contents/Consumo alimentos hogares españoles por Comunidades Autónomas/datos_preprocesados/tabla_procesada.csv",
    'message': 'Agregando archivo CSV',
    'content': encoded_content
}

# Realizar la solicitud POST para crear el archivo
response = rq.post(url, json=data, headers=headers)

print(response.text)

if response.status_code == 201:
    print("Archivo creado exitosamente en GitHub.")
else:
    print("No se pudo crear el archivo en GitHub.")
