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


def calculate_entropy(node, root, data_types):
	
	values = []
	counter = 0
	entropy = 0.0
	denominator = len(node.dataframe) - 1

	for element in data_types[root.name]:
		counter = 0
		for i in range(1, denominator + 1):
			if element == node.dataframe[i][root.number]:
				counter += 1

		if counter > 0:
			entropy_of_element = - ( (counter/denominator) * math.log(counter/denominator, 2))
		else:
			entropy_of_element = 0
		values.append(entropy_of_element)
	for element in values:
		entropy += element

	return entropy


def decision_tree(dataframe, data_types):

	#select the first node to expand
	#to do this calculate te entropy of each attribuste and choose the one with the entropy closest to 0

	#to calculate the entropy
		#use the amount of accurrences of each type and placeit on the formula
		# - type1/totaltypes * log(type1/totaltypes) - type2/totaltypes * log(type2/totaltypes) - typeN/totaltypes * log(typeN/totaltypes)
		#remeber that the log most be base 2

	#after you selected the node
		#start the ID3 algorithm with that node
		#split the node for each value it has 
		#for each value calculate the GAIN of that attribute
		#split each of them in decending order based on the info GAIN (this when the recursion happens)
	
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
	