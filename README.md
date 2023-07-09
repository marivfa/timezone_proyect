# Timezone Data Project

This project queries the TimezoneDB API to retrieve timezone data and populates the database with the obtained information. It consists of a Python script that interacts with the API, handles errors, and stores the data in the database.

## Features

- Retrieves timezone data from the TimezoneDB API
- Populates the `TZDB_TIMEZONES` and `TZDB_ZONE_DETAILS` tables in the database
- Handles errors during API retrieval and logs them in the `TZDB_ERROR_LOG` table

## Prerequisites

- Python 3.10.6
- pip install SQLAlchemy
- pip install mysql-connector-python
- pip install mysqlclient
- MySQL database

## Installation

1. Clone the repository:

```bash
git clone https://github.com/marivfa/timezone_proyect.git
```

2. Change into the project directory:
   cd timezone

3. Install the required dependencies
   pip install -r requirements.txt

## Configuration

    Update the .env file with your TimezoneDB API key and database connection details.

## Usage

    Run the script to populate the database:
        python main.py

    The script will query the TimezoneDB API, retrieve timezone data, and populate the TZDB_TIMEZONES and TZDB_ZONE_DETAILS tables in the database.

## Unit Test

     python -m unittest tests.test_api_client
