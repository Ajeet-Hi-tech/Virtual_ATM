                        ##### MCA MINI PROJECT #####
            ##### CREATED BY THE AJEET & SHIVAM SHUKLA #####
        ##### HI-TECH INSTITUTE OF ENGINEERING OF TECHNOLOGY #####

##### DATABASE CONNECTIVITY ######
import psycopg2 
con = psycopg2.connect(
    host ='localhost',
    database ='imaginary_atm_card',
    user = 'postgres',
    port = '5432',
    password ='12345')

###### CREATING A CURSOR ######
cur = con.cursor()

##### THE DESIGNING OF ATM ######
from tkinter import *
from time import time
bank = Tk() 
bank.title('IMAGINARY ATM...')
canvas =Canvas(bank,width=800,height=600)
bank.geometry('800x600+200+50')
photo = PhotoImage(file='F:\\Your project\\bank1.png')
canvas.create_image(0,0,image=photo,anchor =NW)
canvas.create_text(120,100,text="Virtual ATM Card",anchor = W,font=('purisa',50,'bold'))
canvas.create_text(200,185,text='UserName',anchor = W,font=('purisa',20,'bold'))
canvas.create_text(200,265,text='Password',anchor = W,font=('purisa',20,'bold'))
canvas.create_text(670,550,text='@ copyright 2020',anchor = N ,font=('purisa',15,'bold'))


user = StringVar(value='')
pas = StringVar(value ='')

###### :ENTRY CODEING WINDOW-FIRST: ######
Entry(bank,textvariable = user,justify = 'center',bd=3,width = 25,font =('arial',20,'bold')).place(x=200,y=205)
Entry(bank,textvariable = pas,show = "*",justify = 'center',bd=3,width = 25,font =('arial',20,'bold')).place(x=200,y=285)
Available_pin = 0
 
###### :BUTTON CODEING WINDOW-FIRST: ######  
Button(padx = 10 ,pady = 4,text='submit',fg='black',bg='DarkOliveGreen1',bd=4,font=('arial',15,'bold'),command = lambda:(menu_function())).place(x=205,y=350)
Button(padx = 10 ,pady = 4,text='cancle',fg='black',bg='DarkOliveGreen1',bd=4,font=('arial',15,'bold'),command = lambda:(cancle())).place(x=340,y=350)

def cancle():
    user.set("")        
    pas.set("")

##### MENU EXCEPTION HANDLING & DATABASE CODE #####
def menu_function()    :
    try:
        name = user.get()
        password = pas.get()
        fetch = """SELECT user_name , password,pin FROM imaginary_atm WHERE password = %s;"""
        cur.execute(fetch,[password])
        result = cur.fetchall()
        global Available_pin
        Available_pin = int(result[0][2])
        if(name == result[0][0] or password == result[0][1]):
            signinwindow()
    except Exception as e:
        canvas.create_text(130,450,text='Please Check your username & Password',anchor = W,font=('purisa',20,'bold'))
canvas.pack()
###### SIGNINWINDOW OR MENU WINDOWS #####
def signinwindow():
    global top
    top = Toplevel()
    top.configure(background='orange')
    top.geometry('800x600+200+50')
    ###### LABEL CODEING WINDOW-MENU
    Label(top,text='HI WELCOME',fg='black',bg='orange',font=('vardana',30,'bold')).place(x=275,y=65)
    
    ###### LEFT_SIDE BUTTON CODEING WINDOW-MENU ######     
    Button(top,padx=55,pady=15,text='FAST CASE',fg='black',bd=8,bg='yellow',font=('vardana',12,'bold'),command = lambda:(fastcase())).place(x=440,y=180)
    Button(top,padx=50,pady=15,text='WITHDRAWL',fg='black',bg='yellow',bd=8,font=('vardana',12,'bold'),command = lambda:(withdrawal1())).place(x=440,y=300)
    Button(top,padx=65,pady=15,text='DEPOSIT',fg='black',bg='yellow',bd=8,font=('vardana',12,'bold'),command = lambda:(deposit())).place(x=440,y=420)
        
    ###### RIGHT_SIDE BUTTON CODEING WINDOW-MENU ######   
    Button(top,padx=28,pady=15,text= 'FUND TRANSFER',fg='black',bg='yellow',bd=8,font=('vardana',12,'bold'),command = lambda:(fundtransfer1())).place(x=140,y=180)
    Button(top,padx=18,pady=15,text='BALANCE ENQUIRY',fg='black',bg='yellow',bd=8,font=('vardana',12,'bold'),command = lambda:(balance())).place(x=140,y =300)
    Button(top,padx=45,pady=15,text='PIN CHANGE',fg='black',bd=8,bg='yellow',font=('vardana',12,'bold'),command = lambda:(pinchange())).place(x=140,y=420)

      
    ###### BALANCE ENQUIRY WINDOW-1: ######
    def balance():
        bal = Toplevel()
        bal.configure(background='orange')
        bal.geometry('800x600+200+50')
        
        ##### TEXT AREA COGEING BALANCE ENQUIRY WINDOW-1:######
        pin = IntVar(value ='')    
        Entry(bal,show = "*",width=20,justify ='center',textvariable = pin,bd=5,fg='black',bg='white',font=('helvetica',27,'bold')).place(x=190,y=190)
        
        ##### LABEL CODEING BALANCE ENQUIRY WINDOW-1:###### 
        Label(bal,text='PLEASE ENTER THE PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=235,y=90)

        ##### BALANCE EXCEPTION HANDLING & DATABASE CODE #####
        def balance_transfer():
            try:
                if(pin.get() == Available_pin):
                    user_PIN = """SELECT pin FROM imaginary_atm WHERE pin = %s;"""
                    cur.execute(user_PIN,[pin.get()])         
                    result_pin = cur.fetchall()
                    get_pin = result_pin[0][0]    
                    balance1()
                else:
                    Label(bal,text='PLEASE ENTER THE CORRECT PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=155,y=300)    
            except Exception as e:
                Label(bal,text='PLEASE ENTER THE VALID PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=185,y=300)    
        ##### BUTTON CODEING BALANCE ENQUIRY WINDOW-1:###### 
        Button(bal,padx=40,pady=15,text='CONFIRM',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(balance_transfer())).place(x=510,y=360)
        Button(bal,padx=45,pady=15,text='CANCEL',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(signinwindow())).place(x=510,y=470)
        
        ###### BALANCE ENQUIRY WINDOW-2: ######  
        def balance1():
            bal1 = Toplevel()
            bal1.configure(background='orange')
            bal1.geometry('800x600+200+50')
            start = time()
            
            ##### LABEL CODEING BALANCE ENQUIRY WINDOW-1:######
            Detail ="""SELECT f_name ,l_name, account_no, user_capital, mobile_no FROM imaginary_atm WHERE pin = %s;"""
            cur.execute(Detail,[pin.get()])
            result = cur.fetchall()
            full_name = (result[0][0]+" "+ result[0][1]).upper()
            
            Label(bal1,text='Your PassBook Detail',fg='black',bg='orange',font=('helvetica',25,'bold')).place(x=230,y=65)

            ##### LABEL CODEING BALANCE ENQUIRY WINDOW-1:######
            Label(bal1,text='NAME                                '+full_name,bg='orange',font=('helvetica',20,'bold')).place(x=130,y=200)
            Label(bal1,text='ACCOUNT NO                  '+str(result[0][2]),bg='orange',font=('helvetica',20,'bold')).place(x=130,y=240)
            Label(bal1,text='AVAILABLE BALANCE     '+str(result[0][3])+" rs",bg='orange',font=('helvetica',20,'bold')).place(x=130,y=280)
            Label(bal1,text='MOBILE NO                       '+str(result[0][4]),bg='orange',font=('helvetica',20,'bold')).place(x=130,y=320)
            bank.after(5000,bal1.destroy)
            bank.after(-6,bal.destroy)
            bank.after(-6,top.destroy)
            

                 
###### WITHDRAWL WINDOW-1: ######
def withdrawal1():
    win1 = Toplevel()
    win1.configure(background='orange')
    win1.geometry('800x600+200+50')
    
    ##### LABEL CODEING WITHDRAWL WINDOW-1:###### 
    Label(win1,text='HI WELCOME\n SELECT YOUR ACCOUNT',bg='orange',font=('vardana',20,'bold')).place(x=210,y=50)

    ##### BUTTON CODEING WITHDRAWL WINDOW-1:######
    Button(win1,padx=28,pady=10,text='FROM CURRENT',fg='black',bg='yellow',bd=6,font=('arial',18,'bold'),command = lambda:(current())).place(x=420,y=360)
    Button(win1,padx=40,pady=10,text='FROM SAVING',fg='black',bg='yellow',bd=6,font=('arial',18,'bold'),command=lambda:(saving())).place(x=420,y=480)

    ###### SAVING ACCOUNT ########
    def saving():
        saving ='saving'
        query = """SELECT saving_ac FROM imaginary_atm WHERE pin =%s;"""
        cur.execute(query,[Available_pin])
        con.commit()
        result = cur.fetchone()
        if(saving == result[0]):
            withdrawal2()
    ###### CURRENT ACCOUNT ######
    def current():
        current ='current'
        query = """SELECT current_ac FROM imaginary_atm WHERE pin =%s;"""
        cur.execute(query,[Available_pin])
        con.commit()
        result = cur.fetchone()
        if(current == result[0]):
            withdrawal2() 
    ###### WITHDRAWL WINDOW-2: ######
    def withdrawal2():
        win2 = Toplevel()
        win2.configure(background='orange')
        win2.geometry('800x600+200+50')
        
        ##### TEXT AREA COGEING WINDOW FUNDTRNSFER-5:######
        amount = IntVar(value='')
        Entry(win2,justify = 'center',width=20,textvariable=amount,bd=5,fg='black',bg='white',font=('helvetica',27,'bold')).place(x=190,y=190)
            
        ##### LABEL CODEING WITHDRAWL WINDOW-1:###### 
        Label(win2,text='PLEASE ENTER THE AMOUNT',bg='orange',font=('helvetica',20,'bold')).place(x=190,y=90)

        ##### WITHDRAWAL EXCEPTION HANDLING & DATABASE CODE #####
        def withdrawal1_transfer(): 
            try:
                query1 ="""SELECT user_capital FROM imaginary_atm WHERE pin =%s;"""
                cur.execute(query1,[Available_pin])
                result_am = cur.fetchone()
                global total_amount
                total_amount = int(result_am[0])
                if(total_amount > amount.get()):
                    withdrawal3()
                else:
                    Label(win2,text='YOU DON NOT HAVE A SUFFICIENT AOMOUNT',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=80,y=300)
            except Exception as e:  
                Label(win2,text='PLEASE ENTER THE VALID AOMOUNT',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=125,y=300)
                
        ##### BUTTON CODEING WITHDRAWL WINDOW-1:######
        Button(win2,padx=40,pady=10,text='PRESS IF YES',fg='black',bg='yellow',bd=6,font=('vardana',19,'bold'),command=lambda:(withdrawal1_transfer())).place(x=420,y=360)
        Button(win2,padx=45,pady=10,text='PRESS IF NO',fg='black',bg='yellow',bd=6,font=('vardana',19,'bold'),command=lambda:(withdrawal1())).place(x=420,y=480)

        ###### WITHDRAWL WINDOW-3: ######
        def withdrawal3():
            win3 = Toplevel()
            win3.configure(background='orange')
            win3.geometry('800x600+200+50')
            
            ##### TEXT AREA COGEING WINDOW FUNDTRNSFER-5:######
            pin = IntVar(value='')  
            Entry(win3,width=20,show = "*",justify ='center',textvariable = pin,bd=5,fg='black',bg='white',font=('helvetica',27,'bold')).place(x=190,y=190)
            
            ##### LABEL CODEING WITHDRAWL WINDOW-1:###### 
            Label(win3,text='PLEASE ENTER THE PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=235,y=90)

            ##### WITHDRAWAL EXCEPTION HANDLING & DATABASE CODE #####
            def withdrawal2_transfer(): 
                global remaining_amount
                try:
                    if(Available_pin == pin.get()):
                        remaining_amount = total_amount - pin.get()
                        query2 = """UPDATE imaginary_atm SET user_capital = %s WHERE pin = %s;"""
                        cur.execute(query2,[remaining_amount,pin.get()])
                        con.commit()
                        withdrawal4()
                    else:
                        Label(win3,text='PLEASE ENTER THE CORRECT PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=155,y=300)    
                except Exception as e:
                    Label(win3,text='PLEASE ENTER THE VALID PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=185,y=300)    
                    
                        
            ##### BUTTON CODEING WITHDRAWL WINDOW-1:######
            Button(win3,padx=40,pady=15,text='CONFIRM',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(withdrawal2_transfer())).place(x=510,y=360)
            Button(win3,padx=45,pady=15,text='CANCEL',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(withdrawal2())).place(x=510,y=470)

            ###### WITHDRAWL WINDOW-4: ######
            def withdrawal4():
                win4 = Toplevel()
                win4.configure(background='orange')
                win4.geometry('800x600+200+50')
                start =time()
                
                ##### LABEL CODEING WITHDRAWL WINDOW-1:###### 
                Label(win4,text='ALL ARE CAPACTIAL YOUR \n TRANSACTION IS SUCCESSFUL',bg='orange',font=('herventica',22,'bold')).place(x=170,y=80)

                ##### LABEL CODEING WITHDRAWL WINDOW-1:###### 
                Label(win4,text='AVAILABLE BALANCE   '+str(remaining_amount)+" rs",bg='orange',font=('herventica',28,'bold')).place(x=85,y=290)
                bank.after(5000,win4.destroy)
                bank.after(-6,win3.destroy)
                bank.after(-6,win2.destroy)
                bank.after(-6,win1.destroy)
                bank.after(-6,top.destroy)
                    
                  
  

###### CASE DEPOSIT WINDOW-1: ######
def deposit():
    dep1 = Toplevel()
    dep1.configure(background='orange')
    dep1.geometry('800x600+200+50')
    
    ##### TEXT AREA COGEING CASE DEPOSIT WINDOW-1:######
    pin = IntVar(value ='')   
    Entry(dep1,width=20,show = "*",justify ='center',textvariable = pin,bd=5,fg='black',bg='white',font=('helvetica',27,'bold')).place(x=190,y=190)
            
    ##### LABEL CODEING WITHDRAWL WINDOW-1:###### 
    Label(dep1,text='PLEASE ENTER THE PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=235,y=90)

    ##### DEPOSIT EXCEPTION HANDLING & DATABASE CODE #####
    def deposit1_transfer():
        try:
            if(pin.get() == Available_pin):
                deposit2()
            else:
                Label(dep1,text='PLEASE ENTER THE CORRECT PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=155,y=300)    
        except Exception as e:
            Label(dep1,text='PLEASE ENTER THE VALID PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=185,y=300)    
        
    ##### BUTTON CODEING CASE DEPOSIT WINDOW:#####
    Button(dep1,padx=40,pady=15,text='CONFIRM',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(deposit1_transfer())).place(x=510,y=360)
    Button(dep1,padx=45,pady=15,text='CANCEL',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(signinwindow())).place(x=510,y=470)

    ###### CASE DEPOSIT WINDOW-2: ######
    def deposit2():
        dep2 = Toplevel()
        dep2.configure(background='orange')
        dep2.geometry('800x600+200+50')

        ##### TEXT AREA COGEING CASE DEPOSIT WINDOW-2:######
        global user_account
        user_account = IntVar(value='')
        Entry(dep2,width=20,justify ='center',textvariable = user_account,bd=5,fg='black',bg='white',font=('helvetica',27,'bold')).place(x=190,y=190)
            
        ##### LABEL CODEING CASE DEPOSIT WINDOW-2:###### 
        Label(dep2,text='\nPLEASE ENTER 11 DIGIT \n BENEFICIARY ACCOUNT NUMBER ',bg='orange',font=('hevetica',20,'bold')).place(x=160,y=50)

        ##### DEPOSIT EXCEPTION HANDLING & DATABASE CODE #####
        def deposit2_transfer():
            try:
                query_ac = """SELECT account_no FROM imaginary_atm WHERE pin =%s ;"""
                cur.execute(query_ac,[pin.get()])
                customer_ac = cur.fetchone()
                if(user_account.get() == customer_ac[0]):
                    deposit3()
                else:
                    Label(dep2,text='THERE IS NO ACCOUNT NUMBER EXISTS',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=115,y=290)    
            except Exception as e:
                Label(dep2,text='        PLEASE ENTER THE VALID AC/NO      ',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=100,y=290)

        ##### BUTTON CODING CASE DEPOSIT WINDOW-2:######
        Button(dep2,padx=40,pady=15,text='CONFIRM',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(deposit2_transfer())).place(x=510,y=360)
        Button(dep2,padx=45,pady=15,text='CANCEL',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(deposit())).place(x=510,y=470)
        
        ###### CASE DEPOSIT WINDOW-3: ######
        def deposit3():
            dep3 = Toplevel()
            dep3.configure(background='orange')
            dep3.geometry('800x600+200+50')
            
            ##### DATABASE CODEING ######
            reaccount = IntVar(value = '')
            Entry(dep3,justify='center',textvariable=reaccount,bd=6,fg='black',bg='white',font=('helvetica',27,'bold'),show='*').place(x=190,y=190)               
            
            ##### LABEL CODEING PIN CHANGE WINDOW-2 ###### 
            Label(dep3,text='\nPLEASE RE_ENTER 11 DIGIT \n BENEFICIARY ACCOUNT NUMBER ',bg='orange',font=('helvetical',20,'bold')).place(x=160,y=50) 
            
            ##### DEPOSIT EXCEPTION HANDLING & DATABASE CODE #####
            def deposit3_transfer():
                try:
                    if(user_account.get() == reaccount.get()):
                        deposit4()
                    else:
                        Label(dep3,text='PLEASE RECHECK YOUR ACCOUNT',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=145,y=290)    
                except Exception as e:
                    
                    Label(dep3,text='        PLEASE ENTER THE VALID AC/NO      ',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=100,y=290)
                 
            ##### BUTTON CODING PIN CHANGE WINDOW-1: ######
            Button(dep3,padx=40,pady=15,text='CORRECT',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(deposit3_transfer())).place(x=510,y=360)           
            Button(dep3,padx=30,pady=15,text='INCORRECT',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(deposit2())).place(x=510,y=470)

            ###### WITHDRAWL WINDOW-2: ######
            def deposit4():
                dep4 = Toplevel()
                dep4.configure(background='orange')
                dep4.geometry('800x600+200+50')

                ##### TEXT AREA COGEING WINDOW FUNDTRNSFER-5:######
                amount = IntVar(value='')
                Entry(dep4,justify='center',width=20,bd=5,textvariable = amount,fg='black',bg='white',font=('vardana',27,'bold')).place(x=190,y=190)
    
                ##### LABEL CODEING WITHDRAWL WINDOW-1:###### 
                Label(dep4,text='PLEASE ENTER THE AMOUNT',bg='orange',font=('vardana',20,'bold')).place(x=190,y=90)

                ##### DEPOSIT EXCEPTION HANDLING & DATABASE CODE #####
                def deposit4_transfer():
                    try:
                        query1 ="""SELECT user_capital FROM imaginary_atm WHERE account_no =%s;"""
                        cur.execute(query1,[user_account.get()])
                        result_amount = cur.fetchone()
                        Total_money = amount.get() + result_amount[0]
                        
                        ##### UPDATE AMOUNT ######    
                        query2 = """UPDATE imaginary_atm SET user_capital= %s WHERE account_no =%s;"""
                        cur.execute(query2,[Total_money,user_account.get()])
                        con.commit()
                        deposit5()    
                    except Exception as e:  
                        Label(dep4,text='PLEASE ENTER THE VALID AOMOUNT',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=125,y=300)
                
                ##### BUTTON CODEING WITHDRAWL WINDOW-1:######
                Button(dep4,padx=40,pady=10,text='PRESS IF YES',fg='black',bg='yellow',bd=6,font=('vardana',19,'bold'),command=lambda:(deposit4_transfer())).place(x=420,y=360)
                Button(dep4,padx=45,pady=10,text='PRESS IF NO',fg='black',bg='yellow',bd=6,font=('vardana',19,'bold'),command=lambda:(deposit3())).place(x=420,y=480)
                
                ###### CASE DEPOSIT WINDOW-4: ######
                def deposit5():
                    dep5 = Toplevel()
                    dep5.configure(background='orange')
                    dep5.geometry('800x600+200+50')
                    start = time()
                    
                    ##### LABEL CODEING PIN CHANGE WINDOW-3######
                    Label(dep5,text='THANKS YOU VISIT US ',bg='orange',font=('vardana',25,'bold')).place(x=205,y=90)            
                    Label(dep5,text="YOUR AMOUNT \n IS \n SUCCESSFULY DEPOSIT",bg='orange',font=('vardana',30,'bold')).place(x=140,y=250)  
                    
                    bank.after(3000,dep5.destroy)
                    bank.after(-6,dep4.destroy)
                    bank.after(-6,dep3.destroy)
                    bank.after(-6,dep2.destroy)
                    bank.after(-6,dep1.destroy)
                    bank.after(-6,top.destroy)

         
###### FAST CASE WITHDRAWL WINDOW-1: ######
def fastcase():   
    fast1 = Toplevel()
    fast1.configure(background='orange')
    fast1.geometry('800x600+200+50')
       
    ##### TEXT AREA COGEING FAST CASE WITHDRAWL WINDOW-1: ######
    fast_pin = IntVar(value='')
    Entry(fast1,show = "*",justify='center',width=20,textvariable = fast_pin,bd=5,fg='black',bg='white',font=('helvetica',27,'bold')).place(x=190,y=190)
         
    ##### LABEL CODEING FAST CASE WITHDRAWL WINDOW-1:###### 
    Label(fast1,text='PLEASE ENTER THE PIN',bg='orange',font=('helvetica',20,'bold')).place(x=235,y=90)                          

    ##### FASTCASE EXCEPTION HANDLING & DATABASE CODE #####
    def fast1_transfer():
        try:
            if(fast_pin.get() == Available_pin):
                fastcase2()
            else:
                Label(fast1,text='PLEASE ENTER THE CORRECT PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=155,y=300)    
        except Exception as e:
            Label(fast1,text='PLEASE ENTER THE VALID PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=185,y=300)    
        
    ##### BUTTON CODEING FAST CASE WITHDRAWL WINDOW-1:######
    Button(fast1,padx=40,pady=15,text='CONFIRM',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(fast1_transfer())).place(x=510,y=360)
    Button(fast1,padx=45,pady=15,text='CANCEL',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(signinwindow())).place(x=510,y=470)
    
    ###### FAST CASE WITHDRAWL WINDOW-2: ######
    def fastcase2():   
        fast2 = Toplevel()
        fast2.configure(background='orange')
        fast2.geometry('800x600+200+50')
        
        ##### LABEL COGEING FAST CASE WITHDRAWL WINDOW-2: ######
        Label(fast2,text='PLEASE SELECT AMOUNT',bg='orange',font=('arial',20,'bold')).place(x=230,y=60)
        fastquery = """SELECT user_capital FROM imaginary_atm WHERE pin=%s;"""
        cur.execute(fastquery,[fast_pin.get()])
        con.commit()
        F_case = cur.fetchone()
        
        ##### LEFT SIDE BUTTON CODEING FAST CASE WITHDRAWL WINDOW-2:######
        Button(fast2,padx=35,pady=10,text=':RS 100/-:',fg='black',bg='yellow',bd=6,font=('arial',15,'bold'),command=lambda:(case100())).place(x=150,y=170)
        Button(fast2,padx=35,pady=10,text=':RS 200/-:',fg='black',bg='yellow',bd=6,font=('arial',15,'bold'),command=lambda:(case200())).place(x=150,y=250)
        Button(fast2,padx=35,pady=10,text=':RS 500/-:',fg='black',bg='yellow',bd=6,font=('arial',15,'bold'),command=lambda:(case500())).place(x=150,y=330)
        Button(fast2,padx=30,pady=10,text=':RS 1000/-:',fg='black',bg='yellow',bd=6,font=('arial',15,'bold'),command=lambda:(case1000())).place(x=150,y=410)

        ##### RIGHT SIDE BUTTON CODEING FAST CASE WITHDRAWL WINDOW-2:######
        Button(fast2,padx=27,pady=10,text=':RS 2000/-:',fg='black',bg='yellow',bd=6,font=('arial',15,'bold'),command=lambda:(case2000())).place(x=450,y=170)
        Button(fast2,padx=27,pady=10,text=':RS 3000/-:',fg='black',bg='yellow',bd=6,font=('arial',15,'bold'),command=lambda:(case3000())).place(x=450,y=250)
        Button(fast2,padx=27,pady=10,text=':RS 5000/-:',fg='black',bg='yellow',bd=6,font=('arial',15,'bold'),command=lambda:(case5000())).place(x=450,y=330)
        Button(fast2,padx=22,pady=10,text=':RS 10000/-:',fg='black',bg='yellow',bd=6,font=('arial',15,'bold'),command=lambda:(case10000())).place(x=450,y=410)
        
        ##### ONE HUNDRED CASE #####
        def case100():
            case = 100
            Remain_case = F_case[0] - case
            Update_case = """UPDATE imaginary_atm SET user_capital = %s WHERE pin =%s;"""
            cur.execute(Update_case,[Remain_case,Available_pin])
            con.commit()
            fastcase3()

        ##### TWO HUNDRED CASE #####
        def case200():
            case = 200
            Remain_case = F_case[0] - case
            Update_case = """UPDATE imaginary_atm SET user_capital = %s WHERE pin =%s;"""
            cur.execute(Update_case,[Remain_case,Available_pin])
            con.commit()
            fastcase3()
        
        ##### 500 HUNDRED CASE #####
        def case500():
            case = 500
            Remain_case = F_case[0] - case
            Update_case = """UPDATE imaginary_atm SET user_capital = %s WHERE pin =%s;"""
            cur.execute(Update_case,[Remain_case,Available_pin])
            con.commit()
            fastcase3()

        ##### ONE THOUSAND CASE #####
        def case1000():
            case = 100
            Remain_case = F_case[0] - case
            Update_case = """UPDATE imaginary_atm SET user_capital = %s WHERE pin =%s;"""
            cur.execute(Update_case,[Remain_case,Available_pin])
            con.commit()
            fastcase3()

        ##### FIVE THOUSAND CASE #####
        def case5000():
            case = 5000
            Remain_case = F_case[0] - case
            Update_case = """UPDATE imaginary_atm SET user_capital = %s WHERE pin =%s;"""
            cur.execute(Update_case,[Remain_case,Available_pin])
            con.commit()
            fastcase3()

        ##### TEN THOUSAND CASE #####
        def case10000():
            case = 10000
            Remain_case = F_case[0] - case
            Update_case = """UPDATE imaginary_atm SET user_capital = %s WHERE pin =%s;"""
            cur.execute(Update_case,[Remain_case,Available_pin])
            con.commit()
            fastcase3()

        ##### TWO THOUSAND CASE #####
        def case2000():
            case = 2000
            Remain_case = F_case[0] - case
            Update_case = """UPDATE imaginary_atm SET user_capital = %s WHERE pin =%s;"""
            cur.execute(Update_case,[Remain_case,Available_pin])
            con.commit()
            fastcase3()

        ##### THREE THOUSAND CASE #####
        def case3000():
            case = 3000
            Remain_case = F_case[0] - case
            Update_case = """UPDATE imaginary_atm SET user_capital = %s WHERE pin =%s;"""
            cur.execute(Update_case,[Remain_case,Available_pin])
            con.commit()
            fastcase3()

        ##### FAST CASE WITHDRAWL WINDOW-3: ######
        def fastcase3():
            fast3 = Toplevel()
            fast3.configure(background='orange')
            fast3.geometry('800x600+200+50')
            start = time()
            
            #Label(dep5,text='THANKS YOU VISIT US ',bg='orange',font=('vardana',25,'bold')).place(x=205,y=90)            
            Label(fast3,text='THANKS YOU VISIT US ',bg='orange',font=('vardana',25,'bold')).place(x=205,y=90)
            Label(fast3,text='All AER CAPICITAL YOUR\n TRANSACTION IS SUCCESSFULY',bg='orange',font=('vardana',28,'bold')).place(x=80,y=275)
            bank.after(10000,fast3.destroy)
            bank.after(-6,fast2.destroy)
            bank.after(-6,fast1.destroy)
            bank.after(-6,top.destroy)
            


    
###### FUNDTRANSFER WINDOW-1 ######
def fundtransfer1():
    fund1 = Toplevel()
    fund1.configure(background='orange')
    fund1.geometry('800x600+200+50')

    ##### LABEL CODEING WINDOW FUNDTRNSFER-1:###### 
    Label(fund1,text='TO WHICH ACCOUNT DO \n YOU WANT TO TRASFER FUNDS',bg='orange',font=('vardana',22,'bold')).place(x=170,y=50)
        
    ##### BUTTON CODEING WINDOW FUNDTRNSFER-1:######
    Button(fund1,padx=30,pady=13,text='FROM SAVING',fg='black',bg='yellow',bd=6,font=('arial',15,'bold'),command=lambda:(funsaving())).place(x=470,y=360) 
    Button(fund1,padx=20,pady=13,text='FROM CURRENT',fg='black',bg='yellow',bd=6,font=('arial',15,'bold'),command=lambda:(funcurrent())).place(x=470,y=470)

    ###### SAVING ACCOUNT ######
    def funsaving():
        saving ='saving'
        query = """SELECT saving_ac FROM imaginary_atm WHERE pin =%s;"""
        cur.execute(query,[Available_pin])
        con.commit()
        result = cur.fetchone()
        if(saving == result[0]):
            fundtransfer2()
    ###### CURRENT ACCOUNT ######        
    def funcurrent():
        current ='current'
        query = """SELECT current_ac FROM imaginary_atm WHERE pin =%s;"""
        cur.execute(query,[Available_pin])
        con.commit()
        result = cur.fetchone()
        if(current == result[0]):    
            fundtransfer2()
    ###### FUNDTRANSFER WINDOW-2 ######
    def fundtransfer2():
        fund2 = Toplevel()
        fund2.configure(background='orange')
        fund2.geometry('800x600+200+50')
                    
        ##### TEXT AREA COGEING WINDOW FUNDTRNSFER-2:######
        global account
        account = IntVar(value='')
        Entry(fund2,justify='center',width=20,textvariable = account,bd = 5,fg='black',bg='white',font=('vardana',27,'bold')).place(x=190,y=190)
     
        ##### LABEL CODEING WINDOW FUNDTRNSFER-2:###### 
        Label(fund2,text='\nPLEASE ENTER 11 DIGIT \n BENEFICIARY ACCOUNT NUMBER',bg='orange',font=('arial',20,'bold')).place(x=160,y=50)

        ##### FUNDTRANSFER EXCEPTION HANDLING & DATABASE CODE #####
        def fund1_transfer3():
            try:
                query_ac = """SELECT account_no FROM imaginary_atm WHERE account_no =%s ;"""
                cur.execute(query_ac,[account.get()])
                customer_ac = cur.fetchone()
                if(account.get() == customer_ac[0]):
                    fundtransfer3()
                else:
                    Label(fund2,text='THERE IS NO ACCOUNT NUMBER EXISTS',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=115,y=290)    
            except Exception as e:
                Label(fund2,text='        PLEASE ENTER THE VALID AC/NO      ',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=100,y=290)

        ##### BUTTON CODING WINDOW FUNDTRNSFER-2:######
        Button(fund2,padx=40,pady=15,text='CONFRIM',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(fund1_transfer3())).place(x=510,y=360) 
        Button(fund2,padx=45,pady=15,text='CANCLE',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(fundtransfer1())).place(x=510,y=470)
 
        ###### FUNDTRANSFER WINDOW-3 ######
        def fundtransfer3():
            fund3 = Toplevel()
            fund3.configure(background='orange')
            fund3.geometry('800x600+200+50')

            ##### TEXT AREA COGEING WINDOW FUNDTRNSFER-3 ######
            reaccount = IntVar(value ='')
            Entry(fund3,show = "*",justify='center',width = 20,textvariable = reaccount,bd=6,fg='black',bg='white',font=('vardana',27,'bold')).place(x=190,y=190)
               
            ##### LABEL CODEING WINDOW FUNDTRNSFER-3:######
            Label(fund3,text='\nPLEASE RE_ENTER 11 DIGIT \n BENEFICIARY ACCOUNT NUMBER ',bg='orange',font=('vardana',20,'bold')).place(x=160,y=50)

            ##### FUNDTRANSFER EXCEPTION HANDLING & DATABASE CODE #####
            def fund2_transfer():
                try:
                    if(account.get() == reaccount.get()):
                        fundtransfer4()
                    else:
                        Label(fund3,text='PLEASE RECHECK YOUR ACCOUNT',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=145,y=290)    
                except Exception as e: 
                    Label(fund3,text='        PLEASE ENTER THE VALID AC/NO      ',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=100,y=290)
            
            ##### BUTTON CODING WINDOW FUNDTRNSFER-3:######  
            Button(fund3,padx=40,pady=15,text='CORRECT',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(fund2_transfer())).place(x=510,y=360) 
            Button(fund3,padx=30,pady=15,text='INCORRECT',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(fundtransfer2())).place(x=510,y=470)

            ###### FUNDTRANSFER WINDOW-4:######
            def fundtransfer4():
                fund4 = Toplevel()
                fund4.configure(background='orange')
                fund4.geometry('800x600+200+50')

                ##### TEXT AREA COGEING WINDOW FUNDTRNSFER-4: ######
                global amount
                amount = IntVar(value='')
                Entry(fund4,justify='center',width=20,textvariable = amount,bd=5,fg='black',bg='white',font=('helvetica',27,'bold')).place(x=190,y=190)
                
                ##### LABEL CODEING WINDOW FUNDTRNSFER-4:###### 
                Label(fund4,text='PLEASE ENTER THE AMOUNT',bg='orange',font=('helvetica',20,'bold')).place(x=190,y=90)

                ##### FUNDTRANSFER EXCEPTION HANDLING & DATABASE CODE #####
                def fund3_transfer():
                    try:
                        query ="""SELECT user_capital FROM imaginary_atm WHERE pin =%s;"""
                        cur.execute(query,[Available_pin])
                        result_amount = cur.fetchone()
                        global total_amount
                        total_amount = int(result_amount[0])
                        if(total_amount > amount.get()):
                            fundtransfer5()
                        else:
                            Label(fund4,text='YOU DON NOT HAVE A SUFFICIENT AOMOUNT',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=80,y=300)
                    except Exception as e:  
                        Label(fund4,text='PLEASE ENTER THE VALID AOMOUNT',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=125,y=300)
            
                ##### BUTTON CODING WINDOW FUNDTRNSFER-4:######
                Button(fund4,padx=40,pady=15,text='CORRECT',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(fund3_transfer())).place(x=510,y=360) 
                Button(fund4,padx=30,pady=15,text='INCORRECT',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(fundtransfer3())).place(x=510,y=470)

                ###### FUNDTRANSFER WINDOW-5:######
                def fundtransfer5():
                    fund5 = Toplevel()
                    fund5.configure(background='orange')
                    fund5.geometry('800x600+200+50')

                    ##### TEXT AREA COGEING WINDOW FUNDTRNSFER-5: ######
                    pin = IntVar(value ='')
                    Entry(fund5,show = "*",justify='center',width=20,textvariable = pin,fg='black',bg='white',bd=5,font=('helvetica',27,'bold')).place(x=190,y=190)
                        
                    ##### LABEL CODEING WINDOW FUNDTRNSFER-5:######
                    Label(fund5,text='PLEASE ENTER THE PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=235,y=90)

                    ##### FUNDTRANSFER EXCEPTION HANDLING & DATABASE CODE #####
                    def fund4_transfer():
                        try:
                            global remaining_amount
                            if(Available_pin == pin.get()):
                                remaining_amount = total_amount - amount.get()
                                query1 = """UPDATE imaginary_atm SET user_capital = %s WHERE pin = %s;"""
                                cur.execute(query1,[remaining_amount,pin.get()])
                                con.commit()
                                fundtransfer6()
                            else:
                                Label(fund5,text='PLEASE ENTER THE CORRECT PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=155,y=300)    
                        except Exception as e:
                            Label(fund5,text='PLEASE ENTER THE VALID PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=185,y=300)    
                    
                    ##### BUTTON CODING WINDOW FUNDTRNSFER-5:######
                    Button(fund5,padx=40,pady=15,text='CONFIRM',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(fund4_transfer())).place(x=510,y=360) 
                    Button(fund5,padx=45,pady=15,text='CANCEL',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(fundtransfer4())).place(x=510,y=470)

                        
                    ###### FUNDTRANSFER WINDOW-5:######
                    def fundtransfer6():
                        fund6 = Toplevel()
                        fund6.configure(background='orange')
                        fund6.geometry('800x600+200+50')
                            
                        query = """SELECT account_no, f_name,l_name, user_capital FROM imaginary_atm WHERE account_no =%s;"""
                        cur.execute(query,[account.get()])
                        con.commit()
                        result = cur.fetchall()
                        Account_no = result[0][0]
                        Comp_name = (result[0][1]+" "+ result[0][2]).upper()
                        
                        ##### LABEL CODEING WINDOW FUNDTRNSFER-6:######
                        Label(fund6,text='CONFIDENTIAL DETAIL',bg='orange',font=('arial',23,'bold')).place(x=220,y=70)
                        Label(fund6,text='Account number  '+str(account.get()),bg='orange',font=('vardana',20,'bold')).place(x=160,y=135)
                        Label(fund6,text='Account holder name  '+str(Comp_name),bg='orange',font=('vardana',20,'bold')).place(x=160,y=175)       
                        Label(fund6,text='Amount  '+str(amount.get())+" rs",bg='orange',font=('vardana',20,'bold')).place(x=160,y=215)

                        ##### BUTTON CODING WINDOW FUNDTRNSFER-6:######
                        Button(fund6,padx=40,pady=15,text='CONFIRM',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(fundtransfer7())).place(x=510,y=360) 
                        Button(fund6,padx=45,pady=15,text='CANCEL',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(fundtransfer5())).place(x=510,y=470)
                        
                        ###### FUNDTRANSFER WINDOW-8:######
                        def fundtransfer7():
                            fund7 = Toplevel()
                            fund7.configure(background='orange')
                            fund7.geometry('800x600+200+50')
                                    
                            ##### DATABASE CODEING #####
                            db_query = """SELECT user_capital FROM imaginary_atm WHERE account_no=%s;"""
                            cur.execute(db_query,[account.get()])
                            result = cur.fetchone()
                            Send_amount = result[0] + amount.get()
                            Query = """UPDATE imaginary_atm SET user_capital =%s WHERE account_no = %s;"""
                            cur.execute(Query,[Send_amount,account.get()])
                            con.commit()
                            start = time()
                            ##### LABEL CODEING WINDOW FUNDTRNSFER-8:###### 
                            label1 =Label(fund7,text="YOUR TRANSACTION \n WAS \n SUCCESSFUL",bg='orange',font=('vardana',30,'bold')).place(x=185,y=200)
                            bank.after(5000,fund7.destroy)
                            bank.after(-6,fund6.destroy)
                            bank.after(-6,fund5.destroy)
                            bank.after(-6,fund4.destroy)
                            bank.after(-6,fund3.destroy)
                            bank.after(-6,fund2.destroy)
                            bank.after(-6,fund1.destroy)
                            bank.after(-6,top.destroy)
                                

###### PIN CHANGE WINDOW-1: ######
def pinchange():
    pin1 = Toplevel()
    pin1.configure(background='orange')
    pin1.geometry('800x600+200+50')
            
    ##### TEXT AREA COGEING PIN CHANGE WINDOW-1:######
    account = IntVar(value='')
    Entry(pin1,justify='center',width=20,textvariable = account,bd =5,fg='black',bg='white',font=('vardana',27,'bold')).place(x=190,y=190)
     
    ##### LABEL CODEING PIN CHANGE WINDOW-1: ###### 
    Label(pin1,text='\nPLEASE ENTER 11 DIGIT \n BENEFICIARY ACCOUNT NUMBER ',bg='orange',font=('vardana',20,'bold')).place(x=160,y=50) 

    ##### PINCHANGE EXCEPTION HANDLING & DATABASE CODE #####
    def pin1_transfer():
        try:
            query_ac = """SELECT account_no FROM imaginary_atm WHERE account_no =%s ;"""
            cur.execute(query_ac,[account.get()])
            customer_ac = cur.fetchone()
            if(account.get() == customer_ac[0]):
                pinchange2()
            else:
                Label(pin1,text='THERE IS NO ACCOUNT NUMBER EXISTS',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=115,y=290)    
        except Exception as e:
            Label(pin1,text='        PLEASE ENTER THE VALID AC/NO      ',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=100,y=290)
            print(e)
    ##### BUTTON CODING PIN CHANGE WINDOW-1: ######
    Button(pin1,padx=40,pady=15,text='CONFIRM',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(pin1_transfer())).place(x=510,y=360) 
    Button(pin1,padx=45,pady=15,text='CANCLE',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(signinwindow())).place(x=510,y=470)  
 
    
    ###### PIN CHANGE WINDOW-2: ######
    def pinchange2(): 
        pin2 = Toplevel()
        pin2.configure(background='orange')
        pin2.geometry('800x600+200+50')

        ##### DATABASE CODEING ######
        query_ac = """SELECT account_no FROM imaginary_atm WHERE pin =%s ;"""
        cur.execute(query_ac,[Available_pin])
        con.commit()

        ##### TEXT AREA COGEING PIN CHANGE WINDOW-2: ######
        reaccount = IntVar(value='')
        Entry(pin2,show ="*",justify='center',width=20,textvariable = reaccount,bd=5,fg='black',bg='white',font=('vardana',27,'bold')).place(x=190,y=190)
        
        ##### LABEL CODEING PIN CHANGE WINDOW-2 ###### 
        Label(pin2,text='\nPLEASE RE_ENTER 11 DIGIT \n BENEFICIARY ACCOUNT NUMBER ',bg='orange',font=('vardana',20,'bold')).place(x=160,y=50) 
            
        ##### PINCHANGE EXCEPTION HANDLING & DATABASE CODE #####
        def pin2_transfer():
            try:
                if(account.get() == reaccount.get()):
                    pinchange3()
                else:
                    Label(pin2,text='PLEASE RECHECK YOUR ACCOUNT',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=145,y=290)    
            except Exception as e: 
                Label(pin2,text='        PLEASE ENTER THE VALID AC/NO      ',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=100,y=290)
                
        ##### BUTTON CODING PIN CHANGE WINDOW-1: ######        
        Button(pin2,padx=40,pady=15,text='CORRECT',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(pin2_transfer())).place(x=510,y=360) 
        Button(pin2,padx=30,pady=15,text='INCORRECT',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(pinchange())).place(x=510,y=470)    
            
        ###### PIN CHANGE WINDOW-3: ######
        def pinchange3():
            pin3 = Toplevel()
            pin3.configure(background='orange')
            pin3.geometry('800x600+200+50')
            
            ##### LABEL CODEING PIN CHANGE WINDOW-3######
            Label(pin3,text = 'New password ',fg='black',bg= 'orange',font =('vardana',24,'bold')).place(x=115,y=180)
            Label(pin3,text = 'Confirm password',fg='black',bg= 'orange',font = ('vardana',24,'bold')).place(x=115,y=280)

            ##### TEXT AREA COGEING PIN CHANGE WINDOW-3 ######
            new_pin = IntVar(value='')
            Entry(pin3,width = 12,bd=5,justify='center',textvariable = new_pin,bg='white',font=('vardana',27,'bold')).place(x=420,y=170)
            confirm_pin = IntVar(value='')
            Entry(pin3,show="*",width = 12,bd=5,justify='center',textvariable=confirm_pin,bg='white',font=('vardana',27,'bold')).place(x=420,y=270)

            ##### PINCHNAGE EXCEPTION HANDLING & DATABASE CODE #####
            def pin2_transfer():
                try:
                    if(new_pin.get() == confirm_pin.get()):
                        pinchange4()
                    else:
                        Label(pin3,text='PLEASE RECHECK THE PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=85,y=400)    
                except Exception as e: 
                    Label(pin3,text='PLEASE RECHECK THE PIN',fg='black',bg='orange',font=('helvetica',20,'bold')).place(x=85,y=400)     
                    print(e)
                
            ##### BUTTON CODING PIN CHANGE WINDOW-1: ######
            Button(pin3,padx=35,pady=10,text='CONFROM',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(pin2_transfer())).place(x=480,y=370) 
            Button(pin3,padx=45,pady=10,text='CANCLE',fg='black',bg='yellow',bd=6,font=('vardana',14,'bold'),command=lambda:(pinchange2())).place(x=480,y=470)

            ###### PIN CHANGE WINDOW-4: ######
            def pinchange4():
                pin4 = Toplevel()
                pin4.configure(background='orange')
                pin4.geometry('800x600+200+50')
                start = time()
                
                query = """UPDATE imaginary_atm SET pin =%s WHERE account_no=%s;"""
                cur.execute(query,[new_pin.get(),account.get()])
                con.commit()
                
                ##### LABEL CODEING PIN CHANGE WINDOW-3######
                Label(pin4,text='THANKS YOU VISIT US ',bg='orange',font=('vardana',25,'bold')).place(x=205,y=90)
                Label(pin4,text="YOUR PIN \n is \n SUCCESSFULY CHANGE",bg='orange',font=('vardana',30,'bold')).place(x=140,y=250)
                bank.after(5000,pin4.destroy)
                bank.after(-6,pin3.destroy)
                bank.after(-6,pin2.destroy)
                bank.after(-6,pin1.destroy)
                bank.after(-6,top.destroy)
                 
           
bank.mainloop()




