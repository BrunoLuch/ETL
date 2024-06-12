import pyodbc

# Defina os detalhes da conexão
server = 'LAPTOP-9FC33JKS'
database = 'GIN'  # Substitua pelo nome do seu banco de dados
username = 'sa'  # Substitua pelo seu nome de usuário
password = '1234'  # Substitua pela sua senha


# Crie a string de conexão
conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={192.168.1.164};'
    f'DATABASE={GIN};'
    f'UID={sa};'
    f'PWD={1234};'
)

try:
    # Conecte ao banco de dados
    conn = pyodbc.connect(conn_str)

    # Crie um cursor
    cursor = conn.cursor()

    # Execute uma consulta de exemplo
    cursor.execute("SELECT @@VERSION")

    # Obtenha os resultados
    row = cursor.fetchone()
    while row:
        print(row[0])
        row = cursor.fetchone()

    # Feche o cursor e a conexão
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print(f"Erro ao conectar ao SQL Server: {e}")
