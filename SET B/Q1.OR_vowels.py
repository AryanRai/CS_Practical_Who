print("Enter the name of file with extention: ")
fileName = str(input())
f = open(fileName, "r")
print("The contents of the file are: \n" , f.read())
f.seek(0)

try:
        n = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for char in f.read():
            if char in vowels:
                n = n+1
        f.close()

except Exception:
    print("File not found")

print("\nTotal Vowels are:")
print(n)
