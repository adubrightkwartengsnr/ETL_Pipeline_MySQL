from faker import Faker
import pandas as pd
import numpy as np
import random

fake = Faker()

# Generate demographic data
def generate_demographics():
    employee_name = fake.name()
    employee_address = fake.address()
    department = random.choice(['Mining', 'Safety', 'Maintenance'])
    job_title = random.choice(['Supervisor', 'Technician', 'Operator'])
    location = random.choice(['Pit', 'Plant', 'Office'])
    date_of_birth = fake.date_of_birth()
    current_date = pd.Timestamp.today().date()
    age = current_date.year - date_of_birth.year - ((current_date.month, current_date.day) < (date_of_birth.month, date_of_birth.day))
    salary =  round(np.random.uniform(100000, 1000000), 2)
    return employee_name,employee_address,department,job_title,location,date_of_birth,age,salary

# Generate equipment and safety data
def generate_equipment_safety_activity():
    equipment_id = fake.uuid4().split('-')[0]
    equipment_type = random.choice(['Excavator', 'Dump Truck', 'Drill Rig'])
    equipment_status = random.choice(['Operational', 'Under Maintenance', 'Out of Service'])
    maintenance_cost = round(np.random.uniform(1000, 10000), 2)
    safety_incident = random.choice(['Yes', 'No'])
    environmental_incident = random.choice(['Yes', 'No'])
    community_relations = random.choice(['Good', 'Fair', 'Poor'])
    return equipment_id,equipment_type,equipment_status,maintenance_cost,safety_incident,environmental_incident,community_relations

# Generate transaction activity
def generate_transaction_activity():
    transaction_date = fake.date_between(start_date='-1y', end_date='today')
    gold_price = round(np.random.uniform(1500, 2000), 2)
    production_tonnage = round(np.random.uniform(100, 1000), 2)
    production_cost = round(np.random.uniform(100000, 500000), 2)
    revenue = round(production_tonnage * gold_price, 2)
    profit = round(revenue - production_cost, 2)
    amount = round(random.uniform(10, 1000), 2)
    return transaction_date, amount,profit,gold_price,production_tonnage,production_cost,revenue

# Generate customer preferences
def generate_customer_preferences():
    preferred_app = random.choice(['iOS App', 'Android App'])
    preferred_website = random.choice(['Yes', 'No'])
    return preferred_app, preferred_website

# Generate communication methods
def generate_communication_methods():
    email = fake.email()
    return email

# Generate data for Newmont Golden Ridge Ltd
def generate_newmont_data(num_records):
    data = []
    for i in range(num_records):
        demographics = generate_demographics()
        equipment_and_safety = generate_equipment_safety_activity()
        transaction_activity = generate_transaction_activity()
        customer_preferences = generate_customer_preferences()
        communication_methods = generate_communication_methods()

        record = {
            'Name': demographics[0],
            'Address': demographics[1],
            'Department':demographics[2],
            'Job Title':demographics[3],
            'Location':demographics[4],
            'Date Of Birth':demographics[5],
            'Age':demographics[6],
            'Salary':demographics[7],
            'Equipment Id':equipment_and_safety[0],
            'Equipment Type':equipment_and_safety[1],
            'Equipment Status':equipment_and_safety[2],
            'Maintenance Cost':equipment_and_safety[3],
            'Safety Incident':equipment_and_safety[4],
            'Environmental Incident':equipment_and_safety[5],
            'Community Relations':equipment_and_safety[6],
            'Transaction Date': transaction_activity[0],
            'Transaction Amount': transaction_activity[1],
            'Profit':transaction_activity[2],
            'Gold Price':transaction_activity[3],
            'Production Tonnage':transaction_activity[4],
            'Production Cost':transaction_activity[5],
            'Revenue':transaction_activity[6],
            'Preferred App': customer_preferences[0],
            'Preferred Website': customer_preferences[1],
            'Email': communication_methods
        }
        data.append(record)
    return data

# Generate 100,000 records for Newmont Golden Ridge Ltd
num_records = 100000
newmont_data = generate_newmont_data(num_records)

# Create DataFrame
columns= ['Name', 'Address', 'Department', 'Job Title', 'Location', 
 'Date Of Birth', 'Age', 'Salary', 'Equipment Id', 'Equipment Type',
   'Equipment Status', 'Maintenance Cost', 'Safety Incident', 'Environmental Incident', 
   'Community Relations', 'Transaction Date', 'Transaction Amount', 'Profit', 'Gold Price', 
   'Production Tonnage', 'Production Cost', 'Revenue', 'Preferred App', 'Preferred Website', 'Email']

df = pd.DataFrame(newmont_data, columns=columns)
# convert data to CSV
df.to_csv('newmont_golden_ridge_dataset.csv', index=False)