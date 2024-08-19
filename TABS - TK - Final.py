import smtplib
from email.message import EmailMessage
import mysql.connector as cnkt
import random
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.iconbitmap("C:/gui/icon.ico")
    register_screen.title("TABS - Register")
    register_screen.geometry("500x500")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below to register", height=2, width=500, bg="black", fg='white', font =('calibri',13,'bold')).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ",font=('bold')).pack()
    username_entry = Entry(register_screen,textvariable=username).pack()
    Label(register_screen, text='').pack()
    contactnumber_lable = Label(register_screen, text="Contact Number * ",font=('bold')).pack()
    contactnumber_entry = Entry(register_screen).pack()
    Label(register_screen, text='').pack()
    fathername_lable = Label(register_screen, text="Father's name * ",font=('bold')).pack()
    fathername_entry = Entry(register_screen).pack()
    Label(register_screen, text='').pack()
    dateofbirth_lable = Label(register_screen, text="Date of birth(YYYY-MM-DD ) * ",font=('bold')).pack()
    dateofbirth_entry = Entry(register_screen).pack()
    Label(register_screen, text='').pack()
    emailid_lable = Label(register_screen, text="Email Id * ",font=('bold')).pack()
    emailid_entry = Entry(register_screen).pack()
    Label(register_screen, text='').pack()
    password_lable = Label(register_screen, text="Password * ",font=('bold')).pack()
    password_entry = Entry(register_screen, textvariable=password, show='*').pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="black", fg='white', command = register_user).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    mycon = cnkt.connect(host="localhost", user="root", password="admin", database="TABS")
    mycur = mycon.cursor(buffered=True)
    qur = 'INSERT INTO users(user,pass) VALUES(%s,%s)'
    val = (username_info,password_info)
    mycur.execute(qur,val)
    mycon.commit()
    mycon.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(register_screen, text="Registration Success", bg ='black', fg="white", font=("calibri", 11)).pack()
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.iconbitmap("C:/gui/icon.ico")
    login_screen.title("TABS - Login")
    login_screen.geometry("400x250")
    Label(login_screen, text="Please enter details below to login", bg = 'black', fg='white', height=2, width=400, font=('Calibri',13,'bold')).pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ", font=('bold')).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify).pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ", font=('bold')).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*').pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify,bg='black', fg='white', font=('bold')).pack()
  
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    mycon = cnkt.connect(host="localhost", user="root", password="admin", database="TABS")
    mycur = mycon.cursor(buffered=True)
    mycur.execute('SELECT * FROM users')
    res = mycur.fetchall()
    for row in res:
        if username1 in row[0]:
            if password1 in row [1]: login_sucess()
            else: password_not_recognised()
        else: user_not_found()
    mycon.commit()
    mycon.close()
  
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.iconbitmap("C:/gui/icon.ico")
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=menu).pack()
  
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.iconbitmap("C:/gui/icon.ico")
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
  
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.iconbitmap("C:/gui/icon.ico")
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
  
def delete_login_success():
    login_success_screen.destroy()
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
def deposit():
    global typ
    global am1
    global deposit_screen
    deposit_screen = Toplevel(main_screen)
    deposit_screen.iconbitmap("C:/gui/icon.ico")
    deposit_screen.title("TABS - Deposit")
    deposit_screen.geometry("400x400")
    Label(deposit_screen, text="Please enter details below to deposit",bg="black", fg='white', width="500", height="2", font=("Calibri", 13, 'bold')).pack()
    Label(deposit_screen, text="").pack()

    amount_lable = Label(deposit_screen, text="Amount * ", font=('bold')).pack()
    am1 = Entry(deposit_screen).pack()
    Label(deposit_screen, text='').pack()
    type_label = Label(deposit_screen, text="Transaction type:", font=('bold')).pack()
    typ = Entry(deposit_screen).pack()
    Label(deposit_screen, text='').pack()
    Label(deposit_screen, text='').pack()
    Label(deposit_screen, text="").pack()
    Button(deposit_screen, text="Deposit", width=10, height=1, bg="black", fg='white', font=('bold'), command = savedep).pack()
    Label(deposit_screen, text="").pack()
    Button(deposit_screen,text="GO HOME", height=1 , width=10 ,fg='white',bg='black', font=('bold'), command=main_menu).pack()
    Label(deposit_screen,text="").pack()

def savedep():
    tid = random.randint(100000, 999999)
    tdate = time.strftime("%Y-%m-%d %H:%M:%S")
    ttype = "C"
    description = "CREDITED"

    try:
        amount=float(am1.get())
        ptype=str(typ.get())
    except ValueError:
        Label(deposit_screen, text='Error!')

    mycon = cnkt.connect(host="localhost", user="root", password="admin", database="TABS")
    mycur = mycon.cursor(buffered=True)

    try:
        mycur.execute('SELECT balance FROM transaction_record ORDER BY tdate DESC')
        res = mycur.fetchone()
        account_balance = res[0] + amount
    except TypeError:
        account_balance = amount

    qur = "INSERT INTO transaction_record(tid, tdate, ttype, description, amount, type, balance) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    value = (tid, tdate, ttype, description, amount, ptype, account_balance)
    mycur.execute(qur, value)
    mycon.commit()

    if ptype.lower() == 'cheque':
        qur = "INSERT INTO cheque_record(tid, tdate, ttype, description, amount, type, balance) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur, value)
        mycon.commit()
    elif ptype.lower() == 'dd':
        qur = "INSERT INTO dd_record(tid, tdate, ttype, description, amount, type, balance) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur, value)
        mycon.commit()
    else: pass

    mycon.close()
    msg.showinfo("Deposit Sucess", "Sucess")
    deposit_screen.destroy()

def withdraw():
    global withdraw_screen
    global am2
    global typ2
    withdraw_screen = Toplevel(main_screen)
    withdraw_screen.iconbitmap("C:/gui/icon.ico")
    withdraw_screen.title("TABS - Withdraw")
    withdraw_screen.geometry("400x400")
    Label(withdraw_screen, text="Please enter details below to withdraw",bg="black", fg='white', width="500", height="2", font=("Calibri", 13, 'bold')).pack()
    Label(withdraw_screen, text="").pack()

    amount_lable = Label(withdraw_screen, text="Amount * ",font=('bold')).pack()
    am2 = Entry(withdraw_screen).pack()
    type_label = Label(withdraw_screen, text="Transaction type:",font=('bold')).pack()
    typ2 = Entry(withdraw_screen).pack()
    Label(withdraw_screen, text="").pack()
    Button(withdraw_screen, text="Withdraw", width=10, height=1, fg='white', bg='black', font=('bold'), command=savewith).pack()
    Label(withdraw_screen, text="").pack()
    Button(withdraw_screen, text="GO HOME", height=1, width=10, fg='white', bg='black', font=('bold'), command=main_menu).pack()
    Label(withdraw_screen, text="").pack()

def savewith():
    tid = random.randint(100000, 999999)
    tdate = time.strftime("%Y-%m-%d %H:%M:%S")
    ttype = "D"
    description = "DEBITED"

    try:
        amount = float(am2.get())
        ptype = str(typ2.get())
    except ValueError:
        Label(deposit_screen, text='Error!')

    mycon = cnkt.connect(host="localhost", user="root", password="admin", database="TABS")
    mycur = mycon.cursor(buffered=True)

    mycur.execute('SELECT balance FROM transaction_record ORDER BY tdate DESC')
    res = mycur.fetchone()
    account_balance = res[0] - amount

    qur = "INSERT INTO transaction_record(tid, tdate, ttype, description, amount, type, balance) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    value = (tid, tdate, ttype, description, amount, ptype, account_balance)
    mycur.execute(qur, value)
    mycon.commit()

    if ptype.lower() == 'cheque':
        qur = "INSERT INTO cheque_record(tid, tdate, ttype, description, amount, type, balance) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur, value)
        mycon.commit()
    elif ptype.lower() == 'dd':
        qur = "INSERT INTO dd_record(tid, tdate, ttype, description, amount, type, balance) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur, value)
        mycon.commit()
    else: pass

    mycon.close()

    msg.showinfo("Withdrawl Sucess", "Sucess")
    withdraw_screen.destroy()

def balance():
    balance_screen = Toplevel(main_screen)
    balance_screen.iconbitmap("C:/gui/icon.ico")
    balance_screen.title('Transaction History')
    balance_screen.geometry('1500x800')
    columnst = ('TID', 'TDATE', 'TTYPE', 'DESCRIPTION', 'AMOUNT', 'TYPE', 'BALANCE')
    tree = ttk.Treeview(balance_screen, columns = columnst, show='headings')
    tree.heading('TID', text='TID')
    tree.heading('TDATE', text='TDATE')
    tree.heading('TTYPE', text='TTYPE')
    tree.heading('DESCRIPTION', text='DESCRIPTION')
    tree.heading('AMOUNT', text='AMOUNT')
    tree.heading('TYPE', text='TYPE')
    tree.heading('BALANCE', text='BALANCE')
    mycon = cnkt.connect(host="localhost", user="root", password="admin", database="TABS")
    mycur = mycon.cursor(buffered=True)
    mycur.execute('SELECT * FROM transaction_record')
    res = mycur.fetchall()
    for rec in res:
        tree.insert('',tk.END, values=rec)
    tree.pack()
    mycon.close()
    balance_screen.mainloop()

def cbalance():
    cbalance_screen = Toplevel(main_screen)
    cbalance_screen.iconbitmap("C:/gui/icon.ico")
    cbalance_screen.title('Transaction History')
    cbalance_screen.geometry('1500x800')
    columnst = ('TID', 'TDATE', 'TTYPE', 'DESCRIPTION', 'AMOUNT', 'TYPE', 'BALANCE')
    tree = ttk.Treeview(cbalance_screen, columns = columnst, show='headings')
    tree.heading('TID', text='TID')
    tree.heading('TDATE', text='TDATE')
    tree.heading('TTYPE', text='TTYPE')
    tree.heading('DESCRIPTION', text='DESCRIPTION')
    tree.heading('AMOUNT', text='AMOUNT')
    tree.heading('TYPE', text='TYPE')
    tree.heading('BALANCE', text='BALANCE')
    mycon = cnkt.connect(host="localhost", user="root", password="admin", database="TABS")
    mycur = mycon.cursor(buffered=True)
    mycur.execute('SELECT * FROM cheque_record')
    res = mycur.fetchall()
    for rec in res:
        tree.insert('',tk.END, values=rec)
    tree.pack()
    mycon.close()
    cbalance_screen.mainloop()

def dbalance():
    dbalance_screen = Toplevel(main_screen)
    dbalance_screen.iconbitmap("C:/gui/icon.ico")
    dbalance_screen.title('Transaction History')
    dbalance_screen.geometry('1500x800')
    columnst = ('TID', 'TDATE', 'TTYPE', 'DESCRIPTION', 'AMOUNT', 'TYPE', 'BALANCE')
    tree = ttk.Treeview(dbalance_screen, columns = columnst, show='headings')
    tree.heading('TID', text='TID')
    tree.heading('TDATE', text='TDATE')
    tree.heading('TTYPE', text='TTYPE')
    tree.heading('DESCRIPTION', text='DESCRIPTION')
    tree.heading('AMOUNT', text='AMOUNT')
    tree.heading('TYPE', text='TYPE')
    tree.heading('BALANCE', text='BALANCE')
    mycon = cnkt.connect(host="localhost", user="root", password="admin", database="TABS")
    mycur = mycon.cursor(buffered=True)
    mycur.execute('SELECT * FROM dd_record')
    res = mycur.fetchall()
    for rec in res:
        tree.insert('',tk.END, values=rec)
    tree.pack()
    mycon.close()
    dbalance_screen.mainloop()

def loan_dep():
    global lam1
    global loan_dep_screen
    loan_dep_screen = Toplevel(main_screen)
    loan_dep_screen.iconbitmap("C:/gui/icon.ico")
    loan_dep_screen.title("TABS - Loan Avail")
    loan_dep_screen.geometry("400x400")
    Label(loan_dep_screen, text="Enter the details to avail loan", bg="black", fg='white', width="500", height="2",font=("Calibri", 13, 'bold')).pack()
    Label(loan_dep_screen, text="").pack()

    amount_lable = Label(loan_dep_screen, text="Amount * ", font=('bold')).pack()
    lam1 = Entry(loan_dep_screen).pack()
    Label(loan_dep_screen, text='').pack()
    Button(loan_dep_screen, text="Avail Loan", width=10, height=1, bg="black", fg='white', font=('bold'),command=save_loan_dep).pack()
    Label(loan_dep_screen, text="").pack()
    Button(loan_dep_screen, text="GO HOME", height=1, width=10, fg='white', bg='black', font=('bold'), command=main_menu).pack()
    Label(loan_dep_screen, text="").pack()

def save_loan_dep():
    tid = random.randint(100000, 999999)
    tdate = time.strftime("%Y-%m-%d %H:%M:%S")
    ttype = "C"
    description = "CREDITED"
    ptype = 'LOAN'
    try:
        amount = float(lam1.get())
    except ValueError:
        Label(loan_dep_screen, text='Error!')

    mycon = cnkt.connect(host="localhost", user="root", password="admin", database="TABS")
    mycur = mycon.cursor(buffered=True)

    mycur.execute('SELECT loanbal FROM loan_balance')
    lres = mycur.fetchone()
    chk = int(lres[0])
    if chk >= amount:
        pass
    elif chk <= amount:
        msg.showinfo('Not sufficient cerdibility', 'Failed')
        loan_dep_screen.destroy()
    else:
        msg.showinfo('Server Error', 'Failed')
        loan_dep_screen.destroy()

    mycur.execute('SELECT balance FROM transaction_record ORDER BY tdate DESC')
    res = mycur.fetchone()
    account_balance = res[0] + amount

    qur = "INSERT INTO transaction_record(tid, tdate, ttype, description, amount, type, balance) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    value = (tid, tdate, ttype, description, amount, ptype, account_balance)
    mycur.execute(qur, value)
    mycon.commit()

    qur = "INSERT INTO loan_record(tid, tdate, ttype, description, amount, type, balance) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    value = (tid, tdate, ttype, description, amount, ptype, account_balance)
    mycur.execute(qur, value)
    mycon.commit()

    mycur.execute('DELETE FROM loan_balance')
    wrt = chk - amount
    qur='INSERT INTO loan_balance(loanbal) VALUES(%s)'
    val = (wrt,)
    mycur.execute(qur,val)
    mycon.commit()
    mycon.close()

    email_a = 'tabspublicrelations@gmail.com'
    email_p = 'iamincredible'
    msg = EmailMessage()
    msg['Subject'] = 'Loan Sanctioned - TABS'
    msg['From'] = email_a
    msg['To'] = 'kashwathaman@gmail.com'
    msg.set_content("""Greetings from The Accountables Banking System.
            Your loan was sanctioned and the amount was credited to your account.
            Keep banking with us - IncredibleCEO""")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_a, email_p)
        smtp.send_message(msg)
    smtp.close()
    loan_dep_screen.destroy()

def loan_with():
    global lam2
    global loan_with_screen
    loan_with_screen = Toplevel(main_screen)
    loan_with_screen.iconbitmap("C:/gui/icon.ico")
    loan_with_screen.title("TABS - Loan Repay")
    loan_with_screen.geometry("400x400")
    Label(loan_with_screen, text="Enter the details to repay loan", bg="black", fg='white', width="500", height="2",font=("Calibri", 13, 'bold')).pack()
    Label(loan_with_screen, text="").pack()

    amount_lable = Label(loan_with_screen, text="Amount * ", font=('bold')).pack()
    lam2 = Entry(loan_with_screen).pack()
    Label(loan_with_screen, text='').pack()
    Button(loan_with_screen, text="Repay Loan", width=10, height=1, bg="black", fg='white', font=('bold'),command=save_loan_with).pack()
    Label(loan_with_screen, text="").pack()
    Button(loan_with_screen, text="GO HOME", height=1, width=10, fg='white', bg='black', font=('bold'), command=main_menu).pack()
    Label(loan_with_screen, text="").pack()

def save_loan_with():
    tid = random.randint(100000, 999999)
    tdate = time.strftime("%Y-%m-%d %H:%M:%S")
    ttype = "D"
    description = "DEBITED"
    ptype = 'LOAN'
    try:
        amount = float(lam2.get())
    except ValueError:
        Label(loan_with_screen, text='Error!')

    mycon = cnkt.connect(host="localhost", user="root", password="admin", database="TABS")
    mycur = mycon.cursor(buffered=True)

    mycur.execute('SELECT balance FROM transaction_record ORDER BY tdate DESC')
    res = mycur.fetchone()
    account_balance = res[0] - amount

    qur = "INSERT INTO transaction_record(tid, tdate, ttype, description, amount, type, balance) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    value = (tid, tdate, ttype, description, amount, ptype, account_balance)
    mycur.execute(qur, value)
    mycon.commit()

    qur = "INSERT INTO loan_record(tid, tdate, ttype, description, amount, type, balance) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    value = (tid, tdate, ttype, description, amount, ptype, account_balance)
    mycur.execute(qur, value)
    mycon.commit()

    mycur.execute('SELECT loanbal FROM loan_balance')
    chk = mycur.fetchone()
    mycur.execute('DELETE FROM loan_balance')
    wrt = chk[0] + amount
    qur='INSERT INTO loan_balance(loanbal) VALUES(%s)'
    val = (wrt,)
    mycur.execute(qur,val)
    mycon.commit()

    mycon.close()

    email_a = 'tabspublicrelations@gmail.com'
    email_p = 'iamincredible'
    msg = EmailMessage()
    msg['Subject'] = 'Loan repayment - TABS'
    msg['From'] = email_a
    msg['To'] = 'kashwathaman@gmail.com'
    msg.set_content("""Greetings from The Accountables Banking System.
                Your loan was paid towards recently and the amount was debited from your account.
                Keep banking with us - IncredibleCEO""")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_a, email_p)
        smtp.send_message(msg)
    smtp.close()
    loan_with_screen.destroy()

def lbalance():
    global lbalance_screen
    lbalance_screen = Toplevel(main_screen)
    lbalance_screen.iconbitmap("C:/gui/icon.ico")
    lbalance_screen.title('Transaction History')
    lbalance_screen.geometry('1500x1000')
    columnst = ('TID', 'TDATE', 'TTYPE', 'DESCRIPTION', 'AMOUNT', 'TYPE', 'BALANCE')
    tree = ttk.Treeview(lbalance_screen, columns=columnst, show='headings')
    tree.heading('TID', text='TID')
    tree.heading('TDATE', text='TDATE')
    tree.heading('TTYPE', text='TTYPE')
    tree.heading('DESCRIPTION', text='DESCRIPTION')
    tree.heading('AMOUNT', text='AMOUNT')
    tree.heading('TYPE', text='TYPE')
    tree.heading('BALANCE', text='BALANCE')
    mycon = cnkt.connect(host="localhost", user="root", password="admin", database="TABS")
    mycur = mycon.cursor(buffered=True)
    mycur.execute('SELECT * FROM loan_record')
    res = mycur.fetchall()
    for rec in res:
        tree.insert('', tk.END, values=rec)
    tree.pack()
    mycon.close()
    lbalance_screen.mainloop()

def loans():
    global loans
    loans = Toplevel(main_screen)
    loans.iconbitmap("C:/gui/icon.ico")
    loans.title("TABS - Loan Section")
    loans.geometry("500x500")
    Label(loans,text="Select Your Choice", bg="black", fg='white', width="300", height="3", font=("Calibri", 13,'bold')).pack()
    Label(loans,text="").pack()
    Button(loans,text="Avail Loan", height="2", width="30",fg='white',bg='black', font=("Arial Bold", 10), command=loan_dep).pack()
    Label(loans,text="").pack()
    Button(loans,text="Repay Loan", height="2", width="30",fg='white',bg='black', font=("Arial Bold", 10), command=loan_with).pack()
    Label(loans,text="").pack()
    Button(loans, text="Loan History", height="2", width="30", fg='white', bg='black', font=("Arial Bold", 10), command=lbalance).pack()
    Label(loans, text="").pack()
    Button(loans,text="HOME", height="2", width="30",fg='white',bg='black' , font=("Arial Bold", 10), command=menu).pack()
    Label(loans,text="").pack()

def locker_av():
    global locker_av_screen
    global loartname
    global loartwht
    locker_av_screen = Toplevel(main_screen)
    locker_av_screen.iconbitmap("C:/gui/icon.ico")
    locker_av_screen.title("TABS - Avail Locker")
    locker_av_screen.geometry('500x500')
    Label(locker_av_screen, text="Enter the details to avail locker", bg="black", fg='white', width="500", height="2",font=("Calibri", 13, 'bold')).pack()
    Label(locker_av_screen, text="").pack()

    name_lable = Label(locker_av_screen, text="Name of the Article * ", font=('bold')).pack()
    loartname = Entry(locker_av_screen).pack()
    weight_lable = Label(locker_av_screen, text="Weight of the Article * ", font=('bold')).pack()
    loartwht = Entry(locker_av_screen).pack()
    Label(locker_av_screen,text='').pack()
    Button(locker_av_screen, text="Avail Locker", width=10, height=1, bg="black", fg='white', font=('bold'),command=save_locker_av).pack()
    Label(locker_av_screen, text="").pack()
    Button(locker_av_screen, text="GO HOME", height=1, width=10, fg='white', bg='black', font=('bold'),command=main_menu).pack()
    Label(locker_av_screen, text="").pack()

def save_locker_av():
    ano = random.randint(20, 100)
    tdate = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        name = str(loartname.get())
        weight = float(loartwht.get())
    except ValueError or AttributeError:
        Label(locker_av_screen, text='Error!')
    stcost = float(weight*25)

    tid = random.randint(100000, 999999)
    tdate = time.strftime("%Y-%m-%d %H:%M:%S")
    ttype = "D"
    description = "DEBITED"
    ptype = "LOCKER"

    mycon = cnkt.connect(host='localhost',user='root',password='admin',database='TABS')
    mycur = mycon.cursor(buffered=True)
    mycur.execute('SELECT balance FROM transaction_record ORDER BY tdate DESC')
    res = mycur.fetchone()
    account_balance = res[0] - stcost
    qur = 'INSERT INTO transaction_record (tid, tdate, ttype, description, amount, type, balance)VALUES(%s,%s,%s,%s,%s,%s,%s)'
    val = (tid, tdate, ttype, description, stcost, ptype, account_balance)
    mycur.execute(qur,val)
    mycon.commit()
    qur = 'INSERT INTO locker_record (ano, date, name, weight, stcost) VALUES(%s,%s,%s,%s,%s)'
    val = (ano, tdate, name, weight, stcost)
    mycur.execute(qur,val)
    mycon.commit()
    mycon.close()

    Label(locker_av_screen, text='Locker Availed', font=('bold')).pack()
    email_a = 'tabspublicrelations@gmail.com'
    email_p = 'iamincredible'
    msg = EmailMessage()
    msg['Subject'] = 'Loan Sanctioned - TABS'
    msg['From'] = email_a
    msg['To'] = 'kashwathaman@gmail.com'
    msg.set_content("""Greetings from The Accountables Banking System.
                Your locker was allocted and the single-time amount was debited from your account.
                Your article is safe with us in our foolproof safe in undisclosed location.
                Keep banking with us - IncredibleCEO""")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_a, email_p)
        smtp.send_message(msg)
    smtp.close()

def locker_cl():
    global locker_cl_screen
    global loartno
    locker_cl_screen = Toplevel(main_screen)
    locker_cl_screen.iconbitmap("C:/gui/icon.ico")
    locker_cl_screen.title("TABS - Avail Locker")
    locker_cl_screen.geometry('500x500')
    Label(locker_cl_screen, text="Enter the details to close locker", bg="black", fg='white', width="500", height="2",font=("Calibri", 13, 'bold')).pack()
    Label(locker_cl_screen, text="").pack()

    no_lable = Label(locker_cl_screen, text="Enter the Article number * ", font=('bold')).pack()
    loartno = Entry(locker_cl_screen).pack9
    Label(locker_cl_screen, text='').pack()
    Button(locker_cl_screen, text="Close Locker", width=10, height=1, bg="black", fg='white', font=('bold'),command=save_locker_cl).pack()
    Label(locker_cl_screen, text="").pack()
    Button(locker_cl_screen, text="GO HOME", height=1, width=10, fg='white', bg='black', font=('bold'),command=main_menu).pack()
    Label(locker_cl_screen, text="").pack()

def save_locker_cl():
    try:
        ano = int(loartno.get())
    except:
        Label(locker_cl_screen, text='ERROR!')

    mycon = cnkt.connect(host='localhost', user='root', password='admin', database='TABS')
    mycur = mycon.cursor(buffered=True)
    qur = 'SELECT * FROM locker_record WHERE ano=%s'
    value = (ano,)
    mycur.execute(qur, value)
    rec = mycur.fetchall()
    if mycur.rowcount == 0:
        Label(locker_cl_screen, text='No such article was found', font=('bold')).pack()
    else:
        qur = 'DELETE FROM locker_record WHERE ano=%s'
        value = (ano,)
        mycur.execute(qur, value)
        mycon.commit()
        Label(locker_cl_screen, text='Locker Closed', font=('bold')).pack()

    email_a = 'tabspublicrelations@gmail.com'
    email_p = 'iamincredible'
    msg = EmailMessage()
    msg['Subject'] = 'Loan Sanctioned - TABS'
    msg['From'] = email_a
    msg['To'] = 'kashwathaman@gmail.com'
    msg.set_content("""Greetings from The Accountables Banking System.
                Your locker was closed on account of your choice adn the article can be collected at out nearest branch.
                Keep banking with us - IncredibleCEO""")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_a, email_p)
        smtp.send_message(msg)
    smtp.close()
    mycon.close()

def lohist():
    global  lohist_screen
    lohist_screen = Toplevel(main_screen)
    lohist_screen.iconbitmap("C:/gui/icon.ico")
    lohist_screen.title('Transaction History')
    lohist_screen.geometry('1500x800')
    columnst = ('ANO', 'DATE', 'NAME', 'WEIGHT', 'STCOST')
    tree = ttk.Treeview(lohist_screen, columns=columnst, show='headings')
    tree.heading('ANO', text='ANO')
    tree.heading('DATE', text='DATE')
    tree.heading('NAME', text='NAME')
    tree.heading('WEIGHT', text='WEIGHT')
    tree.heading('STCOST', text='STCOST')
    mycon = cnkt.connect(host="localhost", user="root", password="admin", database="TABS")
    mycur = mycon.cursor(buffered=True)
    mycur.execute('SELECT * FROM locker_record')
    res = mycur.fetchall()
    for rec in res:
        tree.insert('', tk.END, values=rec)
    tree.pack()
    mycon.close()
    lohist_screen.mainloop()

def lockers():
    global lockers
    lockers = Toplevel(main_screen)
    lockers.iconbitmap("C:/gui/icon.ico")
    lockers.title("TABS - Locker Section")
    lockers.geometry("500x500")
    Label(lockers,text="Select Your Choice", bg="black", fg='white', width="300", height="3", font=("Calibri", 13,'bold')).pack()
    Label(lockers,text="").pack()
    Button(lockers,text="Avail Locker", height="2", width="30",fg='white',bg='black', font=("Arial Bold", 10), command=locker_av).pack()
    Label(lockers,text="").pack()
    Button(lockers,text="Close Locker", height="2", width="30",fg='white',bg='black', font=("Arial Bold", 10), command=locker_cl).pack()
    Label(lockers,text="").pack()
    Button(lockers, text="Locker Record", height="2", width="30", fg='white', bg='black', font=("Arial Bold", 10), command=lohist).pack()
    Label(lockers, text="").pack()
    Button(lockers,text="HOME", height="2", width="30",fg='white',bg='black' , font=("Arial Bold", 10), command=menu).pack()
    Label(lockers,text="").pack()

def rep():
    global rtid
    global repd
    global rep_screen
    rep_screen = Toplevel(main_screen)
    rep_screen.iconbitmap("C:/gui/icon.ico")
    rep_screen.title("TABS - Reports")
    rep_screen.geometry("400x400")
    Label(rep_screen, text="Enter the details to file report", bg="black", fg='white', width="500", height="2",font=("Calibri", 13, 'bold')).pack()
    Label(rep_screen, text="").pack()

    tno_lable = Label(rep_screen, text="Transaction ID *", font=('bold')).pack()
    rtid = Entry(rep_screen).pack()
    Label(rep_screen, text='').pack()
    rep_lable = Label(rep_screen, text="Report Details *", font=('bold')).pack()
    repd = Entry(rep_screen).pack()
    Label(rep_screen, text='').pack()
    Button(rep_screen, text="File Report", width=10, height=1, bg="black", fg='white', font=('bold'),command=save_rep).pack()
    Label(rep_screen, text="").pack()
    Button(rep_screen, text="GO HOME", height=1, width=10, fg='white', bg='black', font=('bold'), command=main_menu).pack()
    Label(rep_screen, text="").pack()

def save_rep():
    rtno = 0
    rdes = ''
    try:
        rtno = int(rtid.get())
        rdes = str(repd.get())
    except:
        Label(rep_screen, text='ERROR!')

    rno = random.randint(100000,999999)
    rdate = time.strftime("%Y-%m-%d %H:%M:%S")
    status = "RESOLVED"

    mycon = cnkt.connect(host='localhost', user='root', password='admin', database='TABS')
    mycur = mycon.cursor(buffered=True)
    qur = 'INSERT INTO reports(rno, rdate, tno, description, status) VALUES(%s,%s,%s,%s,%s)'
    val = (rno, rdate, rtno, rdes, status)
    mycur.execute(qur,val)
    mycon.commit()
    mycon.close()

    email_a = 'tabspublicrelations@gmail.com'
    email_p = 'iamincredible'
    msg = EmailMessage()
    msg['Subject'] = 'Report Filed - TABS'
    msg['From'] = email_a
    msg['To'] = 'kashwathaman@gmail.com'
    msg.set_content("""Greetings from The Accountables Banking System.
        We have received the report filed by you on a fradulent transaction on """ + rdate + """ and we are working to resolve your issue as soon as possile.
        Kindly be patient till the issue is resolved""")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_a, email_p)
        smtp.send_message(msg)
    smtp.close()

def main_menu():
    deposit_screen.destroy()

def main_menu1():
    withdraw_screen.destroy()
    
def menu():
    global menu_screen
    menu_screen = Toplevel(main_screen)
    menu_screen.iconbitmap("C:/gui/icon.ico")
    menu_screen.title("TABS - Menu")
    menu_screen.geometry("500x700")
    Label(menu_screen,text="Select Your Choice", bg="black", fg='white', width="300", height="3", font=("Calibri", 13,'bold')).pack()
    Label(menu_screen,text="").pack()    
    Button(menu_screen,text="Deposit", height="2", width="30",fg='white',bg='black', font=("Arial Bold", 10), command=deposit).pack()
    Label(menu_screen,text="").pack()
    Button(menu_screen,text="Withdraw", height="2", width="30",fg='white',bg='black', font=("Arial Bold", 10), command=withdraw).pack()
    Label(menu_screen,text="").pack()
    Button(menu_screen, text="Transaction History", height="2", width="30", fg='white', bg='black', font=("Arial Bold", 10),command=balance).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Cheque History", height="2", width="30", fg='white', bg='black', font=("Arial Bold", 10),command=cbalance).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="DD History", height="2", width="30", fg='white', bg='black', font=("Arial Bold", 10),command=dbalance).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen,text="Loans", height="2", width="30",fg='white',bg='black' , font=("Arial Bold", 10), command=loans).pack()
    Label(menu_screen,text="").pack()
    Button(menu_screen, text="Lockers", height="2", width="30", fg='white', bg='black', font=("Arial Bold", 10),command=lockers).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Reports", height="2", width="30", fg='white', bg='black', font=("Arial Bold", 10), command=rep).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen,text="Logout", height="2", width="10",fg='white',bg='black' , font=("Arial Bold", 10), command=logout2).pack()
    Label(menu_screen,text="").pack()

def logout2():
    menu_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.iconbitmap("C:/gui/icon.ico")
    main_screen.geometry("400x200")
    main_screen.title("TABS - Login")
    Label(text="Select Your Choice", bg="black", fg='white', width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="10",fg='white',bg='black' ,font=("Arial Bold", 10)  ,command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="10",fg='white',bg='black',font=("Arial Bold", 10), command=register).pack()
    Label(text="").pack()

    main_screen.mainloop()
main_account_screen()