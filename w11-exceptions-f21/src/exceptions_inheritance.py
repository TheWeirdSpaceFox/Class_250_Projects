"""
Print all children of BaseException
Indent children relative to their parents
"""
def get_children(children, prefix = ""):

    for child in children:
        print(prefix, child.__name__)
        grandchildren = child.__subclasses__()
        #base case: num of grandchildren == 0 (default)
        # Recursive case
        if len(grandchildren) > 0:
            get_children(grandchildren, prefix=prefix+"   ")



if __name__ == '__main__':
    get_children([BaseException])