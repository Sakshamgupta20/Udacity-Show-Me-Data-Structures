import os
def find_files(suffix, path):
    #Check if file path is invalid
    if(path is None):
        return []
    return find_files_sol(suffix,path,".")

def find_files_sol(suffix,path,current_dir):
    dir_items = os.listdir(current_dir)

    output = []
    if(len(dir_items) == 0):
        return output
    
    for item in dir_items:
        item_path = "{}/{}".format(current_dir,item)
        #If item is file then verifit suffix and path
        if(os.path.isfile(item_path)):
            if(item_path.endswith(path)):
                if(suffix is not None):
                    if(os.path.splitext(item)[0] == suffix):
                        output.append(item_path)
                else:
                    output.append(item_path)
        else:
            #If folder is there then again call same function
            output.extend(find_files_sol(suffix,path,item_path))
    return output


print('''
CASE 1: 
Find files without any path
OUTPUT: {}
'''.format(find_files(None, None))) # []


print('''
CASE 2: 
Find files with path and without suffix
OUTPUT: {}
'''.format(find_files(None, ".c"))) # ['./Practice/Udacity Project/testdir/subdir1/a.c', './Practice/Udacity Project/testdir/subdir3/subsubdir1/b.c', './Practice/Udacity Project/testdir/subdir5/a.c', './Practice/Udacity Project/testdir/t1.c']

print('''
CASE 3: 
Find files with path and  suffix
OUTPUT: {}
'''.format(find_files("a", ".c"))) # ['./Practice/Udacity Project/testdir/subdir1/a.c', './Practice/Udacity Project/testdir/subdir5/a.c']