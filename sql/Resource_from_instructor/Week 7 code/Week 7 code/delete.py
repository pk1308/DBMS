import psycopg2


def deleterecord(num):
    conn=None
    try:
        conn=psycopg2.connect(database='test',user='postgres',password='subendu',host='127.0.0.1',port='5433')
        cur=conn.cursor() #create a new cursor
        cur.execute(''' delete from employee where emp_num=%s''',(num,))
        conn.commit()#commit the changes to the database
        print("record is deleted")
        cur.close()
    except(Exception,psycopg2.DatabaseError)as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()#close the connection
deleterecord(114)