def read_menu():
    dictionary = {}

    with open('jillysCafe.txt', 'r', encoding='utf-8') as f:
        items = f.readlines()

        for x in items:
            # print(x)
            for y in range(len(x)):
                if x[y] =='\t':

                    key = str(x[:y])
                    key.strip('\t')
                    key.strip('\n')

                    value =  x[y:][1:]
                    test = value[:4]

                    dictionary.update(  { key : test }  )
    return dictionary


def order():
    orderItems = []
    orderPrices = []
    
    d = read_menu()

    for key , value in d.items():
        print(key , '---> ' , value)

    while True:
        option = input("Please enter a food item you would like to purchase: ")

        if option in d.keys(): #VALID RESPONSE
            print('\n Great Choice! Item added to order!\n')
            orderItems.append(option)
            orderPrices.append(d[option])

        else: #INVALID RESPONSE
            print('\nI am sorry, That order option was invalid. Please check spelling and try again\n')

        end = input("Please type 'stop' to finish order , Press enter to continue ordering:  ")
        if end.lower() == 'stop':
            break

    total = 0
    for i in orderPrices:
        total += float(i)

    print("Jilly's Cafe Receipt")
    for x in range(len(orderItems)):
        print(  str(orderItems[x]) , str(orderPrices[x])   )
    print('The total of your bill, without tax and tip, comes to: {}'.format(total)  )



order()