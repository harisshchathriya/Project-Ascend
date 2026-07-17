class Student:
    def __init__(self):
        self.students = []

    def add_student(self):
        sid = input("Student ID: ")

        for s in self.students:
            if s["id"] == sid:
                print("Duplicate ID")
                return
            
        name = input("Name: ")
        dept = input("Department: ")
        year = input("Year: ")
        phone = input("Phone: ")
        while len(phone) != 10:
            phone = input("Enter 10-digit Phone: ")

        email = input("Email: ")

        marks = []
        for i in range(5):
            m = int(input(f"Mark {i+1}: "))
            while m < 0 or m > 100:
                m = int(input("Enter mark (0-100): "))
            marks.append(m)

        total = sum(marks)
        avg = total / len(marks)

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "F"

        self.students.append({
            "id": sid,
            "name": name,
            "dept": dept,
            "year": year,
            "phone": phone,
            "email": email,
            "marks": marks,
            "total": total,
            "avg": avg,
            "grade": grade
        })

    def view_students(self):
        for s in self.students:
            print(s)

    def search_id(self):
        sid = input("Enter ID: ")
        for s in self.students:
            if s["id"] == sid:
                print(s)
                return
        print("Not Found")

    def delete_student(self):
        sid = input("Enter ID: ")
        for s in self.students:
            if s["id"] == sid:
                self.students.remove(s)
                print("Deleted")
                return
        print("Not Found")


obj = Student()

while True:
    print("\n1.Add")
    print("2.View")
    print("3.Search By ID")
    print("4.Delete")
    print("5.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        obj.add_student()
    elif ch == 2:
        obj.view_students()
    elif ch == 3:
        obj.search_id()
    elif ch == 4:
        obj.delete_student()
    elif ch == 5:
        break