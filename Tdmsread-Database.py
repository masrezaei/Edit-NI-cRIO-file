import numpy as np
from nptdms import TdmsFile
from nptdms import tdms
import psycopg2



tdms_file = TdmsFile.read("fft2.tdms")
group = tdms_file["Data"]
data=group.as_dataframe();


conn = psycopg2.connect(
    host="localhost",
    database="test1",
    user="postgres",
    password="Password",
    port="5432"
    )
cursor = conn.cursor()
# Print PostgreSQL Connection properties
print ( conn.get_dsn_parameters(),"\n")
# Print PostgreSQL version
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")


create_table_query = '''CREATE TABLE IF NOT EXISTS ffttest4
          (date varchar,
          time varchar(1000),
          kks varchar(1000),
          description varchar(1000),
          unit varchar(1000),
          fft_values json,
          f_0 integer,
          df integer); '''
          
           
           
cursor.execute(create_table_query)
conn.commit()
print("Table created successfully in PostgreSQL ")