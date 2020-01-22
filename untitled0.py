# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 21:22:07 2020

@author: kusha
"""
import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter.ttk import *
import pandas as pd


import sqlite3

class Main():
    connection = sqlite3.connect("sample.db")
    def __init__(self,parent):
        self.parent = parent 
    
        #parent.title("Login Screen")
        self.page = StringVar()
        self.User=StringVar()
        self.password = StringVar()
        self.sts=StringVar()
        self.name = StringVar()
        self.code1 =StringVar()
        self.code2 = StringVar()
        self.createLoginpage()
        self.sss = StringVar()
        self.ddd = StringVar()
        self.fff = StringVar()
        #self.timeSheetpage()
        
    def createLoginpage(self):
        Label(self.parent , textvariable = self.page,font=("",20))
        frame1 = Frame(self.parent)
        #frame1.title("Login Screen")
        Label(frame1, text="user").grid(sticky=W)
        Entry(frame1 , textvariable= self.User).grid(row=0, column = 1,padx=15,pady=20)
        Label(frame1,text="password").grid(sticky=W)
        Entry(frame1 ,textvariable= self.password , show="#").grid(row=1, column = 1,padx=15,pady=20)
        Button(frame1 , text="Login" , command=self.login ).grid(row =2 ,padx=15,pady=20)
        frame1.pack(padx=10,pady=10)
        
        self.loginFrame=frame1
    
        Label(self.parent , textvariable=self.sts).pack()
        frame2 = Frame(self.parent)
        Button(frame2 , text="APPROVE" , command=self.approve ).grid(row =0)
        Button(frame2 , text="REJECT" , command=self.reject ).grid(row =0 ,column =1)
        Button(frame2 , text="CREATE" , command=self.create ).grid(row =1 ,padx=15,pady=20)
        Button(frame2 , text="LOGOUT" , command=self.logout ).grid(row =1 ,column=1 ,padx=15,pady=20)
       
       
        self.timesheetFrame=frame2
        frame3 = Frame(self.parent)
        Label(frame3, text="Name").grid(sticky=W)
        Entry(frame3 , textvariable= self.name).grid(row=0, column = 1,padx=15,pady=20)
        Label(frame3, text="Code1").grid(sticky=W)
        Entry(frame3 , textvariable= self.code1).grid(row=1, column = 1,padx=15,pady=20)
        Label(frame3, text="Code2").grid(sticky=W)
        Entry(frame3 , textvariable= self.code2).grid(row=2, column = 1,padx=15,pady=20)
        Button(frame3 , text="SAVE" , command=self.back ).grid(row =3 ,column=1 ,padx=15,pady=20)
        
        self.createTimesheetFrame=frame3
        
        
        
        
    def login(self):
        username = self.User.get()
        passw =self.password.get()
        
        
        try:
            if username!="aaa" or passw!="aaa":
                self.sts.set("Wrong User or Password")
            else:
                
#               self.sts.set("Logging in ...")
                self.loginFrame.pack_forget()
                self.timesheetFrame.pack()
                self.sts.set("TIMESHEET")
                
                #self.page.set("Timesheet")
                 #
        except:
            self.sts.set(" Cannot login ...")
                 
    def create(self):
        self.timesheetFrame.pack_forget()
        self.createTimesheetFrame.pack()
        self.sts.set(" CREATE ")
        
    def back(self):
        name = self.name.get()
        code1 = self.code1.get()
        code2 = self.code2.get()
        submit = "submitted"
        
        try:
            print(name)
            print(code1)
            print(code2)
            cursor = connection.cursor()
            #sql_command = """INSERT INTO employee VALUES (%s,%d,%d ,%s)""",(name,code1,code2,submit)
            cursor.execute("INSERT INTO employee (name, code1,code2,status) VALUES(?, ?,?,?)", (name,code1,code2,submit))
            connection.commit()
            self.createTimesheetFrame.pack_forget()
            self.timesheetFrame.pack()
            self.sts.set("TIMESHEET")
            print("insert complete")
            #cursor1 = connection.cursor()
            #sql_command1 = """SELECT * FROM employee"""
            #cursor1.execute(sql_cmmand1)
            #results = cursor1.fetchall()
            results = pd.read_sql_query("""SELECT * FROM employee """, connection)
        
            print("bye")
            res = results.to_numpy()
            ress = res[-1]
            
            print((ress[0]))
            
          
            #print(results)
            
            self.sts.set(ress)
            
            
            #for i  in range(len(results)):
                #print("1")
                #results[i].append(ttk.Button(self.frame2 ,text="APPROVE", command=self.approve).grid(row=i,column=1))
                
        
            #for result in results:
             #   results[result] = tk.Button(text="APPROVE", command=self.approve).grid()
                
                
            print("record inserted and displayed")
            sss = ress[0]
            ddd = ress[1]
            fff = ress[2]
            return sss,ddd,fff
            
        except:
            self.sts.set(" Cannot save ...")
            self.createTimesheetFrame.pack_forget()
            self.timesheetFrame.pack()
            
    def logout(self):
        self.timesheetFrame.pack_forget()
        self.parent.destroy()
        
    def approve(self):
        name = self.sss.get()
        code1 = self.ddd.get()
        code2 = self.fff.get()
        cursor = connection.cursor()
        #sql_command = """UPDATE employee SET status = "Approved" where name = (?) , code1=(?) , code2=(?) """
        cursor.execute("""UPDATE employee SET status = "Approved" WHERE name = name AND code1= code1 AND code2=code2 """ )
        print("table updated")
        results1 = pd.read_sql_query("""SELECT * FROM employee """, connection)
        print("byeeee")
        res1 = results1.to_numpy()
        ress1 = res1[-1]
            
        print((ress1))
            
          
            #print(results)
            
        self.sts.set(ress1)
        
    def reject(self):
        name = self.sss.get()
        code1 = self.ddd.get()
        code2 = self.fff.get()
        cursor = connection.cursor()
        #sql_command = """UPDATE employee SET status = "Approved" where name = (?) , code1=(?) , code2=(?) """
        cursor.execute("""UPDATE employee SET status = "Rejected" WHERE name = name AND code1= code1 AND code2=code2 """ )
        print("table updated")
        results2 = pd.read_sql_query("""SELECT * FROM employee """, connection)
        print("byeeee")
        res2 = results2.to_numpy()
        ress2 = res2[-1]
            
        print((ress2))
            
          
            #print(results)
            
        self.sts.set(ress2)
    
if __name__ =="__main__":
    connection = sqlite3.connect("sample.db")
    try:
        cursor = connection.cursor()
        sql_command = """CREATE TABLE IF NOT EXISTS employee (name VARCHAR(5),code1 BIT(1),code2 BIT(1),status VARCHAR(20))"""
        cursor.execute(sql_command)
        print("table created")
    except:
        self.sts.set(" Cannot create ...")
    
    root=Tk()
    Main(root)
    root.mainloop()