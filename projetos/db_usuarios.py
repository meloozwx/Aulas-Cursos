class Database:
    def db():

        import mysql.connector

        connect = mysql.connector.connect(
            host = "localhost",
            user = "root" ,
            password = "543068jl@_()",
            database = "cadastro"
        )

        cursor = connect.cursor()

