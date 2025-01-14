# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10rcAy7RlePidTx23KSSlZcGQFf9VN8By
"""

#importamos las librerias de pyspark
import csv
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


#creamos el spark como registro de asaitencia_media 
spark= SparkSession.builder.appName("Registro de asistencia_media").getOrCreate()
# llamamos el archivo estados
csv_file = "Estados.csv"
# que lea ela archivo
Datos_t = spark.read.csv(csv_file, header=True, inferSchema=True)
Datos_t.show() #y este muestre los datos 
var_moda = Datos_t.groupBy("estados").count().orderBy(col("count").desc()).first()
#con esta consulta, vamos a ver la moda, de los estados, si las personas asisten mas a la reunion o faltan
print("la moda es:",var_moda["estado"])
#se visulizza en el estado