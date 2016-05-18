<<<<<<< HEAD
import path_helper 
import sys, os
import json
=======
import path_helper, json, imp


extensions = ""
with open('extensions.json') as extention:
	extensions = json.load(extention)
	


>>>>>>> 7da394bcc4e4a7e25b2f81428f11591fd41fb60c


sys.path.append('./reader')



path_helper.update_path_cache(['T:/pydev/rootdir']) # Update the file in root folder called paths, it contains the list of


types = {
    'textreader' : ['pdf', 'txt', 'html', 'xhtml', 'rtf', 'conf', 'ini', 'py' , 'c'],
    #'pdfreader' : ['pdf'],
    #'pdfreader' : ['doc', 'docx'],
    #'pdfreader' : ['ppt', 'pptx'],
}


def get_type(file) :

    global types
    for  key, type in types.iteritems():
        if file.endswith(tuple(type)):
            return key
    return None





count = 0
<<<<<<< HEAD
t_data = []
t_sizes = []
for item in path_helper.get_files_list():
    string = ''
    service = get_type(item)
    if service == None: continue

    service = __import__(service)
    res = service.read(item)
    t_sizes.append(os.path.getsize(item))
    t_data.append(res)
=======

for item in path_helper.get_files_list():
	for key, ex in extensions.iteritems():
		
		if(item.endswith(tuple(ex))):
			
			parser = imp.load_source("reader/"+key+ "/" + key, "reader/"+key+ "/" + key+".py")

			res = parser.read_to_string(item)
			print(res)			


	
>>>>>>> 7da394bcc4e4a7e25b2f81428f11591fd41fb60c

#print(t_data)

print(len(t_data))
print(t_sizes)
#print(count, " text files found ")



