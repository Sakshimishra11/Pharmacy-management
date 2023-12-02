from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox

root=Tk()
root.title("Pharmacy Management System")
root.geometry("1550x800+0+0")
#===============================================Add Medvariable===================================

addmed_var=StringVar()
refmed_var=StringVar()




#==============================Main Variable=================================

Ref_var=StringVar()
CmpName_var=StringVar()
TypeMed_var=StringVar()
MedName_var=StringVar()
Lot_var=StringVar()
Issuedate_var=StringVar()
Expdate_var=StringVar()
Product_var=StringVar()
Ussess_var=StringVar()
Sideeffect_var=StringVar()
Warning_var=StringVar()
Dosage_var=StringVar()
Price_var=StringVar()

def Addmed():
    conn=pymysql.connect(host='localhost',user='root',password='',database='pharmadb')
    my_cursor=conn.cursor()
    my_cursor.execute("insert into tabdata1(ref,medname) values(%s,%s)",(
                                                                refmed_var.get(),
                                                                addmed_var.get()

                                              ))

    conn.commit()
    fetch_datamed()
    Medget_cursor()
    conn.close()
    cmb()
    dmb()
    messagebox.showinfo("success","Medicine Added")

def fetch_datamed():
    conn=pymysql.connect(host='localhost',user='root',password='',database='pharmadb')
    my_cursor=conn.cursor()
    my_cursor.execute("select * from tabdata1")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        Medicine_table.delete(*Medicine_table.get_children())
        for i in rows:
            Medicine_table.insert("",END,values=i)
        conn.commit()
    conn.close()
#==========================================MedGetcursor==========================================

def Medget_cursor(event=""):
    cursor_row=Medicine_table.focus()
    content=Medicine_table.item(cursor_row)
    row=content["values"]
    #refmed_var.set(row[0])
    #addmed_var.set(row[1])

def UpdateMed():
    if refmed_var.get()=="" or addmed_var.get()=="":
        messagebox.showerror("Error","All fields are Required")
    else:
        conn=pymysql.connect(host='localhost',user='root',password='',database='pharmadb')
        my_cursor=conn.cursor()
        my_cursor.execute("update tabdata1 set medname=%s where ref=%s",(
                                                                          addmed_var.get(),
                                                                          refmed_var.get(),
                                                                       ))
        conn.commit()
        fetch_datamed()
        conn.close()
        messagebox.showinfo("Success","Medicine has been updated")

def DeleteMed():
    conn=pymysql.connect(host='localhost',user='root',password='',database='pharmadb')
    my_cursor=conn.cursor()
    
    sql="delete from tabdata1 where Ref=%s"
    val=(refmed_var.get(),)
    my_cursor.execute(sql,val)

    conn.commit()
    fetch_datamed()
    conn.close()

def ClearMed():
    refmed_var.set("")
    addmed_var.set("")

#========================================Main Table============================================

def add_data():
    messagebox.showinfo("Error","All fields are required")
    if Ref_var.get()=="" or  Lot_var.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        conn=pymysql.connect(host='localhost',user='root',password='',database='pharmadb')
        my_cursor=conn.cursor()
        my_cursor.execute("insert into tabdata2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                Ref_var.get(),
                                                                                                CmpName_var.get(),
                                                                                                TypeMed_var.get(),
                                                                                                MedName_var.get(),
                                                                                                Lot_var.get(),
                                                                                                Issuedate_var.get(),
                                                                                                Expdate_var.get(),
                                                                                                Product_var.get(),
                                                                                                Ussess_var.get(),
                                                                                                Sideeffect_var.get(),
                                                                                                Warning_var.get(),
                                                                                                Dosage_var.get(),
                                                                                                Price_var.get()
                                                                                                ))
        conn.commit()
        fetch_data()
        conn.close()
        messagebox.showinfo("Success","data has been inserted")

def fetch_data():
        conn=pymysql.connect(host='localhost',user='root',password='',database='pharmadb')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from tabdata2")
        row=my_cursor.fetchall()
        if len(row)!=0:
            pharmacy_table.delete(*pharmacy_table.get_children())
            for i in row: 
                pharmacy_table.insert("",END,value=i)
            conn.commit()
        conn.close()    

def get_cursor(ev=""):  
        cursor_row=pharmacy_table.focus()
        content=pharmacy_table.item(cursor_row)
        row=content["values"]
        Ref_var.set(row[0]),
        CmpName_var.set(row[1]),  
        TypeMed_var.set(row[2]),
        MedName_var.set(row[3]),
        Lot_var.set(row[4]),
        Issuedate_var.set(row[5]),
        Expdate_var.set(row[6]),
        Product_var.set(row[7]),
        Ussess_var.set(row[8]),
        Sideeffect_var.set(row[9]),
        Warning_var.set(row[10]),
        Dosage_var.set(row[11]),
        Price_var.set(row[12]), 

def Update():
        messagebox.showinfo("Error","All fields are Required")
        if Ref_var.get()=="" or Lot_var.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            conn=pymysql.connect(host='localhost',user='root',password='',database='pharmadb')
            my_cursor=conn.cursor()
            my_cursor.execute("update tabdata2 set CmpName=%s,TypeMed=%s,MedName=%s,LotNo=%s,Issuedate=%s,Expdate=%s,Product=%s,Ussess=%s,Sideeffect=%s,Warning=%s,Dosage=%s,Price=%s where Ref_no=%s",(                                                                                                                                                                                
                                                                                                                                                                                        
                                                                                                                                                                                        CmpName_var.get(),
                                                                                                                                                                                        TypeMed_var.get(),
                                                                                                                                                                                        MedName_var.get(),
                                                                                                                                                                                        Lot_var.get(),
                                                                                                                                                                                        Issuedate_var.get(),
                                                                                                                                                                                        Expdate_var.get(),
                                                                                                                                                                                        Product_var.get(),
                                                                                                                                                                                        Ussess_var.get(),
                                                                                                                                                                                        Sideeffect_var.get(),
                                                                                                                                                                                        Warning_var.get(),
                                                                                                                                                                                        Dosage_var.get(),
                                                                                                                                                                                        Price_var.get(),
                                                                                                                                                                                        eval(Ref_var.get())
                                                                                                                                                                            
                                                                                                                                                                                        ))
        conn.commit()
        fetch_data()
        conn.close()
        messagebox.showinfo("Update","Record has been updated successfully") 

def delete():
        messagebox.showinfo("Error","All fields are required")
        if Ref_var.get()=="" or Lot_var.get()=='':
            messagebox.showerror("Error","All fields are required")
        else:
            conn=pymysql.connect(host='localhost',user='root',password='',database='pharmadb')
            my_cursor=conn.cursor()
            my_cursor.execute("delete from tabdata2 where Ref_no=%s",(Ref_var.get(),))
    
        

        conn.commit()
        fetch_data()
        conn.close()

        messagebox.showinfo("Delete","Info deleted successfully")  

def reset():
            Ref_var.set(""),
            CmpName_var.set(""),
            TypeMed_var.set(""),
            MedName_var.set(""),
            Lot_var.set(""),
            Issuedate_var.set(""),
            Expdate_var.set(""),
            Product_var.set(""),
            Ussess_var.set(""),
            Sideeffect_var.set(""),
            Warning_var.set(r""),
            Dosage_var.set(r""),
            Price_var.set(r"")          

def search_data():
        conn=pymysql.connect(host='localhost',user='root',password='',database='pharmadb')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from tabdata2 where "+str(search_var.get())+"LIKE"+str(searchTxt_var.get())+"%")

        rows=my_cursor.fetchall()
        if len(rows)!=0:
            tabdata2_table.delete(*tabdata2_table.get_children())
            for i in rows:
                tabdata2_table.insert_("",END,values=i)
            conn.commit()
        conn.close()
        

#=================================================Label===========================================

labeltitle=Label(root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,
                 relief=RIDGE,bg='white',fg='dark green',font=('times new roman',50,'bold'),padx=2,pady=2)
labeltitle.pack(side=TOP,fill=X)  


#================================================DataFrame========================================

DataFrame=Frame(root,bd=15,relief=RIDGE,padx=20)
DataFrame.place(x=0,y=120,width=1525,height=400)

DataFrameleft=LabelFrame(DataFrame,bd=8,relief=RIDGE,padx=1,text="Medicine Information",fg="darkgreen",
                         font=("arial",12,"bold"))
DataFrameleft.place(x=0,y=5,width=850,height=360)

DataFrameright=LabelFrame(DataFrame,bd=8,relief=RIDGE,padx=10,pady=6,text="Medicine Add Department",fg="darkgreen",
                          font=("arial",12,"bold"))
DataFrameright.place(x=860,y=5,width=600,height=360)

#==============================================ButtonsFrame=======================================

ButtonFrame=Frame(root,bd=12,relief=RIDGE,padx=2)
ButtonFrame.place(x=0,y=525,width=1525,height=57)

#============================================MainButton=======================================
BtnAddData=Button(ButtonFrame,command=add_data,text="Medicine Add",font=("arial",13,"bold"),width=15,bg="darkgreen",fg="white")
BtnAddData.grid(row=0,column=0)

BtnUpdateMed=Button(ButtonFrame,command=Update,text="UPDATE",font=("arial",13,"bold"),width=15,bg="darkgreen",fg="white")
BtnUpdateMed.grid(row=0,column=1)

BtnDeleteMed=Button(ButtonFrame,command=delete,text="DELETE",font=("arial",13,"bold"),width=15,bg="Red",fg="white")
BtnDeleteMed.grid(row=0,column=2)


BtnResMed=Button(ButtonFrame,command=reset,text="RESET",font=("arial",13,"bold"),width=15,bg="darkgreen",fg="white")
BtnResMed.grid(row=0,column=3)

BtnExit=Button(ButtonFrame,command=exit,text="EXIT",font=("arial",13,"bold"),width=16,bg="darkgreen",fg="white")
BtnExit.grid(row=0,column=4)

#===========================================Search by==================================================

lblSearch=Label(ButtonFrame,font=('arial',15,'bold'),text='Search by',bg='red',fg='white',padx=20)
lblSearch.grid(row=0,column=5,sticky=W)

# variable

search_var=StringVar()
comSearch=ttk.Combobox(ButtonFrame,textvariable=search_var,font=("arial",15,"bold"),width=12,state='readonly')
comSearch["values"]=('Ref','Medname','Lot')
comSearch.grid(row=0,column=6)
comSearch.current(0)

searchTxt_var=StringVar()
txtserch=Entry(ButtonFrame,textvariable=search_var,bd=3,relief=RIDGE,width=10,font=('arial',17,'bold'))
txtserch.grid(row=0,column=7)

searchBtn=Button(ButtonFrame,command=search_data,text='SEARCH',font=('arial',13,'bold'),width=12,bg='darkgreen',fg='white')
searchBtn.grid(row=0,column=8)

showall=Button(ButtonFrame,text='SHOW ALL',font=('arial',13,'bold'),width=12,bg='darkgreen',fg='white')
showall.grid(row=0,column=9)

#===================================Label And Entry===============================================

lblRefno=Label(DataFrameleft,font=('arial',14,'bold'),text='Refrence no:',padx=2,pady=6)
lblRefno.grid(row=0,column=0,sticky=W)
def cmb():
    conn=pymysql.connect(host='localhost',user='root',password='',database='pharmadb')
    my_cursor=conn.cursor()
    my_cursor.execute("select ref from tabdata1")
    row=my_cursor.fetchall()
    comRefNo=ttk.Combobox(DataFrameleft,textvariable=Ref_var,font=("arial",15,"bold"),width=20,state='readonly')
    list=[]
    for i in row:
        list.append(i[0])
    comRefNo["values"]=list
    comRefNo.grid(row=0,column=1)
cmb()
lblComName=Label(DataFrameleft,font=('arial',14,'bold'),text='Company Name:',padx=2,pady=7)
lblComName.grid(row=1,column=0,sticky=W)
txtComName=Entry(DataFrameleft,textvariable=CmpName_var,bd=3,relief=RIDGE,width=21,font=('arial',14,'bold'))
txtComName.grid(row=1,column=1)


lblTypeMed=Label(DataFrameleft,font=('arial',14,'bold'),text='Type of Medicine:',padx=2,pady=7)
lblTypeMed.grid(row=2,column=0,sticky=W)


comTypeMed=ttk.Combobox(DataFrameleft,textvariable=TypeMed_var,font=("arial",15,"bold"),width=20,state='readonly')
comTypeMed["values"]=('Tablets','Liquid','Capsules','Topical Medicines','Drops','Inhales','Injection')
comTypeMed.grid(row=2,column=1)
comTypeMed.current(0)

lblMedName=Label(DataFrameleft,font=('arial',14,'bold'),text='Medicine Name:',padx=2,pady=7)
lblMedName.grid(row=3,column=0,sticky=W)

def dmb():
    conn=pymysql.connect(host='localhost',user='root',password='',database='pharmadb')
    my_cursor=conn.cursor()
    my_cursor.execute("select medname from tabdata1")
    med=my_cursor.fetchall()


    comMedName=ttk.Combobox(DataFrameleft,textvariable=MedName_var,font=("arial",15,"bold"),width=20,state='readonly')
    comMedName["values"]=med
    comMedName.grid(row=3,column=1)
dmb()

lblLotno=Label(DataFrameleft,font=('arial',14,'bold'),text='Lot Number :',padx=2,pady=7)
lblLotno.grid(row=4,column=0,sticky=W)
txtLotno=Entry(DataFrameleft,textvariable=Lot_var,bd=3,relief=RIDGE,width=21,font=('arial',14,'bold'))
txtLotno.grid(row=4,column=1)

lblIssuedate=Label(DataFrameleft,font=('arial',14,'bold'),text='Issue Date:',padx=2,pady=6)
lblIssuedate.grid(row=5,column=0,sticky=W)
txtIssuedate=Entry(DataFrameleft,textvariable=Issuedate_var,bd=3,relief=RIDGE,width=21,font=('arial',14,'bold'))
txtIssuedate.grid(row=5,column=1)

lblExpDate=Label(DataFrameleft,font=('arial',14,'bold'),text='Exp Date:',padx=2,pady=6)
lblExpDate.grid(row=6,column=0,sticky=W)
txtExpDate=Entry(DataFrameleft,textvariable=Expdate_var,bd=3,relief=RIDGE,width=21,font=('arial',14,'bold'))
txtExpDate.grid(row=6,column=1)

lblUses=Label(DataFrameleft,font=('arial',14,'bold'),text='Uses:',padx=15,pady=6)
lblUses.grid(row=0,column=2,sticky=W)
txtUses=Entry(DataFrameleft,textvariable=Ussess_var,bd=3,relief=RIDGE,width=21,font=('arial',14,'bold'))
txtUses.grid(row=0,column=3)

lblSideEffect=Label(DataFrameleft,font=('arial',14,'bold'),text='Side Effect:',padx=15,pady=6)
lblSideEffect.grid(row=1,column=2,sticky=W)
txtSideEffect=Entry(DataFrameleft,textvariable=Sideeffect_var,bd=3,relief=RIDGE,width=21,font=('arial',14,'bold'))
txtSideEffect.grid(row=1,column=3)


lblPreWarning=Label(DataFrameleft,font=('arial',14,'bold'),text='Prec&Warning:',padx=15,pady=6)
lblPreWarning.grid(row=2,column=2,sticky=W)
txtPreWarning=Entry(DataFrameleft,textvariable=Warning_var,bd=3,relief=RIDGE,width=21,font=('arial',14,'bold'))
txtPreWarning.grid(row=2,column=3)

lblDosage=Label(DataFrameleft,font=('arial',14,'bold'),text='Dosage:',padx=15,pady=6)
lblDosage.grid(row=3,column=2,sticky=W)
txtDosage=Entry(DataFrameleft,textvariable=Dosage_var,bd=3,relief=RIDGE,width=21,font=('arial',14,'bold'))
txtDosage.grid(row=3,column=3)

lblTabPrice=Label(DataFrameleft,font=('arial',14,'bold'),text='Tablet Price:',padx=15,pady=6)
lblTabPrice.grid(row=4,column=2,sticky=W)
txtTabPrice=Entry(DataFrameleft,textvariable=Price_var,bd=3,relief=RIDGE,width=21,font=('arial',14,'bold'))
txtTabPrice.grid(row=4,column=3)

lblProductQT=Label(DataFrameleft,font=('arial',14,'bold'),text='Product QT:',padx=2,pady=7)
lblProductQT.grid(row=7,column=0,sticky=W)
txtProductQT=Entry(DataFrameleft,textvariable=Product_var,bd=3,relief=RIDGE,width=21,font=('arial',14,'bold'))
txtProductQT.grid(row=7,column=1)

#==================================DataFrame Right===================================

lblRefno=Label(DataFrameright,font=('arial',12,'bold'),text='Refrence No. :')
lblRefno.grid(row=135,column=60,sticky=W)
txtRefno=Entry(DataFrameright,textvariable=refmed_var,bd=3,relief=RIDGE,width=23,font=('arial',15,'bold'))
txtRefno.grid(row=135,column=80)

lblMedname=Label(DataFrameright,font=('arial',12,'bold'),text='Medicine name :',pady=6)
lblMedname.grid(row=136,column=60,sticky=W)
txtMedname=Entry(DataFrameright,textvariable=addmed_var,bd=3,relief=RIDGE,width=23,font=('arial',15,'bold'))
txtMedname.grid(row=136,column=80)

#===================================Side Freame======================================

SideFrame=Frame(DataFrameright,bd=4,relief=RIDGE,bg='white')
SideFrame.place(x=0,y=80,width=290,height=180)

sc_x=ttk.Scrollbar(SideFrame,orient=HORIZONTAL)
sc_x.pack(side=BOTTOM,fill=X)
sc_y=ttk.Scrollbar(SideFrame,orient=VERTICAL)
sc_y.pack(side=RIGHT,fill=Y)

Medicine_table=ttk.Treeview(SideFrame,column=('ref','Medname'),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

sc_x.config(command=Medicine_table.xview)
sc_y.config(command=Medicine_table.yview)

Medicine_table.heading('ref',text='Ref')
Medicine_table.heading('Medname',text='Medicine Name')

Medicine_table["show"]="headings"
Medicine_table.pack(fill=BOTH,expand=1)

Medicine_table.column('ref',width=100)
Medicine_table.column('Medname',width=100)

Medicine_table.bind("<ButtonRelease-1>",Medget_cursor)

#===========================================Medicine Add Buttons===================================

down_frame=Frame(DataFrameright,bd=4,relief=RIDGE,bg='darkgreen')
down_frame.place(x=300,y=80,width=90,height=180)

btnAddmed=Button(down_frame,command=Addmed,text='ADD',font=('arial',10,'bold'),width=9,bg='lime',fg='white',pady=8)
btnAddmed.grid(row=0,column=0)

btnUpdatemed=Button(down_frame,command=UpdateMed,text='UPDATE',font=('arial',10,'bold'),width=9,bg='purple',fg='white',pady=9)
btnUpdatemed.grid(row=1,column=0)

btnDeletemed=Button(down_frame,command=DeleteMed,text='DELETE',font=('arial',10,'bold'),width=9,bg='red',fg='white',pady=9)
btnDeletemed.grid(row=2,column=0)

btnClearmed=Button(down_frame,command=ClearMed,text='CLEAR',font=('arial',10,'bold'),width=9,bg='orange',fg='white',pady=8)
btnClearmed.grid(row=3,column=0)

#=========================================Frame Detail=========================================

FrameDetails=Frame(root,bd=2,relief=RIDGE)
FrameDetails.place(x=0,y=590,width=1525,height=170)

#==================================Main Table & Scroll Bar=======================================

Table_Frame=Frame(FrameDetails,bd=10,relief=RIDGE,padx=20)
Table_Frame.place(x=0,y=1,width=1525,height=170)

scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
scroll_y.pack(side=RIGHT,fill=Y)

pharmacy_table=ttk.Treeview(Table_Frame,column=('ref','companyname','type','tabname','lotno','issuedate','expdate','productqt',
                            'uses','sideeffect','warning','dosage','price'),
                            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=pharmacy_table.xview)
scroll_y.config(command=pharmacy_table.yview)

pharmacy_table["show"]="headings"

pharmacy_table.heading("ref",text="Refrence No")
pharmacy_table.heading("companyname",text="Company Name")
pharmacy_table.heading("type",text="Type of Medicine")
pharmacy_table.heading("tabname",text="MedName")
pharmacy_table.heading("lotno",text="Lot No")
pharmacy_table.heading("issuedate",text="Issue Date")
pharmacy_table.heading("expdate",text="Exp Date")
pharmacy_table.heading("productqt",text="Product QT")
pharmacy_table.heading("uses",text="Uses")
pharmacy_table.heading("sideeffect",text="Side Effect")
pharmacy_table.heading("warning",text="Warning")
pharmacy_table.heading("dosage",text="Dosage")
pharmacy_table.heading("price",text="Price")
pharmacy_table.pack(fill=BOTH,expand=1)

pharmacy_table.column("ref",width=100)
pharmacy_table.column("companyname",width=100)
pharmacy_table.column("type",width=100)
pharmacy_table.column("tabname",width=100)
pharmacy_table.column("lotno",width=100)
pharmacy_table.column("issuedate",width=100)
pharmacy_table.column("expdate",width=100)
pharmacy_table.column("productqt",width=100)
pharmacy_table.column("uses",width=100)
pharmacy_table.column("sideeffect",width=100)
pharmacy_table.column("warning",width=100)
pharmacy_table.column("dosage",width=100)
pharmacy_table.column("price",width=100)
fetch_datamed()
fetch_data()
pharmacy_table.bind("<ButtonRelease-1>",get_cursor)

























root.mainloop()