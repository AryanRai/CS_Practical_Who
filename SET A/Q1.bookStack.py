def push(stack, item):
    stack.append(item)

def pop(stack):
     i = stack.pop()
     return i

def display(stack):
    print("[bookid, bookname]")
    for i in range(len(stack), 0, -1):
        print(stack[i-1])

def main():
    s = list()
    while True:
        print('''\nOPERATIONS:
            1) Push
            2) Pop
            3) Display
            e) Exit \n''')
        c = input("Enter choice (1,2,3,e) :")

        if c == '1':
            i = int(input("Book ID :"))
            n = str(input("Book Name :"))
            push(s, [i,n])
            print("pushed value successfully")

        elif c == '2':
            if len(s)>0:
                n = pop(s)
                print ("value", n, "popped")
        
            elif len(s)==0:
                print("Stack is empty")

        elif c =='3':
            display(s)

        elif c in 'eE':
            break

        else:
            print("wrong input:")
        

if __name__ == '__main__':
    main()
