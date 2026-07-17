tickets=[]
ticket_no=1001
while True:
    print("\n===== TRAIN TICKET RESERVATION =====")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. View Tickets")
    print("4. Exit")
    choice=int(input("Enter Choice: "))
    if choice==1:
        print("\n--- BOOK TICKET ---")
        boarding=input("Boarding Point: ")
        if boarding =="":
            print("Boarding Point cannot be empty")
            continue
        name=input("Name: ")
        if not name.replace(" ","").isalpha():
            print("Invalid Name")
            continue
        age=int(input("Age: "))
        if age<1 or age>120:
            print("Invalid Age")
            continue
        if age<5:
            amount=0
        elif age>=60:
            amount=amount*0.5
        elif age>=5 and age<=12:
            amount=amount*0.75
        else:
            amount=amount*1.0
        print("\nGender")
        print("1. Male")
        print("2. Female")
        print("3. Other")
        g=int(input("Choose: "))
        if g<1 or g>3:
            print("Invalid Gender Choice")
            continue
        if g==1:
            gender="Male"
        elif g==2:
            gender="Female"
        else:
            gender="Other"
        print("\nBerth Preference")
        print("1. Lower")
        print("2. Middle")
        print("3. Upper")
        b=int(input("Choose: "))
        if b<1 or b>3:
            print("Invalid Berth Choice")
            continue
        if b==1:
            berth="Lower"
            amount=amount*1.8
        elif b==2:
            berth="Middle"
            amount=amount*1.5
        else:
            berth="Upper"
            amount=amount*1.3
        mobile=input("Mobile Number: ")
        if len(mobile)!=10 or not mobile.isdigit():
            print("Invalid Mobile Number")
            continue
        travel_date=input("Date of Travel (DD-MM-YYYY): ")
        if len(travel_date)!=10 or travel_date[2]!='-' or travel_date[5]!='-':
            print("Invalid Date Format")
            continue
        print("\nClass of Travel")
        print("1. Sleeper")
        print("2. AC 3 Tier (3A)")
        print("3. AC 2 Tier (2A)")
        print("4. AC First Class (1A)")
        print("5. First Class (FC)")
        c=int(input("Choose: "))
        if c<1 or c>5:  
            print("Invalid Class Choice")
            continue
        if c==1:
            travel_class="Sleeper"
            amount=150
        elif c==2:
            travel_class="AC 3 Tier"
            amount=450
        elif c==3:
            travel_class="AC 2 Tier"
            amount=600
        elif c==4:
            travel_class="AC First Class"
            amount=1000
        else:
            travel_class="First Class"
            amount=800
        ticket = {
            "Ticket ID": "T" + str(ticket_no),
            "Boarding Point": boarding,
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Berth Preference": berth,
            "Mobile": mobile,
            "Date of Travel": travel_date,
            "Class": travel_class,
            "Amount": amount
        }
        tickets.append(ticket)
        print("\nTicket Booked Successfully")
        print("Ticket ID:", "T" + str(ticket_no))
        ticket_no+=1
    elif choice==2:
        tid=input("Enter Ticket ID to Cancel: ")
        found=False
        for ticket in tickets:
            if ticket["Ticket ID"]==tid:
                tickets.remove(ticket)
                found=True
                print("Ticket Cancelled Successfully")
                break
        if not found:
            print("Ticket Not Found")
    elif choice==3:
        if len(tickets)==0:
            print("No Tickets Booked")
        else:
            for ticket in tickets:
                print("\n==============================")
                for key, value in ticket.items():
                    print(key, ":", value)
                print("==============================")
    elif choice==4:
        print("Thank You")
        break
    else:
        print("Invalid Choice")