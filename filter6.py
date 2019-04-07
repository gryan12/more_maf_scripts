import os
import glob

current_abspath = os.path.abspath(os.path.curdir)


def filter_relevant_genes(maf_file):
    gene_list = []
    with open(maf_file) as file:
        content = file.readlines()
    total_count = len(content)
    for line in content:
        wordarray = line.split()
        if (len(wordarray) > 7 and wordarray[8] == "Missense_Mutation"):
            gene_list.append(wordarray[0])
        # if len(wordarray) < 9:
        #     name = maf_file.split("\\")
        #     new_name = name[len(name) - 1]
        #     print(new_name)
        #     split_file_name_array = new_name.split(".")
        #     new_file_name = split_file_name_array[0] + ".fail.txt"
        #     new_path = f'{current_abspath}/failed-filtered-files/{new_file_name}'
        #
        #     with open(new_path, 'w') as file:
        #         file.write("failed")


    l1 = len(gene_list)
    print(f'now filtering {maf_file}. Total gene count: {total_count}. Filtered Gene count: {l1}')

    name = maf_file.split("\\")
    new_name = name[len(name)-1]
    print (new_name)
    split_file_name_array = new_name.split(".")
    # only_file_name = split_file_name_array[0].splid("\\")
    new_file_name =  split_file_name_array[0] + ".non.txt"
    print(new_file_name)
    new_path = f'{current_abspath}\\filtered-files\\{new_file_name}'
    with open(new_path, 'w') as file:
        for gene in gene_list:
            file.write(f'{gene}\n')


def contents(folder): # Recursive, returns list of all files with full paths
    directContents = os.listdir(folder)
    for item in directContents:
        if os.path.isfile (os.path.join(folder, item)):
            if (item.endswith(".maf.txt")):
                filter_relevant_genes((os.path.join(folder, item)))
                print("MAF")
        else:contents(os.path.join(folder, item))
    return;

try:
    os.makedirs(f'{current_abspath}/filtered-files')
except FileExistsError:
    print('filtered-files already exists. proceeding')
    pass

try:
    os.makedirs(f'{current_abspath}/failed-filtered-files')
except FileExistsError:
    pass

#
# for directory in os.listdir(os.curdir):
#     contents(directory)
#
# #

list = []
for path, subdirs, files in os.walk(current_abspath):
    for name in files:
        list.append(os.path.join(path, name))
#
#
# for path, subdirs, files in os.walk(current_abspath):
#     for name in files:
#         print (name)
#         if name.endswith(".maf.txt"):
#             filter_relevant_genes(os.path.join(path, name), name)
#         # print (os.path.join(path, name))


for file in list:
    if file.endswith(".maf.txt"):
      print(file)
      filter_relevant_genes(file)