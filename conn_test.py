import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=split-server.database.windows.net,1433;'
        'DATABASE=split-DB;'
        'UID=AdminSplitDB;'
        'PWD=WelcomeAdmin@123;'
        'timeout=60;'
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
