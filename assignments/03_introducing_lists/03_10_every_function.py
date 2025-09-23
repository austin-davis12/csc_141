things = ['Bicycle', 'Car', 'Motorcycle', 'Unicycle']
things[3] = 'Scooter'
things.append('Unicycle')
things.insert(0, 'Hoverboard')
del things[0]
print(things.pop())
things.sort(reverse=True)
len(things)
print(things)