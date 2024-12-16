import json
import pyodbc

# Load database credentials from config.json
def load_db_config():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("Configuration file not found. Ensure 'config.json' exists.")

# Azure SQL Database Connection Function
def create_connection():
    try:
        # Load database configuration
        config = load_db_config()
        
        # Extract credentials from the loaded JSON
        server = config["DB_SERVER"]
        database = config["DB_NAME"]
        username = config["DB_USER"]
        password = config["DB_PASSWORD"]
        
        # Establish the connection dynamically using the loaded variables
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server},1433;'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password};'
        )
        return conn
    except Exception as e:
        raise ConnectionError(f"Database connection error: {e}")
