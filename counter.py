from tkinter import *

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid(padx=30, pady=20)
        self.create_widgets()

    def create_widgets(self):
        #이름 입력
        Label(self, text="Name").grid(row=0, column=0,sticky=E)
        self.name=Entry(self, width=10)
        self.name.grid(row=0, column=1)
        #Email 입력
        Label(self, text="Email").grid(row=1, column=0, sticky=E)
        self.email=Entry(self, width=10)
        self.email.grid(row=1,column=1)
        Label(self, text="@smash.ac.kr").grid(row=1, column=2, sticky=W)
        #성별 입력
        self.sex=StringVar()
        self.sex.set(None)
        Label(self, text="Sex").grid(row=2, column=0, sticky=E)
        Radiobutton(self, text='male',variable=self.sex, value='male',
                    command=self.write_summary).grid(row=2, column=1)
        Radiobutton(self, text='female', variable=self.sex, value='female',
                    command=self.write_summary).grid(row=2, column=2)
        #맥주 종류 선택
        Label(self, text="Favorites").grid(row=3,column=1)
        self.lagers=BooleanVar()
        Checkbutton(self, text="Lagers", variable=self.lagers).grid(row=4,column=0)
        self.wheetbeer=BooleanVar()
        Checkbutton(self, text="Wheet Beers", variable=self.wheetbeer).grid(row=4, column=1)
        self.pilsners=BooleanVar()
        Checkbutton(self, text="Pilsners", variable=self.pilsners).grid(row=4,column=2)
        self.paleales=BooleanVar()
        Checkbutton(self, text="Paleales", variable=self.paleales).grid(row=5, column=0)
        self.indiapaleales=BooleanVar()
        Checkbutton(self, text="Indiapaleales", variable=self.indiapaleales).grid(row=5, column=1)
        self.stouts=BooleanVar()
        Checkbutton(self, text="Stouts", variable=self.stouts).grid(row=5, column=2)
        #가입 버튼
        Button(self, text="Register", command=self.write_summary).grid(row=6, column=0, columnspan=3,sticky=S)
        #결과창 생성
        self.summary=Text(self,width=48, height=10, wrap=WORD)
        self.summary.grid(row=7, column=0, columnspan=3, sticky=S)
        #종료창 생성
        Button(self, text="Quit", command=self.quit).grid(row=8, column=0, columnspan=3)

    def write_summary(self):
        summary="Name: "+self.name.get()+"\n"
        summary+="Email: "+self.email.get()+"@smash.ac.kr\n"
        summary+="Sex: "+self.sex.get()+"\n"
        summary+="Favorites are: "
        if self.lagers.get():
            summary+="Lagers, "
        if self.wheetbeer.get():
            summary+="Wheet Beers, "
        if self.pilsners.get():
            summary+="Pilsners, "
        if self.paleales.get():
            summary+="Pale Ales, "
        if self.indiapaleales.get():
            summary+="India Pale Ales, "
        if self.stouts.get():
            summary+="Stouts, "
        summary+="..."
        self.summary.delete(0.0, END)
        self.summary.insert(0.0, summary)
        
#main
root=Tk()
root.title("SMaSH Beer Club")
root.geometry("400x400")
app=App(root)
root.mainloop()
