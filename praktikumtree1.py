class Node:
    def __init__(self, name, type):
        self.name = name
        self.type = type  
        self.children = []

def display_filesystem(root, level=0):
    print(" " * level + "- " + root.name + " (" + root.type + ")")
    for child in root.children:
        display_filesystem(child, level + 1)

root = Node("Data_kuliah", "folder")
folder1 = Node("folder1", "folder")
file1 = Node("file1.txt", "file")
file2 = Node("file2.txt", "file")

root.children.append(folder1)
root.children.append(file1)
folder1.children.append(file2)

display_filesystem(root)