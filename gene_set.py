import os

all_genes = set()
list_all_genes = []
print("hello")
print (os.path.abspath(os.curdir))

for filename in os.listdir(os.path.curdir):
    with open(filename) as f:
        content = f.readlines()
        for gene in content:
            all_genes.add(gene)
            list_all_genes.append(gene)

print(len(list_all_genes))
print (len(all_genes))

path = 'C:\\Users\\GAJRy\\files\\python\\cancerGenomics\\dataset\\dataset\\unique_genes.txt'

with open(path, 'w') as file:
    for gene in all_genes:
        file.write(f'{gene}')
        print("written")







