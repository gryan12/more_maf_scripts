import os

path = 'C:\\Users\\GAJRy\\files\\python\\cancerGenomics\\dataset\\dataset\\unique_genes.txt'

with open (path) as file:
    contents = file.readlines()
    print(len(contents))