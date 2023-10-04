from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
      def __init__(self,root):
            self.root=root
            self.root.title("Library Management System")
            self.root.geometry("1550x800+0+0")

            self.member_var=StringVar()
            self.prn_var=StringVar()
            self.id_var=StringVar()
            self.firstname_var=StringVar()
            self.lastname_var=StringVar()
            self.address1_var=StringVar()
            self.address2_var=StringVar()
            self.postcode_var=StringVar()
            self.mobile_var=StringVar()
            self.bookid_var=StringVar()
            self.booktitle_var=StringVar()
            self.author_var=StringVar()
            self.dateborrowed_var=StringVar()
            self.datedue_var=StringVar()
            self.daysonbook_var=StringVar()
            self.latereturnfine_var=StringVar()
            self.dateoverdue_var=StringVar()
            self.finalprice_var=StringVar()
              
              
            lbtitle=Label(self.root, text="Library Management System", bg="powder blue", fg="black",bd=20, relief=RIDGE, font=("times new roman",50,"bold"),padx=2,pady=6)
            lbtitle.pack(side=TOP,fill=X)

            frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
            frame.place(x=0,y=130,width=1468,height=400)

#========Dataframeleft=====#

            DataFrameLeft=LabelFrame(frame,text="Library Memebership Information", bg="powder blue", fg="black",bd=12, relief=RIDGE, font=("times new roman",12,"bold"),padx=2,pady=6)
            DataFrameLeft.place(x=0,y=5,width=750,height=350)

#============Buttons=======#

            lblMember=Label(DataFrameLeft,bg="powder blue", text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblMember.grid(row=0,column=0,sticky=W)


            comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",15,"bold"),width=27,state="readonly")
            comMember["value"]=("Admin Staff","student", "Lecturer")
            comMember.grid(row=0,column=1)


            lblPRN_NO=Label(DataFrameLeft,bg="powder blue", text="PRN NO",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblPRN_NO.grid(row=1,column=0,sticky=W)
            txtPRN_NO=Entry(DataFrameLeft,textvariable=self.prn_var,font=("times new roman",15,"bold"),width=29)
            txtPRN_NO.grid(row=1,column=1)


            lblID=Label(DataFrameLeft,bg="powder blue", text="ID NO",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblID.grid(row=2,column=0,sticky=W)
            txtID=Entry(DataFrameLeft,textvariable=self.id_var,font=("times new roman",15,"bold"),width=29)
            txtID.grid(row=2,column=1)


            lblFirstname=Label(DataFrameLeft,bg="powder blue", text="First Name",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblFirstname.grid(row=3,column=0,sticky=W)
            txtFirstname=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("times new roman",15,"bold"),width=29)
            txtFirstname.grid(row=3,column=1)



            lblLastname=Label(DataFrameLeft,bg="powder blue", text="Last Name",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblLastname.grid(row=4,column=0,sticky=W)
            txtLastname=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("times new roman",15,"bold"),width=29)
            txtLastname.grid(row=4,column=1)


            lblAddress1=Label(DataFrameLeft,bg="powder blue", text="Address 1",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblAddress1.grid(row=5,column=0,sticky=W)
            txtAddress1=Entry(DataFrameLeft, textvariable=self.address1_var,font=("times new roman",15,"bold"),width=29)
            txtAddress1.grid(row=5,column=1)



            lblAddress2=Label(DataFrameLeft,bg="powder blue", text="Address 2",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblAddress2.grid(row=6,column=0,sticky=W)
            txtAddress2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("times new roman",15,"bold"),width=29)
            txtAddress2.grid(row=6,column=1)



            lblPostcode=Label(DataFrameLeft,bg="powder blue", text="Pin Code",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblPostcode.grid(row=7,column=0,sticky=W)
            txtPostcode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("times new roman",15,"bold"),width=29)
            txtPostcode.grid(row=7,column=1)


            lblMobile=Label(DataFrameLeft,bg="powder blue", text="Mobile",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblMobile.grid(row=8,column=0,sticky=W)
            txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("times new roman",15,"bold"),width=29)
            txtMobile.grid(row=8,column=1)





            lblBookid=Label(DataFrameLeft,bg="powder blue", text="Book ID",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblBookid.grid(row=0,column=2,sticky=W)
            txtBookid=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("times new roman",15,"bold"),width=29)
            txtBookid.grid(row=0,column=3)

            lblBooktitle=Label(DataFrameLeft,bg="powder blue", text="Book Title",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblBooktitle.grid(row=1,column=2,sticky=W)
            txtbooktitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("times new roman",15,"bold"),width=29)
            txtbooktitle.grid(row=1,column=3)

            lblAuthor=Label(DataFrameLeft,bg="powder blue", text="Author",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblAuthor.grid(row=2,column=2,sticky=W)
            txtAuthor=Entry(DataFrameLeft,textvariable=self.author_var,font=("times new roman",15,"bold"),width=29)
            txtAuthor.grid(row=2,column=3)

            lblDateborrowed=Label(DataFrameLeft,bg="powder blue", text="Date Borrowed",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblDateborrowed.grid(row=3,column=2,sticky=W)
            txtDateborrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("times new roman",15,"bold"),width=29)
            txtDateborrowed.grid(row=3,column=3)

            lblDuedate=Label(DataFrameLeft,bg="powder blue", text="Due Date",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblDuedate.grid(row=4,column=2,sticky=W)
            txtDuedate=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("times new roman",15,"bold"),width=29)
            txtDuedate.grid(row=4,column=3)

            lblDaysonbook=Label(DataFrameLeft,bg="powder blue", text="Days on Book",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblDaysonbook.grid(row=5,column=2,sticky=W)
            txtDaysonbook=Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("times new roman",15,"bold"),width=29)
            txtDaysonbook.grid(row=5,column=3)

            lblLatereturnfine=Label(DataFrameLeft,bg="powder blue", text="Late Return Fine",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblLatereturnfine.grid(row=6,column=2,sticky=W)
            txtLatereturnfine=Entry(DataFrameLeft,textvariable=self.latereturnfine_var,font=("times new roman",15,"bold"),width=29)
            txtLatereturnfine.grid(row=6,column=3)

            lblDateoverdue=Label(DataFrameLeft,bg="powder blue", text="Date Over Due",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblDateoverdue.grid(row=7,column=2,sticky=W)
            txtDateoverdue=Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("times new roman",15,"bold"),width=29)
            txtDateoverdue.grid(row=7,column=3)

            lblActualprice=Label(DataFrameLeft,bg="powder blue", text="Actual Price",font=("times new roman",15,"bold"),padx=2,pady=6)
            lblActualprice.grid(row=8,column=2,sticky=W)
            txtActualprice=Entry(DataFrameLeft,textvariable=self.finalprice_var,font=("times new roman",15,"bold"),width=29)
            txtActualprice.grid(row=8,column=3)


#=================Dataframeright=======#

            DataFrameRight=LabelFrame(frame,text="Book Details", bg="powder blue", fg="black",bd=12, relief=RIDGE, font=("times new roman",12,"bold"),padx=2,pady=6)
            DataFrameRight.place(x=800,y=5,width=600,height=350)

            self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=41,height=21,padx=2,pady=6)
            self.txtBox.grid(row=0,column=2)

            listScrollBar=Scrollbar(DataFrameRight)
            listScrollBar.grid(row=0,column=1,sticky="ns")

            listBooks=["Mistborn: Final Empire","Mistborn: Well Of Ascension","Mistborn: Hero Of Ages","Harry Potter:Chamber Of Secrets","The Silent Patient","The Maidens",
                   "Elantris","The Seven Husbands Of Evelyn Hugo","Daisy Jones And The Six","Percy Jackson",
                   "Anxious People","Angels And Demons","Inferno","The Da Vinci Code","Origin","Harry Potter:Prisoner Of Azkaban","Harry Potter: Goblet Of Fire","Harry Potter: Order Of The Phoenix","Harry Potter: The Half Blood Prince"]
        

            def SelectBook(event=""):
                  value=str(listBox.get(listBox.curselection()))
                  x=value 
                  if(x=="Mistborn: Final Empire"):
                        self.bookid_var.set("BKID001")
                        self.booktitle_var.set("Fantasy")
                        self.author_var.set("Brandon Sanderson")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2 
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="Mistborn: Well Of Ascension"):
                        self.bookid_var.set("BKID002")
                        self.booktitle_var.set("Fantasy")
                        self.author_var.set("Brandon Sanderson")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.70")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="Mistborn: Hero Of Ages"):
                        self.bookid_var.set("BKID003")
                        self.booktitle_var.set("Fantasy")
                        self.author_var.set("Brandon Sanderson")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="Harry Potter:Chamber Of Secrets"):
                        self.bookid_var.set("BKID004")
                        self.booktitle_var.set("Fantasy")
                        self.author_var.set("J.K.Rowling")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="The Silent Patient"):
                        self.bookid_var.set("BKID005")
                        self.booktitle_var.set("Fiction")
                        self.author_var.set("Alex Michaelides")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="The Maidens"):
                        self.bookid_var.set("BKID006")
                        self.booktitle_var.set("Fiction")
                        self.author_var.set("Alex Michaelides")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="Elantris"):
                        self.bookid_var.set("BKID007")
                        self.booktitle_var.set("Fantasy")
                        self.author_var.set("Brandon Sanderson")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="The Seven Husbands Of Evelyn Hugo"):
                        self.bookid_var.set("BKID008")
                        self.booktitle_var.set("Fiction")
                        self.author_var.set("Taylor Jenkins Reid")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="Daisy Jones And The Six"):
                        self.bookid_var.set("BKID009")
                        self.booktitle_var.set("Fiction")
                        self.author_var.set("Taylor Jenkins Reid")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")
                  

                  elif(x=="Percy Jackson"):
                        self.bookid_var.set("BKID010")
                        self.booktitle_var.set("Fantasy")
                        self.author_var.set("Rick Riodan")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="Anxious People"):
                        self.bookid_var.set("BKID011")
                        self.booktitle_var.set("Comedy")
                        self.author_var.set("Frederik Backman")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="Angels And Demons"):
                        self.bookid_var.set("BKID012")
                        self.booktitle_var.set("Fiction")
                        self.author_var.set("Dan Brown")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="Inferno"):
                        self.bookid_var.set("BKID013")
                        self.booktitle_var.set("Fiction")
                        self.author_var.set("Dan Brown")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="THe Da Vinci Code"):
                        self.bookid_var.set("BKID013")
                        self.booktitle_var.set("Fiction")
                        self.author_var.set("Dan Brown")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="Origin"):
                        self.bookid_var.set("BKID014")
                        self.booktitle_var.set("Fiction")
                        self.author_var.set("Dan Brown")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="Harry Potter: Prisoner Of Azkaban"):
                        self.bookid_var.set("BKID015")
                        self.booktitle_var.set("Fantasy")
                        self.author_var.set("J.K.Rowling")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="Harry Potter: Goblet Of Fire"):
                        self.bookid_var.set("BKID016")
                        self.booktitle_var.set("Fantasy")
                        self.author_var.set("J.K.Rowling")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")


                  elif(x=="Harry Potter: Order Of The Phoenix"):
                        self.bookid_var.set("BKID017")
                        self.booktitle_var.set("Fantasy")
                        self.author_var.set("J.K.Rowling")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var.set("No")
                        self.finalprice_var.set("Rs.500")

                  elif(x=="Harry Potter: The Half Blood Prince"):
                        self.bookid_var.set("BKID018")
                        self.booktitle_var.set("Fantasy")
                        self.author_var.set("J.K.Rowling")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook.set(15)
                        self.latereturnfine_var.set("Rs.60")
                        self.dateoverdue_var("No")
                        self.finalprice_var("Rs.500")



            listBox=Listbox(DataFrameRight,font=("times new roman",15,"bold"),width=36,height=17)
            listBox.bind("<<ListboxSelect>>",SelectBook)
            listBox.grid(row=0,column=0,padx=4)
            listScrollBar.config(command=listBox.yview)


            for item in listBooks:
                  listBox.insert(END, item)


#=================Button Frame===========#

            Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
            Framebutton.place(x=0,y=530,width=1468,height=70)

            btnAddData=Button(Framebutton,text="Add Data",command=self.add_data,font=("times new roman",15,"bold"),width=23,bg="Blue", fg="Black")
            btnAddData.grid(row=0,column=0)

            btnShowData=Button(Framebutton, text="Show Data",command=self.showData, font=("times new roman",15,"bold"),width=23,bg="Blue", fg="Black")
            btnShowData.grid(row=0,column=1)

            btnUpdateData=Button(Framebutton, text="Update",command=self.update, font=("times new roman",15,"bold"),width=23,bg="Blue", fg="Black")
            btnUpdateData.grid(row=0,column=2)

            btnDeleteData=Button(Framebutton, text="Delete",command=self.delete,font=("times new roman",15,"bold"),width=23,bg="Blue", fg="Black")
            btnDeleteData.grid(row=0,column=3)
        
            btnResetData=Button(Framebutton, text="Reset",command=self.reset, font=("times new roman",15,"bold"),width=23,bg="Blue", fg="Black")
            btnResetData.grid(row=0,column=4)

            btnExit=Button(Framebutton, text="Exit",command=self.iExit, font=("times new roman",15,"bold"),width=23,bg="Blue", fg="Black")
            btnExit.grid(row=0,column=5)

#=================Information Frame===========#

            Framedetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
            Framedetails.place(x=0,y=600,width=1468,height=310)

            Table_frame=Frame(Framedetails,bd=6, relief=RIDGE, bg="powder blue")
            Table_frame.place(x=0,y=2,width=1410,height=270)


            xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
            yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


            self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2","postid",
                                                           "mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine",
                                                           "dateoverdue","finalprice"),xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        

            xscroll.pack(side=BOTTOM,fill=X)
            yscroll.pack(side=RIGHT,fill=Y)
            xscroll.config(command=self.library_table.xview)
            yscroll.config(command=self.library_table.yview)

            self.library_table.heading("membertype",text="Member Type")
            self.library_table.heading("prnno",text="Reference No")
            self.library_table.heading("title",text="Title")
            self.library_table.heading("firstname",text="First Name")
            self.library_table.heading("lastname",text="Last Name")
            self.library_table.heading("address1",text="Address 1")
            self.library_table.heading("address2",text="Address 2")
            self.library_table.heading("postid",text="Post ID")
            self.library_table.heading("mobile",text="Mobile")
            self.library_table.heading("bookid",text="Book ID")
            self.library_table.heading("booktitle",text="Book Title")
            self.library_table.heading("author",text="Author")
            self.library_table.heading("dateborrowed",text="Date Borrowed")
            self.library_table.heading("datedue",text="Due Date")
            self.library_table.heading("days",text="Days On Book")
            self.library_table.heading("latereturnfine",text="Late Return Fine")
            self.library_table.heading("dateoverdue",text="Date Over Due")
            self.library_table.heading("finalprice",text="Final Price")



            self.library_table["show"]="headings"
            self.library_table.pack(fill=BOTH,expand=1)
            self.library_table.column("membertype",width=100)
            self.library_table.column("prnno",width=100)
            self.library_table.column("title",width=100)
            self.library_table.column("firstname",width=100)
            self.library_table.column("lastname",width=100)
            self.library_table.column("address1",width=100)
            self.library_table.column("address2",width=100)
            self.library_table.column("postid",width=100)
            self.library_table.column("mobile",width=100)
            self.library_table.column("bookid",width=100)
            self.library_table.column("booktitle",width=100)
            self.library_table.column("author",width=100)
            self.library_table.column("dateborrowed",width=100)
            self.library_table.column("datedue",width=100)
            self.library_table.column("days",width=100)
            self.library_table.column("latereturnfine",width=100)
            self.library_table.column("dateoverdue",width=100)
            self.library_table.column("finalprice",width=100)

            self.fetch_data()
            self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


      def add_data(self):
            conn=mysql.connector.connect(host="localhost",username="root", password="AGPagp001*",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                   self.member_var.get(),
                                                                                                                   self.prn_var.get(),
                                                                                                                   self.id_var.get(),
                                                                                                                   self.firstname_var.get(),
                                                                                                                   self.lastname_var.get(),
                                                                                                                   self.address1_var.get(),
                                                                                                                   self.address2_var.get(),
                                                                                                                   self.postcode_var.get(),
                                                                                                                   self.mobile_var.get(),
                                                                                                                   self.bookid_var.get(),
                                                                                                                   self.booktitle_var.get(),
                                                                                                                   self.author_var.get(),
                                                                                                                   self.dateborrowed_var.get(),
                                                                                                                   self.datedue_var.get(),
                                                                                                                   self.daysonbook_var.get(),
                                                                                                                   self.latereturnfine_var.get(),
                                                                                                                   self.dateoverdue_var.get(),
                                                                                                                   self.finalprice_var.get(),
                                                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success","Member has been inserted successfully.")

      def update(self):
            conn=mysql.connector.connect(host="localhost",username="root", password="AGPagp001*",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update library set Member_Type=%s,ID=%s,First_Name=%s,Last_Name=%s,Address_1=%s,Address_2=%s,Post_Code=%s,Mobile=%s,Book_ID=%s,Book_Title=%s,Author=%s,Borrow_Date=%s,Due_Date=%s,Days_On_Book=%s,Late_Return_Fine=%s,Date_Over_Due=%s,Final_Price=%s where Ref_No=%s",(
                                                                                                                  self.member_var.get(),
                                                                                                                  self.id_var.get(),
                                                                                                                  self.firstname_var.get(),
                                                                                                                  self.lastname_var.get(),
                                                                                                                  self.address1_var.get(),
                                                                                                                  self.address2_var.get(),
                                                                                                                  self.postcode_var.get(),
                                                                                                                  self.mobile_var.get(),
                                                                                                                  self.bookid_var.get(),
                                                                                                                  self.booktitle_var.get(),
                                                                                                                  self.author_var.get(),
                                                                                                                  self.dateborrowed_var.get(),
                                                                                                                  self.datedue_var.get(),
                                                                                                                  self.daysonbook_var.get(),
                                                                                                                  self.latereturnfine_var.get(),
                                                                                                                  self.dateoverdue_var.get(),
                                                                                                                  self.finalprice_var.get(),
                                                                                                                  self.prn_var.get(),                                                                                                                                                                                                
            ))
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been updated.")




      def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root", password="AGPagp001*",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select* from library")
            rows=my_cursor.fetchall()

            if len(rows)!=0:
                  self.library_table.delete(*self.library_table.get_children())
                  for i in rows:
                        self.library_table.insert("",END,values=i)
                  conn.commit()
            conn.close()

      def get_cursor(self,event=""):
            cursor_row=self.library_table.focus()
            content=self.library_table.item(cursor_row)
            row=content['values']

            self.member_var.set(row[0]),
            self.prn_var.set(row[1]),
            self.id_var.set(row[2]),
            self.firstname_var.set(row[3]),
            self.lastname_var.set(row[4]),
            self.address1_var.set(row[5]),
            self.address2_var.set(row[6]),
            self.postcode_var.set(row[7]),
            self.mobile_var.set(row[8]),
            self.bookid_var.set(row[9]),
            self.booktitle_var.set(row[10]),
            self.author_var.set(row[11]),
            self.dateborrowed_var.set(row[12]),
            self.datedue_var.set(row[13]),
            self.daysonbook_var.set(row[14]),
            self.latereturnfine_var.set(row[15]),
            self.dateoverdue_var.set(row[16]),
            self.finalprice_var.set(row[17])

      def showData(self):
            self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n"),
            self.txtBox.insert(END,"PRN No\t\t"+self.prn_var.get()+"\n"),
            self.txtBox.insert(END,"ID NO\t\t"+self.id_var.get()+"\n"),
            self.txtBox.insert(END,"First Name\t\t"+self.firstname_var.get()+"\n"),
            self.txtBox.insert(END,"Last Name\t\t"+self.lastname_var.get()+"\n"),
            self.txtBox.insert(END,"Address 1\t\t"+self.address1_var.get()+"\n"),
            self.txtBox.insert(END,"Address 2\t\t"+self.address2_var.get()+"\n"),
            self.txtBox.insert(END,"Post Code\t\t"+self.postcode_var.get()+"\n"),
            self.txtBox.insert(END,"Mobile\t\t"+self.mobile_var.get()+"\n"),
            self.txtBox.insert(END,"Book ID\t\t"+self.bookid_var.get()+"\n"),
            self.txtBox.insert(END,"Book Title\t\t"+self.booktitle_var.get()+"\n"),
            self.txtBox.insert(END,"Author\t\t"+self.author_var.get()+"\n"),
            self.txtBox.insert(END,"Borrow Date\t\t"+self.dateborrowed_var.get()+"\n"),
            self.txtBox.insert(END,"Due Date\t\t"+self.datedue_var.get()+"\n"),
            self.txtBox.insert(END,"Days On Book\t\t"+self.daysonbook_var.get()+"\n"),
            self.txtBox.insert(END,"Late Return Fine\t\t"+self.latereturnfine_var.get()+"\n"),
            self.txtBox.insert(END,"Date Over Due\t\t"+self.dateoverdue_var.get()+"\n"),
            self.txtBox.insert(END,"Final Price\t\t"+self.finalprice_var.get()+"\n")
            

      def reset(self):
            self.member_var.set(""),
            self.prn_var.set(""),
            self.id_var.set(""),
            self.firstname_var.set(""),
            self.lastname_var.set(""),
            self.address1_var.set(""),
            self.address2_var.set(""),
            self.postcode_var.set(""),
            self.mobile_var.set(""),
            self.bookid_var.set(""),
            self.booktitle_var.set(""),
            self.author_var.set(""),
            self.dateborrowed_var.set(""),
            self.datedue_var.set(""),
            self.daysonbook_var.set(""),
            self.latereturnfine_var.set(""),
            self.dateoverdue_var.set(""),
            self.finalprice_var.set("")


      def iExit(self):
            iExit=tkinter.messagebox.askyesno("Library Management System","Are you sure you want to exit ?")
            if iExit>0:
                  self.root.destroy()
                  return 
            

      def delete(self):
            if self.prn_var.get()=="" or self.id_var.get()=="":
                  messagebox.showerror("Error", "Select member first.")
            else:
                  conn=mysql.connector.connect(host="localhost",username="root", password="AGPagp001*",database="mydata")
                  my_cursor=conn.cursor()
                  query="delete from library where Ref_No=%s"
                  value=(self.prn_var.get(),)
                  my_cursor.execute(query,value)



                  conn.commit()
                  self.fetch_data()
                  self.reset()
                  conn.close()


                  messagebox.showinfo("Success","member has been deleted")




if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
    