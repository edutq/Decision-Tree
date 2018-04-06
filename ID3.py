import fileinput
import re
import math
import copy

class Node:
	def __init__(self, name, entropy, children, father, number, dataframe, answer, column):
		self.entropy = entropy
		self.name = name
		self.children = children
		self.father =  father
		self.number = number
		self.dataframe = dataframe
		self.answer = answer
		self.column = column

	def setEntropy(self, ent):
		self.entropy = ent

	def setChildren(self, newChild):
		self.children.append(newChild)

	def setFather(self, newFather):
		self.father = newFather

	def showTree(self, spaces):
		if self.name != self.dataframe[0][-1]:
			print("  " * spaces + self.column + ": " +self.name)
		if self.answer:
			print ("  " * spaces + "  " +  "ANSWER: " + self.answer)
		for child in self.children:
			child.showTree(spaces + 1)
		
		

def ID3(node, root, data_types, visited_list):
	
	#print(root.dataframe[0][node.number])
	#print(visited_list)
	new_list = copy.deepcopy(visited_list)
	node.entropy = calculate_entropy(node, root, data_types)
	#print(node)
	if float(node.entropy) == 0.0:
		
		#print("LEAF NODE")
		node.answer = node.dataframe[1][-1]
		#print(node.answer)
		return 0
	#print("entropy " + str(node.entropy))
	gains = {}
	#print(node.dataframe)
	for i in range(0, len(node.dataframe[0]) -1):
		if i not in visited_list:
			next_node = Node(node.dataframe[0][i], None, None, node, i, node.dataframe, None, None)
			gains[node.dataframe[0][i]] = information_gain(node, next_node, root, data_types)
	#print(gains)
	split_to_node = find_greater_gain(gains)

	#print(split_to_node)
	new_number = root.dataframe[0].index(split_to_node)
	new_list.append(new_number)

	for element in data_types[split_to_node]:

		new_dataframe = []
		new_dataframe.append(root.dataframe[0])
		new_node = Node(element, None, [], node, new_number, None, None, node.dataframe[0][new_number])
		
		for row in node.dataframe:
			
			if row[new_number] == element:
				new_dataframe.append(row)
		
		new_node.dataframe = new_dataframe
		node.children.append(new_node)
		ID3(new_node, root, data_types, new_list)
	return 0

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

def information_gain(actual_node, next_node, root, data_types):

	gain = 0.0
	entropy = 0.0
	values = []
	gains = {}
	for key in data_types.keys():
		
		if key == next_node.name:
			for datatype in data_types[key]:
				aux_data = []
				aux_data.append(root.dataframe[0])
				for i in range(1, len(next_node.dataframe)):

					if next_node.dataframe[i][next_node.number] == datatype:
						aux_data.append(next_node.dataframe[i])
				new_node = Node(next_node.name, None, None, next_node, next_node.number, aux_data, None, None)
				val = calculate_entropy(new_node, root, data_types)
				val = val * ((len(new_node.dataframe) - 1) / (len(root.dataframe) -1) )

				values.append(val)
			for element in values:
				entropy += element
			gain = actual_node.entropy - entropy
	return gain

def find_greater_gain(gains):

	greater = 0.0

	for element in gains:
		if gains[element] > greater:
			greater = gains[element]

	for element in gains:
		if gains[element] == greater:
			return element

def decision_tree(dataframe, data_types):

	start = Node(dataframe[0][-1], None, [], None, len(dataframe[0]) -1, dataframe, None, dataframe[0][-1] )
	ID3(start, start, data_types, [])
	start.showTree(-1)
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
	decision_tree(dataframe, data_types)
