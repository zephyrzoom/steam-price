import MySQLdb

db = MySQLdb.connect(host='localhost',
        user='root',
        passwd='zoom',
        db='steam')
cur = db.cursor()
cur.execute('select * from games')
for row in cur.fetchall():
    print row[0]
db.close()
