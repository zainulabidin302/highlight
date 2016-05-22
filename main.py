from __future__ import print_function
import path_helper
import sys, os, re
import json, unicodedata
import textract
import time
from pytrie import SortedStringTrie as trie



path_helper.update_path_cache(['T:/pydev/rootdir/rrr'])
#sys.path.append('./reader')

def build_indexes(files_list, index_file):
    toolbar_width = len(files_list)
    print(toolbar_width)
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
    hash_index = {}
    for item in files_list:
        text = textract.process(item)
        details = re.split("[, \t\n\\t:;]",  text)
        for i in details:
            if i == "" : continue
            if hash_index.has_key((i)) :
                if hash_index[(i)].has_key((item)):
                    hash_index[(i)][(item)] += 1
                else:
                    hash_index[(i)][(item)] = 1
            else:
                hash_index[(i)] = {}
                if hash_index[(i)].has_key(item):
                    hash_index[(i)][(item)] += 1
                else:
                    hash_index[(i)][(item)] = 1


        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("\n")
    fp = open(index_file, "w")
    json.dump(hash_index, fp)
    fp.close()

#build_indexes(path_helper.get_files_list(), 'index')


def fuzzyfinder(user_input, collection):
        suggestions = []
        pattern = '.*'.join(user_input)   # Converts 'djm' to 'd.*j.*m'
        regex = re.compile(pattern)  # Compiles a regex.
        for item in collection:
            match = regex.search(item)   # Checks if the current item matches the regex.
            if match:
                suggestions.append(item)
        return suggestions


def load_indexes(file):
    fp = open(file, "r")
    hash_index = json.load(fp)
    fp.close()
    return hash_index


hi = load_indexes("index")
inp = ""





keys = hi.keys()

while(inp != "0"):
    inp = raw_input("Enter a word: ")

    ls = fuzzyfinder(inp, keys)

    if len(ls) > 0:
        for i in ls:
            if hi.has_key(i):
                print((i)  )
                #print((i) + " => ", end="" )
                print(hi[i].keys())
            else:
                print('not found!')
        print("")
    else:
        print("not found")



"""

def get_type(file) :
    types = {
        #'textreader' : ['pdf', 'txt', 'html', 'xhtml', 'rtf', 'conf', 'ini', 'py' , 'c'],
        #'textreader' : ['txt', 'html', 'xhtml', 'rtf', 'conf', 'ini', 'py' , 'c'],
        'pdfreader' : ['pdf'],
        #'pdfreader' : ['doc', 'docx'],
        #'pdfreader' : ['ppt', 'pptx'],
    }

    for  key, type in types.iteritems():
        if file.endswith(tuple(type)):
            return key
    return None

def build_indexes2(files_list, file):
    hash_index = {}

    for item in files_list:
        service = get_type(item)
        if service == None: continue
        service = __import__(service)
        res = service.read(item)

        details = re.split("[, \t\n\\t:;]",  res)
        print(details)
        return
        for i in details:
            if i == "" : continue
            if hash_index.has_key((i)) :
                if hash_index[(i)].has_key((item)):
                    hash_index[(i)][(item)] += 1
                else:
                    hash_index[(i)][(item)] = 1
            else:
                hash_index[(i)] = {}
                if hash_index[(i)].has_key(item):
                    hash_index[(i)][(item)] += 1
                else:
                    hash_index[(i)][(item)] = 1

    fp = open(file, "w")
    json.dump(hash_index, fp)
    fp.close()



#build_indexes(path_helper.get_files_list(), "index" )
#build_indexes(['T:/pydev/rootdir/a.pdf'], "index" )
build_indexes2(path_helper.get_files_list(), "index" )



"""







