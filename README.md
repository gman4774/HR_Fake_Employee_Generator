# Python script for generating a report from CSV files

## Prerequisites

* Python 3.x

## Required Libraries

* sys
* csv
* argparse

## Usage

The script can be executed with the following command:

python report.py -t <teammap_file_path> -p <productmaster_file_path> -s <sales_file_path> --team-report <teamreport_file_path> --product-report <productreport_file_path>

## Command-line arguments

The script accepts the following command-line arguments:

* -t: The file path for the team mapping CSV file.
* -p: The file path for the product master CSV file.
* -s: The file path for the sales CSV file.
* --team-report: The file path for the team report CSV file to be generated.
* --product-report: The file path for the product report CSV file to be generated.

## Code Overview

1. Parse command-line arguments using argparse.
2. Verify all user input is CSV file format.
3. Create empty dictionaries for teams and products.
4. Read the team mapping CSV file and add the team names and initial gross revenue values to the teams dictionary.
5. Read the product master CSV file and add the product names, prices, and lot sizes values to the products dictionary.
6. Create an empty product report dictionary with product IDs as keys and product names, gross revenues, total units sold, and discount costs as values.
7. Read the sales CSV file and update the teams and product report dictionaries with sales data.
8. Sort the teams dictionary by gross revenue in descending order and create a list of tuples for the team report.
9. Sort the product report dictionary by gross revenue in descending order and create a list of tuples for the product report.
10. Write the team report to a CSV file.
11. Write the product report to a CSV file.

