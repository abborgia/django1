import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# conexion db sqlite3

# SQLITE = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# conexion db MySql

# MYSQL = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'hackathon',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

#  PostgreSQL

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': '1582',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# SQL Server

# SQLSERVER = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'NAME': 'db_almacen',
#         'USER': 'usr_almacen',
#         'PASSWORD': 'mipassword',
#         'HOST': '127.0.0.1',
#         'PORT': '1433',

#         'OPTIONS': {
#             'driver': 'ODBC Driver 13 for SQL Server',
#         },
#     }
# }