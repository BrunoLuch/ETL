import pandas as pd
import pyodbc

# Configurações de conexão
# Substitua pelo nome ou endereço IP do seu servidor SQL Server
server = 'LAPTOP-9FC33JKS\MSSQLSERVER01'
database = 'GIN'  # Substitua pelo nome do seu banco de dados
username = 'sa'  # Substitua pelo seu nome de usuário
password = '1234'  # Substitua pela sua senha

# Conexão ao banco de dados
try:
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )
    print("Conexão bem-sucedida!")
except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)
    exit()

# Leitura do arquivo CSV
# Use 'r' para uma string bruta
csv_file = r'C:\Users\bruno\uk\nyc_tlc_yellow_trips_2018_subset_1.csv'
df = pd.read_csv(csv_file)

# Exibição dos dados lidos
print(df.head())  # Exibe as primeiras linhas do DataFrame para verificação

# Nome da tabela no banco de dados
table_name = 'trips'  # Substitua pelo nome da sua tabela

# Inserção dos dados no banco de dados
try:
    # Criação de um cursor
    cursor = connection.cursor()

    # Construção da query de inserção
    for index, row in df.iterrows():
        cursor.execute(
            f"INSERT INTO {table_name} (vendor_id, pickup_datetime, dropoff_datetime, passenger_count, trip_distance, rate_code, store_and_fwd_flag, payment_type, fare_amount, extra, mta_tax, tip_amount, tolls_amount, imp_surcharge, total_amount, pickup_location_id, dropoff_location_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            row['vendor_id'], row['pickup_datetime'], row['dropoff_datetime'], row['passenger_count'], row['trip_distance'], row['rate_code'], row['store_and_fwd_flag'], row['payment_type'], row[
                'fare_amount'], row['extra'], row['mta_tax'], row['tip_amount'], row['tolls_amount'], row['imp_surcharge'], row['total_amount'], row['pickup_location_id'], row['dropoff_location_id']
        )

    connection.commit()
    print("Dados inseridos com sucesso!")
except Exception as e:
    print("Erro ao inserir os dados:", e)

# Fechamento da conexão
connection.close()
