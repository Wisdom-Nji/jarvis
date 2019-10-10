#!/bin/python


import csv


class Data:
	def __init__(self, data):
		self.data = data

class Node:
	'this are columns in database'
	def __init__(self, name, dataset):
		self.name = name
		self.dataset = []
		for data in dataset:
			_data = Data(data)
			self.dataset.append(_data)

	def raw_print(self, tab_length="\t"):
		datalist = []
		for data in self.dataset:
			datalist.append(data.data);
		print(tab_length, datalist)
class Table:
	def __init__(self, dataset):
		self.nodeset = []
		for header in dataset:
			node = Node(header, dataset[header])
			self.nodeset.append(node)
		'''
		for names in self.dataset['name']:
			print(names.data)
		'''

	def raw_print(self):
		for node in self.nodeset:
			print(Node.__name__, "=> ", node.name)
			node.raw_print()
			print()

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
	csv_file = open(filename)
	csv_data = csv.DictReader( csv_file )

	#print(csv_data.fieldnames
	return csv_data


csv_data = read_csv_file( "dataset/Users.csv" )
dataset = csv_data_parser(csv_data)

table = Table(dataset)
table.raw_print()
