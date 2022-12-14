def validation(input):
    for line in input:
        if "cd" in line and "$" in line:
            pass

def get_file_sizes(input):
    file_sizes = {}
    file_sizes["/"] = 0
    for line in input:
        if line[0] != "$":
            size_str_list = re.findall("\d+", line)
            if size_str_list:
                size_str = size_str_list[0]
                size = int(size_str)
            else:
                size = 0
            name_list = re.findall("\D+[^\n]", line)
            name = name_list[0]
            file_sizes[name.replace("dir ", "")] = size
    return file_sizes

def create_adjacency_list(input):
    total_lines_read = 0
    adj_list = {} # <dir -> [parent dir, [subdirs], [not subdirs]]>
    # add dir names as keys
    adj_list["/"] = ["/", [], []]
    for line in input:
        if "dir" in line:
            dir_name = line[4:-1]
            adj_list[dir_name] = ["", [], []]

    # populate subdirectories in adjacency list
    current_dir = "/"
    listing = False
    for line in input:
        if "cd" in line and "$" in line: # change directory
            current_dir = line[5:-1]
            listing = False
        elif "ls" in line and "$" in line: # list contents
            listing = True
        elif listing:
            if "dir " in line:
                line = line.replace("\n", "")
                adj_list[current_dir][1].append(line)
                adj_list[current_dir][2].append(line.replace("dir ", ""))
            else:
                line = line.replace("\n", "")
                match = re.findall("\d+", line)
                match = line.replace(match[0], "")
                adj_list[current_dir][2].append(match)

    # populate parent directories in adjacency list and fix children syntax
    for key in adj_list:
        children = adj_list[key][1]
        for child in children:
            if "dir" in child:
                dir = child.replace("dir ", "")
                adj_list[dir][0] = key
    
    # print("\nPrinting adjacency list:")
    # for entry in adj_list:
    #     print(str(entry)+" -> "+str(adj_list[entry]))
    return adj_list

def traverse(adj_list, node, visited, calc_list):
    visited.add(node)

    for subdir in adj_list[node]:
        if subdir not in visited:
            traverse(adj_list, subdir, visited, calc_list)
    calc_list.append(node) # print(node, end=' ')

def get_dir_sizes(adj_list, file_sizes):
    # reformat adj list
    fixed_adj_list = {}
    for key in adj_list:
        fixed_adj_list[key] = []
    for key in adj_list:
        for dir in adj_list[key][1]:
            if "dir" in dir:
                fixed_adj_list[key].append(dir.replace("dir ", ""))
    # "dfs" of adj list
    visited = set()
    calc_list = list()
    traverse(fixed_adj_list, "/", visited, calc_list)
    # calculate dir sizes with calc_list
    dir_sizes = {}
    for dir in calc_list:
        size = 0
        addup = adj_list[dir][2]
        for file in addup:
            size += file_sizes[file]
        dir_sizes[dir] = size
        file_sizes[dir] = size
        # print(str(dir)+" -> "+str(size))
    return dir_sizes       

def find_removable(dir_sizes):
    total_sum = 0
    for dir in dir_sizes:
        if dir_sizes[dir] <= 100000:
            total_sum += dir_sizes[dir]
    return total_sum

def part1():
    with open(sys.argv[1]) as f:
        input = f.readlines()
    file_sizes = get_file_sizes(input)
    adj_list = create_adjacency_list(input)
    dir_sizes = get_dir_sizes(adj_list, file_sizes)
    total_sum = find_removable(dir_sizes)

    print("\nPart 1: Total sum = "+str(total_sum)+" (answer is not 1248969)")

import sys, re 
if len(sys.argv) != 2:
    sys.exit("[ERROR: Carmen] Invalid input args")

part1()