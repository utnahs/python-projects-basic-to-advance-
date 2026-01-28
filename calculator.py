add = lambda x,y:x+y
subtract = lambda x,y:x-y
divide = lambda x,y: x/y #if x>y else y/x
multiply = lambda x,y:x*y

operations = {'+':add,'-':subtract,'*':multiply,'/':divide}

def calc():
    
    to_continue = True
    first_num = float(input("Enter the first number:\n"))

    while to_continue:
        print("What operation you want to perform?")  

        for operation in operations:
            print(operation)

        operator = input("\n")
        second_num = float(input("Enter the second number:\n"))
        final_result = operations[operator](first_num,second_num)
        print(f"{first_num} {operator} {second_num} = {final_result}")
        to_cont = input(f"Do you want to continue with {final_result} \nType 'y' for yes or 'n' for no\n").lower()

        if to_cont != 'y':
            to_continue=False
            calc()
        else:
            first_num = final_result
            print("\n"*20)
calc()



