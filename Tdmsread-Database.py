import numpy as np
import json
from nptdms import TdmsFile
from nptdms import tdms
import psycopg2
from datetime import datetime
from psycopg2.extensions import register_adapter, AsIs
import time as dt

def addapt_numpy_array(numpy_array):
    return AsIs(tuple(numpy_array))
register_adapter(np.ndarray, addapt_numpy_array)

tdms_file = TdmsFile.read("fft2.tdms")
group = tdms_file["Data"]
group2 = tdms_file["Info"]
data=group.as_dataframe();
data2=group2.as_dataframe();
#data2['fft'] =[np.asarray(data2['Channel ' + str(i+1)]) for i in range(8)];
ch = group2['date'];





conn = psycopg2.connect(
    host="localhost",
    database="masoud",
    user="postgres",
    password="password",
    port="5432"
    )
cursor = conn.cursor()
# Print PostgreSQL Connection properties
print ( conn.get_dsn_parameters(),"\n")
# Print PostgreSQL version
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")


create_table_query = '''CREATE TABLE IF NOT EXISTS test25
          (date varchar,
          time varchar,
          kks varchar , 
          description varchar,
          unit varchar,
          fft_values json,
          f_0  integer,
          df  integer); '''
          
           
           
cursor.execute(create_table_query)
conn.commit()
print("Table created successfully in PostgreSQL ")

a=34;
date=group2['date'].data[0];
time=group2['time'].data[0];
ddd=(group2['kks'].data)
for i in range(len(group2['kks'].data)) :
    kks=group2['kks'].data[i];
    description=group2['description'].data[i];
    unit=group2['unit'].data[i];
    fft_values = json.dumps(list(group['Channel '+str(i+1)].data))
#    fft_values=str(list(group['Channel '+str(i+1)].data));
    f_0=group2['f_0'].data[i];
    df=group2['df'].data[i];
    gt=str(list([5,6]));
    write_data='''INSERT INTO test25
    (date,time, kks, description, unit,fft_values, f_0, df) 
    VALUES ('{}','{}','{}','{}','{}','{}',{},{})'''.format(date,time, kks, description, unit,fft_values, f_0, df);
    write_data2='''INSERT INTO test25
    (fft_values) VALUES ('{}')'''.format(fft_values)

    cursor.execute(write_data)
    #cursor.execute(write_data2)
    conn.commit()
    print("Table created successfully in PostgreSQL ")
#INSERT INTO TABLE_NAME (column1, column2, column3,...columnN)
#VALUES (value1, value2, value3,...valueN);















