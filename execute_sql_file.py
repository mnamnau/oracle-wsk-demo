import sys
import os
from oracle_utils import initialize_oracle_client, get_connection

# Initialize Oracle client
initialize_oracle_client()

# Get database connection
connection = get_connection()

cursor = connection.cursor()

# Check if SQL file path is provided as argument
if len(sys.argv) < 2:
    print("Error: Please provide the SQL file path as an argument")
    print("Usage: python exute_sql_file.py <sql_file_path>")
    sys.exit(1)

# Get SQL file path from command line arguments
sql_file_path = sys.argv[1]

# Read SQL from file
try:
    with open(sql_file_path, 'r') as sql_file:
        sql_query = sql_file.read()
    # Strip trailing semicolons and whitespace that might cause Oracle errors
    sql_query = sql_query.strip().rstrip(';')
    # Execute the SQL query from file
    cursor.execute(sql_query)
except FileNotFoundError:
    print(f"Error: SQL file '{sql_file_path}' not found")
    sys.exit(1)
except Exception as e:
    print(f"Error executing SQL: {e}")
    sys.exit(1)

for row in cursor:
    print(row)

cursor.close()
connection.close()