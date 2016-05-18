import path_helper 
import sys, os
import json


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

#print(t_data)

print(len(t_data))
print(t_sizes)
#print(count, " text files found ")



