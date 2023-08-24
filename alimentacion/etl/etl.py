# Importo las librerías que voy a utilizar en este proyecto

import pandas as pd
import requests as rq
import os

# EXTRACIÓN DE LOS DATOS

# Creo las listas con el nombre de los documentos

lista_archivos = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011",
                  "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]


# Creo las funciones que me permitirá cargar los datos de los archivos alojados en el repositorio de GitHub


def carga_consumoxcapita(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/alimentacion/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{nombre_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    if int(nombre_archivo) <= 2019:
        df_consumoxcapita = pd.read_excel(response.content, sheet_name=4, header=2, engine="openpyxl")
        df_consumoxcapita["AÑO"] = int(nombre_archivo)
    else:
        df_consumoxcapita = pd.read_excel(response.content, sheet_name=5, header=2, engine="openpyxl")
        df_consumoxcapita["AÑO"] = int(nombre_archivo)
    return df_consumoxcapita


def carga_gastoxcapita(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/alimentacion/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{nombre_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    if int(nombre_archivo) <= 2019:
        df_gastoxcapita = pd.read_excel(response.content, sheet_name=5, header=2, engine="openpyxl")
        df_gastoxcapita["AÑO"] = int(nombre_archivo)
    else:
        df_gastoxcapita = pd.read_excel(response.content, sheet_name=6, header=2, engine="openpyxl")
        df_gastoxcapita["AÑO"] = int(nombre_archivo)
    return df_gastoxcapita


def carga_precio(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/alimentacion/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{nombre_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    if int(nombre_archivo) <= 2019:
        df_precio = pd.read_excel(response.content, sheet_name=6, header=2, engine="openpyxl")
        df_precio["AÑO"] = int(nombre_archivo)
    else:
        df_precio = pd.read_excel(response.content, sheet_name=4, header=2, engine="openpyxl")
        df_precio["AÑO"] = int(nombre_archivo)
    return df_precio


# Cargo los datos correspondientes con las hojas consumoxcapita de cada archivo.


lista_df_consumoxcapita = []

for archivo in lista_archivos:
    df = carga_consumoxcapita(archivo)
    lista_df_consumoxcapita.append(df)

# Realizo EDA en cada marco de datos

for i, df in enumerate(lista_df_consumoxcapita):
    tabla_nombre = f"df_{2000 + i}"
    print("Nombre de la tabla de datos:", tabla_nombre)
    print(df.info())

# Elimino las variables correspondientes a los territorios que no voy a utilizar

columnas_eliminar = ["T.ANDALUCIA", "ANDALUCÍA", "CASTILLA LEON", "CASTILLA Y LEÓN", "NORESTE", "LEVANTE", "CENTRO-SUR",
                     "NOROESTE", "NORTE", "T.CANARIAS"]


for i, df in enumerate(lista_df_consumoxcapita):
    if 4 <= i <= 18:
        df.drop(columns=columnas_eliminar, errors="ignore", inplace=True)

# Corrijo el nombre de las variables correspondientes a las comunidades autónomas.

for df in lista_df_consumoxcapita:
    df.columns = df.columns.str.replace("Unnamed: 0", "CATEGORIAS", regex=False)
    df.columns = df.columns.str.replace(".TOTAL ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("T.ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA-LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("RIOJA", "LA RIOJA", regex=False)
    df.columns = df.columns.str.replace("ARAGÓN", "ARAGON", regex=False)
    df.columns = df.columns.str.replace("ILLES BALEARS", "BALEARES", regex=False)
    df.columns = df.columns.str.replace("COMUNITAT VALENCIANA", "VALENCIA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA - LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("PRINCIPADO DE ASTURIAS", "ASTURIAS", regex=False)
    df.columns = df.columns.str.replace("C. FORAL DE NAVARRA", "NAVARRA", regex=False)
    df.columns = df.columns.str.replace("REGIÓN DE MURCIA", "MURCIA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA Y LEÓN", "CASTILLA Y LEON", regex=False)
    df.columns = df.columns.str.replace("ANDALUCÍA", "ANDALUCIA", regex=False)
    df.columns = df.columns.str.replace("COMUNIDAD DE MADRID", "MADRID", regex=False)
    df.columns = df.columns.str.replace("LA LA RIOJA", "LA RIOJA", regex=False)
    df.sort_index(axis=1, inplace=True)

# Transformo el formato de ancho a largo, manteniendo las columnas "AÑO", "CATEGORIAS" y "ANALISIS" como identificadores

for i, df in enumerate(lista_df_consumoxcapita):
    lista_df_consumoxcapita[i] = df.melt(id_vars=["AÑO", "CATEGORIAS"], var_name="REGION", value_name="CONSUMOXCAPITA")


# Cargo los datos correspondientes con las hojas gastoxcapita de cada archivo.


lista_df_gastoxcapita = []

for archivo in lista_archivos:
    df = carga_gastoxcapita(archivo)
    lista_df_gastoxcapita.append(df)

# Realizo EDA en cada marco de datos

for i, df in enumerate(lista_df_gastoxcapita):
    tabla_nombre = f"df_{2000 + i}"
    print("Nombre de la tabla de datos:", tabla_nombre)
    print(df.info())

# Elimino las variables correspondientes a los territorios que no voy a utilizar

columnas_eliminar = ["T.ANDALUCIA", "ANDALUCÍA", "CASTILLA LEON", "CASTILLA Y LEÓN", "NORESTE", "LEVANTE", "CENTRO-SUR",
                     "NOROESTE", "NORTE", "T.CANARIAS"]


for i, df in enumerate(lista_df_gastoxcapita):
    if 4 <= i <= 18:
        df.drop(columns=columnas_eliminar, errors="ignore", inplace=True)

# Corrijo el nombre de las variables correspondientes a las comunidades autónomas.

for df in lista_df_gastoxcapita:
    df.columns = df.columns.str.replace("Unnamed: 0", "CATEGORIAS", regex=False)
    df.columns = df.columns.str.replace(".TOTAL ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("T.ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA-LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("RIOJA", "LA RIOJA", regex=False)
    df.columns = df.columns.str.replace("ARAGÓN", "ARAGON", regex=False)
    df.columns = df.columns.str.replace("ILLES BALEARS", "BALEARES", regex=False)
    df.columns = df.columns.str.replace("COMUNITAT VALENCIANA", "VALENCIA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA - LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("PRINCIPADO DE ASTURIAS", "ASTURIAS", regex=False)
    df.columns = df.columns.str.replace("C. FORAL DE NAVARRA", "NAVARRA", regex=False)
    df.columns = df.columns.str.replace("REGIÓN DE MURCIA", "MURCIA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA Y LEÓN", "CASTILLA Y LEON", regex=False)
    df.columns = df.columns.str.replace("ANDALUCÍA", "ANDALUCIA", regex=False)
    df.columns = df.columns.str.replace("COMUNIDAD DE MADRID", "MADRID", regex=False)
    df.columns = df.columns.str.replace("LA LA RIOJA", "LA RIOJA", regex=False)
    df.sort_index(axis=1, inplace=True)

# Transformo el formato de ancho a largo, manteniendo las columnas "AÑO", "CATEGORIAS" y "ANALISIS" como identificadores

for i, df in enumerate(lista_df_gastoxcapita):
    lista_df_gastoxcapita[i] = df.melt(id_vars=["AÑO", "CATEGORIAS"], var_name="REGION", value_name="GASTOXCAPITA")


# Cargo los datos correspondientes con las hojas precio de cada archivo


lista_df_precio = []

for archivo in lista_archivos:
    df = carga_precio(archivo)
    lista_df_precio.append(df)

# Realizo EDA en cada marco de datos

for i, df in enumerate(lista_df_precio):
    tabla_nombre = f"df_{2000 + i}"
    print("Nombre de la tabla de datos:", tabla_nombre)
    print(df.info())

# Elimino las variables correspondientes a los territorios que no voy a utilizar

columnas_eliminar = ["T.ANDALUCIA", "ANDALUCÍA", "CASTILLA LEON", "CASTILLA Y LEÓN", "NORESTE", "LEVANTE", "CENTRO-SUR",
                     "NOROESTE", "NORTE", "T.CANARIAS"]


for i, df in enumerate(lista_df_precio):
    if 4 <= i <= 18:
        df.drop(columns=columnas_eliminar, errors="ignore", inplace=True)

# Corrijo el nombre de las variables correspondientes a las comunidades autónomas.

for df in lista_df_precio:
    df.columns = df.columns.str.replace("Unnamed: 0", "CATEGORIAS", regex=False)
    df.columns = df.columns.str.replace(".TOTAL ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("T.ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA-LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("RIOJA", "LA RIOJA", regex=False)
    df.columns = df.columns.str.replace("ARAGÓN", "ARAGON", regex=False)
    df.columns = df.columns.str.replace("ILLES BALEARS", "BALEARES", regex=False)
    df.columns = df.columns.str.replace("COMUNITAT VALENCIANA", "VALENCIA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA - LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("PRINCIPADO DE ASTURIAS", "ASTURIAS", regex=False)
    df.columns = df.columns.str.replace("C. FORAL DE NAVARRA", "NAVARRA", regex=False)
    df.columns = df.columns.str.replace("REGIÓN DE MURCIA", "MURCIA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA Y LEÓN", "CASTILLA Y LEON", regex=False)
    df.columns = df.columns.str.replace("ANDALUCÍA", "ANDALUCIA", regex=False)
    df.columns = df.columns.str.replace("COMUNIDAD DE MADRID", "MADRID", regex=False)
    df.columns = df.columns.str.replace("LA LA RIOJA", "LA RIOJA", regex=False)
    df.sort_index(axis=1, inplace=True)

# Transformo el formato de ancho a largo, manteniendo las columnas "AÑO", "CATEGORIAS" y "ANALISIS" como identificadores

for i, df in enumerate(lista_df_precio):
    lista_df_precio[i] = df.melt(id_vars=["AÑO", "CATEGORIAS"], var_name="REGION", value_name="PRECIO")


# Ahora merged_df contendrá la unión horizontal de los tres DataFrames

lista_df = []

for i in range (0, 23, 1):
    df = lista_df_consumoxcapita[i].merge(lista_df_gastoxcapita[i], on=['AÑO', 'CATEGORIAS', 'REGION'], how='outer')
    df = df.merge(lista_df_precio[i], on=['AÑO', 'CATEGORIAS', 'REGION'], how='outer')
    lista_df.append(df)


# Uno todas las tablas en una sola df_total de forma vertical

df_total = pd.concat(objs=lista_df, axis=0)

# Realizo EDA en cada marco de datos

print(df_total.info())

"""
5) CARGA

"""

# Convierto df_total  a un archivo CSV
csv_content = df_total.to_csv(index=False)

# Obtengo la ruta de la carpeta de descargas del usuario
download_folder = os.path.expanduser("~")
csv_filename = "tabla_procesada.csv"
csv_path = os.path.join(download_folder, csv_filename)

# Guardo el contenido del archivo CSV en la ubicación deseada
with open(csv_path, "w", encoding="utf-8") as f:
    f.write(csv_content)

print(f"Archivo CSV guardado en: {csv_path}")
