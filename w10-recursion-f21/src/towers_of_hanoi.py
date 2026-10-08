move_count =0
def move(n, source, target, auxiliary):
    global move_count
    if n > 0:
        #moving n-1 disks from source to aux, so there ut of the way
        print(f"----m1----{n}----{move_count}\n{source}\n{auxiliary}\n{target}\n")
        move(n-1, source, auxiliary, target)

        #move nth disk from source to target
        target.append(source.pop())

        print(f"----After Popping----{n}----{move_count}\n{source}\n{auxiliary}\n{target}\n")

        #move n-1 disks that we left on aux to target
        move(n-1, auxiliary, target, source)


# initiate call from source A to target C with auxiliary B
a=['A','B','C']
b=[]
c=[]
print(a, b, c, '##############', sep='\n')

move_count = 0
move(len(a), a, c, b)
#move(3, a, c, b)

print(a, b, c, '##############', sep='\n')
