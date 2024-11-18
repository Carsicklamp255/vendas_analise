import numpy as np
import csv
import os
import pandas as pd

df = pd.read_csv('vendas.csv')
print(df.to_string())

#1) Leitura e Preparação dos Dados:
#Carrega os dados do arquivo CSV para um array numpy. Cada linha do dataset representa um array unidimensional,
# em uma matriz 2D.

#converte as colunas de data, quantidade e preço para tipos apropriados 
# (data como string ou datetime, quantidade e preço como numéricos).

#2) Análise Estatística
#Calcule a média, mediana e desvio padrão do Valor Total das vendas.

#Encontre o produto com a maior quantidade vendida e o produto com o maior valor total de vendas.

#Calcule o valor total de vendas por região.

#Determine a venda média por dia.

#3)Análise Temporal
#Determine o dia da semana com maior número de vendas.

#Calcule a variação diária no valor total de vendas, ou seja, a diferença
#  entre as vendas de um dia e o dia seguinte.

#4)Desafios Adicionais (Opcional)
#Crie uma função que, dada uma região e um produto, retorne o total de vendas dessa combinação.
#Implemente uma análise de crescimento das vendas ao longo do tempo, ou seja, compare o total de vendas entre 
# dois períodos (ex: janeiro de 2024 e fevereiro de 2024) e calcule o aumento ou diminuição percentual.