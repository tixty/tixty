#Importing modules
import time
import mysql.connector as mysql
print("PLEASE WAIT WHILE WE ESTABILISH CONNECTION")
time.sleep(1)
print("...ESTABILISHING CONNECTION FROM PYTHON TO MYSQL...")
time.sleep(1.5)
print("CONNECTING...")
time.sleep(01.5)
connect = mysql.connect(host = 'localhost', user = 'root', passwd = '6125', database = 'gym')
if connect.is_connected():
    print("CONNECTED TO THE SERVER")
    time.sleep(0.5)
cursor = connect.cursor()
#Information Input Command
def infoinput():
    memberno=int(input("Enter Membership Number: "))
    name=input("Enter Your Full Name: ")
    age=int(input("Enter Your Age: "))
    contact=input("Enter your phone Number (+966xxxxxxxxx): ")
    info="INSERT INTO member_info VALUES ({},'{}',{},'{}');".format(memberno,name,age,contact)
    cursor.execute(info)
    print("inserting values...")
    connect.commit()
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("values inserted successfully")
    exitop()
#Information Display Command
def infoshow():
    print("1. Show All Info")
    time.sleep(0.5)
    print("2. Show My Info")
    time.sleep(0.5)
    choiceshow=int(input("|ENTER CHOICE 1/2. |: "))
    time.sleep(0.25)
    if choiceshow==1:
        showall="SELECT * from member_info"
        cursor.execute(showall)
        data1=cursor.fetchall()
        print("(Membership NO. NAME  AGE CONTACT)")
        for row in data1:   
            print(row)
        exitop()
    elif choiceshow==2:
        memberinput=int(input("Enter Your Membership Number: "))
        showone="SELECT * from member_info WHERE memberno={}".format(memberinput)
        cursor.execute(showone)
        data2=cursor.fetchall()
        print("(Membership NO. NAME  AGE CONTACT)")
        for row in data2:
            print(row)
            time.sleep(1)
        exitop()
#Delete Member info with membership given
def infodelete():
    mem=int(input("Enter your membership number: "))
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("ARE YOU SURE YOU WANT TO DELETE THE DATA RELATED TO THE MEMBERSHIP NUMBER:",mem)
    time.sleep(0.5)
    print("1.YES (Delete)")
    time.sleep(0.5)
    print("2.NO (Cancel)")
    time.sleep(0.5)
    choice=int(input("Enter Your Choice 1/2: "))
    if choice==1:
        dele="DELETE FROM member_info WHERE memberno={}".format(mem)
        cursor.execute(dele)
        connect.commit()
        print("DATA DELETED :<")
        exitop()
    else:
        print("DATA DELETION CANCELLED :>")
        exitop()
#Leaderboard INPUT
def leaderinput():
    print("WARNING! YOU CAN ONLY ENTER YOUR DETAILS IF YOU HAVE A MEMBERSHIP ALREADY")
    time.sleep(1)
    print("Enter Leaderboard Details-> : ")
    time.sleep(1)
    memberno=int(input("Enter Your Membership Number: "))
    name=input("Enter Your full name: ")
    sq=int(input("Enter Your Squat PR(kgs): "))
    dl=int(input("Enter Your Deadlift PR(kgs): "))
    cu=int(input("Enter Your Current Weight: "))
    st=int(input("Enter Your Weight When You Started: "))
    leader="INSERT INTO member_leader VALUES ({},'{}',{},{},{},{});".format(memberno,name,sq,dl,cu,st)
    cursor.execute(leader)
    print("inserting values...")
    connect.commit()
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("values inserted successfully")
    exitop()
#Leadeboard Show
def leadershow():
    print("1. Show All Info")
    time.sleep(0.5)
    print("2. Show My Info")
    time.sleep(0.5)
    choiceshow=int(input("|ENTER CHOICE 1/2. |: "))
    time.sleep(0.25)
    if choiceshow==1:
        showall="SELECT * from member_leader"
        cursor.execute(showall)
        data1=cursor.fetchall()
        print("(Member NO.|NAME|Squat-PR|Dead-PR|Cur-Weight|Strt-Weight)")
        for row in data1:   
            print(row)
        exitop()
    elif choiceshow==2:
        memberinput=int(input("Enter Your Membership Number: "))
        showone="SELECT * from member_leader WHERE memberno={}".format(memberinput)
        cursor.execute(showone)
        data2=cursor.fetchall()
        print("(Member NO.|NAME|Squat-PR|Dead-PR|Cur-Weight|Strt-Weight)")
        for row in data2:
            print(row)
        exitop()
#squats New PR
def squpdate(mem):
    print("|SQUATS UPDATE|")
    newsq=int(input("Enter Your New Squat PR: "))
    upd="UPDATE member_leader SET SquatPR_KG={} where memberno={}".format(newsq,mem)
    cursor.execute(upd)
    print("updating values...")
    connect.commit()
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("values updated successfully")
    exitop()
#Deadlift new pr
def dlupdate(mem):
    print("|DEADLIFT UPDATE|")
    newdl=int(input("Enter Your New Deadlift PR: "))
    upd="UPDATE member_leader SET DL_PR_KG={} where memberno={}".format(newdl,mem)
    cursor.execute(upd)
    print("updating values...")
    connect.commit()
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("values updated successfully")
    exitop()
#PR update command
def prupdate():
    print("What PR do you want to update->")
    time.sleep(0.25)
    print("1. Squats")
    print("2. Deadlifts")
    print("3. Both")
    print("4.Exit Module")
    mem=int(input("Enter Your Membership Number: "))
    choicepr=int(input("Enter Your Choice 1/2/3/4: "))
    if choicepr==1:
        squpdate(mem)
    elif choicepr==2:
        dlupdate(mem)
    elif choicepr==3:
        squpdate(mem)
        dlupdate(mem)
    elif choicepr==4:
        exitop()
#Current Weight Update
def weupdate():
    mem=int(input("Enter Your Membership Number: "))
    neww=int(input("Enter Current Weight: "))
    upd="UPDATE member_leader SET currentweight_KG={} WHERE memberno={}".format(neww,mem)
    cursor.execute(upd)
    print("updating values...")
    connect.commit()
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("values updated successfully")
    exitop()
#leaderboard values delete
def leaderdelete():
    mem=int(input("Enter your membership number: "))
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("ARE YOU SURE YOU WANT TO DELETE THE DATA RELATED TO THE MEMBERSHIP NUMBER:",mem)
    time.sleep(0.5)
    print("1.YES (Delete)")
    time.sleep(0.5)
    print("2.NO (Cancel)")
    time.sleep(0.5)
    choice=int(input("Enter Your Choice 1/2: "))
    if choice==1:
        dele="DELETE FROM member_leader WHERE memberno={}".format(mem)
        cursor.execute(dele)
        connect.commit()
        print("DATA DELETED :<")
        exitop()
    else:
        print("DATA DELETION CANCELLED :>")
        exitop()
#exiting the module
def exitpage():
    print("Exiting the program")
    for i in range(20):
        print(".",end="")
        time.sleep(0.15)
    cursor.close()
    exit()
#Display page list
def displaypage():
    print("1.Show Member Information")
    print("2.Show Progress Information")
    print("3.Exit")
    ans=int(input("Enter your choice 1/2/3: "))
    if ans==1:
        print("Re-Directing...")
        time.sleep(1)
        infoshow()
    elif ans==2:
        print("Re-Directing...")
        time.sleep(1)
        showpage()
    else:
        exitop()
#main home page
def homepage():
    time.sleep(2)
    print("|WELCOME TO THE P TOWN GYM'S USER INTERFACE|")
    time.sleep(1)
    print("-----------------WE GO JIM-----------------")
    print("1.Display Data")
    time.sleep(0.5)
    print("2.Enter/Edit Data")
    time.sleep(0.5)
    print("3.Exit")
    page=int(input("Enter your choice 1/2/3: "))
    if page==1:
        print("Re-Directing to Display Page...")
        time.sleep(1)
        displaypage()
    elif page==2:
        print("Re-Directing to Edit Page...")
        time.sleep(1)
        editpage()
    elif page==3:
        exitpage()
#leaderboard order list
def showpage():
    print("1.Show Leaderboard (no order/single row)")
    time.sleep(0.5)
    print("2.Show Leaderboard (Sorted by name)")
    time.sleep(0.5)
    print("3.Show Leaderboard (sorted by squat PR)")
    time.sleep(0.5)
    print("4.Show leaderboard (sorted by DL PR)")
    time.sleep(0.5)
    print("5.Show Leaderboard (Sorted by Current Weight)")
    time.sleep(0.5)
    print("6.Show Leaderboard (Sorted by Starting Weight)")
    time.sleep(0.5)
    print("7.Exit")
    time.sleep(0.5)
    ans=int(input("Enter Your Choice 1/2/3/4/5/6/7: "))
    if ans==1:
        time.sleep(1)
        print("no order/single row")
        leadershow()
    elif ans==2:
        time.sleep(1)
        namesort()
    elif ans==3:
        time.sleep(1)
        sqsort()
    elif ans==4:
        time.sleep(1)
        dlsort()
    elif ans==5:
        time.sleep(1)
        cwsort()
    elif ans==6:
        time.sleep(1)
        swsort()
    elif ans==7:
        time.sleep(1)
        exitop()
#sort by name
def namesort():
    print("SORTED BY NAME:")
    sort="SELECT * from member_leader order by Name"
    cursor.execute(sort)
    data=cursor.fetchall()
    print("(Member NO.|NAME|Squat-PR|Dead-PR|Cur-Weight|Strt-Weight)")
    for row in data:
        print(row)
        time.sleep(0.5)
    exitop()
#sort by squat pr
def sqsort():
    print("SORTED BY Squat PR:")
    sort="SELECT * from member_leader order by SquatPR_KG"
    cursor.execute(sort)
    data=cursor.fetchall()
    print("(Member NO.|NAME|Squat-PR|Dead-PR|Cur-Weight|Strt-Weight)")
    for row in data:
        print(row)
        time.sleep(0.5)
    exitop()
#sort by deadlift squat
def dlsort():
    print("SORTED BY Deadlift PR:")
    sort="SELECT * from member_leader order by DL_PR_KG"
    cursor.execute(sort)
    data=cursor.fetchall()
    print("(Member NO.|NAME|Squat-PR|Dead-PR|Cur-Weight|Strt-Weight)")
    for row in data:
        print(row)
        time.sleep(0.5)
    exitop()
#sort by current weight
def cwsort():
    print("SORTED BY Current weight:")
    sort="SELECT * from member_leader order by currentweight_KG"
    cursor.execute(sort)
    data=cursor.fetchall()
    print("(Member NO.|NAME|Squat-PR|Dead-PR|Cur-Weight|Strt-Weight)")
    for row in data:
        print(row)
        time.sleep(0.5)
    exitop()
#sort by starting weight
def swsort():
    print("SORTED BY Starting weight:")
    sort="SELECT * from member_leader order by startweight_KG"
    cursor.execute(sort)
    data=cursor.fetchall()
    print("(Member NO.|NAME|Squat-PR|Dead-PR|Cur-Weight|Strt-Weight)")
    for row in data:
        print(row)
        time.sleep(0.5)
    exitop()
#homepage or exit
def exitop():
    time.sleep(1)
    print("----1.Back to homapage")
    time.sleep(1)
    print("----2.Exit the module")
    time.sleep(1)
    ans=int(input("Enter your choice 1/2 : "))
    if ans==1:
        homepage()
    else:
        exitpage()
def editpage():
    time.sleep(1)
    print("1.Input New Member Information")
    time.sleep(1)
    print("2.Input New Leaderboard Data")
    time.sleep(1)
    print("3.Update New PR In Leaderboard Table")
    time.sleep(1)
    print("4.Update Current Weight in Leaderboard Table")
    time.sleep(1)
    print("5.Delete member Information from the Information Table")
    time.sleep(1)
    print("6.Delete a Leaderboard Data from the Leaderboard Table")
    time.sleep(1)
    print("7.EXIT")
    page=int(input("Enter Your Choice 1/2/3/4/5/6/7: "))
    if page==1:
        infoinput()
    elif page==2:
        leaderinput()
    elif page==3:
        prupdate()
    elif page==4:
        weupdate()
    elif page==5:
        infodelete()
    elif page==6:
        leaderdelete()
    elif page==7:
        exitop()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------       MAIN PROGRAM       ------------------------------------------------------------------------------#
homepage()
