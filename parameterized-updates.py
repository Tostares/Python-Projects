import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='employees',
                                         user='root',
                                         password='password')

    cursor = connection.cursor(prepared=True)
    sql_update_query = """UPDATE employees set birth_date = %s where emp_no = %s"""

    data_tuple = ("2024-03-21", 1)
    cursor.execute(sql_update_query, data_tuple)
    connection.commit()
    print("Employee table updated using the prepared statement")

except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
