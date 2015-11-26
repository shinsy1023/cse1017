# Input and Output View

class Reader(object):
    
    @staticmethod
    def ox(message):
        response = input(message).lower()
        while not (response == 'o' or response == 'x'):
            response = input(message).lower()
        return response == 'o'
    
    @staticmethod
    def get_number(message,low,high):
        response = input(message)
        while not (response.isdigit() and low <= int(response) <= high):
            response = input(message)
        return int(response)
    
    @staticmethod   
    def get_names(message,n):
        names = []
        for i in range(1,n+1):
            s = input("#" + str(i) + ", " + message)
            names.append(s)
        return names
    
    @staticmethod
    def load_members():
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
                line=line[pos+1:]
                if i!=2:
                    pos=line.index(',')
                else:
                    pos=line.index('\n')
                for j in range(pos):
                    num=num+line[j]
                if i==1:
                    element=element+(float(num), )
                else:
                    element=element+(int(num), )
                num=''
                members[name]=element
            name=""
        file.close()
        return members

class Writer(object):
    
    @staticmethod
    def show_history(names):
        out = ""
        members = Reader.load_members()
        for name in members:
            if name in names:
                num1=str(members[name][1])
                num2=str(members[name][0])
                num3=str(members[name][2])
                num4=str(round(members[name][1]/members[name][0]*100, 1))
                out=name+" : "+ num4 + "% (" +num1+ "/" + num2+ ") : "+ " "+num3
                print(out)

    @staticmethod
    def update_history(results):
        members = Reader.load_members()
        member=list(members.keys())
        player=list(results.keys())
        for players in member:
            if players in player:
                members[players]=(members[players][0]+results[players][0],\
                                 members[players][1]+results[players][1],\
                                 members[players][2]+results[players][2])
        file = open("members.txt","w")
        file.write(members)
        file.close()
    
    @staticmethod
    def show_top5():
        print("== end ==")
        print()
        print("SMaSH Casino Hall-of-Famers")
        members = Reader.load_members()
        
    
