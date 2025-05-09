import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import sys

# Load environment variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASS")

#Print environment variables
print("Using DB credentials:")
print("USER:", DB_USER)
print("HOST:", DB_HOST)
print("PORT:", DB_PORT)
print("NAME:", DB_NAME)

# Set up DB connection string
connection_str = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?sslmode=require"
)
engine = create_engine(connection_str)

# Read DataFrame
df = pd.read_csv('youtube_alex_data_transformed.csv')  

# Table name to write to
table_name = "alex_youtube_data"
schema_name = "Youtube"
# Load DataFrame into PostgreSQL
#df.to_sql(table_name, schema_name, engine, if_exists='replace', index=False)
#print("Data loaded successfully.")

try:
    df = pd.read_csv('youtube_alex_data_transformed.csv')
    table_name = "alex_youtube_data"
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print("✅ Data loaded successfully into table:", table_name)
except Exception as e:
    print("❌ Error loading data into PostgreSQL:", e)
    sys.exit(1)
