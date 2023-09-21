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
    if i <= 3:
        df.drop(columns=".TOTAL ESPAÑA", errors="ignore", inplace=True)
    if 4 <= i <= 12:
        df.drop(columns=[".TOTAL ESPAÑA", "T.ANDALUCIA", "CASTILLA LEON", "NORESTE", "LEVANTE", "CENTRO-SUR",
                         "NOROESTE", "NORTE", "T.CANARIAS"], errors="ignore", inplace=True)
    if 13 <= i <= 18:
        df.drop(columns=["T.ESPAÑA", "ANDALUCIA", "CASTILLA Y LEÓN", "NORESTE", "LEVANTE", "CENTRO-SUR", "NOROESTE",
                         "NORTE", "T.CANARIAS"], errors="ignore", inplace=True)
    else:
        df.drop(columns="T.ESPAÑA", errors="ignore", inplace=True)

# Corrijo el nombre de las variables correspondientes a las comunidades autónomas.

for df in lista_df_volumen:
    df.columns = df.columns.str.replace("Unnamed: 0", "CATEGORÍAS", regex=False)
    df.columns = df.columns.str.replace("ARAGÓN", "ARAGON", regex=False)
    df.columns = df.columns.str.replace("ILLES BALEARS", "BALEARES", regex=False)
    df.columns = df.columns.str.replace("COMUNITAT VALENCIANA", "VALENCIA", regex=False)
    df.columns = df.columns.str.replace("REGIÓN DE MURCIA", "MURCIA", regex=False)
    df.columns = df.columns.str.replace("ANDALUCÍA", "ANDALUCIA", regex=False)
    df.columns = df.columns.str.replace("COMUNIDAD DE MADRID", "MADRID", regex=False)
    df.columns = df.columns.str.replace("CASTILLA-LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA - LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA Y LEÓN", "CASTILLA Y LEON", regex=False)
    df.columns = df.columns.str.replace("PRINCIPADO DE ASTURIAS", "ASTURIAS", regex=False)
    df.columns = df.columns.str.replace("RIOJA", "LA RIOJA", regex=False)
    df.columns = df.columns.str.replace("LA LA RIOJA", "LA RIOJA", regex=False)
    df.columns = df.columns.str.replace("C. FORAL DE NAVARRA", "NAVARRA", regex=False)
    df.loc[:, sorted(df.columns)] = df.loc[:, df.columns]

# Añado la columna AÑO con los valores correspondiente al año del marco de datos

for i, df in enumerate(lista_df_volumen):
    df["AÑO"] = int(lista_archivos[i])

# Uno todas las tablas en una sola df_total

df_total = pd.concat(objs=lista_df_volumen, axis=0)

# Transformo el formato de ancho a largo, manteniendo las columnas "AÑO" y "CATEGORÍAS" como identificadores

df_total = df_total.melt(id_vars=["AÑO", "CATEGORÍAS"],
                         var_name="REGIONES",
                         value_name="VOLUMEN")

# Creamos un diccionario con las denominaciones a sustituir junto a su sustituto
reemplazos = {"T.HUEVOS KGS": "Huevos", "HUEVOS KGS": "Huevos", "MIEL": "Miel", "TOTAL CARNE": "Carne",
              "AGUA MINERAL": "Agua", "LECHE LIQUIDA RECONST": "Preparados lacteos",  "TOTAL PESCA": "Pesca",
              "TOTAL LECHE LIQUIDA": "Leche líquida", "TOTAL OTRAS LECHES": "Otras leches",
              "PREPARADOS LACTEOS": "Preparados lacteos", "DERIVADOS LACTEOS": "Derivados lacteos", "PAN": "Pan",
              "ARROZ": "Arroz", "TOTAL PASTAS": "Pasta", "AZUCAR": "Azucar", "EDULCORANTES": "Edulcorante",
              "LEGUMBRES": "Legumbre", "TOTAL ACEITE": "Aceite", "MARGARINA": "Margarina", "ACEITUNAS": "Aceitunas",
              "VINAGRE": "Vinagre", "TOTAL ZUMO Y NECTAR": "Zumos", "TOTAL PATATAS": "Patatas",
              "T.HORTALIZAS FRESCAS": "Hortalizas frescas", "T.FRUTAS FRESCAS": "Frutas frescas",
              "FRUTOS SECOS": "Frutos secos", "T.FRUTA Y HORTA.TRANSF": "Frutas y Hortalizas Transformadas",
              "PLATOS PREPARADOS": "Platos preparados", "CAFES E INFUSIONES": "Cafés e infusiones", "CALDOS": "Caldos",
              "SALSAS": "Salsas", "AGUA DE BEBIDA ENVAS.": "Agua",  "GASEOSAS Y BEBID.REFR": "Refrescos",
              "BASES PIZZAS Y MASAS HO": "Masas", "HARINAS Y SEMOLAS": "Harinas", "ENCURTIDOS": "Encurtidos",
              "ESPECIAS Y CONDIMENTO": "Especias", "SAL": "Sal", "OTROS PROD.EN PESO": "Otros productos en peso",
              "OTROS PROD.EN VOLUMEN": "Otros productos en volumen", "BOLL.PAST.GALLET.CERE": "Boll/Past/Gallet/Cere",
              "CHOCOLATES/CACAOS/SUC": "Choco/Cacao/Suc"}

# Sustituimos en la columna "Categoría" los valores definidos en el diccionario anterior
df_total["CATEGORÍAS"] = df_total["CATEGORÍAS"].replace(reemplazos)


# Creamos una nueva tabla de datos con las categorias de alimentación que nos interesan para el análisis
categoria = ["Huevos", "Miel", "Carne",  "Agua", "Preparados lacteos", "Pesca", "Leche líquida", "Otras leches",
             "Derivados lacteos", "Pan", "Arroz", "Pasta", "Azucar", "Edulcorante", "Legumbre", "Aceite", "Margarina",
             "Aceitunas", "Vinagre", "Zumos", "Patatas", "Hortalizas frescas",  "Frutas frescas", "Frutos secos",
             "Frutas y Hortalizas Transformadas", "Platos preparados", "Cafés e infusiones", "Caldos", "Salsas",
             "Refrescos", "Masas", "Harinas", "Encurtidos", "Especias", "Sal", "Otros productos en peso",
             "Otros productos en volumen", "Boll/Past/Gallet/Cere", "Choco/Cacao/Suc"]

df_total = df_total[df_total["CATEGORÍAS"].isin(categoria)]

# Ajusto el tipo de dato de la variable AÑO para que sea de tipo fecha.

df_total["AÑO"] = df_total["AÑO"].astype(str)
df_total["AÑO"] = pd.to_datetime(df_total["AÑO"], format='%Y')

# Redondeo los datos e Volumen a dos decimales

df_total["VOLUMEN"] = df_total["VOLUMEN"].round(2)

# Cambio el formato del nombre de las Regiones

df_total["REGIONES"] = df_total["REGIONES"].str.title()


"""
4) CARGA DEL MARCO RESULTANTE

Finalmente, del marco de datos resultantes, creo un documento con extensión .csv, que, posteriormente, voy a guardar en
la carpeta de descarga de la máquina local
"""

# Convierto df_total  a un archivo CSV
csv_content = df_total.to_csv(index=False)

# Obtengo la ruta de la carpeta de descargas del usuario
download_folder = os.path.expanduser('~')
csv_filename = 'volumen_categorias.csv'
csv_path = os.path.join(download_folder, csv_filename)

# Guardo el contenido del archivo CSV en la ubicación deseada
with open(csv_path, 'w', encoding='utf-8') as f:
    f.write(csv_content)

print(f'Archivo CSV guardado en: {csv_path}')