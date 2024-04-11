import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



# Path to the CSV file
data_path = "../data/newmont_golden_ridge_dataset.csv"

# load database configurations
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host_name = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")


# Database connection string
connection_string = f"mysql+mysqlconnector://{username}:{password}@{host_name}:{port}/{database}"

# Create database engine
engine = create_engine(connection_string, echo=True)

# Read CSV file
df = pd.read_csv(data_path)

# Data Transformation
# Transform data (drop NaN values)
df_cleaned = df.dropna()

# Drop Duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Define table name
table_name = "newmont_golden_ridge_dataset"

# Insert data into MySQL database table
df_cleaned.to_sql(table_name, engine, index=False)
