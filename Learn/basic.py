# String
def String():
    first_name = "Sastra"
    last_name = "Nur"

    print(f"Hello {first_name} {last_name}")

    # Slicing and edit with func
    input_string = "I love programming with python!"
    print(input_string.split()[1].upper())


#### LIST
def listBasic():
    myvar = "NEW"
    mylist = [100, 200, 300, 400, 500]
    print(mylist[0])
    print(mylist[0:4])
    # add
    mylist.insert(0, myvar)
    print(mylist)
    # remove
    item_removed = mylist.pop()
    print(item_removed)

    # TASK: Sort the list and print the first three elements of the sorted list 
    unsorted_list = [123, 5, 4, 14215, 2, 6, 12467, 1, 923, 991, 42]
    unsorted_list.sort()
    print(unsorted_list[0:3])



####
def dictionaries():
    employees = {"chef":"Amy",
                "ceo":"Jason"}
    print(employees["ceo"])
    
    # Add to dict
    employees["waiter"] = "Mike"
    print(employees)
    
    # updatew
    employees["ceo"] = "Lala"
    print(employees)



# TASK: Print whether my_string1 and my_string2 start with A and end with a
def boolean():
    my_string1 = "Alpha"
    my_string2 = "Anaconda"
    print(my_string1[0] == "A" and my_string1[-1] == "a" and my_string2[0] == "A" and my_string2[-1] == "a")

# IF ELSE
def ifelse():
    a = 23
    b = 8
    aandb = a + b
    
    if aandb == 42:
        print(42)
    elif aandb >= 30 and aandb <= 41:
        print(aandb)
    else:
        print("False")

# LOOP
def tryloop():
    sales = [1, 2, 3, 4]
    
    for num in sales:
        print(f"List: {num}")
    
    my_list1 = [1, 2, 3, 4, 5, 10]
    my_list2 = []

    for num in my_list1:
        my_list2.append(num+42)
        print(my_list2)

    print(my_list2)

tryloop()