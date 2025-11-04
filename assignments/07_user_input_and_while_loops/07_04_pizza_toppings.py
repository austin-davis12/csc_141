pizza = "\nGive me a topping you want on your pizza. "
pizza += "\nEnter 'quit' when you are done ordering. "

topping = ''
while topping != 'quit':
    topping = input(pizza)
    
    if topping != 'quit':
        print(topping)
    