#!/usr/bin/env python3

import sys
import csv
import argparse


def main():
	# Define the command-line arguments using the argparse module
	parser  = argparse.ArgumentParser()
	parser.add_argument('-t', dest = 'teammap', type=str, help = 'file path for team mapping CSV', required=True)
	parser.add_argument('-p', dest = 'productmaster', type=str, help = 'file path for product master CSV', required=True)
	parser.add_argument('-s', dest = 'sales', type=str, help = 'file path for sales CSV', required=True)
	parser.add_argument('--team-report', dest = 'teamreport', type=str, help = 'file path for exporting team report CSV', required=True)
	parser.add_argument('--product-report', dest = 'productreport', type=str, help = 'file path for exporting product report CSV', required=True)
	args = parser.parse_args()

	# Quick verification to make sure all files are CSV format. If not, error displays incorrect user input
	for a in vars(args):
		if getattr(args, a)[-4:].lower() != '.csv':
			print('All files must be CSV format verify your input and try again')
			print('Failed input: ' + getattr(args, a))
			quit()


	# Initialize dictionaries to store teams and products data
	teams = {}
	products = {}

	# Open and read the team mapping CSV file, then populate the 'teams' dictionary
	with open(args.teammap, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			# Assign the team name and an initial gross revenue of 0 to the corresponding team ID
			teams[row['TeamId']] = row['Name'], float(0)

	# Open and read the product master CSV file, then populate the 'products' dictionary
	with open(args.productmaster, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			# Assign the product name, price, and lot size to the corresponding product ID
			products[row[0]] = row[1], float(row[2]), int(row[3])

	#Initialize a dictionary to store product report data
	productreport = {}

	# Populate the 'productreport' dictionary with product data and initial values of 0
	for product in products:
		# Assign the product name, and initial value of 0 for 'GrossRevenue', 'TotalUnits', 'DiscountCost'
		productreport[product] = products[product][0], float(0), int(0), float(0)


	# Open and read the sales CSV file, then update the 'teams' and 'productreport' dictionaries accordingly
	with open(args.sales, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			# Extract data from the row
			lotssold = int(row[3])
			discount = float(row[4])
			teamid = row[2]
			teamname = teams[teamid][0]
			productid = row[1]
			productprice = float(products[productid][1])
			productlotsize = int(products[productid][2])
			productupdatedgross = productreport[productid][1] + ((lotssold * productlotsize) * productprice)
			producttotalunits = productreport[productid][2] + (lotssold * productlotsize)
			productdiscountcost = productreport[productid][3] + discount
			teamupdatedgross = ((teams[teamid][1]) + ((lotssold * productlotsize) * productprice))
			# Update 'teams' and 'productreport' dictionaries with updated sales data
			teams[teamid] = teamname, teamupdatedgross
			productreport[productid] = products[productid][0], productupdatedgross, producttotalunits, productdiscountcost 


	# Sort the team and product report data in descending order by gross revenue
	sortedteamreport = []
	for team in teams:
		sortedteamreport.append((teams[team][0], teams[team][1]))
	sortedteamreport = sorted(sortedteamreport, key = lambda x: x[1], reverse = True)

	sortedproductreport = []
	for s in productreport:
		sortedproductreport.append((productreport[s][0], productreport[s][1], productreport[s][2], productreport[s][3]))
	sortedproductreport = sorted(sortedproductreport, key = lambda x: x[1], reverse = True)


	# Write the team and product report to CSV files
	with open(args.teamreport, 'w') as file:
		writer = csv.writer(file)
		writer.writerow(('Team', 'GrossRevenue'))
		for x in sortedteamreport:
			writer.writerow(x)

	with open(args.productreport, 'w') as file:
		writer = csv.writer(file)
		writer.writerow(('Name', 'GrossRevenue', 'TotalUnits', 'DiscountCost'))
		for x in sortedproductreport:
			writer.writerow(x)



if __name__ == '__main__':
	main()
