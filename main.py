#!/bin/python


import csv;


class Node:

	def __init__(self, csv_data ):
		'convert from DictReader to List'
		headers = csv_data.fieldnames

		self.dataset = {}
		for columns in csv_data:
			for header in headers:
				row = columns[header]
				print("[%s]" %(header))
				print(row)
				
		#print(self.dataset)



def read_csv_file( filename ):
	csv_file = open(filename);
	csv_data = csv.DictReader( csv_file );

	#print(csv_data.fieldnames
	return csv_data


csv_data = read_csv_file( "dataset/Users.csv" )


node = Node( csv_data )
