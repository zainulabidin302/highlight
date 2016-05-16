import path_helper, json, imp


extensions = ""
with open('extensions.json') as extention:
	extensions = json.load(extention)
	



path_helper.update_path_cache(['/home']) # Update the file in root folder called paths, it contains the list of 



count = 0

for item in path_helper.get_files_list():
	for key, ex in extensions.iteritems():
		
		if(item.endswith(tuple(ex))):
			
			parser = imp.load_source("reader/"+key+ "/" + key, "reader/"+key+ "/" + key+".py")

			res = parser.read_to_string(item)
			print(res)			


	


print(count, " text files found ")



