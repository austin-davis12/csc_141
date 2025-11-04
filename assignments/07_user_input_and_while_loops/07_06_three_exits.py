pizza = "\nGive me a topping you want on your pizza. "
pizza += "\nEnter 'quit' when you are done ordering. "

active = True
while active:
    topping = input(pizza)

    if topping == 'quit':
        break
    else: 
        print(topping)