#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa
where name matches the argument."""
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

    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cur.execute(query, (arguments[4],))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
