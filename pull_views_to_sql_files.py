import os
import sys
import pathlib
from oracle_utils import initialize_oracle_client, get_connection

# Initialize Oracle client
initialize_oracle_client()

# Get database connection
connection = get_connection()

# Create views directory if it doesn't exist
views_dir = os.path.join(os.getcwd(), "views")
pathlib.Path(views_dir).mkdir(exist_ok=True)
print(f"Views will be saved to: {views_dir}")

# Create a cursor
cursor = connection.cursor()

try:
    # Query to get all user views
    print("Fetching list of views...")
    cursor.execute("""
        SELECT view_name 
        FROM user_views 
        ORDER BY view_name
    """)
    
    views = cursor.fetchall()
    
    if not views:
        print("No views found in the database.")
        sys.exit(0)
    
    print(f"Found {len(views)} views. Extracting DDL for each view...")
    
    # For each view, get its DDL and save to a file
    for view_tuple in views:
        view_name = view_tuple[0]
        print(f"Processing view: {view_name}")
        
        # Query to get the DDL for the view
        cursor.execute("""
            SELECT DBMS_METADATA.GET_DDL('VIEW', :view_name) 
            FROM dual
        """, view_name=view_name)
        
        result = cursor.fetchone()
        if result and result[0]:
            view_ddl = result[0].read()  # CLOB to string
            
            # Create file path
            file_path = os.path.join(views_dir, f"{view_name.lower()}.sql")
            
            # Write DDL to file
            with open(file_path, 'w') as f:
                f.write(view_ddl)
            
            print(f"Saved view DDL to: {file_path}")
        else:
            print(f"Could not retrieve DDL for view: {view_name}")
    
    print("View extraction complete!")

except Exception as e:
    print(f"Error extracting views: {e}")
    sys.exit(1)
finally:
    cursor.close()
    connection.close()
    print("Database connection closed.")
