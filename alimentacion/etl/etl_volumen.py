# Importo las librerías que voy a utilizar en este proyecto

import pandas as pd
import requests as rq
import os

# 2) EXTRACCIÓN DE LOS DATOS

# Creo las listas con el nombre de los documentos

lista_archivos = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011",
                  "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]


# Creo la función que me permitirá extraer los datos de los archivos alojados en el repositorio de GitHub
def carga_volumen(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/alimentacion/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{nombre_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    df_volumen = pd.read_excel(response.content, sheet_name=2, header=2, engine="openpyxl")
    return df_volumen


# Cargo los datos correspondientes con las hojas volumen de cada archivo

lista_df_volumen = []

for archivo in lista_archivos:
    df = carga_volumen(archivo)
    lista_df_volumen.append(df)

# 3) TRANSFORMACIÓN DE LOS DATOS

# Elimino las variables correspondientes a los territorios que no voy a utilizar

# Iterar a través de los DataFrames y las columnas a eliminar
for i, df in enumerate(lista_df_volumen):
    if i>=4 and i<=12:
        df.drop(columns=["T.ANDALUCIA", "CASTILLA LEON", "NORESTE", "LEVANTE", "CENTRO-SUR", "NOROESTE", "NORTE",
                         "T.CANARIAS"], errors="ignore", inplace=True)
    if i>=13 and i<=18:
        df.drop(columns=["ANDALUCIA", "CASTILLA Y LEÓN", "NORESTE", "LEVANTE", "CENTRO-SUR", "NOROESTE", "NORTE",
                         "T.CANARIAS"], errors="ignore", inplace=True)

# Corrijo el nombre de las variables correspondientes a las comunidades autónomas.

for df in lista_df_volumen:
    df.columns = df.columns.str.replace(".TOTAL ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("T.ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("Unnamed: 0", "PRODUCTOS", regex=False)
    df.columns = df.columns.str.replace("ARAGÓN", "ARAGON", regex=False)
    df.columns = df.columns.str.replace("ILLES BALEARS", "BALEARES", regex=False)
    df.columns = df.columns.str.replace("COMUNITAT VALENCIANA", "VALENCIA", regex=False)
    df.columns = df.columns.str.replace("REGIÓN DE MURCIA", "MURCIA", regex=False)
    df.columns = df.columns.str.replace("ANDALUCÍA", "ANDALUCIA", regex=False)
    df.columns = df.columns.str.replace("COMUNIDAD DE MADRID", "MADRID", regex=False)
    df.columns = df.columns.str.replace("CASTILLA-LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA - LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA Y LEÓN", "CASTILLA Y LEON", regex=False)
    df.columns = df.columns.str.replace("RIOJA", "LA RIOJA", regex=False)
    df.columns = df.columns.str.replace("C. FORAL DE NAVARRA", "NAVARRA", regex=False)
    df.loc[:, sorted(df.columns)] = df.loc[:, df.columns]

# Añado la columna AÑO con los valores correspondiente al año del marco de datos

for i, df in enumerate(lista_df_volumen):
    df["AÑO"] = int(lista_archivos[i])

# Uno todas las tablas en una sola df_total

df_total = pd.concat(objs=lista_df_volumen, axis=0)

# Transformo el formato de ancho a largo, manteniendo las columnas "AÑO" y "PRODUCTOS" como identificadores

df_total = df_total.melt(id_vars=["AÑO", "PRODUCTOS"],
                         var_name="REGIONES",
                         value_name="VOLUMEN")

"""
4) EXPORTACIÓN DEL MARCO RESULTANTE

Finalmente, del marco de datos resultantes, creo un documento con extensión .csv, que, posteriormente, voy a guardar en
la carpeta de descarga de la máquina local
"""

# Convierto df_total  a un archivo CSV
csv_content = df_total.to_csv(index=False)

# Obtengo la ruta de la carpeta de descargas del usuario
download_folder = os.path.expanduser('~')
csv_filename = 'volumen.csv'
csv_path = os.path.join(download_folder, csv_filename)

# Guardo el contenido del archivo CSV en la ubicación deseada
with open(csv_path, 'w', encoding='utf-8') as f:
    f.write(csv_content)

print(f'Archivo CSV guardado en: {csv_path}')
