import sys
import os
import oracledb
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

# If the path is relative, make it absolute from the current working directory
if not os.path.isabs(sql_file_path):
    sql_file_path = os.path.abspath(os.path.join(os.getcwd(), sql_file_path))

# Read SQL from file
try:
    with open(sql_file_path, 'r') as sql_file:
        sql_query = sql_file.read()
    # Strip trailing semicolons and whitespace that might cause Oracle errors
    #sql_query = sql_query.strip().rstrip(';')
    # Execute the SQL query from file
    cursor.execute(sql_query)
except FileNotFoundError:
    print(f"Error: SQL file '{sql_file_path}' not found")
    sys.exit(1)
except oracledb.DatabaseError as e:
    error_obj, = e.args
    print(f"Oracle Error Code: {error_obj.code}")
    print(f"Oracle Error Message: {error_obj.message}")
    
    # If available, show position of syntax error
    if hasattr(error_obj, 'offset'):
        print(f"Error position: character {error_obj.offset}")
        if error_obj.offset > 0 and error_obj.offset <= len(sql_query):
            # Show the part of the query with the error
            start = max(0, error_obj.offset - 20)
            end = min(len(sql_query), error_obj.offset + 20)
            context = sql_query[start:end]
            pointer = ' ' * (min(20, error_obj.offset - start)) + '^'
            print(f"Context: ...{context}...")
            print(f"         ...{pointer}...")
    
    # Show help URL if available
    error_code = str(error_obj.code)
    print(f"Help: https://docs.oracle.com/error-help/db/ora-{error_code.zfill(5)}/")
    sys.exit(1)
except Exception as e:
    print(f"Error executing SQL: {e}")
    sys.exit(1)

for row in cursor:
    print(row)

cursor.close()
connection.close()