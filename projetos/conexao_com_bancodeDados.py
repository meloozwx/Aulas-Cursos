import mysql.connector


conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '543068jl@_()',
    database = 'teste_database'
)

##cursor que enviará comandos para o banco##
cursor = conexao.cursor()

insert = "INSERT INTO informacao (id, nome, idade) VALUES (%s, %s, %s)"
sql = (1, "João", 25)

cursor.execute(insert, sql)
conexao.commit()

cursor.close()   
conexao.close()