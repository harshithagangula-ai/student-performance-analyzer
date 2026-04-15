import csv

def add_record():
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        
        name = input("Enter name: ")
        age = input("Enter age: ")
        marks = input("Enter marks: ")
        
        writer.writerow([name, age, marks])
        print("Record added!")

def display_records():
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No records found!")

def average_marks():
    total = 0
    count = 0
    
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += int(row[2])
                count += 1
        
        if count > 0:
            print("Average Marks:", total / count)
        else:
            print("No data!")
    except:
        print("Error reading file!")

while True:
    print("\n1.Add Record\n2.Display\n3.Average\n4.Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_record()
    elif choice == '2':
        display_records()
    elif choice == '3':
        average_marks()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")