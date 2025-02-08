import mysql.connector

connection = mysql.connector.connect(user='root',
      password='RootingItToTheBottomASAP6!',
      host='localhost',
      auth_plugin='mysql_native_password')
                                                                                                                                                                                                      
cursor = connection.cursor()

# Define SQL query to create the MSTR_20 table with Business_ID as primary key
create_table_query = '''
    CREATE TABLE MSTR_20 (
    Business_ID INT NOT NULL,
    Business VARCHAR(100) NOT NULL,
    Jan INT,
    Feb INT,
    Mar INT,
    Apr INT,
    May INT,
    Jun INT,
    Jul INT,
    Aug INT,
    Sep INT,
    Oct INT,
    Nov INT,
    `Dec` INT,  -- Enclose 'Dec' in backticks since it's a reserved keyword
    PRIMARY KEY (Business_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

'''

try:
    # Execute the SQL query to create the table
    cursor.execute(create_table_query)
    print("Table 'MSTR_20' created successfully with Business_ID as primary key!")

except mysql.connector.Error as error:
    print(f"Error creating table: {error}")

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
