import oracledb
import dotenv
import os

oracledb.init_oracle_client(lib_dir=r"C:\Users\klimentt\OneDrive - AMU v Praze\Plocha\instantclient_23_7")

# dotenv must be loaded after Oracle, for Oracle client to even work - it fails with ORA-28759 otherwise.
dotenv.load_dotenv() 

# Nastavení přihlašovacích údajů
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
wallet_password = os.getenv("DB_WALLET_PASSWORD")

wallet_location = r".\Wallet_DEMO"

# Set TNS_ADMIN environment variable to point to the wallet directory
# This is needed for the Oracle client to find the wallet
os.environ["TNS_ADMIN"] = wallet_location

# Připojení přes mTLS (wallet)
connection = oracledb.connect(
    user=user,
    password=password,
    dsn="demo_high",
    wallet_location=wallet_location,
    wallet_password=wallet_password
)

cursor = connection.cursor()

# Výpis z view
cursor.execute("SELECT * FROM v_studenti_kurzy")

for row in cursor:
    print(row)

cursor.close()
connection.close()