
def add(a,b):
    print(str(a) + ' + ' + str(b) + ' = ' + str(a+b))

def multiply (a,b):
    print(str(a) + ' * ' + str(b) + ' = ' + str(a*b))

def divide(a,b):
    print(str(a) + ' / ' + str(b) + ' = ' + str(a/b))

def deduct(a,b):
    print(str(a) + ' - ' + str(b) + ' = ' + str(a-b))

while True: 
    text = ''' what do u want to do?
    + = add
    - = deduct 
    * = multiply 
    / = divide
    . = exit
    '''
    choice = input(text)

    if choice in ["+" , "-" , "*" , "/"]: 
        a = int(input('tell me 1st number: '))
        b = int(input('tell me 2cnd number: '))
    
        if choice == "+":
            add(a,b)
        elif choice == "*":
            multiply(a,b) 
        elif choice == "/":
            divide(a,b)
        elif choice == "-":
            deduct(a,b) 
    elif choice == ".":
            print('Exit')
            quit() 
    else: 
        print('Error: Enter right charactor')

        
