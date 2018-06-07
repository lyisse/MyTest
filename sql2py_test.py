import pymysql
db = pymysql.connect(host='localhost',user='root',password='',
                     db='mysql',port='6689',charset='utf8')
cur = db.cursor()

update_sql ="select * from user_score;"

try:
    cur.execute(update_sql)
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()