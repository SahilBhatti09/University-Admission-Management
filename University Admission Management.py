# University Admission Management

FILENAME = 'admission.txt'


def add_admission(name, cnic, father_name, age, address, academic_history):
    with open(FILENAME, 'a') as file:
        file.write(f'Name: {name}\n')
        file.write(f'CNIC: {cnic}\n')
        file.write(f'Father Name: {father_name}\n')
        file.write(f'Age: {age}\n')
        file.write(f'Address: {address}\n')
        file.write(f'Academic History: {academic_history}\n')
        file.write('---\n')  # record separator
    print("Admission data added successfully!\n")


def list_admissions():
    try:
        with open(FILENAME, 'r') as file:
            admissions = file.read().strip().split('---\n')
            if not admissions or admissions == ['']:
                print("No admissions found.\n")
                return
            print("\nList of all admissions:\n")
            for index, admission in enumerate(admissions, 1):
                print(f"Student #{index}")
                print(admission.strip())
                print("-" * 40)
    except FileNotFoundError:
        print("No admission records found.\n")


def search_admission(keyword):
    try:
        with open(FILENAME, 'r') as file:
            admissions = file.read().strip().split('---\n')
            found = False
            for admission in admissions:
                if keyword.lower() in admission.lower():
                    print("\nStudent Record Found:")
                    print(admission.strip())
                    print("-" * 40)
                    found = True
            if not found:
                print("No admission data found for the given keyword.\n")
    except FileNotFoundError:
        print("No admission records found.\n")


def university_admission():
    while True:
        print("\nWelcome to Forman Christian College")
        print("(A Chartered University)")
        print("1. Add new admission")
        print("2. List all new admissions")
        print("3. Search a student")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter your name: ").strip()
            cnic = input("Enter your CNIC: ").strip()
            father_name = input("Enter your father's name: ").strip()
            age = input("Enter your age: ").strip()
            address = input("Enter your address: ").strip()
            academic_history = input("Enter your previous degree: ").strip()

            if not name or not cnic:
                print("Name and CNIC are required fields.\n")
                continue

            add_admission(name, cnic, father_name, age, address, academic_history)

        elif choice == '2':
            list_admissions()

        elif choice == '3':
            search_by = input("Search by Name or CNIC? (N/C): ").strip().upper()
            if search_by == 'N':
                keyword = input("Enter the name of the student: ").strip()
            elif search_by == 'C':
                keyword = input("Enter the CNIC of the student: ").strip()
            else:
                print("Invalid input. Try again.\n")
                continue
            search_admission(keyword)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid input. Try again.\n")


# Run the program
university_admission()
