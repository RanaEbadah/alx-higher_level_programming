#!/usr/bin/python3
import sys
import MySQLdb

arguments = sys.argv
db = MySQLdb.connect(host='localhost', port=3306, user=arguments[1], passwd=arguments[2], db=arguments[3])
cur = db.cursor()

cur.execute("select * from states order by states.id ASC")
states = cur.fetchall()
for state in states:
    print ("(%s , '%s')" % (state[0], state[1]))
