import fileinput

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
			words =line.split(' ', 2)
			
			attributes.append(words[1])
			words[2] = words[2].replace('{', "")
			words[2] = words[2].replace('}', "")
			words[2] = words[2].replace(' ', "")
			words[2] = words[2].replace('\n', "")
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
	dataframe.append(attributes)
	for element in data:
		dataframe.append(element)
	decision_tree(dataframe, data_types)