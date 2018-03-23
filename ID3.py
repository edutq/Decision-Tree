import fileinput
import re

class Node:
	def __init__(self, name, entropy, children, father):
		self.entropy = entropy
		self.name = name
		self.children = children
		self.father =  father

	def setEntropy(self, ent):
		self.entropy = ent

	def setChildren(self, newChild):
		self.children.append(newChild)

	def setFather(self, newFather):
		self.father = newFather


def calculate_entropy(node, dataframe, data_types):



	return nodes


def decision_tree(dataframe, data_types):
	
	return 0

if __name__ == "__main__":

	dataframe = []
	attributes = []
	data_flag= False
	data = []
	data_types = {}
	for line in fileinput.input():

		if "@attribute" in line:
			words =re.split("[ \t]+|[ \t]+$", line,2)
			#print(words)
			attributes.append(words[1])
			words[2] = words[2].replace('{', "")
			words[2] = words[2].replace('}', "")
			words[2] = words[2].replace(' ', "")
			words[2] = words[2].replace('\n', "")
			#print(words[2])
			values = words[2].split(',')
			values_list = []
			for val in values:
				values_list.append(val)
			data_types[words[1]] = values_list
		if data_flag:

			if not "%" in line:
				new_line = line.replace('\n', "")
				values = new_line.split(',')
				aux_data = []
				for val in values:
					aux_data.append(val)
				data.append(aux_data)

		if "@data" in line:
			data_flag = True
	#print(attributes)
	dataframe.append(attributes)
	for element in data:
		dataframe.append(element)
	for element in dataframe:
		print(element)
	print(data_types)
	decision_tree(dataframe, data_types)