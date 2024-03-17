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
    stateName = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         user=USR, passwd=PASS, db=DB, port=3306)
    cur = db.cursor()

    cur.execute("""SELECT cities.name
                FROM cities JOIN states ON (cities.state_id = states.id)
                WHERE states.name LIKE %s
                ORDER BY states.id""", ('%' + stateName + '%',))
    rows = cur.fetchall()

    result = ""
    for row in rows:
        result += row[0]
        result += ", "
    result = result[:-2]
    print(result)

    cur.close()
    db.close()
