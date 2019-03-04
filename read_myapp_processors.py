import re
import sys
import pickle

content = sys.argv[1]
outfile = sys.argv[2]

match_type = re.search(r'id=[a-zA-Z0-9-]+', content)

if match_type is not None:
	flow_file_str = match_type.group().replace("id=","")
	with open (outfile, 'rb') as fp:
		main_list = pickle.load(fp)
	
	if flow_file_str in main_list:
		date = re.search(r'\d{4}-\d{2}-\d{2}', content).group()
		time = re.search(r'\d{2}:\d{2}:\d{2}', content).group()
		log_level = content.split("~")[1]
		processor = content.split("~")[2].split("[id=")[0]
		processor_id = content.split("~")[2].split("[id=")[1].replace("]","")
		message = content.split("~")[3]
		print(log_level + "," + processor_id + "," + processor + "," + message + "," + date + "," + time)
	else:
		print("not matched")
else:
	print("not matched")