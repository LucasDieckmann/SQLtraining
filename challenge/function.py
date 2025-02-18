import pandas as pd
import json
from sqlalchemy import create_engine

def dfj(df):
    """Retorna o DataFrame em formato JSON"""
    return df.to_json(orient='records', indent=4)

def ordenar_herois(df, coluna, ordem='crescente'):
    """Ordena os heróis com base na coluna escolhida e na ordem"""
    df.columns = df.columns.str.strip() 
    
    if coluna not in df.columns:
        print(f"Colunas disponíveis: {list(df.columns)}")
        raise ValueError(f"Coluna '{coluna}' não encontrada no DataFrame.")
    
    ascendente = True if ordem == 'crescente' else False
    df_ordenado = df.sort_values(by=coluna, ascending=ascendente)
    return df_ordenado

# Conexão com o banco de dados
conn = create_engine('sqlite:///brawlhalla.db').connect()

# Carregar os dados
df = pd.read_sql("SELECT * FROM brawlhalla", conn)

print("Colunas disponíveis:", df.columns) 
json_data = dfj(df) 
print(json_data)

try:
    df_ordenado = ordenar_herois(df, 'forca', 'decrescente')
    print(df_ordenado)
except ValueError as e:
    print(e)

