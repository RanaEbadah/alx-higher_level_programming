#!/usr/bin/python3
"""script that takes in arguments and displays
all values in the states table of
hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""
import sys
import MySQLdb

if __name__ == "__main__":
    USR = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         user=USR, passwd=PASS, db=DB, port=3306)
    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities JOIN states ON (cities.state_id = states.id)
                ORDER BY states.id""")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
