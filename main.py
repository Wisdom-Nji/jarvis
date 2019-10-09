#!/bin/python


import csv;


class Node:
	def __init__(self, data):
		self.data = data;


class Nodes:

	def __init__(self, csv_data ):
		'convert from DictReader to List'
		headers = csv_data.fieldnames

		self.dataset = {}
		for header in headers:
			self.dataset[header] = []
		for columns in csv_data:
			for header in headers:
				entire_row = columns[header]
				for column in entire_row:
					self.dataset[header].append(Node(column))
				
		#print(self.dataset)
		#print(self.dataset['name'])


def read_csv_file( filename ):
	csv_file = open(filename);
	csv_data = csv.DictReader( csv_file );

	#print(csv_data.fieldnames
	return csv_data


csv_data = read_csv_file( "dataset/Users.csv" )


nodes = Nodes( csv_data )
