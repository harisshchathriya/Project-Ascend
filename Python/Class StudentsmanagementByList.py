from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, boarding, name, age, gender, berth, mobile, travel_date, travel_class, amount, seat_no):
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

    def get_ticket_id(self):
        return self.__ticket_id

    def get_boarding(self):
        return self.__boarding

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_berth(self):
        return self.__berth

    def get_mobile(self):
        return self.__mobile

    def get_travel_date(self):
        return self.__travel_date

    def get_travel_class(self):
        return self.__travel_class

    def get_amount(self):
        return self.__amount

    def get_seat_no(self):
        return self.__seat_no

    def set_mobile(self, mobile):
        self.__mobile = mobile

    def set_travel_date(self, travel_date):
        self.__travel_date = travel_date

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
        print("Amount :", format(self.__amount, ".2f"))
        print("==============================")


class TrainReservation:
    def __init__(self):
        self.__tickets = []
        self.__ticket_no = 1001
        self.__total_bookings = 0
        self.__total_cancellations = 0
        self.__total_revenue = 0.0
        self.__seat_dict = {
            "Sleeper": ["SL-01", "SL-02", "SL-03", "SL-04", "SL-05", "SL-06", "SL-07", "SL-08", "SL-09", "SL-10"],
            "AC 3 Tier": ["3A-01", "3A-02", "3A-03", "3A-04", "3A-05", "3A-06", "3A-07", "3A-08"],
            "AC 2 Tier": ["2A-01", "2A-02", "2A-03", "2A-04", "2A-05", "2A-06"],
            "AC First Class": ["1A-01", "1A-02", "1A-03", "1A-04"],
            "First Class": ["FC-01", "FC-02", "FC-03", "FC-04"]
        }

    def _find_ticket_index(self, ticket_id):
        for index, ticket in enumerate(self.__tickets):
            if ticket.get_ticket_id() == ticket_id:
                return index
        return -1

    def _read_non_empty_alpha_text(self, prompt):
        while True:
            value = input(prompt).strip()
            if value and all(ch.isalpha() or ch.isspace() for ch in value):
                return value
            print("Invalid input. Use alphabets only.")

    def _read_age(self):
        while True:
            value = input("Age: ").strip()
            if value.isdigit():
                age = int(value)
                if 1 <= age <= 120:
                    return age
            print("Invalid Age. Enter a value between 1 and 120.")

    def _read_mobile(self, prompt="Mobile Number: "):
        while True:
            mobile = input(prompt).strip()
            if len(mobile) == 10 and mobile.isdigit():
                return mobile
            print("Invalid Mobile Number. Enter exactly 10 digits.")

    def _read_travel_date(self, prompt="Date of Travel (DD-MM-YYYY): "):
        while True:
            travel_date = input(prompt).strip()
            try:
                datetime.strptime(travel_date, "%d-%m-%Y")
                return travel_date
            except ValueError:
                print("Invalid Date. Use DD-MM-YYYY format with a valid calendar date.")

    def _read_menu_choice(self, prompt, minimum, maximum):
        while True:
            value = input(prompt).strip()
            if value.isdigit():
                choice = int(value)
                if minimum <= choice <= maximum:
                    return choice
            print("Invalid choice. Try again.")

    def _get_gender(self):
        print("\nGender")
        print("1. Male")
        print("2. Female")
        print("3. Other")
        choice = self._read_menu_choice("Choose: ", 1, 3)
        if choice == 1:
            return "Male"
        if choice == 2:
            return "Female"
        return "Other"

    def _get_travel_class(self):
        print("\nClass of Travel")
        print("1. Sleeper")
        print("2. AC 3 Tier")
        print("3. AC 2 Tier")
        print("4. AC First Class")
        print("5. First Class")
        choice = self._read_menu_choice("Choose: ", 1, 5)
        if choice == 1:
            return "Sleeper", 150
        if choice == 2:
            return "AC 3 Tier", 450
        if choice == 3:
            return "AC 2 Tier", 600
        if choice == 4:
            return "AC First Class", 1000
        return "First Class", 800
    
    def _get_berth(self):
        print("\nBerth Preference")
        print("1. Lower")
        print("2. Middle")
        print("3. Upper")
        choice = self._read_menu_choice("Choose: ", 1, 3)
        if choice == 1:
            return "Lower"
        if choice == 2:
            return "Middle"
        return "Upper"

    def _calculate_amount(self, base_fare, age):
        if age < 5:
            return 0.0
        if 5 <= age <= 12:
            return base_fare * 0.75
        if age >= 60:
            return base_fare * 0.5
        return float(base_fare)

    def _book_seat(self, travel_class):
        if not self.__seat_dict[travel_class]:
            return None
        return self.__seat_dict[travel_class].pop(0)

    def _return_seat(self, travel_class, seat_no):
        self.__seat_dict[travel_class].append(seat_no)
        self.__seat_dict[travel_class].sort()

    def _print_ticket_list(self):
        if not self.__tickets:
            print("No Tickets Booked")
            return
        for ticket in self.__tickets:
            ticket.display()

    def book_ticket(self):
        print("\n--- BOOK TICKET ---")
        boarding = self._read_non_empty_alpha_text("Boarding Point: ")
        name = self._read_non_empty_alpha_text("Name: ")
        age = self._read_age()
        gender = self._get_gender()
        mobile = self._read_mobile()
        travel_date = self._read_travel_date()
        travel_class, base_fare = self._get_travel_class()

        if not self.__seat_dict[travel_class]:
            print("No Seats Available in selected class.")
            return

        berth = self._get_berth()
        seat_no = self._book_seat(travel_class)
        if seat_no is None:
            print("No Seats Available in selected class.")
            return

        amount = self._calculate_amount(base_fare, age)
        ticket_id = "T" + str(self.__ticket_no)
        ticket = Ticket(ticket_id, boarding, name, age, gender, berth, mobile, travel_date, travel_class, amount, seat_no)
        self.__tickets.append(ticket)
        self.__ticket_no += 1
        self.__total_bookings += 1
        self.__total_revenue += amount

        print("\nTicket Booked Successfully")
        ticket.display()

    def cancel_ticket(self):
        print("\n--- CANCEL TICKET ---")
        ticket_id = input("Enter Ticket ID to Cancel: ").strip()
        index = self._find_ticket_index(ticket_id)
        if index == -1:
            print("Ticket Not Found")
            return

        ticket = self.__tickets.pop(index)
        self._return_seat(ticket.get_travel_class(), ticket.get_seat_no())
        self.__total_cancellations += 1
        self.__total_revenue -= ticket.get_amount()
        if self.__total_revenue < 0:
            self.__total_revenue = 0.0
        print("Ticket Cancelled Successfully")

    def view_tickets(self):
        print("\n--- VIEW TICKETS ---")
        self._print_ticket_list()

    def search_ticket(self):
        print("\n--- SEARCH TICKET ---")
        ticket_id = input("Enter Ticket ID: ").strip()
        index = self._find_ticket_index(ticket_id)
        if index == -1:
            print("Ticket Not Found")
            return
        self.__tickets[index].display()


    def menu(self):
        while True:
            print("\n===== TRAIN TICKET RESERVATION SYSTEM =====")
            print("1. Book Ticket")
            print("2. Cancel Ticket")
            print("3. View Tickets")
            print("4. Search Ticket")
            print("5. Exit")
            choice = self._read_menu_choice("Enter Choice: ", 1, 5)

            if choice == 1:
                self.book_ticket()
            elif choice == 2:
                self.cancel_ticket()
            elif choice == 3: 
                self.view_tickets()  
            elif choice == 4:
                self.search_ticket()
            else:
                print("Thank You")
                break


obj = TrainReservation()
obj.menu()
