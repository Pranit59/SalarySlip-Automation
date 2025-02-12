from tkinter import *
from tkinter import messagebox as tmsg  

def submit():
    TravelAllowance=(aa2.get()/100)*aa1.get()
    DearnessAllowance=(aa3.get()/100)*aa1.get()
    HouseRentAllowance=(aa4.get()/100)*aa1.get()
    aa2.set(str(TravelAllowance))
    aa3.set(str(DearnessAllowance))
    aa4.set(str(HouseRentAllowance))
    totalearning=aa1.get()+TravelAllowance+DearnessAllowance+HouseRentAllowance
    tt1.set(str(totalearning))
    T1=aa1.get()/aa5.get()
    providentfund=totalearning-T1
    T2=aa6.get()*(aa1.get()/30)
    leavededuction=totalearning-T2
    aa5.set(str(T1))
    aa6.set(str(T2))
    Totaldeductions=T1+T2
    tt2.set(str(Totaldeductions))
    Netsalary=(providentfund+leavededuction)-totalearning
    tt3.set(str(Netsalary))
    with open('Salary-slip.txt','a')as f:
        #print(f"{ss1.get(),ss2.get(),ss3.get(),ss4.get(),ss5.get(),ss6.get()}")
        #print(f"{aa1.get(),aa2.get(),aa3.get(),aa4.get(),aa5.get(),aa6.get()}")
        #print(f"{tt1.get(),tt2.get(),tt3.get()}")
        f.write(f"===============Employee Details ===============\n")        
        f.write(f"Date of Joining  : {ss1.get()}\n")
        f.write(f"Employee Name : {ss2.get()}\n")
        f.write(f"Employee ID : {ss3.get()}\n")
        f.write(f"Designation : {ss4.get()}\n")
        f.write(f"Working Period : {ss5.get()}\n")
        f.write(f"Department : {ss6.get()}\n")
        f.write(f"===============*****===============\n")        
        f.write(f"Basic : {aa1.get()}\n")
        f.write(f"Travel Allowance : {aa2.get()}\n")
        f.write(f"Dearness Allowance : {aa3.get()}\n")
        f.write(f"House Rent Allowance : {aa4.get()}\n")
        f.write(f"Provident Fund : {aa5.get()}\n")
        f.write(f"Leave Deduction : {aa6.get()}\n")
        f.write(f"===============*****===============\n")  
        f.write(f"Total Earnings : {tt1.get()}\n")
        f.write(f"Total Deductions : {tt2.get()}\n")
        f.write(f"Net Salary : {tt3.get()}\n")
        f.write(f"\n===============THE END ===============\n") 
    tmsg.showinfo('Submit', 'Submited Successfully')


def reset():
    ss1.set('')
    ss2.set('')
    ss3.set('')
    ss4.set('')
    ss5.set('')
    ss6.set('')
    aa1.set('')
    aa2.set('')
    aa3.set('')
    aa4.set('')
    aa5.set('')
    aa6.set('')
    tt1.set('')
    tt2.set('')
    tt3.set('')
    


           
root=Tk()
root.geometry("1620x1010")
root.title("Salary Slip")
root.config(bg='white',borderwidth=10)

Label(root,text='UNISYS INFOTECH CORPORATION',bg='white',font="Century 35 underline bold").pack(pady=10)

Label(root,text='SALARY SLIP',bg='white',font="Century 25 bold").pack(pady=20)

Doj=Label(root,text="Date of Joining :",bg='white',font='Century 18 bold').place(x=200,y=190)
Ename=Label(root,text="Employee Name :",bg='white',font='Century 18 bold').place(x=200,y=240)
pp=Label(root,text="Employee ID :",bg='white',font='Century 18 bold').place(x=790,y=190)
des=Label(root,text="Designation :",bg='white',font='Century 18 bold').place(x=800,y=240)
wopr=Label(root,text="Working Period :",bg='white',font='Century 18 bold').place(x=200,y=290)
dep=Label(root,text="Department :",bg='white',font='Century 18 bold').place(x=800,y=290)

ss1=StringVar()
ss2=StringVar() 
ss3=StringVar() 
ss4=StringVar()
ss5=StringVar() 
ss6=StringVar()


s1=Entry(root,textvariable=ss1,font='Century 17 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=470,y=195)
s2=Entry(root,textvariable=ss2,font='Century 17 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=470,y=245)
s3=Entry(root,textvariable=ss3,font='Century 17 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=1010,y=195)          
s4=Entry(root,textvariable=ss4,font='Century 17 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=1010,y=245)
s5=Entry(root,textvariable=ss5,font='Century 17 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=470,y=295)
s6=Entry(root,textvariable=ss6,font='Century 17 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=1010,y=295)

Label(root,bg='gray95',font="Century 22 ",width=80,height=1).place(x=30,y=350)
Label(root,text='Earnings',fg='Black',font="Century 17 bold").place(x=250,y=350)
Label(root,text='Amount',fg='Black',font="Century 17 bold").place(x=550,y=350)
Label(root,text='Deduction',fg='Black',font="Century 17 bold").place(x=850,y=350)
Label(root,text='Amount',fg='Black',font="Century 17 bold").place(x=1200,y=350)

Basic=Label(root,text='Basic',bg='white',font='Century 16 bold').place(x=260,y=410)
TA=Label(root,text='Travel Allowance',bg='white',font='Century 16 bold').place(x=200,y=440)
DA=Label(root,text="Dearness Allowance",bg='white',font='Century 16 bold').place(x=180,y=480)
HRA=Label(root,text="House Rent Allowance",bg='white',font='Century 16 bold').place(x=170,y=520)
PA=Label(root,text="Provident Fund",bg='white',font='Century 16 bold').place(x=830,y=410)
LD=Label(root,text="Leave Deduction",bg='white',font='Century 16 bold').place(x=830,y=460)

aa1=IntVar()
aa2=IntVar() 
aa3=IntVar()
aa4=IntVar()
aa5=IntVar() 
aa6=IntVar()

a1=Entry(root,textvariable=aa1,font='Century 16 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=470,y=415)
a2=Entry(root,textvariable=aa2,font='Century 16 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=470,y=450)
a3=Entry(root,textvariable=aa3,font='Century 16 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=470,y=485)          
a4=Entry(root,textvariable=aa4,font='Century 16 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=470,y=520)
a5=Entry(root,textvariable=aa5,font='Century 16 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=1120,y=415)
a6=Entry(root,textvariable=aa6,font='Century 16 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=1120,y=465)

TE=Label(root,text="Gross Salary",bg='white',font='Century 16 bold').place(x=230,y=610)
TD=Label(root,text="Total Deductions",bg='white',font='Century 16 bold').place(x=850,y=590)
NP=Label(root,text="Net Salary",bg='white',font='Century 16 bold').place(x=900,y=640)

tt1=IntVar()
tt2=IntVar()
tt3=IntVar()

t1=Entry(root,textvariable=tt1,font='Century 16 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=470,y=615)
t2=Entry(root,textvariable=tt2,font='Century 16 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=1120,y=595)
t3=Entry(root,textvariable=tt3,font='Century 16 bold',bg='white',borderwidth=3,relief=GROOVE).place(x=1120,y=645)

Button(root,text='Submit',command=submit,bg='blue',fg='white',font='Century 16 bold',borderwidth=15,relief=GROOVE).place(x=650,y=720)
Button(root,text='Reset',command=reset,bg='red',fg='white',font='Century 16 bold',borderwidth=15,relief=GROOVE).place(x=820,y=720)

root.mainloop()

