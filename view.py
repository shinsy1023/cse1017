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
        for line in file:
            pass # fill here
        file.close()
        return members

class Writer(object):
    
    @staticmethod
    def show_history(names):
        out = ""
        members = Reader.load_members()
        for name in members:
            if name in names:
                pass # fill here
        print(out)

    @staticmethod
    def update_history(results):
        members = Reader.load_members()
        pass # fill here
        file = open("members.txt","w")
        pass # fill here
        file.close()
    
    @staticmethod
    def show_top5():
        print("== end ==")
        print()
        print("SMaSH Casino Hall-of-Famers")
        members = Reader.load_members()
        pass # fill here
    
