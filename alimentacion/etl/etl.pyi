# Importo las librerías que voy a utilizar en este proyecto

import pandas as pd
import requests as rq
# import os

# Creo las listas con el nombre de los documentos

lista_archivo = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011",
                  "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]


# Creo las funciones que me permitirá cargar los datos de los archivos alojados en el repositorio de GitHub


def carga_consumoxcapita(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/alimentacion/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{lista_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    if int(nombre_archivo) <= 2019:
        df_consumoxcapita = pd.read_excel(response.content, sheet_name=4, header=2, engine="openpyxl")
        df_consumoxcapita["Año"] = int(nombre_archivo)
    else:
        df_consumoxcapita = pd.read_excel(response.content, sheet_name=5, header=2, engine="openpyxl")
        df_consumoxcapita["Año"] = int(nombre_archivo)
    return df_consumoxcapita


def carga_gastoxcapita(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/alimentacion/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{lista_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    if int(nombre_archivo) <= 2019:
        df_gastoxcapita = pd.read_excel(response.content, sheet_name=5, header=2, engine="openpyxl")
        df_gastoxcapita["Año"] = int(nombre_archivo)
    else:
        df_gastoxcapita = pd.read_excel(response.content, sheet_name=6, header=2, engine="openpyxl")
        df_gastoxcapita["Año"] = int(nombre_archivo)
    return df_gastoxcapita


def carga_precio(nombre_archivo):
    base_url = "https://raw.githubusercontent.com"
    usuario_git = "DMorgon"
    repositorio = "portafolios/main/alimentacion/datos_origen"
    ruta_archivo = f"{base_url}/{usuario_git}/{repositorio}/{lista_archivo}.xlsx"
    response = rq.get(ruta_archivo)
    if int(nombre_archivo) <= 2019:
        df_precio = pd.read_excel(response.content, sheet_name=6, header=2, engine="openpyxl")
        df_precio["Año"] = int(nombre_archivo)
    else:
        df_precio = pd.read_excel(response.content, sheet_name=4, header=2, engine="openpyxl")
        df_precio["Año"] = int(nombre_archivo)
    return df_precio

# Cargo los datos correspondientes con las hojas consumoxcapita de cada archivo.


lista_df_consumoxcapita = []

for archivo in lista_archivo:
    df = carga_consumoxcapita(archivo)
    lista_df_consumoxcapita.append(df)

# Cargo los datos correspondientes con las hojas gastoxcapita de cada archivo.


lista_df_gastoxcapita = []

for archivo in lista_archivo:
    df = carga_gastoxcapita(archivo)
    lista_df_gastoxcapita.append(df)


# Cargo los datos correspondientes con las hojas precio de cada archivo


lista_df_precio = []

for archivo in lista_archivo:
    df = carga_precio(archivo)
    lista_df_precio.append(df)