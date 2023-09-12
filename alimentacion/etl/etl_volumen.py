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

columnas_eliminar_1 = ["NORESTE", "LEVANTE", "ANDALUCIA", "CENTRO-SUR", "CASTILLA Y LEON", "NOROESTE", "NORTE",
                       "T.CANARIAS"]

for i, df in enumerate(lista_df_volumen):
    if i <= 12:
        # Eliminar columnas para los primeros 13 DataFrames
        columns_to_drop = ["T.ANDALUCIA", "CASTILLA LEON", "NORESTE", "LEVANTE", "CENTRO-SUR", "NOROESTE", "NORTE",
                           "T.CANARIAS"]
    else:
        # Eliminar columnas para los DataFrames restantes
        columns_to_drop = ["ANDALUCÍA", "CASTILLA Y LEÓN", "NORESTE", "LEVANTE", "CENTRO-SUR", "NOROESTE", "NORTE",
                           "T.CANARIAS"]

    # Utilizar el método drop para eliminar las columnas especificadas
    df.drop(columns=columns_to_drop, errors="ignore", inplace=True)

# Corrijo el nombre de las variables correspondientes a las comunidades autónomas.

for df in lista_df_volumen:
    df.columns = df.columns.str.replace(".TOTAL ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("T.ESPAÑA", "ESPAÑA", regex=False)
    df.columns = df.columns.str.replace("Unnamed: 0", "ALIMENTOS", regex=False)
    df.columns = df.columns.str.replace("CASTILLA-LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("RIOJA", "LA RIOJA", regex=False)
    df.columns = df.columns.str.replace("ARAGÓN", "ARAGON", regex=False)
    df.columns = df.columns.str.replace("ILLES BALEARS", "BALEARES", regex=False)
    df.columns = df.columns.str.replace("COMUNITAT VALENCIANA", "VALENCIA", regex=False)
    df.columns = df.columns.str.replace("REGIÓN DE MURCIA", "MURCIA", regex=False)
    df.columns = df.columns.str.replace("ANDALUCÍA", "ANDALUCIA", regex=False)
    df.columns = df.columns.str.replace("COMUNIDAD DE MADRID", "MADRID", regex=False)
    df.columns = df.columns.str.replace("CASTILLA - LA MANCHA", "CASTILLA LA MANCHA", regex=False)
    df.columns = df.columns.str.replace("CASTILLA Y LEÓN", "CASTILLA Y LEON", regex=False)
    df.columns = df.columns.str.replace("PRINCIPADO DE ASTURIAS", "ASTURIAS", regex=False)
    df.columns = df.columns.str.replace("C. FORAL DE NAVARRA", "NAVARRA", regex=False)
    df.loc[:, sorted(df.columns)] = df.loc[:, df.columns]

# Añado la columna AÑO con los valores correspondiente al año del marco de datos

for i, df in enumerate(lista_df_volumen):
    df["AÑO"] = int(lista_archivos[i])

# Corrijo el nombre de algunas categorias de alimentos

for i in range(23):
    lista_df_volumen[i]['ALIMENTOS'] = lista_df_volumen[i]['ALIMENTOS'].replace({
        "ACEITE DE OLIVA": "TOTAL ACEITES DE OLIVA",
        "HUEVOS KGS": "T.HUEVOS KGS",
        "AGUA MINERAL": "AGUA DE BEBIDA ENVAS.",
        "LECHE LIQUIDA RECONST": "PREPARADOS LACTEOS",
        "BASES PIZZAS&MASAS HO": "BASES PIZZAS Y MASAS HO"
    })

# Uno todas las tablas en una sola df_total

df_total = pd.concat(objs=lista_df_volumen, axis=0)

# Realizó un filtro en df_total para sólo quedarme con las categorías de alimentos que voy a utilizar

lista_categoria = ["ARROZ", "PAN", "BOLL./PAST.ENVASADA", "BOLL./PAST.GRANEL", "GALLETAS ENVASADAS", "GALLETAS GRANEL",
                   "P.P.PASTA RESTO", "P.P.CONSERVA PASTA", "P.P.CONGELADO PASTA", "TOTAL PASTAS",
                   "OTROS P.P.CONGELADO", "P.P.PIZZA", "O.PASTEL/TARTA GRA", "O.PASTEL/TARTA ENV",
                   "CEREALES DESAY.ENV.", "BASES PIZZAS Y MASAS HO", "HARINAS Y SEMOLAS", "CARNE VACUNO", "C.CONG.VACA",
                   "CARNE CERDO", "C.CONG.CERDO", "CARNE OVINO/CAPRINO", "CARNE POLLO", "AVESTRUZ", "PAVO",
                   "OTRAS AVES", "C.CONG.POLLO", "CARNE TRANSFORMADA", "P.P.CONSERVA CARNE", "P.P.CONGELADO CARNE",
                   "PLAT.PREP.OTROS", "SALCHICHAS FRESCAS", "SALCHICHAS CONGELAD", "CARNE DESPOJOS", "CARNE CONEJO",
                   "OTRAS CARNES FRESCA", "CARNE CONGELADA", "PESCADOS FRESCOS", "PESCADOS CONGELADOS",
                   "MARISCO/MOLUSCO/CRUS", "SALMON AHUMADO", "TRUCHA AHUMADA", "OTROS AHUMADOS", "PESCADO SALADO",
                   "CONS.PESCADO/MOLUSCO", "P.P.CONSERV PESCADO", "P.P.CONGEL.PESCADO", "LECHE CRUDA", "LECHE ENTERA",
                   "LECHE SEMIDESNATAD", "LECHE DESNATADA", "TOTAL OTRAS LECHES", "PREPARADOS LACTEOS",
                   "LECHES FERMENTADAS", "BATIDOS DE YOGURT", "CUAJADAS", "QUESO", "NATA", "NATILLAS",
                   "FLANES PREPARADOS", "CREMA DE CHOCOLATE", "CREMA CATALANA", "POSTRES CON NATA",
                   "OT.DERIVADOS LACTEOS", "BATIDOS DE LECHE", "T.HUEVOS KGS", "TORTILLAS REFRIGERAD", "MANTEQUILLA",
                   "MARGARINA", "TOTAL ACEITES DE OLIVA", "ACEITE DE ORUJO", "ACEITE DE GIRASOL", "ACEITE DE MAIZ",
                   "ACEITE DE SOJA", "ACEITE DE SEMILLA", "TOCINO Y MANTECA", "NARANJAS", "MANDARINAS", "LIMONES",
                   "PLATANOS", "MANZANAS", "MANZANAS", "MELOCOTONES", "ALBARICOQUES", "CIRUELAS", "CEREZAS", "AGUACATE",
                   "FRESAS/FRESON", "UVAS", "MELON", "SANDIA", "KIWI", "PIÑA", "OTRAS FRUTAS FRESCAS", "FRUTOS SECOS",
                   "FRUTA CONS/ALMIBAR", "RESTO FRUTA CONSER", "FRUTAS CONGELADAS", "LECHUGA/ESC./ENDIVIA",
                   "VERDURAS DE HOJA", "COLES", "TOMATES", "JUDIAS VERDES", "PIMIENTOS", "PEPINOS", "BERENJENAS",
                   "CALABACINES", "CEBOLLAS", "AJOS", "ZANAHORIAS", "ESPARRAGOS", "CHAMPIÑONES+O.SETAS",
                   "OTR.HORTALIZAS/VERD.", "LEGUMBRES SECAS", "P.P.CONGEL.VEGETAL", "VERD./HORT.CONGELAD",
                   "LEGUMBRES COCIDAS", "ACEITUNAS", "GUISANTES", "JUDIAS VERDES", "PIMIENTOS", "ESPARRAGOS",
                   "ALCACHOFAS", "CHAMPIÑOSNES+SETAS", "MAIZ DULCE", "MENESTRA", "TOMATES", "OTRA VERD/HORT.CON",
                   "P.P.CONGEL.VEGETAL", "ENCURTIDOS", "TOMATE FRITO", "PATATAS FRESCAS", "PATATAS CONGELADAS",
                   "PATATAS PROCESADAS", "AZUCAR", "EDULCORANTES", "MIEL", "MERMELADAS,CONFIT.",
                   "CHOCOLATES/CACAOS/SUC", "TURRON DE CHOCOLATE", "CACAO SOLUBLE", "PRODUCTOS NAVIDEÑOS",
                   "FRUTA ESCARCHADA", "HELADOS Y TARTAS", "SALSAS", "SAL", "ESPECIAS Y CONDIMENTO", "CALDOS",
                   "P.P.SOPAS Y CREMAS",  "OTROS PROD.EN PESO", "CAFE G. O M.TORREFAC", "CAFE G. O M.NATURAL",
                   "CAFE G. O M.MEZCLA", "CAFE G. O M.DESCA", "CAFE SOLUBLE", "SUCEDANEOS DE CAFE", "TE", "MANZANILLA",
                   "POLEO", "OTRAS INFUSIONES", "AGUA DE BEBIDA ENVAS.", "GASEOSAS Y BEBID.REFR", "TOTAL ZUMO Y NECTAR",
                   "ZUMOS DE HORTALIZAS", "VINAGRE", "OTROS PROD.EN VOLUMEN"]

df_total = df_total[df_total["ALIMENTOS"].isin(lista_categoria)]

# Transformo el formato de ancho a largo, manteniendo las columnas "AÑO" y "ALIMENTOS"  como identificadores


df_total = df_total.melt(id_vars=["AÑO", "ALIMENTOS"], var_name="REGIONES",
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
