#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    USR = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]
    db = MySQLdb.connect(host='localhost',
                         user=USR, passwd=PASS, db=DB, port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
