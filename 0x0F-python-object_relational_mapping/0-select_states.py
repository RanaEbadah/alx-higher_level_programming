#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb


if __name__ == "__main__":
    arguments = sys.argv
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=arguments[1],
        passwd=arguments[2],
        db=arguments[3]
    )
    cur = db.cursor()

    cur.execute("select * from states order by states.id ASC")
    states = cur.fetchall()
    for state in states:
        print("(%s , '%s')" % (state[0], state[1]))
    cur.close()
    db.close()
