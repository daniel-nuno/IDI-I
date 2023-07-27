# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

df_datosPE = pd.read_excel('C:/Users/nuno/Downloads/datosPE.xlsx')

""" El vector de IMC """
df_datosPE['IMC'] = df_datosPE['Peso']/df_datosPE['Estatura']**2
""" La media de los pesos y la media de las estaturas """
avg_peso = df_datosPE['Peso'].mean()
avg_Estatura = df_datosPE['Estatura'].mean()

""" El ID de la persona de mayor peso, de la persona de menor estatura """
id_mayor_peso = df_datosPE[['ID Persona']][df_datosPE.Peso == df_datosPE.Peso.max()]
id_menor_estatura = df_datosPE[['ID Persona']][df_datosPE['Estatura']==df_datosPE['Estatura'].min()]

df_datosPE.loc[df_datosPE['Peso'].idxmax()]['ID Persona']
df_datosPE.loc[df_datosPE['Estatura'].idxmin()]['ID Persona']


"El vector de los ID de las personas con IMC>=28 "
personas_IMC_sobre28 = df_datosPE[['ID Persona']][df_datosPE['IMC']>=28]

resultados = [df_datosPE['IMC'], avg_peso, avg_Estatura, id_mayor_peso, id_menor_estatura, personas_IMC_sobre28]
print(resultados)
