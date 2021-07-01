# Creates and opens a new file named 'logger'
import csv

def create_logfile(filename):
    with open (filename + '.csv', 'w') as file:
        writer = csv.writer(file)

    #file.write('Hello World')

create_logfile('Courtland')


