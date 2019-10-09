#!/bin/python


import csv;


class Node:
	def __init__(self, data):
		self.data = data;
	

class Nodes:
	def __init__(self, dataset):
		self.dataset = {}
		for header in dataset:
			self.nodes = []
			for data in dataset[header]:
				self.nodes.append(Node(data))
			self.dataset[header] = self.nodes

		for names in self.dataset['name']:
			print(names.data)

def csv_data_parser(csv_data ):
	'convert from DictReader to List'
	headers = csv_data.fieldnames

	dataset = {}
	for header in headers:
		dataset[header] = []
	for columns in csv_data:
		for header in headers:
			entire_row = columns[header]
			dataset[header].append(entire_row)
	return dataset


def read_csv_file( filename ):
	csv_file = open(filename);
	csv_data = csv.DictReader( csv_file );

	#print(csv_data.fieldnames
	return csv_data


csv_data = read_csv_file( "dataset/Users.csv" )
dataset = csv_data_parser(csv_data)

nodes = Nodes(dataset)
