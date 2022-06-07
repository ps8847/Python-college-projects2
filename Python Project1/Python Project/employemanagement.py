from tkinter import *
from tkinter import ttk
import cx_Oracle
import tkinter.messagebox as tmsg

root  = Tk()
root.title("EMPLOYEE MANAGEMENT GUI APPLICATION FOR MANAGEMENT By GROUP 'P20' ")
root.geometry("1400x800+0+0")
title = Label(root,text="EMPLOYEE MANAGEMENT APPLICATION ",bd=5,relief=RIDGE,font="Comic-Sans-MS 30 bold",bg="black",fg="white")
title.pack(side=TOP,fill=X)

number1=Frame(root,bd=1,relief=RIDGE,bg="white")
number1.place(x=40,y=63,width=620,height=450)

framefortitle_number1=Frame(root,relief=RIDGE,bg="white")
framefortitle_number1.place(x=40,y=63,width=620,height=55)
tittle = Label(framefortitle_number1,text="ENTER  EMPLOYEE'S DATA ",font=("times new roman",15,"bold"),bg="red",fg="white").place(x=170,y=10)

empidvar=StringVar()
enamevar=StringVar()
egendervar=StringVar()
empdobvar=StringVar()
eaddressvalue=StringVar()
yearofjoining=StringVar()
ephonevalue=StringVar()

empid = Label(number1,text="Employee ID",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=30,y=70)
empid_enter = Entry(number1,textvariable=empidvar,font=("times new roman",15,"bold"),bg="lightgray").place(x=30,y=100,width=200)

empname = Label(number1,text="Employee Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=70)
empname_enter = Entry(number1,textvariable=enamevar,font=("times new roman",15,"bold"),bg="lightgray").place(x=350,y=100,width=200)

empgender = Label(number1,text="Employee Gender",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=30,y=150)
gender_scrollbox= ttk.Combobox(number1,textvariable=egendervar,font="Comic-Sans-MS 10 bold",state="readonly")
gender_scrollbox['values']=("Male","Female","Others")
gender_scrollbox.place(x=30,y=180,height=25)

empDOB = Label(number1,text="Date Of Birth",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=150)
empDOB_enter = Entry(number1,textvariable=empdobvar,font=("times new roman",15,"bold"),bg="lightgray").place(x=350,y=180,width=200)

year_of_joining =  Label(number1,text="Year Of Joining",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=30,y=220)
joining_scrollbox= ttk.Combobox(number1,textvariable=yearofjoining,font="Comic-Sans-MS 10 bold",state="readonly")
joining_scrollbox['values']=("2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025")
joining_scrollbox.place(x=30,y=250,height=25)

empcontact = Label(number1,text="Employee Contact",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=220)
empcontact_enter = Entry(number1,textvariable=ephonevalue,font=("times new roman",15,"bold"),bg="lightgray").place(x=350,y=250,width=200)

empaddress = Label(number1,text="Employee Address",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=30,y=280)
empaddress_enter = Entry(number1,textvariable=eaddressvalue,font=("times new roman",15,"bold"),bg="lightgray").place(x=30,y=310,width=525,height=70)

chk=Checkbutton(number1,text="I'm Confirming that Form Entered is Correct",bg="white",font=("times new roman",10,"bold")).place(x=50,y=400)

button_frame = Frame(root,bd=4,relief=RIDGE,bg="lightgray")
button_frame.place(x=720,y=63,width=300,height=450)


def addstudents():
    try:
      
        if empidvar.get()=="" or enamevar.get()=="" or egendervar.get()=="" or eaddressvalue.get()=="" or yearofjoining.get()=="" or ephonevalue.get()=="" or empdobvar.get()=="":
            tmsg.showerror("Error","All Fields Are Required!")
        else:
            con= cx_Oracle.connect("SYSTEM/hello")
            cur = con.cursor()
            e1=empidvar.get()
            e2=enamevar.get()
            e3=egendervar.get()
            e4=eaddressvalue.get()
            e5=yearofjoining.get()
            e6=ephonevalue.get()
            e7=empdobvar.get()
            cur.execute("Insert Into company Values(:1,:2,:3,:4,:5,:6,:7)",(e1,e2,e3,e4,e5,e6,e7))
                            
            con.commit()
            con.close()
            tmsg.showinfo("SUCCESS","RECORD HAS BEEN INSERTED")
    except cx_Oracle.IntegrityError as e:
        tmsg.showerror("Error","This Employee ID Already Excist")
    except cx_Oracle.DatabaseError as e:
        tmsg.showerror("Error","EMPLOYEE ID and EMPLOYEE CONTACT Should Be in Numbers")
        
def update_data():
    con= cx_Oracle.connect("SYSTEM/hello")
    cur = con.cursor()
    e1=empidvar.get()
    e2=enamevar.get()
    e3=egendervar.get()
    e4=eaddressvalue.get()
    e5=yearofjoining.get()
    e6=ephonevalue.get()
    e7=empdobvar.get()
    cur.execute("update company set ename=:1,egender=:2,eaddress=:3,eyear_of_joining=:4,ephone=:5,edob=:6 where empid=:7",(e2,e3,e4,e5,e6,e6,e1))
    con.commit()
    con.close()
    tmsg.showinfo("SUCCESS","RECORD HAS BEEN UPDATED")
def clearscreen():
    empidvar.set("")
    enamevar.set("")
    egendervar.set("")
    eaddressvalue.set("")
    yearofjoining.set("")
    ephonevalue.set("")
    empdobvar.set("")
def delete_data():
    con= cx_Oracle.connect("SYSTEM/hello")
    cur= con.cursor()
    e1=empidvar.get()
    e2=enamevar.get()
    e3=egendervar.get()
    e4=eaddressvalue.get()
    e5=yearofjoining.get()
    e6=ephonevalue.get()
    e7=empdobvar.get()
    cur.execute("Delete from company Where empid=:1",(e1,))
    con.commit()
    con.close()
    tmsg.showinfo("SUCCESS","RECORD HAS BEEN INSERTED")


def frame_number2():
    def showdata():
        conn= cx_Oracle.connect("SYSTEM/hello")
        cur=conn.cursor()
        cur.execute("select * from company")
        rows = cur.fetchall()
        if len(rows)!=0:
            for row in rows:
                employee_table.insert('',END,values=row)
            conn.commit()
        conn.close()

    root  = Tk()
    root.title("STUDENT MANAGEMENT GUI APPLICATION FOR SCHOOL/COLLEGE MANAGEMENT By GROUP 'P20' ")
    root.geometry("700x600")
    frame_number2=Frame(root,bd=4,relief=RIDGE,bg="black")
    frame_number2.place(x=30,y=32,width=650,height=490)
        
 
    table_frame = Frame(frame_number2,bd=1,relief=RIDGE,bg="black")
    table_frame.place(x=10,y=60,width=700,height=380)

    scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y = Scrollbar(table_frame,orient=VERTICAL)
    employee_table = ttk.Treeview(table_frame,columns=("EMPID","ENAME","EGENDER","EADDRESS","EYEAROFJOINING","EPHONE","EDOB"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=employee_table.xview)
    scroll_y.config(command=employee_table.yview)
    employee_table.heading("EMPID",text="Employee ID")
    employee_table.heading("ENAME",text="Employee NAME")
    employee_table.heading("EGENDER",text="Employee GENDER")
    employee_table.heading("EADDRESS",text="Employee ADDRESS")
    employee_table.heading("EYEAROFJOINING",text="Employee YEAR of JOINING")
    employee_table.heading("EPHONE",text="Employee PHONE")
    employee_table.heading("EDOB",text="Employee Date Of Birth")
    employee_table["show"]="headings"
    
    employee_table.pack(fill=BOTH)
    
    showdata()
    clearscreen()
    root.mainloop()

clearbtn= Button(number1,text="CLEAR",command=clearscreen,font=("times new roman",12,"bold"),fg="green").grid(padx=490,pady=400)
addbtn = Button(button_frame,bg="white",fg="black",font="comicsansms 15 bold",text="ENTER RECORDS",command=addstudents).pack(pady=3,side=TOP,anchor="s")
showbtn = Button(button_frame,bg="white",fg="black",font="comicsansms 15 bold",command=frame_number2,text="SHOW RECORDS").pack(pady=30,side=TOP,anchor="s")
updbtn = Button(button_frame,bg="white",fg="black",font="comicsansms 15 bold",text="UPGRADE RECORDS",command=update_data).pack(pady=10,side=TOP,anchor="s")
dltbtn = Button(button_frame,bg="white",fg="black",font="comicsansms 15 bold",text="REMOVE RECORDS",command=delete_data).pack(pady=30,side=TOP,anchor="s")

root.mainloop()