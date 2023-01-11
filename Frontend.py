from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import Error

try: 
    conn = mysql.connector.connect(host='localhost', database='pes1ug20cs461_blood_bank', user='root',password='') 
    if conn.is_connected():
        cursor=conn.cursor() 
        window = Tk()
        window.title("DBMS")
        # window.geometry("1250x675")
        window.configure(bg='#ec5454')
        window.attributes('-fullscreen',True)

        frame = Frame(window)
        # frame.grid()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        #image file
        # Create an object of tkinter ImageTk
        img = ImageTk.PhotoImage(Image.open("image_for_frontend.png"))
        label = Label(frame, image = img)
        label.grid()
        lb1=Label(window,text="BLOOD BANK",bg='#ec5050',font=("Times New Roman",50))
        lb1.grid(row=4,padx=425)


#function of Registering a person on first window    
        def onClickRegister():
            sub1 = Tk()
            sub1.title("Registration")
            sub1.configure(bg='#ec5050')
            sub1.geometry("1030x525")

            lb1=Label(sub1,text="To register a person enter the following details and click the submit button",bg='#ec5454',font=("Times New Roman",17))
            lb1.grid(row=2,columnspan=5)

            def add_data():
                pid = e1.get()
                fname = e2.get()
                lname = e3.get()
                dob = e4.get()
                address = e5.get()
                sex = e6.get()
                phone = e7.get()
                height = float(e8.get())
                weight = float(e9.get())
                can = e10.get()
                last = e11.get()
                query="INSERT INTO `461_PERSON` VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                data=(pid,fname,lname,dob,address,sex,phone,height,weight,can,last)
                print(query,data)
                cursor.execute(query,data)
                conn.commit()
                print("INSERTED SUCESSFULLY")
                
            def del_data():
                query="DELETE FROM `461_PERSON` WHERE "
                data=(edel.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("DELETED SUCESSFULLY")

            def update_data():
                query="UPDATE `461_PERSON` SET "
                data = (eup.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("UPDATED SUCESSFULLY")

            #Data for the table 
            lb3= Label(sub1,text="Enter PID",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=4)
            e1= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e1.grid(row=5,pady=10,padx=10)

            lb3= Label(sub1,text="Enter First Name",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=4,column=2)
            e2= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e2.grid(row=5,column=2,padx=10)

            lb3= Label(sub1,text="Enter Last Name",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=4,column=3)
            e3= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e3.grid(row=5,column=3)

            lb3= Label(sub1,text="Enter DOB in yyyy-mm-dd format",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=6)
            e4= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e4.grid(row=7,pady=10)

            lb3= Label(sub1,text="Enter Address",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=6,column=2)
            e5= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e5.grid(row=7,column=2)

            lb3= Label(sub1,text="Enter Gender",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=6,column=3)
            e6= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e6.grid(row=7,column=3)

            lb3= Label(sub1,text="Enter phone number",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=8)
            e7= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e7.grid(row=9,pady=10)

            lb3= Label(sub1,text="Enter height",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=8,column=2)
            e8= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e8.grid(row=9,column=2)

            lb3= Label(sub1,text="Enter weight",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=8,column=3)
            e9= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e9.grid(row=9,column=3)

            lb3= Label(sub1,text="Enter can_donate",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=10)
            
            e10= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e10.grid(row=11,pady=10)
            
            lb3= Label(sub1,text="Enter last_donation",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=10,column=2)
            
            e11= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e11.grid(row=11,column=2)
            
            b1 = Button(sub1,  text='Add Record',font=("Footlight MT Light",17) ,command=add_data,bg='#71f55f')  
            b1.grid(row=11,column=3)
            
            lb3= Label(sub1,text="DELETE FROM `461_PERSON` WHERE",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=15,pady=10)
            edel= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            edel.grid(row=16,pady=10)
            b1 = Button(sub1,  text='Delete Record',font=("Footlight MT Light",17) ,command=del_data,bg='#71f55f')  
            b1.grid(row=17, pady=10)

            lb3= Label(sub1,text="UPDATE `461_PERSON` SET",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=15,pady=10,column=2)
            eup= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            eup.grid(row=16,pady=10,column=2)
            b2 = Button(sub1,  text='Update Record', font=("Footlight MT Light",17) , command=update_data,bg='#71f55f')  
            b2.grid(row=17,pady=10,column=2)

            #function of END on second window 
            def display_key():
                lb1=Label(window,text="Thank you for Registering",bg='#ec5050',font=("Footlight MT Light",20))
                lb1.grid(pady=5)
            btn_2 = Button(sub1, text="CLOSE", font=("Footlight MT Light",17) ,command=lambda:[sub1.destroy(),display_key()],bg="#71f55f")
            btn_2.grid(pady=10,columnspan=5)
        bt1=Button(window,text="REGISTER PERSON",font=("Footlight MT Light",17),command= onClickRegister,bg="#71f55f" )
        bt1.grid(row=7,pady=10)

#function of Donating blood on first window    
        def onClickDonate():
            sub1 = Tk()
            sub1.title("Donation")
            sub1.configure(bg='#ec5050')
            sub1.geometry("1200x525")
            lb1=Label(sub1,text="To donate blood enter the following details and click the submit button",bg='#ec5050',font=("Times New Roman",17))
            lb1.grid(row=2,columnspan=5)

            #Data for the table 
            def add_data():
                did = e1.get()
                dod = e2.get()
                type = e3.get()
                amt = float(e4.get())
                bg = e5.get()
                fpid = e6.get()
                feid = e7.get()
                query="INSERT INTO `461_DONATION` VALUES(%s,%s,%s,%s,%s,%s,%s)"
                data=(did,dod,type,amt,bg,fpid,feid)
                print(query,data)
                cursor.execute(query,data)
                conn.commit()
                print("INSERTED SUCESSFULLY")
                
            def del_data():
                query="DELETE FROM `461_DONATION` WHERE "
                data=(edel.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("DELETED SUCESSFULLY")

            def update_data():
                query="UPDATE `461_DONATION` SET "
                data = (eup.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("UPDATED SUCESSFULLY")

            #Data for the table 
            lb3= Label(sub1,text="Enter DID",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=4)
            e1= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e1.grid(row=5,pady=10,padx=10)

            lb3= Label(sub1,text="Enter date of donation in yyyy-mm-dd format",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=4,column=2)
            e2= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e2.grid(row=5,column=2,padx=10)

            lb3= Label(sub1,text="Enter Type: Blood, Platelets or Plasma",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=4,column=3)
            e3= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e3.grid(row=5,column=3)

            lb3= Label(sub1,text="Enter quantity",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=6)
            e4= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e4.grid(row=7,pady=10)

            lb3= Label(sub1,text="Enter blood group",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=6,column=2)
            e5= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e5.grid(row=7,column=2)

            lb3= Label(sub1,text="Enter Patient ID: (P_XX)",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=6,column=3)
            e6= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e6.grid(row=7,column=3)

            lb3= Label(sub1,text="Enter Employee ID of nurse who took the donation: (E_XX)",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=9,column=2)
            e7= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e7.grid(row=10,column=2,pady=10)

            b1 = Button(sub1,  text='Add Record',font=("Footlight MT Light",17) ,command=add_data,bg='#71f55f')
            b1.grid(row=10,column=3)
            
            lb3= Label(sub1,text="DELETE FROM `461_DONATION` WHERE",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=13,pady=10)
            edel= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            edel.grid(row=14,pady=10)
            b1 = Button(sub1,  text='Delete Record',font=("Footlight MT Light",17) ,command=del_data,bg='#71f55f')  
            b1.grid(row=16, pady=10)

            lb3= Label(sub1,text="UPDATE `461_DONATION` SET",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=13,pady=10,column=2)
            eup= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            eup.grid(row=14,pady=10,column=2)
            b2 = Button(sub1,  text='Update Record', font=("Footlight MT Light",17) , command=update_data,bg='#71f55f')  
            b2.grid(row=16,pady=10,column=2)

            #function of END on second window 
            def display_key():
                lb1=Label(window,text="Thank you for Donating",bg='#ec5050',font=("Footlight MT Light",20))
                lb1.grid(pady=5)
            btn_2 = Button(sub1, text="CLOSE", font=("Footlight MT Light",17) ,command=lambda:[sub1.destroy(),display_key()],bg="#71f55f")
            btn_2.grid(pady=10,columnspan=5)
        bt1=Button(window,text="MAKE A DONATION",font=("Footlight MT Light",17),command= onClickDonate,bg="#71f55f" )
        bt1.grid(row=17,pady=10)

#function of Registering a person on first window    
        def onClickReceiver():
            sub1 = Tk()
            sub1.title("Donation")
            sub1.configure(bg='#ec5050')
            sub1.geometry("1030x525")
            lb1=Label(sub1,text="Enter the following details for receiving blood",bg='#ec5050',font=("Times New Roman",17))
            lb1.grid(row=2,columnspan=5)
            
            #Data for the table 
            def add_data():
                rid = e1.get()
                dor = e2.get()
                typer = e3.get()
                amtr = float(e4.get())
                bgr = e5.get()
                query="INSERT INTO `461_RECEIVE` VALUES(%s,%s,%s,%s,%s)"
                data=(rid,dor,typer,bgr,amtr)
                print(query,data)
                cursor.execute(query,data)
                conn.commit()
                print("INSERTED SUCESSFULLY")
                
            def del_data():
                query="DELETE FROM `461_RECEIVE` WHERE "
                data=(edel.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("DELETED SUCESSFULLY")

            def update_data():
                query="UPDATE `461_RECEIVE` SET "
                data = (eup.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("UPDATED SUCESSFULLY")

            #Data for the table 
            lb3= Label(sub1,text="Enter RID",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=4)
            e1= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e1.grid(row=5,pady=10,padx=10)

            lb3= Label(sub1,text="Enter date received in yyyy-mm-dd format",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=4,column=2)
            e2= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e2.grid(row=5,column=2,padx=53)

            lb3= Label(sub1,text="Enter Type: Blood, Platelets or Plasma",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=4,column=3)
            e3= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e3.grid(row=5,column=3)

            lb3= Label(sub1,text="Enter quantity",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=6)
            e4= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e4.grid(row=7,pady=10)

            lb3= Label(sub1,text="Enter blood group",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=6,column=2)
            e5= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            e5.grid(row=7,column=2)

            b1 = Button(sub1,  text='Add Record',font=("Footlight MT Light",17) ,command=add_data,bg="#71f55f")  
            b1.grid(row=7,column=3)
            
            lb3= Label(sub1,text="DELETE FROM `461_RECEIVE` WHERE",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=11,pady=10)
            edel= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            edel.grid(row=12,pady=10)
            b1 = Button(sub1,  text='Delete Record',font=("Footlight MT Light",17) ,command=del_data,bg="#71f55f")  
            b1.grid(row=14, pady=10)

            lb3= Label(sub1,text="UPDATE `461_RECEIVE` SET",bg='#ec5050',font=("Footlight MT Light",15))
            lb3.grid(row=11,pady=10,column=2)
            eup= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            eup.grid(row=12,pady=10,column=2)
            b2 = Button(sub1,  text='Update Record', font=("Footlight MT Light",17) , command=update_data,bg="#71f55f")  
            b2.grid(row=14,pady=10,column=2)

            #function of END on second window 
            def display_key():
                lb1=Label(window,text="Receiver Details logged",bg='#ec5050',font=("Footlight MT Light",20))
                lb1.grid(pady=5)
            btn_2 = Button(sub1, text="CLOSE", font=("Footlight MT Light",17) ,command=lambda:[sub1.destroy(),display_key()],bg="#71f55f")
            btn_2.grid(pady=10,columnspan=5)
        bt1=Button(window,text="NEED BLOOD",font=("Footlight MT Light",17),command= onClickReceiver,bg="#71f55f")
        bt1.grid(row=27,pady=10)

#function of running any Query on first window
        def QRes():
            def getres():
                ans = Tk()
                query = eq.get()
                cursor.execute(query)
                result=cursor.fetchall()
                # print(type(result))
                columns=[]
                for cd in cursor.description:
                    columns.append(cd[0])
                result.insert(0,columns)
                total_rows = len(result)
                total_columns = len(result[0])
                for i in range(total_rows):
                    for j in range(total_columns):
                        e = Entry(ans, width=14,bg='#f49393', fg='black',font=('Times New Roman',12))
                        e.grid(row=i, column=j)
                        if(result[i][j]==None):
                            e.insert(END,"NULL")
                        else:
                            e.insert(END, result[i][j])
            sub1 = Tk()
            sub1.title("Query Results")
            sub1.configure(bg='#ec5050')
            sub1.geometry("525x325")
            lb1=Label(sub1,text="Enter any Query below",bg='#ec5050',font=("Times New Roman",17))
            lb1.grid(row=2,pady=7)
            eq= Entry(sub1,width=25,borderwidth=2,font=("Footlight MT Light",15))
            eq.grid(row=3,pady=10,padx=10)
            bt=Button(sub1,text="Submit",font=("Footlight MT Light",16),command= getres,bg="#71f55f" )
            bt.grid(row=5)
            def display_key():
                lb1=Label(window,text="Query Results displayed",bg='#ec5050',font=("Footlight MT Light",20))
                lb1.grid(pady=5)
            btn_2 = Button(sub1, text="CLOSE", font=("Footlight MT Light",17) ,command=lambda:[sub1.destroy(),display_key()],bg="#71f55f")
            btn_2.grid(row=6,pady=10)
        bt1=Button(window,text="ANY QUERY",font=("Footlight MT Light",17),command= QRes,bg="#71f55f" )
        bt1.grid(row=37,pady=10)

#Close the main window 
        bt1 = Button(window, text="EXIT", font=("Footlight MT Light",17) ,command=window.destroy,bg="#71f55f")
        bt1.grid(row=47,pady=10)
        window.mainloop()
except Error as e: 
    print("Error while connecting to MySQL", e) 
finally: 
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")