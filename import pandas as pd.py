import pandas as pd
import pyodbc

# Configurações de conexão
# Substitua pelo nome ou endereço IP do seu servidor SQL Server
server = 'LAPTOP-9FC33JKS'
database = 'GIN'  # Substitua pelo nome do seu banco de dados
username = 'sa'  # Substitua pelo seu nome de usuário
password = '1234'  # Substitua pela sua senha

# Conexão ao banco de dados
try:
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER=' + 192.168.1.164 + ';'
        f'DATABASE=' + GIN + ';'
        f'UID=' + sa + ';'
        f'PWD=' + 1234
    )
    print("Conexão bem-sucedida!")
except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)
    exit()

# Leitura do arquivo CSV
# Substitua pelo caminho do seu arquivo CSV
csv_file = 'C:\Downloads\nyc_tlc_yellow_trips_2018_subset_1'
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
            f"INSERT INTO {trips} (vendor_id, pickup_datetime, dropoff_datetime, passenger_count, trip_distance, rate_code, store_and_fwd_flag, payment_type, fare_amount,extra,mta_tax, tip_amount,tolls_amount, imp_surcharge, total_amount,pickup_location_id, dropoff_location_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?  ...)",
            row['coluna1'], row['coluna2'], row['coluna3'], row['coluna4'], row['coluna5']['coluna6'], row['coluna7'], row[
                'coluna8'], row['coluna9'], row['coluna10']['coluna11'], row['coluna12'], row['coluna13'], row['coluna14'], row['coluna15']
            ['coluna17'], row['coluna18']
        )
    connection.commit()
    print("Dados inseridos com sucesso!")
except Exception as e:
    print("Erro ao inserir os dados:", e)

# Fechamento da conexão
connection.close()
