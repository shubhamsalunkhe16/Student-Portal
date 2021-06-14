import pymysql as p

def getConnection():
    return p.connect(host='localhost',user='root',password='',database='record')

def insertData(t):
    db=getConnection()
    cr=db.cursor()
    sql='insert into student values(%s,%s,%s,%s,%s,%s,%s)'
    cr.execute(sql,t)
    db.commit()
    db.close()

def selectAllStd():
    db=getConnection()
    cr=db.cursor()
    sql='select * from student'
    cr.execute(sql)
    slist=cr.fetchall()
    db.commit()
    db.close()
    return slist

def deleteData(id):
    db=getConnection()
    cr=db.cursor()
    sql='delete from student where id=%s'
    cr.execute(sql,id)
    db.commit()
    db.close()

def selectStdById(id):
    db=getConnection()
    cr=db.cursor()
    sql='select * from student where id=%s'
    cr.execute(sql,id)
    slist=cr.fetchall()
    db.commit()
    db.close()
    return slist[0]

def updateData(t):
    db=getConnection()
    cr=db.cursor()
    sql='update student set name=%s,schoolname=%s,address=%s,email=%s,phone=%s,password=%s where id=%s'
    cr.execute(sql,t)
    db.commit()
    db.close()

def logIn(email,password):
    db=getConnection()
    cr=db.cursor()
    sql="""select * from `student` where `email` like '{}' and `password` like'{}'""".format(email,password)
    cr.execute(sql)
    users=cr.fetchall()
    db.commit()
    db.close()
    return users

