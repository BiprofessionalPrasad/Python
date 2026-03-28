import pandas as pd
import psycopg as py
# open database connection (insert your own values here)
conn = py.connect("dbname=postgres user=postgres password=gaitonde port=5432")
cr = conn.cursor()
 
# retrieve data from SQL query
cr.execute("SELECT * FROM sales WHERE sdate = '01-03-2024'")
tuples = cr.fetchall()

# retrieve column headers to pass to Pandas
column_hdrs= [d[0] for d in cr.description]
df = pd.DataFrame(tuples, columns=column_hdrs)
 
# write retrieved data to Parquet. Specified path must exist.
df.to_parquet('C:\\Temp', partition_cols='sdate', existing_data_behavior='delete_matching')
