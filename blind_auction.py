def database():    
    more_bidders = True
    data={}
    while more_bidders:
        print('\n'*100)
        name = input("What is your name?\n")
        bid = int(input("How much you want to bid?\n"))
        data[name]=bid
        are_more_bidders = input("Are there any more bidders Type 'y' for yes and 'n' for no \n").lower()
        if are_more_bidders!='y':
            more_bidders = False
    return data

def max():
    max = 0
    bidders_data=database()
    for name in bidders_data:
        if bidders_data[name]>max:
            max = bidders_data[name]
    return max,bidders_data

def winner():
    max_value,dict_=max()
    for key,value in dict_.items():
        if max_value==value:
            print(f'The winner is {key}')


winner()
    
