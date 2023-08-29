import os
folder_names = """Basic Part I,Basic  Part II,Python Programming Puzzles,Condition Statements and Loops,Recursion,String,JSON,List,List Advanced,Dictionary,Tuple,Sets,Collections,Array,Enum,Class,Python Unit test,Python Exception Handling,Python Object-Oriented Programming,Decorator,Functions,Lambda,Map,Itertools,Date Time,File Input Output,CSV Read, Write,Regular Expression,Search and Sorting,Linked List,
Binary Search Tree,Heap queue algorithm,Bisect,Boolean Data Type,None Data Type,Bytes and Byte Arrays,Memory Views exercises,Frozenset Views exercises,Threading,Asynchronous,Modules,Operating System Services,Math,Requests"""


def create_folders(folder_names_lst):
    folder_names_lst = folder_names_lst.strip().split(',')

    for name in range(len(folder_names_lst)):
        if name < 10:
            name = '0' + str(name)
        # print(folder_names_lst[int(name)])
        path = './Python  Exercises W3resources/{}_{}'.format(
            name, folder_names_lst[int(name)])
        # print(path)
        os.mkdir(path)


create_folders(folder_names)
