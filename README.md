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
  ```

- Alternatively, you can use the setup_env.sh script (Mac/Linux) to automatically set the path to the Oracle Instant Client:

  ```bash
  chmod +x setup_env.sh
  ./setup_env.sh
  ```

### 5. Run SQL Queries

#### Windows

```cmd
# Activate the virtual environment
venv\Scripts\activate

# Run the script with an SQL file
python execute_sql_file.py select_join_table.sql
```

#### Mac/Linux

```bash
# Use the prepared script
chmod +x run_sql.sh
./run_sql.sh select_join_table.sql