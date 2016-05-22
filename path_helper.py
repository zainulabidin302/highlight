import os, fnmatch, json
def get_files(path):
	matches = []
	for root, dirnames, filenames in os.walk(path):
	    for filename in fnmatch.filter(filenames, '*'):
	        matches.append(os.path.join(root, filename))
	return matches


def update_path_cache(paths):
	tmp = []
	for item in paths:
		tmp.extend(get_files(item))

	file = json.dump(tmp, open("paths", "w"))

def get_files_list():
	return (json.load(open("paths", "r+")))