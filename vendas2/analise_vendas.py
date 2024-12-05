import numpy as np
import pandas as pd
#1) Leitura e Preparação dos Dados:
#Carrega os dados do arquivo CSV para um array numpy. Cada linha do dataset representa um array unidimensional,
# em uma matriz 2D.
#converte as colunas de data, quantidade e preço para tipos apropriados 
# (data como string ou datetime, quantidade e preço como numéricos).
def conta_linhas_em_chunks(arquivo, chunk_size=10000):
    chunk_iter = pd.read_csv(arquivo, chunksize=chunk_size)
    total_linhas = 0

    for chunk in chunk_iter:
        total_linhas += len(chunk)
       
        for linha in chunk.values:
            print(linha)  

    print(f'O arquivo possui {total_linhas} linhas.')

arquivo = 'vendas.csv'
conta_linhas_em_chunks(arquivo)

arquivo = 'vendas.csv'

#2) Análise Estatística
#Calcule a média, mediana e desvio padrão do Valor Total das vendas.
#Encontre o produto com a maior quantidade vendida e o produto com o maior valor total de vendas.
#Calcule o valor total de vendas por região.
#Determine a venda média por dia.
def calculo_media(arquivo):
    df = pd.read_csv(arquivo)
    soma = df['Valor Total'].sum()
    linhas = len(df['Valor Total'])
    media = soma / linhas
    return media
arquivo = 'vendas.csv'
media = calculo_media(arquivo)
print(f"a média do valor total é: {media:.2f}")


def calculo_mediana(arquivo):
    df = pd.read_csv(arquivo)
    valores = df['Valor Total'].sort_values()
    n = len(valores)
        
    if n % 2 == 1:
        mediana = valores.iloc[n // 2]
    else:
        mid1 = valores.iloc[n // 2 - 1]
        mid2 = valores.iloc[n // 2]
        mediana = (mid1 + mid2) / 2
    
    return mediana

arquivo = 'vendas.csv'
mediana = calculo_mediana(arquivo)
print(f"A mediana do valor total é: {mediana:.2f}")


def calculo_desvio_padrao(arquivo):
    df = pd.read_csv(arquivo)
    
    desvio_padrao = df['Valor Total'].std()
    
    return desvio_padrao

arquivo = 'vendas.csv'  
desvio = calculo_desvio_padrao(arquivo)
print(f"O desvio padrão do é: {desvio:.2f}")

def produtos_com_maior_quantidade_e_valor(arquivo):
   
    df = pd.read_csv(arquivo)
    
    produto_quantidade = df.groupby('Produto')['Quantidade Vendida'].sum()
    produto_maior_quantidade = produto_quantidade.idxmax()  
    maior_quantidade = produto_quantidade.max() 
    
    
    produto_valor_total = df.groupby('Produto')['Valor Total'].sum()
    produto_maior_valor = produto_valor_total.idxmax()  
    maior_valor = produto_valor_total.max()  
    
    return produto_maior_quantidade, maior_quantidade, produto_maior_valor, maior_valor


arquivo = 'vendas.csv'
produto_quantidade, quantidade, produto_valor, valor_total = produtos_com_maior_quantidade_e_valor(arquivo)


print(f"Produto com a maior quantidade vendida: {produto_quantidade} ({quantidade} unidades)")
print(f"Produto com o maior valor total de vendas: {produto_valor} (R$ {valor_total:.2f})")


def vendas_por_regiao(arquivo):
    df = pd.read_csv(arquivo)
    
    vendas_regiao = df.groupby('Região')['Valor Total'].sum()
    
    return vendas_regiao


arquivo = 'vendas.csv'
vendas_regiao = vendas_por_regiao(arquivo)

print("Valor total de vendas por região:")
print(vendas_regiao)


def venda_media_por_dia(arquivo):
    df = pd.read_csv(arquivo)
    df['Data'] = pd.to_datetime(df['Data'])
    
    vendas_por_dia = df.groupby('Data')['Valor Total'].sum()
    
    venda_media = vendas_por_dia.mean()
    
    return venda_media


arquivo = 'vendas.csv'
media_venda = venda_media_por_dia(arquivo)
print(f"A venda média por dia é: {media_venda:.2f}")
#3)Análise Temporal
#Determine o dia da semana com maior número de vendas.
def dia_com_maior_venda(arquivo):

    df = pd.read_csv(arquivo)
    
    df['Data'] = pd.to_datetime(df['Data'])
    
    df['Dia da Semana'] = df['Data'].dt.day_name()
    
    vendas_por_dia = df.groupby('Dia da Semana')['Quantidade Vendida'].sum()
    
    dia_maior_venda = vendas_por_dia.idxmax()  
    maior_venda = vendas_por_dia.max()  
    
    return dia_maior_venda, maior_venda

arquivo = 'vendas.csv'
dia, quantidade = dia_com_maior_venda(arquivo)


print(f"O dia da semana com o maior número de vendas é {dia} ({quantidade} unidades).")
#Calcule a variação diária no valor total de vendas, ou seja, a diferença
#  entre as vendas de um dia e o dia seguinte.
def variacao_diaria(arquivo):
    df = pd.read_csv(arquivo)
    
    df['Data'] = pd.to_datetime(df['Data'])
    
    df['Valor Total'] = df['Quantidade Vendida'] * df['Preço Unitário']
    
    vendas_diarias = df.groupby('Data')['Valor Total'].sum()
    
    
    variacao = vendas_diarias.diff().dropna() 
    return variacao


arquivo = 'vendas.csv'
variacao = variacao_diaria(arquivo)

print("Variação diária no valor total de vendas:")
print(variacao)
