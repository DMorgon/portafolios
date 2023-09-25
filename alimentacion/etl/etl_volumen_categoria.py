# Importo las librerías que voy a utilizar en este proyecto

import pandas as pd
import os

# 2) EXTRACCIÓN DE LOS DATOS

# URL del archivo CSV en GitHub
base_url = "https://raw.githubusercontent.com"
usuario_git = "DMorgon"
repositorio = "portafolios/main/alimentacion/datos_procesados"
nombre_archivo = "volumen.csv"
ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{nombre_archivo}"

# Cargar el archivo CSV en un DataFrame de Pandas
volumen = pd.read_csv(ruta_archivo)

# 3) TRANSFORMACIÓN DE LOS DATOS
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
volumen["CATEGORIAS"] = volumen["CATEGORIAS"].replace(reemplazos)


# Creamos una nueva tabla de datos con las categorias de alimentación que nos interesan para el análisis
categoria = ["Huevos", "Miel", "Carne",  "Agua", "Preparados lacteos", "Pesca", "Leche líquida", "Otras leches",
             "Derivados lacteos", "Pan", "Arroz", "Pasta", "Azucar", "Edulcorante", "Legumbre", "Aceite", "Margarina",
             "Aceitunas", "Vinagre", "Zumos", "Patatas", "Hortalizas frescas",  "Frutas frescas", "Frutos secos",
             "Frutas y Hortalizas Transformadas", "Platos preparados", "Cafés e infusiones", "Caldos", "Salsas",
             "Refrescos", "Masas", "Harinas", "Encurtidos", "Especias", "Sal", "Otros productos en peso",
             "Otros productos en volumen", "Boll/Past/Gallet/Cere", "Choco/Cacao/Suc"]

volumen = volumen[volumen["CATEGORIAS"].isin(categoria)]

"""
4) CARGA DEL MARCO RESULTANTE

Finalmente, del marco de datos resultantes, creo un documento con extensión .csv, que, posteriormente, voy a guardar en
la carpeta de descarga de la máquina local
"""

# Convierto volumen  a un archivo CSV
csv_content = volumen.to_csv(index=False)

# Obtengo la ruta de la carpeta de descargas del usuario
download_folder = os.path.expanduser('~')
csv_filename = 'volumen_categorias.csv'
csv_path = os.path.join(download_folder, csv_filename)

# Guardo el contenido del archivo CSV en la ubicación deseada
with open(csv_path, 'w', encoding='utf-8') as f:
    f.write(csv_content)

print(f'Archivo CSV guardado en: {csv_path}')
