import random

class Ticket:
    def __init__(self, ticket_id, boarding, name, age, gender,
                 berth, mobile, travel_date, travel_class,
                 amount, seat_no):

        self.__ticket_id = ticket_id
        self.__boarding = boarding
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__berth = berth
        self.__mobile = mobile
        self.__travel_date = travel_date
        self.__travel_class = travel_class
        self.__amount = amount
        self.__seat_no = seat_no

    def display(self):
        print("\n==============================")
        print("Ticket ID :", self.__ticket_id)
        print("Boarding Point :", self.__boarding)
        print("Name :", self.__name)
        print("Age :", self.__age)
        print("Gender :", self.__gender)
        print("Berth Preference :", self.__berth)
        print("Seat Number :", self.__seat_no)
        print("Mobile :", self.__mobile)
        print("Date of Travel :", self.__travel_date)
        print("Class :", self.__travel_class)
        print("Amount : ₹", self.__amount)
        print("==============================")


tickets = []
ticket_no = 1001
total_bookings = 0
total_cancellations = 0
total_revenue = 0

seats = {
    "Sleeper": ["S1-01", "S1-02", "S1-03", "S1-04", "S1-05"],
    "AC 3 Tier": ["B1-01", "B1-02", "B1-03", "B1-04", "B1-05"],
    "AC 2 Tier": ["A1-01", "A1-02", "A1-03"],
    "AC First Class": ["H1-01", "H1-02"],
    "First Class": ["F1-01", "F1-02"]
}

while True:

    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. View Tickets")
    print("4. Search Ticket")
    print("5. Update Ticket")
    print("6. Statistics")
    print("7. Available Seats")
    print("8. Exit")

    choice = int(input("Enter Choice: "))
    if choice == 1:
        print("\n--- BOOK TICKET ---")
        boarding = input("Boarding Point: ")
        if boarding == "":
            print("Boarding Point cannot be empty")
            continue
        name = input("Name: ")
        if not name.replace(" ", "").isalpha():
            print("Invalid Name")
            continue
        age = int(input("Age: "))
        if age < 1 or age > 120:
            print("Invalid Age")
            continue
        print("\nGender")
        print("1. Male")
        print("2. Female")
        print("3. Other")
        g = int(input("Choose: "))
        if g < 1 or g > 3:
            print("Invalid Gender Choice")
            continue
        if g == 1:
            gender = "Male"
        elif g == 2:
            gender = "Female"
        else:
            gender = "Other"

        mobile = input("Mobile Number: ")
        if len(mobile) != 10 or not mobile.isdigit():
            print("Invalid Mobile Number")
            continue

        travel_date = input("Date of Travel (DD-MM-YYYY): ")
        if len(travel_date) != 10 or travel_date[2] != '-' or travel_date[5] != '-':
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
        if len(seats[travel_class])==0:
            print("No Seats Available")
            continue
        seat_no=seats[travel_class].pop(0)

        print("\nBerth Preference")
        print("1. Lower")
        print("2. Middle")
        print("3. Upper")
        b=int(input("Choose: "))
        if b<1 or b>3:
            print("Invalid Berth Choice")
            seats[travel_class].insert(0, seat_no)
            continue
        if b==1:
            berth="Lower"
        elif b==2:
            berth="Middle"
        else:
            berth="Upper"
        
        if age<5:
            amount=0
        elif age>=60:
            amount=amount * 0.5
        elif age>=5 and age<=12:
            amount=amount * 0.75

        ticket=Ticket(
            "T" + str(ticket_no),
            boarding,
            name,
            age,
            gender,
            berth,
            mobile,
            travel_date,
            travel_class,
            amount,
            seat_no
        )
        tickets.append(ticket)
        total_bookings += 1
        total_revenue += amount

        print("\nTicket Booked Successfully")
        print("Ticket ID :", "T" + str(ticket_no))
        print("Seat Number :", seat_no)
        print("Amount : ₹", amount)
        ticket_no+=1

    elif choice==2:
        tid = input("Enter Ticket ID to Cancel: ")
        found = False
        for ticket in tickets:
            if ticket.__ticket_id==tid:
                seats[ticket.__travel_class].append(ticket.__seat_no)
                tickets.remove(ticket)
                total_cancellations += 1
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
                ticket.display()

    elif choice==4:
        tid=input("Enter Ticket ID: ")
        found=False
        for ticket in tickets:
            if ticket.__ticket_id==tid:
                ticket.display()
                found=True
                break
        if not found:
            print("Ticket Not Found")

    elif choice==5:
        tid=input("Enter Ticket ID: ")
        found=False
        for ticket in tickets:
            if ticket.__ticket_id==tid:
                found=True
                print("\n1. Update Mobile")
                print("2. Update Travel Date")
                ch=int(input("Choose: "))
                if ch==1:
                    new_mobile = input("New Mobile Number: ")
                    if len(new_mobile)==10 and new_mobile.isdigit():
                        ticket.__mobile=new_mobile
                        print("Mobile Updated Successfully")
                    else:
                        print("Invalid Mobile Number")
                elif ch==2:
                    new_date = input("New Travel Date (DD-MM-YYYY): ")
                    if len(new_date)==10 and new_date[2]=='-' and new_date[5]=='-':
                        ticket.__travel_date = new_date
                        print("Travel Date Updated Successfully")
                    else:
                        print("Invalid Date Format")
                else:
                    print("Invalid Choice")
                break
        if not found:
            print("Ticket Not Found")

    elif choice == 6:
        print("\n===== STATISTICS =====")
        print("Total Bookings :", total_bookings)
        print("Total Cancellations :", total_cancellations)
        print("Total Revenue : ₹", total_revenue)

    elif choice == 7:
        print("\n===== AVAILABLE SEATS =====")
        for cls in seats:
            print(cls, ":", len(seats[cls]), "Seats Available")

    elif choice==8:
        print("Thank You")
        break
    else:
        print("Invalid Choice")