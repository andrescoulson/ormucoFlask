from config import POSTGRES,dbname
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE

try:
    con = psycopg2.connect("dbname="+dbname, user=POSTGRES.get('user'), host=POSTGRES.get('host'), password=POSTGRES.get('pw'))
except:
    print("Error connection")



con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE

cur = con.cursor()
cur.execute("CREATE DATABASE %s  ;" % POSTGRES.get('db'))