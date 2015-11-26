file = open("members.txt","r")
members = {}
name=""
for line in file:
        line=tuple(line)
        pos=line.index(',')
        for i in range(pos):
                name=name+line[i]
        num=''
        element=()
        for i in range(3):
                if i!=2:
                        line=line[pos+1:]
                        pos=line.index(',')
                for j in range(pos):
                        num=num+line[j]
                print(num)
                if i==1:
                        element=element+(float(num), )
                else:
                        element=element+(int(num), )
                num=''
                members[name]=element
        name=""
print(members)
file.close()
