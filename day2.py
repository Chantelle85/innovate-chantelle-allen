
# def add_up(): 
#     num1 = input("What is the first number you'd like to add up? \n") 
#     num2 = input("What is the second number you'd like to add up? \n") 
#     try: 
#         print(f"{num1} + {num2} is {(int(num1) + int(num2))}!”) 
#     except: 
#         print("\n ERROR: please input only numerical values. \n") 
#         print("**************************** \n") 
#         add_up() 
# add_up()

light = False 
def light_switch():  
    global light
    if light: 
        print("Whoa! It's bright in here")  
        light = False 
    else: 
        print("Who turned out the lights?") 
        light = True 
light_switch() 
light_switch()


