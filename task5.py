names = []
c_n = []
n = int(input("Enter no.of contacts: "))
for i in range(n):
    name = input("Name: ")
    contact_number = int(input("Contact Number: ")) 
    names.append(name)
    c_n.append(contact_number)
print("\nName\t\t\tContact Number\n")
for i in range(n):
    print("{}\t\t\t{}".format(names[i], c_n[i]))
term = input("\nEnter search term: ")
print("Search result:")
if term in names:
    index = names.index(term)
    contact_number = c_n[index]
    print("Name: {}, Phone Number: {}".format(term, contact_number))
else:
    print("No records")
