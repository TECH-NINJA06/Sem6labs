data = input("Enter data string: ")
stuffed = data.replace('E', 'EE').replace('F', 'EF')
print(f"Framed Data: F{stuffed}F")