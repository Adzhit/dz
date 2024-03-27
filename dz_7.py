         #1
list_1 = [12, 3, 4, 10]

if len(list_1) > 0:
    popped_list_1 = list_1.pop(3)
    last_to_first_1 = popped_list_1
    list_1.insert(0, last_to_first_1)

    print(list_1)
         #2
list_2 = [1]

if len(list_2) > 0:
    popped_list_2 = list_2.pop(0)
    last_to_first_2 = popped_list_2
    list_2.insert(0, last_to_first_2)

    print(list_2)
        #3
list_3 = []

if len(list_3) > 0:
    popped_list_3 = list_3.pop()
    last_to_first_3 = popped_list_3
    list_3.insert(0, last_to_first_3)

    print(list_3)
        # 4

list_4 = [12, 3, 4, 10, 8]

if len(list_4) > 0:
    popped_list_4 = list_4.pop(4)
    last_to_first_4 = popped_list_4
    list_4.insert(0, last_to_first_4)

    print(list_4)

