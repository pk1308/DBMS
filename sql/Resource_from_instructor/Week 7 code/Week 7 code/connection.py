import psycopg2
conn=None
try:
    conn=psycopg2.connect(database='test',user='postgres',password='subendu',host='127.0.0.1',port='5433')
    print("Database connected succesfully")
    print(conn)
except(Exception,psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()