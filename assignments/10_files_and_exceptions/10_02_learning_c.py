

with open("learning_python.txt") as file:
    lines = file.readlines()

for line in lines:
    print(line.replace("Python", "C").rstrip())
