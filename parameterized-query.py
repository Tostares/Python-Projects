import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='employees',
                                         user='root',
                                         password='password')

    cursor = connection.cursor(prepared=True)
    # Parameterized query
    sql_insert_query = """ INSERT INTO employees
                       (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES (%s,%s,%s,%s,%s,%s)"""
    # tuple to insert at placeholder
    tuple1 = (1, "2019-03-23", "MYKILL", "FENBIES", "F", "2020-03-23")
    tuple2 = (2, "2019-05-19", "why", "GENDER", "M", "2021-03-2")

    cursor.execute(sql_insert_query, tuple1)
    cursor.execute(sql_insert_query, tuple2)
    connection.commit()
    print("Data inserted successfully into employee table using the prepared statement")

except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")