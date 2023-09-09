# Employee Data Generator

This Python script generates employee data for a fictitious company. It utilizes the Faker library to create random employee profiles and pandas for data manipulation. The generated data includes employee details such as name, address, date of birth, contact information, and more. Additionally, it simulates employees leaving the company and logs their departure reasons.
### Table of Contents

    Installation
    Usage
    Features


## Installation
Clone the repository or download the script.
```bash
git clone https://github.com/your-username/employee-data-generator.git
```
Install the required Python libraries using pip.
```bash
pip install faker pandas us timezonefinder
```
Prepare a CSV file named 'reason.csv' with removal reasons to be used in the script.

## Usage
Run the Python script.
```bash
python employee_data_generator.py
```

The script generates two CSV files:
* current_employees.csv: Contains the data of current employees.
* former_employees.csv: Contains the data of former employees, including their removal reasons and departure dates.

## Features
Generates random employee profiles, including personal and contact details.
Simulates employees leaving the company and logs reasons for departure.
Supports generating employees in multiple states and time zones within the USA.
## Use in Tableau dashboard
This data was generated, cleaned and used to create an HR dashboard in Tableau which can be viewed here: https://public.tableau.com/app/profile/grzegorz.furmanski5996/viz/TurnoverDashboard_16928136278190/Dashboard1
