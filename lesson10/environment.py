import os
from dotenv import load_dotenv

load_dotenv()

database_name = os.getenv("DB_NAME")
database_user = os.getenv("DB_USER")
database_host = os.getenv("DB_HOST")

print("Database:", database_name)
print("User:", database_user)
print("Host:", database_host)