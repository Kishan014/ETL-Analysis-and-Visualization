import csv
import mysql.connector
from mysql.connector import Error

# Establish MySQL connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='RootingItToTheBottomASAP6!',
    database='your_database'
)

cursor = connection.cursor()

# Path to your CSV file
csv_file_path = r'C:\Users\Kishan\Documents\MSTR_2020.csv'

def convert_to_int(value):
    """Convert string value to integer, handling NULL and comma-formatted numbers"""
    if value and value.upper() != 'NULL':
        return int(value.replace(',', ''))
    return None

try:
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Prepare the REPLACE INTO query
        replace_query = """
            REPLACE INTO mstr_20 (
                Business_ID, Business, Jan, Feb, Mar, Apr, May, Jun,
                Jul, Aug, Sep, Oct, Nov, `Dec`
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """
        
        # Process each row
        for row in reader:
            values = (
                int(row['Business_ID']),
                row['Business'],
                convert_to_int(row['Jan']),
                convert_to_int(row['Feb']),
                convert_to_int(row['Mar']),
                convert_to_int(row['Apr']),
                convert_to_int(row['May']),
                convert_to_int(row['Jun']),
                convert_to_int(row['Jul']),
                convert_to_int(row['Aug']),
                convert_to_int(row['Sep']),
                convert_to_int(row['Oct']),
                convert_to_int(row['Nov']),
                convert_to_int(row['Dec'])
            )
            
            cursor.execute(replace_query, values)
        
        # Commit all changes
        connection.commit()
        print("Data successfully imported!")

except FileNotFoundError:
    print(f"Error: CSV file not found at path '{csv_file_path}'")
except Error as error:
    print(f"Database error: {error}")
    if connection.is_connected():
        connection.rollback()
except Exception as error:
    print(f"Error: {error}")
    if connection.is_connected():
        connection.rollback()
finally:
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")
