file = open("members.txt","r")
members = {}
for line in file:
    name=line[:line.index(',')]
    line=line[line.index(',')+1:]
    members[name]=()
    for i in range(3):
        if i!=2:
            pos=line.index(',')
        else:
            pos=line.index("\n")
        num=int(line[:pos])
        members[name]=members[name]+tuple(str(num))
        line=line[pos+1:]
print(members)
