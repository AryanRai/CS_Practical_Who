import pickle
def add_record():
    f=open("emp.dat", "wb")
    emp={}
    name=input("Enter Employee Name:")
    i_d = int(input("Enter Employee Code"))
    emp["Name"]= name
    emp["ID"] = i_d
    pickle.dump(emp,f)
    f.close()

def display_record():
    f=open("emp.dat", "rb")
    emp=pickle.load(f)
    print(emp)
    f.close()

def search():
    f=open("emp.dat", "rb")
    emp=pickle.load(f)
    i_d = int(input("Enter Employee id:"))
    if emp["ID"]== i_d:
        print(emp["Name"],emp["ID"])
    else:
        print("Invalid ID")
    f.close()

while True:
    print("1. Add Record")
    print("2. Display Record")
    print("3. Search Record")
    print("4. Exit")

    ch=int(input("Enter choice:"))
    if ch == 1:
        add_record()

    elif ch == 2:
        display_record()

    elif ch == 3:
        search()

    elif ch == 4:
        break
    else:
        print("Invalid choice")
