
import csv

apartments = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('jurmala.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartments.append(row)

# remove header row
apartments.pop(0)

# print(apartments)
print("apartments list command:")
jurmala=apartments.copy()
def sort_price(jurmala):
    return int(jurmala[8])
while True:
    print("1. Get apartments by sequence number")
    print("2. Top 10 by highest price")
    print("3. Top 10 by lowest price")
    print("4. 20 items, cheaper than price")
    print("5. 20 items, expensive than price")
    print("6. -- Filter of your choice --")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        a=int(input("Please write apartaments sequence number: "))
        print(jurmala[a-1])
        # https://www.w3schools.com/python/python_lists_access.asp
        pass
    elif choice == '2':
        jurmala.sort(key = sort_price, reverse = True)
        print(jurmala[0:10])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        jurmala.sort(key = sort_price)
        print(jurmala[0:10])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        a=int(input("Please enter your highest price: "))
        newlist = []
        jurmala.sort(key = sort_price)
        newlist=[x for x in jurmala if a>int(x[8])]
        print(newlist[0:20])
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        pass
    elif choice == '5':
        a=int(input("Please enter your lowest price: "))
        newlist = []
        jurmala.sort(key = sort_price)
        newlist=[x for x in jurmala if a<int(x[8])]
        print(newlist[0:20])
        

        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        pass

    elif choice == '6':
        print("some words of motivation.....buy, rent, get rich")
        pass
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 7")

    print("==========================")


