import pandas as pd
import mysql.connector
from mysql.connector import Error

# Configurações de conexão com o banco de dados
config = {
    "user": "digitalstoregame",
    "password": "@Lt057869",
    "host": "digitalstoregames.mysql.pythonanywhere-services.com",
    "database": "digitalstoregame$digitalstoregames",
    "autocommit": True,
    "port": 3306
}

# Caminho para o arquivo CSV
caminho_arquivo_csv = './sendgrid.csv'

def processFile():
    df = pd.read_csv(caminho_arquivo_csv)        
    df = df.where(pd.notna(df), None)
    # Group by 'email' and aggregate 'clicks' and 'opened'
    result_df = df.groupby(['email', 'event']).size().unstack(fill_value=0).reset_index()
    # Merge with the 'processed' events DataFrame, specify suffixes
    processed_events_df = df[df['event'] == 'processed'][['email', 'processed']]
    result_df = pd.merge(result_df, processed_events_df, on='email', how='left')
    result_df.drop(['processed_y'], axis=1, inplace=True)
    # Rename columns and convert 'processed_date' to datetime
    result_df.rename(columns={'processed_x': 'processed_date'}, inplace=True)
    result_df['processed_date'] = pd.to_datetime(result_df['processed_date'])
    # Include additional columns in the final DataFrame
    additional_columns = ['message_id', 'recv_message_id', 'subject', 'from', 'originating_ip', 'url', 'user_agent', 'type', 'is_unique']
    result_df = pd.merge(result_df, df[additional_columns + ['email']], on='email', how='left')
    # Drop duplicates based on the 'email' column
    result_df.drop_duplicates(subset=['email'], inplace=True)
    result_df.rename(columns={'from': 'origen'}, inplace=True)
    # Display the resulting DataFrame
    return (result_df)

def saveEmailActivity():
    # Nome da tabela no banco de dados MySQL
    nome_da_tabela = 'EmailActivity'
    connection = None

    try:
        # Conectar ao banco de dados MySQL
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            # Ler o arquivo CSV para um DataFrame
            df = pd.read_csv(caminho_arquivo_csv)

            # Substituir NaN (valores nulos) por NULL
            df = df.where(pd.notna(df), None)

            # Criar uma conexão de cursor
            cursor = connection.cursor()

            # Inserir dados no MySQL
            for index, row in df.iterrows():
                sql = f"INSERT INTO {nome_da_tabela} ({', '.join(df.columns)}) VALUES ({', '.join(['%s'] * len(df.columns))})"
                cursor.execute(sql, tuple(row))

            # Commit para salvar as alterações
            connection.commit()

    except Error as e:
        print(f"Erro: {e}")

    finally:
        # Fechar o cursor e a conexão
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão encerrada.")


processFile()