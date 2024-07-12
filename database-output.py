#Needs to have python3 and pymsql installed with pip
import pymysql 

#function to connect to your database
def mysqlconnect(): 
    # To connect MySQL database 
    conn = pymysql.connect( 
        host='localhost', 
        user='root',  
        password = "pass", 
        db='employees', 
        ) 
      
    cur = conn.cursor() 
      
    # Select the query you want to show in the console, here: departments
    cur.execute("select * from departments") 
    output = cur.fetchall() 
      
    for i in output: 
        print(i) 
      
    # To close the connection 
    conn.close() 
  
# Driver Code 
if __name__ == "__main__" : 
    mysqlconnect()
