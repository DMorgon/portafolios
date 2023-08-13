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


def carga_consumoxcapita(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/Consumo alimentos hogares españoles por Comunidades Autónomas/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{nombre_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    df_valor = pd.read_excel(response.content, sheet_name=13, header=2, engine="openpyxl")
    return df_valor

# Cargo los datos correspondientes con las hojas valor de cada archivo


lista_df = []

for archivo in lista_archivos:
    df = carga_consumoxcapita(archivo)
    lista_df.append(df)

"""
3. ANÁLISIS EXPLORATORIO DE DATOS

A continuación realizó un Análisis Exploratorio de Datos (EDA) en cada marco de datos de la lista_df, para obtener
información y anomalías de las mismas.

"""

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
"""
Revisando la información de cada marco de datos, encontramos las siguientes anomalías:

1) df_2000 y df_2001 no tienen las variables referentes al ciclo de vida del hogar, con lo que podemos prescindir 
los dos marcos de datos

2) En todos los marcos de datos existen variables con respecto a la región, que no son necesarias, con lo que se podría 
eliminar.

3) El nombre de las variables no coincide en todas los marcos de datos


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

# Creo la lista de marcos de datos sin df_2000 y df_2001

del lista_df[:2]


# Elimino las variables que no se van a utilizar.

variables_eliminar = [".TOTAL ESPAÑA", "NORESTE", "LEVANTE", "ANDALUCIA", "CENTRO-SUR", "CASTILLA Y LEON", "NOROESTE",
                      "NORTE", "CANARIAS", "T.CANARIAS", "T.ESPAÑA", "MAS DE 50 AÑOS"]

for df in lista_df:
    df.drop(columns=variables_eliminar, errors="ignore", inplace=True)


# Corrijo el nombre de las variables

for df in lista_df:
    df.columns = df.columns.str.replace(">500000", "Mas de 500000", regex=False)
    df.columns = df.columns.str.replace("+ DE 500000", "Mas de 500000", regex=False)
    df.columns = df.columns.str.replace("JOVENES INDEPENDIE", "JOVENES INDEPENDIENTES", regex=False)
    df.columns = df.columns.str.replace("JOVENES INDEPENDIENTESNTES", "JOVENES INDEPENDIENTES", regex=False)
    df.columns = df.columns.str.replace("PAREJ.JOVENES SIN", "PAREJ.JOVENES SIN HIJOS", regex=False)
    df.columns = df.columns.str.replace("PAREJ.JOVENES SIN HIJOS HIJOS", "PAREJ.JOVENES SIN HIJOS", regex=False)
    df.columns = df.columns.str.replace("PAREJ.CON HIJOS PE", "PAREJ.CON HIJOS PEQUEÑOS", regex=False)
    df.columns = df.columns.str.replace("PAREJ.CON HIJOS PEQUEÑOSQUEÑOS", "PAREJ.CON HIJOS PEQUEÑOS", regex=False)
    df.columns = df.columns.str.replace("PAREJ.CON HIJOS ED", "PAREJ.CON HIJOS EDAD MEDIA", regex=False)
    df.columns = df.columns.str.replace("PAREJ.CON HIJOS EDAD MEDIAAD MEDIA", "PAREJ.CON HIJOS EDAD MEDIA", regex=False)
    df.columns = df.columns.str.replace("PAREJ.CON HIJOS MA", "PAREJ.CON HIJOS MAYORES", regex=False)
    df.columns = df.columns.str.replace("PAREJ.CON HIJOS MAYORESYORES", "PAREJ.CON HIJOS MAYORES", regex=False)
    df.columns = df.columns.str.replace("HOGARES MONOPARENT", "HOGARES MONOPARENTALES", regex=False)
    df.columns = df.columns.str.replace("HOGARES MONOPARENTALESALES", "HOGARES MONOPARENTALES", regex=False)
    df.columns = df.columns.str.replace("PAREJAS ADULTAS SI", "PAREJAS ADULTAS SIN HIJOS", regex=False)
    df.columns = df.columns.str.replace("PAREJAS ADULTAS SIN HIJOSN HIJOS", "PAREJAS ADULTAS SIN HIJOS", regex=False)
    df.columns = df.columns.str.replace("ADULTOS INDEPENDIE", "ADULTOS INDEPENDIENTES", regex=False)
    df.columns = df.columns.str.replace("ADULTOS INDEPENDIENTESNTES", "ADULTOS INDEPENDIENTES", regex=False)
    df.columns = df.columns.str.replace("- 6 AÑOS", "NIÑOS - 6 AÑOS", regex=False)
    df.columns = df.columns.str.replace("NIÑOS NIÑOS - 6 AÑOS", "NIÑOS - 6 AÑOS", regex=False)
    df.columns = df.columns.str.replace("DE 6 A 15", "NIÑOS 6 A 15 AÑOS", regex=False)
    df.columns = df.columns.str.replace("- 35 AÑOS", "MENOS DE 35 AÑOS", regex=False)
    df.columns = df.columns.str.replace("35 A 49 AÑOS", "DE 35 A 49 AÑOS", regex=False)
    df.columns = df.columns.str.replace("DE DE 35 A 49 AÑOS", "DE 35 A 49 AÑOS", regex=False)
    df.columns = df.columns.str.replace("50 A 64 AÑOS", "DE 50 A 64 AÑOS", regex=False)
    df.columns = df.columns.str.replace("DE DE 50 A 64 AÑOS", "DE 50 A 64 AÑOS", regex=False)
    df.loc[:, sorted(df.columns)] = df.loc[:, df.columns]

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

# Añado la columna AÑO con los valores correspondiente al año del marco de datos

for i, df in enumerate(lista_df):
    df["AÑO"] = 2002 + i

# Uno todas las tablas en una sola df_total

df_total = pd.concat(objs=lista_df, axis=0)

# Modifico el nombre de la variable Unamed: 0 a CATEGORIAS.

df_total.rename(columns={"Unnamed: 0": "CATEGORIAS"}, inplace=True)

# Realizo un filtro en df_total para solo quedarme con las categorías de alimentos que voy a utilizar

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

# Realizo EDA en cada marco de datos

print(df_total.info())
if df_total.isna().any().any():
    print("Hay valores NA en la tabla de datos" + "\n")
else:
    print("No hay valores NA en la tabla de datos" + "\n")

# Transformo el formato de ancho a largo, manteniendo las columnas "AÑO", "CATEGORIAS" como identificadores

df_total = df_total.melt(id_vars=["AÑO", "CATEGORIAS"], var_name="CONDICIONES SOCIOECONÓMICAS",
                         value_name="CANTIDAD")

# Creo la variable "ANALISIS"


def mapeo(variable):
    if variable in ["< 2000 HABIT.", "2000 A 10000", "10001 A 100000", "100001 A 500000", "Mas de 500000"]:
        return "Población del municipio"
    elif variable in ["1 PERSONA", "2 PERSONAS", "3 PERSONAS", "4 PERSONAS", "5 Y MAS PERSONAS"]:
        return "Número de personas del hogar"
    elif variable in ["ALTA Y MEDIA ALTA", "MEDIA", "MEDIA BAJA", "BAJA"]:
        return "Clase social del hogar"
    elif variable in ["SIN NIÑOS", "NIÑOS - 6 AÑOS", "NIÑOS 6 A 15 AÑOS"]:
        return "Edad de los niños en el hogar"
    elif variable in ["ACTIVA", "NO ACTIVA"]:
        return "Actividad del responsable de la compra del hogar"
    elif variable in ["MENOS DE 35 AÑOS", "DE 35 A 49 AÑOS", "DE 50 A 64 AÑOS", "65 Y MAS AÑOS"]:
        return "Edad del responsable de la compra del hogar"
    else:
        return "Tipo de hogar"


df_total["ANALISIS"] = df_total["CONDICIONES SOCIOECONÓMICAS"].apply(mapeo)

# Cambia el formato de los valores en la columna CONDICIONES SOCIOECONÓMICAS a título

df_total["CONDICIONES SOCIOECONÓMICAS"] = df_total["CONDICIONES SOCIOECONÓMICAS"].str.title()

# Realizo EDA en cada marco de datos

print(df_total.info())
if df_total.isna().any().any():
    print("Hay valores NA en la tabla de datos" + "\n")
else:
    print("No hay valores NA en la tabla de datos" + "\n")

"""
5) EXPORTACIÓN DEL MARCO RESULTANTE

Finalmente, del marco de datos resultantes, creo un documento con extensión .csv, que, posteriormente, voy a guardar en
la carpeta de descarga de la máquina local
"""

# Convierto df_total  a un archivo CSV
csv_content = df_total.to_csv(index=False)

# Obtengo la ruta de la carpeta de descargas del usuario
download_folder = os.path.expanduser('~')
csv_filename = 'tabla_procesada_socioeconómico.csv'
csv_path = os.path.join(download_folder, csv_filename)

# Guardo el contenido del archivo CSV en la ubicación deseada
with open(csv_path, 'w', encoding='utf-8') as f:
    f.write(csv_content)

print(f'Archivo CSV guardado en: {csv_path}')
