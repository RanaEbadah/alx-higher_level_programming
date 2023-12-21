#!/usr/bin/python3
""" lists all cities of that state, using the database hbtn_0e_4_usa"""
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

    cur.execute("""SELECT c.id, c.name, s.name FROM cities c inner
                 join states s on c.state_id = s.id order by c.id""")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
