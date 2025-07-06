# Oracle SQL + Git Walking Skeleton

## Installation Guide

### Requirements

- Python 3.6 or newer
- Oracle Instant Client
- Oracle Wallet files

### 1. Download Oracle Instant Client

#### Windows

- Download Oracle Instant Client from the official Oracle website
- Extract the downloaded ZIP file to a folder (e.g., C:\instantclient_19_8)
- Create an `instantclient` folder in the project root directory and copy the contents of the extracted folder into it

#### Mac

- Download Oracle Instant Client from the official [Oracle website](https://www.oracle.com/database/technologies/instant-client/macos-arm64-downloads.html)
- Extract the downloaded ZIP file to a folder (e.g., /Users/username/Downloads/instantclient_19_8)
- Create an `instantclient` folder in the project root directory and copy the contents of the extracted folder into it

### 2. Download Oracle Wallet

- Log in to the Oracle Cloud Console
- Navigate to the Autonomous Database section
- Select your database
- Click on "DB Connection"
- Click on "Download Wallet"
- Enter a password for the wallet and download the ZIP file
- Extract the downloaded ZIP file to a folder named `Wallet` in the project root directory

### 3. Set Up the Python Environment

#### Windows

- Create a virtual environment

  ```bash
  python -m venv venv
  ```

- Activate the virtual environment

  ```bash
  venv\Scripts\activate
  ```

- Install dependencies

  ```bash
  pip install -r requirements.txt
  ```

#### Mac/Linux

- Create a virtual environment

  ```bash
  python3 -m venv venv
  ```

- Activate the virtual environment

  ```bash
  source venv/bin/activate
  ```

- Install dependencies

  ```bash
  pip install -r requirements.txt
  ```

### 4. Configure the Environment

- Create .env file from .env.example

  ```bash
  # Windows
  copy .env.example .env
  
  # Mac/Linux
  cp .env.example .env
  ```

- Edit the .env file and set the following variables:

  ```bash
  DB_USER="your_username"
  DB_PASSWORD="your_password"
  DB_WALLET_PASSWORD="your_wallet_password"
  ORACLE_CLIENT_PATH="path/to/instantclient"
  WALLET_LOCATION="path/to/wallet"  # Optional, defaults to ./Wallet
  TNS_NAME="your_tns_name"  # e.g., "dbname_high"
  CONNECTION_TYPE="wallet"  # Optional, can be "wallet" or "basic"
  ```
  
  For basic connection (without wallet), you can use these settings instead:
  
  ```bash
  DB_USER="your_username"
  DB_PASSWORD="your_password"
  ORACLE_CLIENT_PATH="path/to/instantclient"
  CONNECTION_TYPE="basic"
  DB_HOSTNAME="your_db_hostname"
  DB_PORT="1521"  # Optional, defaults to 1521
  DB_SERVICE_NAME="your_service_name"
  ```

## Usage

### Run SQL Queries

#### Windows Example

```cmd
# Activate the virtual environment
venv\Scripts\activate

# Run the script with an SQL file
python execute_sql_file.py select_join_table.sql
(1, 'Anna', 'Nováková', 'Databáze')
(1, 'Anna', 'Nováková', 'Statistika')
(2, 'Petr', 'Svoboda', 'Databáze')
```

#### Mac/Linux Example

```bash
# Use the prepared script
chmod +x run_sql.sh
./run_sql.sh select_join_table.sql
(1, 'Anna', 'Nováková', 'Databáze')
(1, 'Anna', 'Nováková', 'Statistika')
(2, 'Petr', 'Svoboda', 'Databáze')
```

### Sync Database Views to Local Files

You can synchronize all views from your Oracle database to local SQL files in a `views` directory:

#### Windows Example

```cmd
# Activate the virtual environment
venv\Scripts\activate

# Run the script to pull all views
python pull_views_to_sql_files.py
Views will be saved to: C:\path\to\project\views
Fetching list of views...
Found 3 views. Extracting DDL for each view...
Processing view: VIEW1
Saved view DDL to: C:\path\to\project\views\view1.sql
...
View extraction complete!
```

#### Mac/Linux Example

```bash
# Activate the virtual environment
source venv/bin/activate

# Run the script to pull all views
python3 pull_views_to_sql_files.py
Views will be saved to: /path/to/project/views
Fetching list of views...
Found 3 views. Extracting DDL for each view...
Processing view: VIEW1
Saved view DDL to: /path/to/project/views/view1.sql
...
View extraction complete!
```

### Running Scripts from Different Directories

All scripts are designed to work from any directory. They will:

1. Load the `.env` file from the current working directory
2. Create output files in the current working directory
3. Automatically resolve paths to the Oracle client and wallet

Example:

```bash
# From a different directory with its own .env file
cd /path/to/another/project
python3 /path/to/oracle-wsk-demo/pull_views_to_sql_files.py
```