# <p align="center">Análisis del Volumen de Consumo de Alimentos por Categoría en Hogares Españoles</p>
## <p align="center">David Moreno</p>
##  <p align="center">2023-09-20</p>

## **Introducción**

El análisis de datos desempeña un papel fundamental en la comprensión de los patrones de consumo de alimentos, un tema de importancia crítica en la sociedad actual. En el marco de un proyecto más amplio, destinado a demostrar nuestras capacidades en el análisis de datos, nos adentramos en el apasionante mundo de la alimentación. Este primer análisis se centra en el estudio del consumo de alimentos en hogares españoles, con el objetivo de arrojar luz sobre las preferencias alimentarias, los cambios a lo largo del tiempo y las variaciones geográficas en la elección de alimentos.

La alimentación es un aspecto fundamental de la vida de las personas y desempeña un papel central en la salud, la cultura y la economía. Entender cómo, cuánto y qué tipos de alimentos consumen los hogares es esencial tanto para las empresas de la industria alimentaria como para los encargados de formular políticas públicas en materia de salud y alimentación.

Nuestro análisis se basa en un conjunto de datos exhaustivo que abarca desde el año 2000 hasta el año 2022 y se desglosa por regiones de España. Nos sumergimos en la riqueza de estos datos para comprender las tendencias de consumo de alimentos a lo largo de las dos últimas décadas y para identificar patrones que puedan informar decisiones futuras en el campo de la alimentación y la nutrición.

Los objetivos específicos de este análisis incluyen:

Evaluar las categorías de alimentos más consumidas en los hogares españoles.
Identificar las categorías de alimentos que han experimentado cambios significativos en su consumo a lo largo del tiempo.
Analizar las variaciones geográficas en las preferencias alimentarias, centrándonos en las diferencias regionales.
Este análisis no solo representa una oportunidad para explorar la riqueza de los datos sobre consumo de alimentos, sino que también sienta las bases para futuros análisis dentro de nuestro proyecto más amplio. Los resultados obtenidos en este análisis nos guiarán en la formulación de nuevas preguntas y enfoques que se abordarán en análisis posteriores.

En resumen, este análisis inicial sobre el consumo de alimentos en hogares españoles establece la base para una exploración más profunda de los patrones alimentarios y sus implicaciones. Esperamos que este informe no solo ofrezca una visión clara de nuestros hallazgos, sino que también inspire futuros análisis y reflexiones en el ámbito del análisis de datos aplicado a la alimentación.

## **1. Objetivos**

Este análisis inicial sobre el consumo de alimentos en hogares españoles tiene como objetivo principal explorar y comprender las tendencias y patrones generales relacionados con las preferencias alimentarias a lo largo del tiempo y en diferentes regiones de España. Para lograr este objetivo, hemos establecido los siguientes objetivos específicos:

1. **Evaluar las Tendencias Temporales en el Consumo de Alimentos**. Aquí, examinaremos cómo ha variado el consumo de alimentos a lo largo del tiempo, identificando cambios significativos en la elección de alimentos y buscando explicaciones para estas fluctuaciones. Esto nos permitirá comprender mejor las dinámicas de consumo a lo largo de los años.

Pregunta guía: ¿Qué tendencias temporales pueden identificarse en el consumo de alimentos a lo largo de las dos últimas décadas?

Pregunta guía: ¿Cuáles son las categorías de alimentos que predominan en la dieta de los hogares españoles y cómo ha evolucionado su consumo a lo largo de los años?

2. **Determinar las categorías de alimentos más consumidas en los hogares españoles**. Este análisis ayudará a identificar las preferencias alimentarias fundamentales que han perdurado a lo largo del tiempo y a comprender cómo se han modificado estas preferencias en respuesta a cambios sociales, económicos o culturales.

Pregunta guía: ¿Cuáles son las categorías de alimentos que predominan en la dieta de los hogares españoles y cómo ha evolucionado su consumo a lo largo de los años?

3. **Analizar las Variaciones Regionales en las Preferencias Alimentarias**. Aquí, examinaremos si las preferencias alimentarias varían significativamente según la ubicación geográfica en España. Identificar y comprender estas diferencias puede proporcionar información valiosa sobre las influencias regionales en las elecciones de alimentos.

Pregunta guía: ¿Existen diferencias notables en las preferencias alimentarias entre las diferentes regiones de España, y en caso afirmativo, cuáles son esas diferencias?

Finalmente, el cuarto objetivo consiste en utilizar los resultados de este análisis como punto de partida para futuras investigaciones. A medida que identifiquemos patrones y tendencias, surgirán nuevas preguntas que requerirán análisis posteriores. Este objetivo implica la formulación de hipótesis y preguntas que guiarán la siguiente fase del proyecto.

En resumen, los objetivos de este análisis de consumo de alimentos en hogares españoles están diseñados para arrojar luz sobre las preferencias alimentarias a lo largo del tiempo y en diferentes regiones, al tiempo que proporcionan una base sólida para investigaciones futuras. A través de estas metas, buscamos contribuir al conocimiento en el campo de la alimentación y el análisis de datos.

## **2. Recursos**

En la ejecución de este proyecto de análisis de datos sobre el consumo de alimentos en hogares españoles, hemos empleado una serie de recursos y herramientas para recopilar, procesar, analizar y comunicar la información. Estos recursos se han seleccionado cuidadosamente para garantizar la calidad y eficiencia de todo el proceso.

### **2.1. Fuentes de Datos**

El conjunto de datos fundamental se compone de 22 archivos en formato Excel, uno para cada año desde el 2000 hasta el 2022. Cada uno de estos archivos contiene varias hojas de datos relacionadas con el consumo de alimentos en hogares españoles. Para este análisis específico, nos hemos centrado en la hoja de datos que registra el "Volumen" de consumo de alimentos.

Estos archivos se obtuvieron de fuentes confiables, específicamente del sitio web del Ministerio de Agricultura, Pesca y Alimentación. Con el fin de mantener la transparencia y la accesibilidad, estos archivos se albergan en el repositorio de GitHub bajo el directorio "datos_origen". Estos datos proporcionan la base fundamental para todas las etapas del análisis.

### **2.2. Herramientas y Tecnologías**

#### **2.2.1. Proceso ETL**

Para la extracción, transformación y carga (ETL) de los datos, hemos utilizado Python, un lenguaje de programación ampliamente reconocido por su versatilidad en el análisis de datos. Los scripts ETL se encuentran organizados en la carpeta "código", y desempeñan un papel esencial en la preparación de los datos para el análisis.

las bibliotecas empleadas de Python son:

- os: Para operaciones de sistema y manejo de archivos.
- requests: Para realizar solicitudes HTTP y descargar datos.
- pandas: Para la manipulación y análisis de datos.
- openpyxl: Para trabajar con archivos Excel.

#### **2.2.2. Análisis Exploratorio de Datos (EDA)**

RStudio, un entorno de desarrollo integrado (IDE) para R, se ha empleado para llevar a cabo el análisis exploratorio de datos (EDA). Este entorno proporciona las herramientas necesarias para visualizar y comprender los datos en profundidad. Los resultados de este análisis se documentan en la carpeta "eda", junto con los recursos utilizados para crear visualizaciones significativas.

El análisis exploratorio de datos se llevó utilizando las siguientes bibliotecas de R:

- readxl: Para leer archivos Excel.
- httr: Para realizar solicitudes HTTP.
- tidyverse: Un conjunto de paquetes que incluye herramientas para manipulación y visualización de datos.
- rmarkdown: Para la generación de informes y documentos.
- dplyr: Para la manipulación de datos y la creación de resúmenes.
- corrplot: Para la visualización de matrices de correlación.

#### **2.2.3. Visualizaciones: Google Looker**

La creación de visualizaciones interactivas y cuadros de mando es esencial para comunicar los hallazgos del análisis. Google Looker se ha utilizado para diseñar cuadros de mando que permiten una exploración más profunda de los datos. Las capturas de estas visualizaciones se almacenan en la carpeta "visualizaciones" para su posterior inclusión en los informes.

Google Looker es una plataforma de inteligencia empresarial y visualización de datos que permite a las organizaciones analizar y compartir datos de manera efectiva. Fue adquirida por Google en 2020 y se ha integrado estrechamente en Google Cloud Platform (GCP) para brindar soluciones de análisis de datos en la nube

#### **2.2.4. Informes Finales**

Los informes finales que resumen y comunican los resultados de cada análisis se crean utilizando Markdown, un lenguaje de marcado ligero que facilita la generación de documentos bien estructurados y formateados. Estos informes se encuentran en la carpeta "informes", y constituyen una parte crucial de la documentación del proyecto.

### **2.3. Organización de Recursos**

Para mantener una organización clara y accesible de todos los recursos, hemos estructurado el proyecto en diversas carpetas:

- **datos_origen**: Contiene los archivos Excel de las fuentes de datos originales.
- **código**: Alberga los scripts en Python utilizados en el proceso ETL.
- **eda**: Incluye los documentos y recursos utilizados para el análisis exploratorio de datos en RStudio.
- **visualizaciones**: Guarda las capturas de pantalla de las visualizaciones y cuadros de mando de Google Looker.
- **informes**: Contiene los informes finales escritos en Markdown, que resumen los resultados de cada análisis.
- **datos_procesados**: Almacena los datos resultantes del proceso ETL en formato CSV, listos para su análisis.

Estos recursos y herramientas han sido esenciales para la realización de un análisis de datos efectivo y comprensible. Su combinación nos permite extraer conocimientos valiosos de los datos y comunicarlos de manera clara y efectiva.

## **3. Preparación de los datos**
## **4. Análisis Exploratorio de los Datos**
## **5. Conclusiones**
## **5. Trabajos futuros**

