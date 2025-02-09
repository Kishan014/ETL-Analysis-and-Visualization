import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='RootingItToTheBottomASAP6!',
    database='your_database'
)

cursor = connection.cursor()

try:
    
    sql_query1 = """
        SELECT
            business,
            jan,
            feb,
            mar
        FROM
            mstr_20
        WHERE
            jan > 10000 OR feb > 10000 OR mar > 10000;
    """
    
   
    cursor.execute(sql_query1)
    
    
    rows1 = cursor.fetchall()
    
  
    print("Results of first query:")
    for row in rows1:
        print(row)
    
   
    sql_query2 = """
        UPDATE
            mstr_20
        SET
            jan = jan * 1.1,
            feb = feb * 1.1
        WHERE
            business = 'SomeBusiness';
    """
    
    
    cursor.execute(sql_query2)
    
    
    connection.commit()
    print("Second query executed successfully. Data updated!")
    
 
    sql_query3 = """
        SELECT
            Business
        FROM
            mstr_20
        WHERE
            JAN > 9000
        LIMIT 1000;
    """
    
    
    cursor.execute(sql_query3)
    
   
    rows3 = cursor.fetchall()
    
   
    print("\nBusinesses where JAN > 9000 (limited to 1000 rows):")
    for row in rows3:
        print(row[0])  

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
 
    cursor.close()
    connection.close()
