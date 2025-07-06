import oracledb
import dotenv
import os
import sys

def initialize_oracle_client():
    """Initialize the Oracle client using the path from environment variables."""
    # Load environment variables from the current working directory
    dotenv.load_dotenv(dotenv_path=os.path.join(os.getcwd(), '.env'))
    
    # Get Oracle client path from environment variables
    oracle_client_path = os.getenv("ORACLE_CLIENT_PATH")
    if not oracle_client_path:
        print("Error: ORACLE_CLIENT_PATH not set in .env file")
        sys.exit(1)
        
    # If the path is relative, make it absolute from the current working directory
    if not os.path.isabs(oracle_client_path):
        oracle_client_path = os.path.abspath(os.path.join(os.getcwd(), oracle_client_path))

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
    # Load environment variables from the current working directory if not already loaded
    dotenv.load_dotenv(dotenv_path=os.path.join(os.getcwd(), '.env'))
    
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
        
        # Get wallet location from environment variables with fallbacks
        # First check for TNS_ADMIN in env, then WALLET_LOCATION, then default to ./Wallet
        wallet_location = os.getenv("TNS_ADMIN") or os.getenv("WALLET_LOCATION") or "./Wallet"
        
        # If the path is relative, make it absolute from the current working directory
        if not os.path.isabs(wallet_location):
            wallet_location = os.path.abspath(os.path.join(os.getcwd(), wallet_location))
        
        # Check if the wallet directory exists
        if not os.path.isdir(wallet_location):
            # Try looking in the Oracle client directory for network/admin
            network_admin_path = os.path.join(oracle_client_path, "network", "admin")
            if os.path.isdir(network_admin_path):
                wallet_location = network_admin_path
            else:
                print(f"Warning: Wallet directory not found at {wallet_location}")
                print(f"Checking if tnsnames.ora exists in {wallet_location}")
        
        # Check if tnsnames.ora exists in the wallet location
        tnsnames_path = os.path.join(wallet_location, "tnsnames.ora")
        if not os.path.isfile(tnsnames_path):
            print(f"Warning: tnsnames.ora not found at {tnsnames_path}")
            print(f"TNS_NAME={tns_name} may not be resolved correctly")
        
        # Set TNS_ADMIN environment variable to point to the wallet directory
        # This is needed for the Oracle client to find the wallet
        os.environ["TNS_ADMIN"] = wallet_location
        print(f"Using TNS_ADMIN: {wallet_location}")
        
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
