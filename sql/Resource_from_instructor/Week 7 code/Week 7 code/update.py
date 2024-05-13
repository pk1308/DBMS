import psycopg2
def updaterecord(num,dept):
    conn=None
    try:
        #connect to the postgresql database
        conn=psycopg2.connect(database='test',user='postgres',password='subendu',host='127.0.0.1',port='5433')
        cur=conn.cursor()#create a new cursor
        cur.execute("update employee set department=%s where emp_num=%s",(dept,num))
        conn.commit()
        print("Record is updated")
        cur.close()#close the cursor
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
updaterecord(113,'IT')