# Newmont Golden Ridge Data Pipeline
## Project Description
This is the fourth assignment of the Trestle Academy Data Engineering Graduate Trainee Program aimed at understanding the club hundred companies in Ghana and applying knowledge in an ETL data pipeline to build a pipeline for Newmont Golden Ridge the company in review.

## Overview
The Newmont Golden Ridge Data Pipeline project aims to generate a dataset of 100,000 records using the Faker library and build a pipeline to ingest this data from a CSV file into a MySQL database. Additionally, it provides scripts for performing analytical queries on the ingested data for further analysis.

## Features
- Generates synthetic demographic, equipment, safety, transaction activity, customer preferences, and communication methods data using the Faker library.
- Saves the generated data to a CSV file (`newmont_golden_ridge_dataset.csv`).
- Builds a data pipeline to ingest the generated CSV data into a MySQL database.
- Performs data transformation, including dropping NaN values and duplicates, before inserting the data into the database.
- Provides analytical queries for extracting insights from the ingested data.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python (version 3.6 or higher)
- pandas library
- SQLAlchemy library
- Faker library
- MySQL database server

## Getting Started
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/adubrightkwartengsnr/ETL_Pipeline_MySQL.git 
    ```

2. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have a MySQL database server set up and running. Update the database configurations in the `.env` file with your MySQL database details:

    ```
    DB_DATABASE=your_database_name
    DB_USERNAME=your_username
    DB_PASSWORD=your_password
    DB_HOST=your_host
    ```

4. Run the data generation script to create the synthetic dataset:

    ```bash
    python faker_data_generator.py
    ```

5. After the CSV file `newmont_golden_ridge_dataset.csv` is generated, run the pipeline script to ingest the data into the MySQL database:

    ```bash
    python pipeline.py
    ```

6. Once the data is ingested into the database, you can run analytical queries to extract insights from the data.

## Project Structure
The project structure is organized as follows:
- `faker_data_generator.py`: Python script to generate synthetic data using the Faker library and save it to a CSV file.
- `data_analysis.ipynb`: Jupyter Notebook File containing all the analysis questions.
- `pipeline.py`: Python script to ingest data from the CSV file into a MySQL database.
- `newmont_golden_ridge_dataset.csv`: Generated synthetic dataset in CSV format.
- `.env`: Environment variables file containing database configurations.
- `README.md`: Detailed instructions on how to run the project.

## Credits
I would like to extend my sincere appreciation to the following individuals and organizations for their support and contributions to this project:
- **Trestle Academy Ghana**: Our official training academy.
- **INNGEN Technology Solutions**: Sponsor and partnering company
- **Derek Degbedzui**: Lead Data Engineering trainer at Trestle Academy Ghana.
- **Theophilus Akugre**: Trainer at Trestle Academy Ghana.

## Contributing
Contributions to this project are welcome! Feel free to submit bug reports, feature requests, or pull requests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Owner
Bright Kwarteng Senior Adu
