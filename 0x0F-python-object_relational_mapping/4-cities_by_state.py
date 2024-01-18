#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    username, passwd, db_name = sys.argv[1:4]

    query = """SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
    """
    conn = MySQLdb.connect(
        user=username, passwd=passwd, db=db_name, host="localhost", port=3306
    )
    cursor = conn.cursor()
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()
