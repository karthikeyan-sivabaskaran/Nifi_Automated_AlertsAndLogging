import os,sys,json,requests,pickle

#main_pg_list = ['0169100e-67fc-125a-40c6-7ec3e9d63d73'] # main id will be initially given here
# outfile = 'D:\\tmp\\nifi_data\\outfile'

main_pg_list = sys.argv[1].split(",")
outfile = sys.argv[2]

loop_pg_list = []
print(main_pg_list)
main_curl_url = 'http://localhost:8080/nifi-api/process-groups/' + main_pg_list[0] + '/process-groups'
main_json_data = requests.get(main_curl_url).json()

if len(main_json_data) > 0:
	for data in main_json_data['processGroups']:
		loop_pg_list.append(data['id'])

print(loop_pg_list)

while len(loop_pg_list) > 0:
	for loop_pg_id in loop_pg_list:
		loop_pg_list.remove(loop_pg_id)
		main_pg_list.append(loop_pg_id)
		loop_curl_url = 'http://localhost:8080/nifi-api/process-groups/' + loop_pg_id + '/process-groups'
		loop_json_data = requests.get(loop_curl_url).json()
		if len(loop_json_data) > 0:
			for data in loop_json_data['processGroups']:
				loop_pg_list.append(data['id'])
				
print(main_pg_list)

processor_id_list = []
processor_name_list = []

if len(main_pg_list) > 0:
	for pg_id in main_pg_list:
		curl_url = 'http://localhost:8080/nifi-api/process-groups/' + pg_id + '/processors'		
		json_data = requests.get(curl_url).json()
		if len(json_data) > 0:
			for data in json_data['processors']:
				processor_id_list.append(data['component']['id'])
				processor_name_list.append(data['component']['name'])
				
print(processor_id_list)
print(processor_name_list)
		

with open(outfile, 'wb') as fp:
    pickle.dump(processor_id_list, fp)
	
print("file written successfully")
