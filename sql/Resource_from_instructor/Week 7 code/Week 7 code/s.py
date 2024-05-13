import psycopg2
def selectall():
    conn=None
    try:
        #connect to the postgresql database
        conn=psycopg2.connect(database='test',user='postgres',password='subendu',host='127.0.0.1',port='5433')
        cur=conn.cursor() #create a new cursor
        cur.execute("select * from employee")
        result=cur.fetchall()
        print(result)
        for i in result:
            print(i[0],i[1],i[2])
        cur.close() # close the cursor
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
selectall()
