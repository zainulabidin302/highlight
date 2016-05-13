import path_helper 
import json

path_helper.update_path_cache(['/home']) # Update the file in root folder called paths, it contains the list of 

count = 0
for item in path_helper.get_files_list():
	
	if(item.endswith('txt')):
		count += 1
	


print(count, " text files found ")



