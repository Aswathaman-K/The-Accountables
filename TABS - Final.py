
import smtplib
from email.message import EmailMessage
import mysql.connector as cnkt
mycon = cnkt.connect(
    host="localhost",
    user="root",
    password="admin",
    database="TABS",
)
mycur = mycon.cursor()


def deposit():
    global ptype
    global account_balance
    import random
    import time

    account_balance = 0
    with open("balance.txt", "r") as balancefile:
        lines = balancefile.readlines()
        for line in lines:
            if line.isdigit():
                account_balance = int(line)

    print("\n\t\t---IncreDEPOSIT!---")
    amount = int(input("\n\nEnter the amount to be deposited:"))
    print("1.Cash\n2.Cheque\n3.Demand Deposit")

    cho = int(input("\nEnter the type of transaction:"))
    if cho == 1:
        ptype = "CASH"
        qur = """insert into transaction_record(tid, tdate, ttype, description, amount, type, balance)
                values(%s,%s,%s,%s,%s,%s,%s)"""
        tid = random.randint(100000, 999999)
        tdate = time.strftime("%Y-%m-%d %H:%M:%S")
        ttype = "C"
        description = "CREDITED"
        account_balance += amount
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur, value)
        mycon.commit()

        print("\nRs",amount,"has been credited to account by",ptype)

        with open("balance.txt", "w") as balancefile:
            balancefile.write(str(account_balance))

    elif cho == 2:
        ptype = "CHEQUE"
        qur2 = """insert into transaction_record(tid, tdate, ttype, description, amount, type, balance)
        values(%s,%s,%s,%s,%s,%s,%s)"""
        tid = random.randint(100000, 999999)
        tdate = time.strftime("%Y-%m-%d %H:%M:%S")
        ttype = "C"
        description = "CREDITED"
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur2, value)
        mycon.commit()

        qur3 = """insert into cheque_record(tid, tdate, ttype, description, amount, type, balance)
                        values(%s,%s,%s,%s,%s,%s,%s)"""
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur3, value)
        mycon.commit()

        print("\nRs", amount, "has been credited to account by", ptype)

        with open("balance.txt", "w") as balancefile:
            balancefile.write(str(account_balance))

    elif cho == 3:
        ptype = "DD"
        qur2 = """insert into transaction_record(tid, tdate, ttype, description, amount, type, balance)
                values(%s,%s,%s,%s,%s,%s,%s)"""
        tid = random.randint(100000, 999999)
        tdate = time.strftime("%Y-%m-%d %H:%M:%S")
        ttype = "C"
        description = "CREDITED"
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur2, value)
        mycon.commit()

        qur3 = """insert into dd_record(tid, tdate, ttype, description, amount, type, balance)
                                values(%s,%s,%s,%s,%s,%s,%s)"""
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur3, value)
        mycon.commit()

        print("\nRs", amount, "has been credited to account by", ptype)

        with open("balance.txt", "w") as balancefile:
            balancefile.write(str(account_balance))


def withdraw():
    global ptype
    global account_balance
    import random
    import time

    account_balance = 0
    with open("balance.txt", "r") as balancefile:
        lines = balancefile.readlines()
        for line in lines:
            if line.isdigit():
                account_balance = int(line)
                
    print("\n\t\t---Withdraw Incredibly!---")
    amount = int(input("\n\nEnter the amount to be withdrawn:"))
    print("\n1.Cash\n2.Cheque\n3.Demand Deposit")
    account_balance -= amount

    cho = int(input("\nEnter the type of transaction:"))
    if cho == 1:
        ptype = "CASH"
        qur = """insert into transaction_record(tid, tdate, ttype, description, amount, type, balance)
                values(%s,%s,%s,%s,%s,%s,%s)"""
        tid = random.randint(100000, 999999)
        tdate = time.strftime("%Y-%m-%d %H:%M:%S")
        ttype = "D"
        description = "DEBITED"
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur, value)
        mycon.commit()

        print("Rs", amount, "has been debited from account by", ptype)

        with open("balance.txt", "w") as balancefile:
            balancefile.write(str(account_balance))

    elif cho == 2:
        ptype = "CHEQUE"
        qur2 = """insert into transaction_record(tid, tdate, ttype, description, amount, type, balance)
        values(%s,%s,%s,%s,%s,%s,%s)"""
        tid = random.randint(100000, 999999)
        tdate = time.strftime("%Y-%m-%d %H:%M:%S")
        ttype = "D"
        description = "DEBITED"
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur2, value)
        mycon.commit()

        qur3 = """insert into cheque_record(tid, tdate, ttype, description, amount, type, balance)
                        values(%s,%s,%s,%s,%s,%s,%s)"""
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur3, value)
        mycon.commit()

        print("Rs", amount, "has been debited from account by", ptype)

        with open("balance.txt", "w") as balancefile:
            balancefile.write(str(account_balance))

    elif cho == 3:
        ptype = "DD"
        qur2 = """insert into transaction_record(tid, tdate, ttype, description, amount, type, balance)
                values(%s,%s,%s,%s,%s,%s,%s)"""
        tid = random.randint(100000, 999999)
        tdate = time.strftime("%Y-%m-%d %H:%M:%S")
        ttype = "D"
        description = "DEBITED"
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur2, value)
        mycon.commit()

        qur3 = """insert into dd_record(tid, tdate, ttype, description, amount, type, balance)
                                values(%s,%s,%s,%s,%s,%s,%s)"""
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur3, value)
        mycon.commit()

        print("Rs", amount, "has been debited from account by", ptype)

        with open("balance.txt", "w") as balancefile:
            balancefile.write(str(account_balance))


def loan_avail():
    global ptype
    global account_balance
    global loan_balance
    import random
    import time
    import smtplib
    from email.message import EmailMessage

    account_balance = 0
    loan_balance = 0
    with open("balance.txt","r") as balancefile:
        lines = balancefile.readlines()
        for line in lines:
            if line.isdigit():
                account_balance = int(line)

    with open("loan.txt","r") as loanfile:
        lines2 = loanfile.readlines()
        for line2 in lines2:
            if line2.isdigit():
                loan_balance = int(line2)

    print("\n\t\t---Guess what's new?!....We got you loans without interest!!...Thats..INCREDIBLE!!---")
    amount = int(input("\n\nEnter the amount to be taken as loan:"))
    if amount > loan_balance:
        print("Loan amount too high")
        print("Repay earlier loan amounts to proceed")
        exit()
    else:
        account_balance += amount
        loan_balance -= amount
        tid = random.randint(100000,999999)
        tdate = time.strftime("%Y-%m-%d %H:%M:%S")
        ttype = "C"
        description = "CREDITED"
        ptype = "LOAN"

        qur = """insert into transaction_record(tid, tdate, ttype, description, amount, type, balance)
                        values(%s,%s,%s,%s,%s,%s,%s)"""
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur,value)
        mycon.commit()

        with open("balance.txt", "w") as balancefile:
            balancefile.write(str(account_balance))

        qur2 = """insert into loan_record(tid, tdate, ttype, description, amount, type, balance)
                                values(%s,%s,%s,%s,%s,%s,%s)"""
        value = (tid, tdate, ttype, description, amount, ptype, account_balance)
        mycur.execute(qur2,value)
        mycon.commit()

        print("\nRs", amount, "has been credited to account by", ptype)

        with open("loan.txt", "w") as loanfile:
            loanfile.write(str(loan_balance))

    email_a = 'tabspublicrelations@gmail.com'
    email_p = 'iamincredible'

    msg = EmailMessage()
    msg['Subject'] = 'Loan Sanctioned - TABS'
    msg['From'] = email_address
    msg['To'] = 'kashwathaman@gmail.com'
    msg.set_content("""Greetings from The Accountables Banking System.
        
        Your loan was sanctioned and the amount was credited to your account.
        
        Keep banking with us - IncredibleCEO""")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_pass)

        smtp.send_message(msg)

    smtp.close()


def loan_repay():
    global ptype
    global account_balance
    global loan_balance
    import random
    import time
    import smtplib
    from email.message import EmailMessage

    account_balance = 0
    loan_balance = 0
    with open("balance.txt","r") as balancefile:
        lines = balancefile.readlines()
        for line in lines:
            if line.isdigit():
                account_balance = int(line)

    with open("loan.txt","r") as loanfile:
        lines2 = loanfile.readlines()
        for line2 in lines2:
            if line2.isdigit():
                loan_balance = int(line2)

    print("\n\t\t---We are happy to receive this from you....youre an Incredible customer...!---")
    amount = int(input("\n\nEnter the amount to be repayed towards loan:"))
    account_balance = account_balance - amount
    loan_balance += amount
    tid = random.randint(100000,999999)
    tdate = time.strftime("%Y-%m-%d %H:%M:%S")
    ttype = "D"
    description = "DEBITED"
    ptype = "LOAN"

    qur = """insert into transaction_record(tid, tdate, ttype, description, amount, type, balance)
                        values(%s,%s,%s,%s,%s,%s,%s)"""
    value = (tid, tdate, ttype, description, amount, ptype, account_balance)
    mycur.execute(qur,value)
    mycon.commit()

    with open("balance.txt", "w") as balancefile:
        balancefile.write(str(account_balance))

    qur2 = """insert into loan_record(tid, tdate, ttype, description, amount, type, balance)
                                values(%s,%s,%s,%s,%s,%s,%s)"""
    value = (tid, tdate, ttype, description, amount, ptype, account_balance)
    mycur.execute(qur2,value)

    print("\nRs", amount, "has been debited from account by", ptype)

    with open("balance.txt", "w") as balancefile:
        balancefile.write(str(account_balance))

    email_a = 'tabspublicrelations@gmail.com'
    email_p = 'iamincredible'

    msg = EmailMessage()
    msg['Subject'] = 'Loan repayment - TABS'
    msg['From'] = email_address
    msg['To'] = 'kashwathaman@gmail.com'
    msg.set_content("""Greetings from The Accountables Banking System.

            Your loan was paid towards recently and the amount was debited from your account.

            Keep banking with us - IncredibleCEO""")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_pass)

        smtp.send_message(msg)

    smtp.close()


def locker_avail():
    global ptype
    global account_balance
    import random
    import time
    import smtplib
    from email.message import EmailMessage

    account_balance = 0
    with open("balance.txt", "r") as balancefile:
        lines = balancefile.readlines()
        for line in lines:
            if line.isdigit():
                account_balance = int(line)

    print("\n\t\t---Guess what's Incredible about us?.....We can even keep Mr.Incredible out of our lockers!!!---")
    qur2 = """insert into locker_record(ano, date, name, weight, stcost)
                            values(%s,%s,%s,%s,%s)"""
    ano = random.randint(20, 100)
    tdate = time.strftime("%Y-%m-%d %H:%M:%S")
    name = input("\n\nEnter the name of article:")
    weight = float(input("Enter the weight of the article:"))
    stcost = float(weight * 25)

    value2 = (ano, tdate, name, weight, stcost)
    mycur.execute(qur2, value2)
    mycon.commit()

    tid = random.randint(100000, 999999)
    tdate = time.strftime("%Y-%m-%d %H:%M:%S")
    ttype = "D"
    description = "DEBITED"
    ptype = "LH"
    account_balance = account_balance - stcost

    qur = """insert into transaction_record(tid, tdate, ttype, description, amount, type, balance)
                                values(%s,%s,%s,%s,%s,%s,%s)"""
    value = (tid, tdate, ttype, description, stcost, ptype, account_balance)
    mycur.execute(qur, value)
    mycon.commit()

    print("\nRs", stcost, "has been debited from account by", ptype)
    print("\nYour article",name,"has been offered a locker!")

    with open('balance.txt', "w") as balancefile:
        balancefile.write(str(account_balance))

    email_a = 'tabspublicrelations@gmail.com'
    email_p = 'iamincredible'

    msg = EmailMessage()
    msg['Subject'] = 'Loan Sanctioned - TABS'
    msg['From'] = email_address
    msg['To'] = 'kashwathaman@gmail.com'
    msg.set_content("""Greetings from The Accountables Banking System.

            Your locker was allocted and the single-time amount was debited from your account.
            Your article is safe with us in our foolproof safe in undisclosed location.

            Keep banking with us - IncredibleCEO""")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_pass)

        smtp.send_message(msg)

    smtp.close()

def issue_cheque():
    global account_balance
    import time
    import random

    account_balance = 0
    with open("balance.txt","r") as balancefile:
        lines = balancefile.readlines()
        for line in lines:
            if line.isdigit():
                account_balance = int(line)
                
    print("\n\t\t---If you are banking with us then the cheques you issue is going to be Incredibly precious!---")
    amount = int(input("\n\nEnter the amount you wish to issue cheque for:"))
    tid = random.randint(100000,999999)
    tdate = time.strftime("%Y-%m-%d %H:%M:%S")
    ttype = "D"
    description = "DEBITED"
    type = "CHEQUE"
    account_balance -= amount

    qur = """insert into cheque_record(tid, tdate, ttype, description, amount, type, balance)
                            values(%s,%s,%s,%s,%s,%s,%s)"""
    value = (tid, tdate, ttype, description, amount, type, account_balance)
    mycur.execute(qur, value)
    mycon.commit()

    qur2 = """insert into transaction_record(tid, tdate, ttype, description, amount, type, balance)
                                        values(%s,%s,%s,%s,%s,%s,%s)"""
    value2 = (tid,tdate, ttype, description, amount, type, account_balance)
    mycur.execute(qur2,value2)
    mycon.commit()

    print("\nRs.",amount,"has been debited from account by",type)

    with open("balance.txt","w") as balancefile:
        balancefile.write(str(account_balance))


def issue_dd():
    global account_balance
    import time
    import random

    account_balance = 0
    with open("balance.txt","r") as balancefile:
        lines = balancefile.readlines()
        for line in lines:
            if line.isdigit():
                account_balance = int(line)

    print("\n\t\t---The guy who going to receive this DD is Incredibly lucky!---")
    amount = int(input("\n\nEnter the amount you wish to issue DD for:"))
    tid = random.randint(100000,999999)
    tdate = time.strftime("%Y-%m-%d %H:%M:%S")
    ttype = "D"
    description = "DEBITED"
    type = "DD"
    account_balance -= amount

    qur = """insert into dd_record(tid, tdate, ttype, description, amount, type, balance)
                            values(%s,%s,%s,%s,%s,%s,%s)"""
    value = (tid, tdate, ttype, description, amount, type, account_balance)
    mycur.execute(qur, value)
    mycon.commit()

    qur2 = """insert into transaction_record(tid, tdate, ttype, description, amount, type, balance)
                                        values(%s,%s,%s,%s,%s,%s,%s)"""
    value2 = (tid,tdate, ttype, description, amount, type, account_balance)
    mycur.execute(qur2,value2)
    mycon.commit()

    print("\nRs.",amount,"has been debited from account by",type)

    with open("balance.txt","w") as balancefile:
        balancefile.write(str(account_balance))


def view_cheque():
    qur = """select * from cheque_record"""
    mycur.execute(qur)
    rec = mycur.fetchall()
    if(rec == None):
        print("NO RECORD WAS FOUND IN THE DATABASE")
    else:
        print("TID\t\tDate\t\tType\t\tDescription\t\tAmount\t\tMode\t\tBalance")
        for row in rec:
            print(row)


def view_dd():
    qur = """select * from dd_record"""
    mycur.execute(qur)
    rec = mycur.fetchall()
    if(rec == None):
        print("NO RECORD WAS FOUND IN THE DATABASE")
    else:
        print("TID\t\tDate\t\tType\t\tDescription\t\tAmount\t\tMode\t\tBalance")
        for row in rec:
            print(row)


def view_transaction():
    qur = """select * from transaction_record"""
    mycur.execute(qur)
    rec = mycur.fetchall()
    if(rec == None):
        print("NO RECORD WAS FOUND IN THE DATABASE")
    else:
        print("TID\tDate\tType\tDescription\tAmount\t\tMode\tBalance")
        for row in rec:
            print(row)


def view_loan():
    qur = """select * from loan_record"""
    mycur.execute(qur)
    rec = mycur.fetchall()
    if(rec == None):
        print("NO RECORD WAS FOUND IN THE DATABASE")
    else:
        print("TID\t\tDate\t\tType\t\tDescription\t\tAmount\t\tMode\t\tBalance")
        for row in rec:
            print(row)


def view_locker():
    qur = """select * from locker_record"""
    mycur.execute(qur)
    rec = mycur.fetchall()
    if(rec == None):
        print("NO RECORD WAS FOUND IN THE DATABASE")
    else:
        print("ArticleNo\t\tDate\t\tName\t\tWeight\t\tSTCost")
        for row in rec:
            print(row)


def locker_retrieve():
    print("\n\t\t---Your item was Incredibly safe with us!! Hope you are Incredibly happy!!---")
    rno = int(input("\n\nEnter the article number to retrieve:"))
    qur = """select * from locker_record where ano=%s"""
    value = (rno,)
    mycur.execute(qur,value)
    rec = mycur.fetchall()
    if mycur.rowcount == 0:
        print("NO SUCH ARTICLE WAS FOUND")
    else:
        qur2 = """delete from locker_record where ano=%s"""
        value2 = (rno,)
        mycur.execute(qur2,value2)
        mycon.commit()
        print("The selected article was retrieved sucessfully")

    email_a = 'tabspublicrelations@gmail.com'
    email_p = 'iamincredible'

    msg = EmailMessage()
    msg['Subject'] = 'Loan Sanctioned - TABS'
    msg['From'] = email_address
    msg['To'] = 'kashwathaman@gmail.com'
    msg.set_content("""Greetings from The Accountables Banking System.

            Your locker was closed on account of your choice adn the article can be collected at out nearest branch.

            Keep banking with us - IncredibleCEO""")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_pass)

        smtp.send_message(msg)

    smtp.close()


def report():
    import smtplib
    import random
    import time

    email_address = "tabspublicrelations@gmail.com"
    email_pass = "iamincredible"

    rno = random.randint(100000,999999)
    rdate = time.strftime("%Y-%m-%d %H:%M:%S")
    tno = int(input("Enter the transaction id to proceed:"))
    description = input("Enter the issue:")
    status = "UNRESOLVED"

    qur = """insert into reports(rno, rdate, tno, description, status)
                        values(%s,%s,%s,%s,%s)"""
    value = (rno, rdate, tno, description, status)
    mycur.execute(qur,value)
    mycon.commit()

    msg = EmailMessage()
    msg['Subject'] = 'Report on fradulent transaction on ' + rdate
    msg['From'] = email_address
    msg['To'] = 'kashwathaman@gmail.com'
    msg.set_content("""Greetings from The Accountables Banking System.
    We have received the report filed by you on a fradulent transaction on """+rdate+""" and we are working to resolve your issue as soon as possile.
    Kindly be patient till the issue is resolved""")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_pass)

        smtp.send_message(msg)

    smtp.close()

    print("The issue was brought to the bank's notice...Our associates will reach out to you shortly.")

global account_balance
account_balance = 0

print("                                                  ---The Accountables Banking System---")
print("                                              'so easy to use even my grandmother can do it'")
email_address = "tabspublicrelations@gmail.com"
email_pass = "iamincredible"
user = input("Username:")
if user == "IncredibleCEO":
    password = input("Password:")
    if password == "iamincredible":

        print("\nWelcome Mr.Incredible CEO")
        while True:

            print("\n1.Transactions\n2.Cheques\n3.Demand Drafts\n4.Loans\n5.Lockers\n6.EXIT")
            choice = int(input("\nEnter your desired action:"))

            if choice == 1:

                with open("balance.txt", "r") as balancefile:
                    lines = balancefile.readlines()
                    for line in lines:
                        if line.isdigit():
                            account_balance = int(line)
                            print("Your current balance is",account_balance)

                print("\n1.Deposit money\n2.Withdraw money\n3.View transaction history\n4.Report Fradulent Transaction\n5.BACK")
                cho2 = int(input("\nEnter your choice:"))
                if cho2 == 1:
                    deposit()
                elif cho2 == 2:
                    withdraw()
                elif cho2 == 3:
                    view_transaction()
                elif cho2 == 4:
                    report()
                elif cho2 == 5:
                    print("Going back...")
                    break
                else:
                    print("Wrong Choice")
                    break

            elif choice == 2:

                with open("balance.txt", "r") as balancefile:
                    lines = balancefile.readlines()
                    for line in lines:
                        if line.isdigit():
                            account_balance = int(line)
                            print("Your current balance is",account_balance)

                print("\n1.Issue Cheque\n2.View cheque history\n3.Report Fradulent Transaction\n4.BACK")
                cho3 = int(input("\nEnter your desired choice:"))
                if cho3 == 1:
                    issue_cheque()
                elif cho3 == 2:
                    view_cheque()
                elif cho3 == 3:
                    report()
                elif cho3 == 4:
                    print("Going back...")
                    break
                else:
                    print("\nWrong Choice")
                    break

            elif choice == 3:

                with open("balance.txt", "r") as balancefile:
                    lines = balancefile.readlines()
                    for line in lines:
                        if line.isdigit():
                            account_balance = int(line)
                            print("Your current balance is",account_balance)

                print("\n1.Issue Demand Draft\n2.View DD history\n3.Report Fradulent Transaction\n4.BACK")
                cho3 = int(input("\nEnter your desired choice:"))
                if cho3 == 1:
                    issue_dd()
                elif cho3 == 2:
                    view_dd()
                elif cho3 == 3:
                    report()
                elif cho3 == 4:
                    print("\nGoing back...")
                    break
                else:
                    print("\nWrong Choice")
                    break

            elif choice == 4:

                with open("loan.txt","r") as loanfile:
                    lines = loanfile.readlines()
                    for line in lines:
                        if line.isdigit():
                            loan_balance = int(line)

                with open("balance.txt", "r") as balancefile:
                    lines = balancefile.readlines()
                    for line in lines:
                        if line.isdigit():
                            account_balance = int(line)
                            print("Your current balance is",account_balance)

                loan_taken = 1000000-loan_balance
                print("\nSanctionable loan amount:",loan_balance)
                print("Loan taken:",loan_taken)
                print("\n1.Take loan\n2.Repay loan\n3.View loan history\n4.Report Fradulent Transaction\n5.BACK")

                cho4 = int(input("\nEnter your choice:"))
                if cho4 == 1:
                    loan_avail()
                elif cho4 == 2:
                    loan_repay()
                elif cho4 == 3:
                    view_loan()
                elif cho4 == 4:
                    report()
                elif cho4 == 5:
                    print("\nGoing back...")
                    break
                else:
                    print("Wrong Choice")
                    break

            elif choice == 5:
                print("\n1.Avail new locker\n2.Retrieve\n3.View locker record\n4.Report Fradulent Transaction\n5.BACK")
                cho5 = int(input("\nEnter your choice:"))
                if cho5 == 1:
                    locker_avail()
                elif cho5 == 2:
                    locker_retrieve()
                elif cho5 == 3:
                    view_locker()
                elif cho5 == 4:
                    report()
                elif cho5 == 5:
                    print("Going back...")
                    break
                else:
                    print("Wrong choice")
                    break
            elif choice == 6:
                print("\t\t\tThanks for choosing The Accountables Banking System")
                print("      \t\t\t\tTOLD YOU IT IS SO EASY TO USE")
                break
        else:
            print("Wrong password")
    else:
        print("Wrong username")

print("Our CEO is Incredible...You are Incredible too...We all are Incredible")
print("Service Shutdown...")

mycon.close()
