# This week we will create a program that performs file processing activities.
# Your program this week will use the OS library in order to validate that a directory
# exists before creating a file in that directory.
# Your program will prompt the user for the directory they would like
# to save the file in as well as the name of the file.
# The program should then prompt the user for their name, address, and phone number.
# Your program will write this data to a comma separated line in a file and store
# the file in the directory specified by the user. 
# Once the data has been written your program should read the file you
# just wrote to the file system and display the file contents to the user for validation purposes.

import os
import csv

user_filepath = input('Where would you like to store the file?')
user_filename = input('What would you like to name the file?')
full_filepath_filename = user_filepath + user_filename
user_name = input('What is your name? ')
user_address = input('What is your address? ')
user_phone = input('What is your phone number? ')

with open(user_filename, mode='a') as user_filename:
    fieldnames = ['Name', 'Address', 'Phone']
    user_writer = csv.DictWriter(user_filename, fieldnames=fieldnames)
    user_writer.writeheader()
    user_writer = csv.writer(user_filename, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    user_writer.writerow([user_name, user_address, user_phone])

print("Your information has been save in: ", full_filepath_filename)

with open(full_filepath_filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["Name"]} lives at {row["Address"]} and their number is {row["Phone"]}.')
        line_count += 1

