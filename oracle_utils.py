import oracledb
import dotenv
import os
import sys

def initialize_oracle_client():
    """Initialize the Oracle client using the path from environment variables."""
    # Load environment variables first
    dotenv.load_dotenv()
    
    # Get Oracle client path from environment variables
    oracle_client_path = os.getenv("ORACLE_CLIENT_PATH")
    if not oracle_client_path:
        print("Error: ORACLE_CLIENT_PATH not set in .env file")
        sys.exit(1)

    # Initialize Oracle client with path from .env
    try:
        oracledb.init_oracle_client(lib_dir=oracle_client_path)
    except Exception as e:
        print(f"Error initializing Oracle client: {e}")
        sys.exit(1)

def get_connection():
    """
    Establish and return a database connection based on the connection type
    specified in environment variables.
    
    Returns:
        oracledb.Connection: An active Oracle database connection
    """
    # Load environment variables if not already loaded
    dotenv.load_dotenv()
    
    # Get connection credentials
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    # Determine connection type from environment variable
    connection_type = os.getenv("CONNECTION_TYPE", "wallet").lower()

    # Establish database connection based on connection type
    if connection_type == "basic":
        # Basic connection using hostname, port, and service name (Oracle SQL Developer style)
        hostname = os.getenv("DB_HOSTNAME")
        port = os.getenv("DB_PORT", "1521")
        service_name = os.getenv("DB_SERVICE_NAME")
        
        # Validate required parameters
        if not hostname or not service_name:
            print("Error: DB_HOSTNAME and DB_SERVICE_NAME must be set for basic connection")
            sys.exit(1)
        
        # Create DSN string in the format: hostname:port/service_name
        dsn = f"{hostname}:{port}/{service_name}"
        
        # Connect using basic connection
        try:
            connection = oracledb.connect(
                user=user,
                password=password,
                dsn=dsn
            )
            return connection
        except Exception as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)
            
    else:  # wallet-based connection
        # Get wallet-specific parameters
        wallet_password = os.getenv("DB_WALLET_PASSWORD")
        tns_name = os.getenv("TNS_NAME")
        
        # Validate required parameters
        if not tns_name:
            print("Error: TNS_NAME must be set for wallet-based connection")
            sys.exit(1)
        
        # Define wallet_location using the correct directory name
        wallet_location = "./Wallet"
        
        # Set TNS_ADMIN environment variable to point to the wallet directory
        # This is needed for the Oracle client to find the wallet
        os.environ["TNS_ADMIN"] = wallet_location
        
        # Connect using wallet
        try:
            connection = oracledb.connect(
                user=user,
                password=password,
                dsn=tns_name,
                wallet_location=wallet_location,
                wallet_password=wallet_password
            )
            return connection
        except Exception as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)
