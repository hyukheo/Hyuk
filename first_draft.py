#-*- coding: utf-8 -*-

from Tkinter import *

root=Tk()
root.geometry("1440x810+100+100")
root.resizable(True,True)

# photo=PhotoImage(file="design.png")
# label1=Label(root, image=photo)
label1=Label(root)
def click_startb():
       root.destroy()
       

startb=Button(root,text="start", command=click_startb,width=5)
startb.pack(side="right", padx=10, pady=10)


label1.pack()


root.mainloop()

window=Tk()
window.title("Choose most important number")
window.geometry("1440x810+100+100")
window.resizable(True,True)



import numpy as np
SK1=np.array([55,44,55,44,11])
Doosan1=np.array([55,55,44,33,55])
Hanhwa1=np.array([11,22,55,55,33])
Nexen1=np.array([33,33,44,44,22])
Kia1=np.array([44,55,11,33,44])
Lotte1=np.array([44,44,22,11,11])
LG1=np.array([22,22,33,11,33])
Samsung1=np.array([22,33,33,55,55])
NC1=np.array([11,11,11,22,22])
KT1=np.array([33,11,22,22,44])



ranking=[0,0,0,0,0]
i=1

newSK1 = [0, 0, 0, 0, 0]
newDoosan1 = [0, 0, 0, 0, 0]
newHanhwa1 = [0, 0, 0, 0, 0]
newNexen1 = [0, 0, 0, 0, 0]
newKia1 = [0, 0, 0, 0, 0]
newLotte1 = [0, 0, 0, 0, 0]
newLG1 = [0, 0, 0, 0, 0]
newSamsung1 = [0, 0, 0, 0, 0]
newNC1 = [0, 0, 0, 0, 0]
newKT1 = [0, 0, 0, 0, 0]

def click_button1():
    global i
    ranking[0]=i
    i+=1
    b1.destroy()
              
              
def click_button2():
    global i
    ranking[1]=i
    i+=1
    b2.destroy()
    
def click_button3():
    global i
    ranking[2]=i
    i+=1
    b3.destroy()
     
def click_button4():
    global i
    ranking[3]=i
    i+=1
    b4.destroy()
  
def click_button5():
    global i
    ranking[4]=i
    i+=1
    b5.destroy()
    
def click_pass():
    for i in range(5):
        newSK1=SK1*(51-(10*(ranking[i]-1)))
        newDoosan1=Doosan1*(51-(10*(ranking[i]-1)))
        newHanhwa1=Hanhwa1*(51-(10*(ranking[i]-1)))
        newNexen1=Nexen1*(51-(10*(ranking[i]-1)))
        newKia1=Kia1*(51-(10*(ranking[i]-1)))
        newLotte1=Lotte1*(51-(10*(ranking[i]-1)))
        newLG1=LG1*(51-(10*(ranking[i]-1))) 
        newSamsung1=Samsung1*(51-(10*(ranking[i]-1)))
        newNC1=NC1*(51-(10*(ranking[i]-1)))
        newKT1=KT1*(51-(10*(ranking[i]-1)))

    window.destroy()

   
xPos, yPos = 0, 0

label1=Label(window, text="Choose most important number", fg="black",anchor=N)
label1.pack()

b1=Button(window, text="1", width=25, command=click_button1,height=10)
b1.place(x=20, y=300)

b2=Button(window,text="2",width=25, command=click_button2, height=10)
b2.place(x=320, y=300)

b3=Button(window,text="3",width=25, command=click_button3, height=10) 
b3.place(x=620, y=300)

b4=Button(window,text="4",width=25, command=click_button4, height=10) 
b4.place(x=920, y=300)

b5=Button(window,text="5", width=25,command=click_button5, height=10)
b5.place(x=1220, y=300)

bpass=Button(window, text="6 =>", width=25, command=click_pass, height=10)
bpass.place(x=620, y=550)


asdf=Tk()
asdf.title('Choose your neighbor')
asdf.geometry('1440x810+100+100')
asdf.resizable(False,False)


j=1


SK = 0
Doosan = 0
Hanhwa = 0
Nexen = 0
Kia = 0
LG = 0
Lotte = 0
NC = 0
KT = 0
Samsung = 0


def click_button01():
    global j
    global Doosan
    global LG
    global Nexen
    j+=1
    Doosan+=165
    LG+=165
    Nexen+=165
    calculation()
    if j==2:
       asdf.destroy()
def click_button02():
    global j
    global Lotte
    j+=1
    Lotte+=165
    calculation()
    if j==2:
       asdf.destroy()
def click_button03():
    global j
    global Samsung
    j+=1
    Samsung+=165
    calculation()
    if j==2:
       asdf.destroy()
def click_button04():
    global j
    global Hanhwa
    j+=1
    Hanhwa+=165
    calculation()
    if j==2:
       asdf.destroy()
def click_button05():
    global j
    global SK
    j+=1
    SK+=165
    calculation()
    if j==2:
       asdf.destroy()
def click_button06():
    global j
    global KT
    j+=1
    KT+=165
    calculation()
    if j==2:
       asdf.destroy()
def click_button07():
    global j
    global Kia
    j+=1
    Kia+=165
    calculation()
    if j==2:
       asdf.destroy()

def click_button08():
    global j
    global NC
    j+=1
    NC+=165
    calculation()
    if j==2:
       asdf.destroy()

def calculation():
    global SK
    global Doosan
    global Hanhwa
    global Nexen
    global Kia
    global LG
    global Lotte
    global NC
    global KT
    global Samsung

    SK=sum(newSK1)
    Doosan=sum(newDoosan1)
    Hanhwa=sum(newHanhwa1)
    Nexen=sum(newNexen1)
    Kia=sum(newKia1)
    LG=sum(newLG1)
    Lotte=sum(newLotte1)
    NC=sum(newNC1)
    KT=sum(newKT1)
    Samsung=sum(newSamsung1)



xPos, yPos = 0, 0

label01=Label(asdf, text='당신의 주변 지역을 선택하세요', font=('돋움체',30), fg='black', anchor=N)
label01.pack()

b01=Button(asdf,text='서울', width=25, command=click_button01, height=10)
b01.place(x=88, y=100)

b02=Button(asdf,text='부산', width=25, command=click_button02, height=10)
b02.place(x=449, y=100)

b03=Button(asdf,text='대구', width=25, command=click_button03, height=10)
b03.place(x=810, y=100)

b04=Button(asdf,text='대전', width=25, command=click_button04, height=10)
b04.place(x=1171, y=100)

b05=Button(asdf,text='인천', width=25, command=click_button05, height=10)
b05.pack(side='left',padx=88, pady=200)

b06=Button(asdf,text='수원', width=25, command=click_button06, height=10)
b06.pack(side='left',padx=88, pady=200)

b07=Button(asdf,text='광주', width=25, command=click_button07, height=10)
b07.pack(side='left',padx=88, pady=200)

b08=Button(asdf,text='창원', width=25, command=click_button08, height=10)
b08.pack(side='left',padx=88, pady=200)




List=[SK,Doosan,Hanhwa,Nexen,Kia,LG,Lotte,NC,KT,Samsung]
name_List=['SK','두산','한화','넥센','기아','LG','롯데','NC','KT','삼성']
number=max(List)
if number == List[0]:
   answer=name_List[0]
elif number == List[1]:
     answer = name_List[1]
elif number == List[2]:
     answer = name_List[2]
elif number == List[3]:
     answer = name_List[3]
elif number == List[4]:
     answer = name_List[4]
elif number == List[5]:
     answer = name_List[5]
elif number == List[6]:
     answer = name_List[6]
elif number == List[7]:
     answer = name_List[7]
elif number == List[8]:
     answer = name_List[8]
else:
     answer = name_List[9]

asdf.mainloop()

print(answer)
ending=Tk()
ending.geometry('1440x810+100+100')
ending.resizable(False,False)
ending.mainloop
label2=Label(ending,text="당신에게 딱 맞는 팀은 {0}! 야구장에서 만나요".format(answer),font=("돋움체",30),fg="black", anchor=N)
label2.pack()

def click_Button_Go():
       ending.destroy()
Button_Go=Button(ending,text='치어리더들을 만나러 가요!', command=click_Button_Go)
Button_Go.pack()
ending.mainloop()

cheer=Tk()
cheer.geometry('1440x810+100+100')
cheer.resizable(False,False)

Cheer_List=["nexen.png","hanhwa.png","lg.png","nc.png","sk.png","kt.png",\
            "samsung.png","lotte.png","doosan.png","kia.png"]

PhotoList=[None]*10
for k in range(0,9):
       PhotoList[k] = PhotoImage(file=Cheer_List[k])
if answer=='넥센':  

       A1=Label(cheer, image=PhotoList[0])

       A1.pack(padx=300,pady=100)
elif answer=='한화':

       A2=Label(cheer, image=PhotoList[1])

       A2.pack(padx=300,pady=100)
elif answer=='LG':

       A3=Label(cheer, image=PhotoList[2])

       A3.pack(padx=300,pady=100)
elif answer=='NC':

       A4=Label(cheer, image=PhotoList[3])

       A4.pack(padx=300,pady=100)
elif answer=='SK':

       A5=Label(cheer, image=PhotoList[4])

       A5.pack(padx=300,pady=100)
elif answer=='KT':

       A6=Label(cheer, image=PhotoList[5])
       A6.pack(padx=300,pady=100)
elif answer=='삼성':

       A7=Label(cheer, image=PhotoList[6])
       A7.pack(padx=300,pady=100)
elif answer=='롯데':

       A8=Label(cheer, image=PhotoList[7])
       A8.pack(padx=300,pady=100)
elif answer=='두산':

       A9=Label(cheer, image=PhotoList[8])
       A9.pack(padx=300,pady=100)
else:

       A10=Label(cheer, image=PhotoList[9])
       A10.pack(padx=300,pady=100)

cheer.mainloop


