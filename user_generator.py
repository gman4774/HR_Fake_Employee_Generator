from faker import Faker
import pandas as pd
import us
from timezonefinder import TimezoneFinder
import datetime
import random


fake = Faker(['en_us'])

years = 5
date_list = pd.date_range(start='1-1-2018', end='1-1-2023', freq='M')

employee_df = pd.DataFrame(columns = ['ID', 'Last Name', 'First Name', 'Date of Birth', 'Address', 'City', 'State', 'Country', 'Zip Code', 'Time Zone', 'Gender', 'Phone Number', 'SSN', 'Username', 'Company Email', 'Personal Email', 'Date Added', 'Date Removed', 'Removal Reason'], index = [0])
former_employee_df = employee_df.copy()

# generate remove list
reason_to_remove = pd.read_csv('reason.csv')

obj = TimezoneFinder()

employee_id_count = 0
for date in date_list:
	#adding new employees
	users_to_generate = random.randint(0,18)
	for i in range(0,users_to_generate):
		employee_id_count += 1
		while True:
			try:
				current_employee = fake.profile()
				state = str(current_employee['residence'].split('\n')[1].split(',')[1].split(' ')[1])
				if len(us.states.lookup(state).time_zones) > 1:
					tz = us.states.lookup(state).time_zones[0]
				else:
					tz = us.states.lookup(state).time_zones
				employee_df.loc[employee_id_count, 'ID'] = str(employee_id_count)
				employee_df.loc[employee_id_count, 'Last Name'] = current_employee['name'].split(' ')[1]
				employee_df.loc[employee_id_count, 'First Name'] = current_employee['name'].split(' ')[0]
				employee_df.loc[employee_id_count, 'Date of Birth'] = current_employee['birthdate']
				employee_df.loc[employee_id_count, 'Address'] = current_employee['residence'].split('\n')[0]
				employee_df.loc[employee_id_count, 'City'] = current_employee['residence'].split('\n')[1].split(',')[0]
				employee_df.loc[employee_id_count, 'State'] = state
				employee_df.loc[employee_id_count, 'Country'] = 'USA'
				employee_df.loc[employee_id_count, 'Zip Code'] = current_employee['residence'].split('\n')[1].split(',')[1].split(' ')[2]
				employee_df.loc[employee_id_count, 'Time Zone'] = tz
				employee_df.loc[employee_id_count, 'Gender'] = current_employee['sex']
				employee_df.loc[employee_id_count, 'Phone Number'] = fake.phone_number()
				employee_df.loc[employee_id_count, 'SSN'] = current_employee['ssn']
				employee_df.loc[employee_id_count, 'Username'] = current_employee['name'].split(' ')[0][0] + current_employee['name'].split(' ')[1][-3:] + str(employee_id_count)#first initial, last three last name and ID
				employee_df.loc[employee_id_count, 'Company Email'] = current_employee['name'].split(' ')[0][0] + current_employee['name'].split(' ')[1][-3:] + str(employee_id_count) + '@NotaFakeCompany.com'
				employee_df.loc[employee_id_count, 'Personal Email'] = current_employee['mail']
				employee_df.loc[employee_id_count, 'Date Added'] = date #hiring date
				break
			except:
				pass
	for index, row in employee_df.iterrows():
		flip = random.randint(0, 90)
		if flip != 0:
			pass
		else:
			former_employee_df.loc[index] = row
			former_employee_df.loc[index, 'Date Removed'] = date
			reason_num = random.randint(0,len(reason_to_remove.index) - 1)
			former_employee_df.loc[index, 'Removal Reason'] = reason_to_remove.iloc[reason_num][0]
			employee_df.drop([index], inplace=True)
			

cur = employee_df.index
form = former_employee_df.index

#export current employees CSV
employee_df.to_csv('current_employees.csv')
#export former employees CSV
former_employee_df.to_csv('former_employees.csv')














# 
