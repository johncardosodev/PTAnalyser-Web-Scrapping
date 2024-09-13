from mysql.connector import connect 
#este módulo fornece uma API para a comunicação com o MySQL para recolher todos os links da coluna website_index

def connect_to_database(): # Definir a função connect_to_database
    mysql_database_user = "Raquel"
    mysql_database_user_password = "Silva1234"
    mysql_database_name = "bdptanalyser"
    mysql_database_host = "62.28.39.135"

    return connect( # Retornar uma conexão à base de dados
        host=mysql_database_host, # Utilizar a variável mysql_database_host do ficheiro config.py
        user=mysql_database_user, # Utilizar a variável mysql_database_user do ficheiro config.py
        password=mysql_database_user_password, # Utilizar a variável mysql_database_user_password do ficheiro config.py
        database=mysql_database_name, # Utilizar a variável mysql_database_name do ficheiro config.py
        charset='utf8mb4', # Utilizar o conjunto de caracteres utf8mb4 (suporta emojis) e charset português
        collation='utf8mb4_unicode_ci' # Utilizar a colação utf8mb4_unicode_ci (suporta emojis)    
    )

def get_website_(column_name):
    try:
        # Connect to MySQL
        db = connect_to_database()
        cursor = db.cursor()       

        # SQL statement to select specific text from the table
        sql = "SELECT {column1} FROM `empresa`".format(column1=column_name)

        # Execute the SQL statement
        cursor.execute(sql)

        # Fetch the result
        results = cursor.fetchall()

        # Extract the specific text for every row
        specific_texts = [row[0] for row in results] #devolve a lista com os valores da coluna website_index

        return specific_texts #devolve a lista com os valores da coluna website_index

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        # Close MySQL connection
        if db.is_connected():
            cursor.close()
            db.close()

spec=get_website_('website_index')
#for i in spec:
 #   print(i)