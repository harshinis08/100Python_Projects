import MySQLdb

try:
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        password='FlaskPractice123!!',
        db='flask_database'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print(f"Database version : {data}")
    cursor.close()
    connection.close()
except MySQLdb.Error as e:
    print(f"Error: {e}")
