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

"""
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

"""
# Cargo los datos correspondientes con las hojas consumoxcapita de cada archivo.


lista_df_consumoxcapita = []

for archivo in lista_archivos:
    df = carga_consumoxcapita(archivo)
    lista_df_consumoxcapita.append(df)


lista_df_gastoxcapita = []

for archivo in lista_archivos:
    df = carga_gastoxcapita(archivo)
    lista_df_gastoxcapita.append(df)

"""
lista_df_precio = []

for archivo in lista_archivos:
    df = carga_precio(archivo)
    lista_df_precio.append(df)
"""

# TRANSFORMACIÓN DE LOS DATOS

# Elimino las columnas que no se van a necesitar

columnas_eliminar = ["T.ANDALUCIA", "CASTILLA LEON", "NORESTE", "LEVANTE", "CENTRO-SUR", "NOROESTE", "NORTE",
                     "T.CANARIAS", "ANDALUCÍA", "CASTILLA Y LEÓN"]


for i, df in enumerate(lista_df_consumoxcapita):
    if 4 <= i <= 18:
        df.drop(columns=columnas_eliminar, errors="ignore", inplace=True)


for i, df in enumerate(lista_df_gastoxcapita):
    if 4 <= i <= 18:
        df.drop(columns=columnas_eliminar, errors="ignore", inplace=True)

"""
for i, df in enumerate(lista_df_precio):
    if 4 <= i <= 18:
        df.drop(columns=columnas_eliminar, errors="ignore", inplace=True)
"""
# Unifico el nombre de las variables

for df in lista_df_consumoxcapita:
    df.columns = df.columns.str.replace("Unnamed: 0", "ALIMENTOS", regex=False)
    df.columns = df.columns.str.replace(".TOTAL ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("T.ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA-LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA - LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA Y LEÓN", "CASTILLA Y LEON", regex=False)
    df.columns = df.columns.str.replace("RIOJA", "LA RIOJA", regex=False)
    df.columns = df.columns.str.replace("ILLES BALEARS", "BALEARES", regex=False)
    df.columns = df.columns.str.replace("COMUNITAT VALENCIANA", "VALENCIA", regex=False)
    df.columns = df.columns.str.replace("REGIÓN DE MURCIA", "MURCIA", regex=False)
    df.columns = df.columns.str.replace("COMUNIDAD DE MADRID", "MADRID", regex=False)
    df.columns = df.columns.str.replace("PRINCIPADO DE ASTURIAS", "ASTURIAS", regex=False)
    df.columns = df.columns.str.replace("C. FORAL DE NAVARRA", "NAVARRA", regex=False)
    df.columns = df.columns.str.replace("ARAGÓN", "ARAGON", regex=False)
    df.loc[:, sorted(df.columns)] = df.loc[:, df.columns]

for df in lista_df_gastoxcapita:
    df.columns = df.columns.str.replace("Unnamed: 0", "ALIMENTOS", regex=False)
    df.columns = df.columns.str.replace(".TOTAL ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("T.ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA-LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA - LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA Y LEÓN", "CASTILLA Y LEON", regex=False)
    df.columns = df.columns.str.replace("RIOJA", "LA RIOJA", regex=False)
    df.columns = df.columns.str.replace("ILLES BALEARS", "BALEARES", regex=False)
    df.columns = df.columns.str.replace("COMUNITAT VALENCIANA", "VALENCIA", regex=False)
    df.columns = df.columns.str.replace("REGIÓN DE MURCIA", "MURCIA", regex=False)
    df.columns = df.columns.str.replace("COMUNIDAD DE MADRID", "MADRID", regex=False)
    df.columns = df.columns.str.replace("PRINCIPADO DE ASTURIAS", "ASTURIAS", regex=False)
    df.columns = df.columns.str.replace("C. FORAL DE NAVARRA", "NAVARRA", regex=False)
    df.columns = df.columns.str.replace("ARAGÓN", "ARAGON", regex=False)
    df.loc[:, sorted(df.columns)] = df.loc[:, df.columns]
"""
for df in lista_df_precio:
    df.columns = df.columns.str.replace("Unnamed: 0", "ALIMENTOS", regex=False)
    df.columns = df.columns.str.replace(".TOTAL ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("T.ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA-LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA - LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA Y LEÓN", "CASTILLA Y LEON", regex=False)
    df.columns = df.columns.str.replace("RIOJA", "LA RIOJA", regex=False)
    df.columns = df.columns.str.replace("ILLES BALEARS", "BALEARES", regex=False)
    df.columns = df.columns.str.replace("COMUNITAT VALENCIANA", "VALENCIA", regex=False)
    df.columns = df.columns.str.replace("REGIÓN DE MURCIA", "MURCIA", regex=False)
    df.columns = df.columns.str.replace("COMUNIDAD DE MADRID", "MADRID", regex=False)
    df.columns = df.columns.str.replace("PRINCIPADO DE ASTURIAS", "ASTURIAS", regex=False)
    df.columns = df.columns.str.replace("C. FORAL DE NAVARRA", "NAVARRA", regex=False)
    df.columns = df.columns.str.replace("ARAGÓN", "ARAGON", regex=False)
    df.loc[:, sorted(df.columns)] = df.loc[:, df.columns]
"""

# Transformo de formato ancho a largo los marcos de datos

for i, df in enumerate(lista_df_consumoxcapita):
    lista_df_consumoxcapita[i] = df.melt(id_vars=["AÑO", "ALIMENTOS"], var_name="REGION", value_name="CONSUMOXCAPITA")

for i, df in enumerate(lista_df_gastoxcapita):
    lista_df_gastoxcapita[i] = df.melt(id_vars=["AÑO", "ALIMENTOS"], var_name="REGION", value_name="GASTOXCAPITA")
"""
for i, df in enumerate(lista_df_precio):
    lista_df_precio[i] = df.melt(id_vars=["AÑO", "ALIMENTOS"], var_name="REGION", value_name="PRECIO")
"""
# Uno verticalmente los marcos de datos de cada lista

consumoxcapita = pd.concat(lista_df_consumoxcapita, axis=0)

gastoxcapita = pd.concat(lista_df_gastoxcapita, axis=0)
"""
precio = pd.concat(lista_df_precio, axis=0)
"""

# Uno los marcos de datos resultantes horizontalmente

df_total = pd.concat([consumoxcapita[['AÑO', 'ALIMENTOS', 'REGION', 'CONSUMOXCAPITA']],
                      gastoxcapita[['GASTOXCAPITA']]], axis=1)

#  CARGO LOS DATOS

# Convierto df_total  a un archivo CSV
csv_content = df_total.to_csv(index=False)

# Obtengo la ruta de la carpeta de descargas del usuario
download_folder = os.path.expanduser("~")
csv_filename = "datos.csv"
csv_path = os.path.join(download_folder, csv_filename)

# Guardo el contenido del archivo CSV en la ubicación deseada
with open(csv_path, "w", encoding="utf-8") as f:
    f.write(csv_content)
