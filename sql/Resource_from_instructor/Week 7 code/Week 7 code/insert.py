import psycopg2
def insertrecord(num,name,dept):
    try:
        conn=None
        #connect to the postgresql database
        conn=psycopg2.connect(database='test',user='postgres',password='subendu',host='127.0.0.1',port='5433')
        cur=conn.cursor()#create a new cursor
        cur.execute(''' insert into employee values(%s,%s,%s)''',(num,name,dept))
        conn.commit()#commit the changes to the database
        print("record is inserted sucesfully")
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
insertrecord(114,'piyus','ME')
