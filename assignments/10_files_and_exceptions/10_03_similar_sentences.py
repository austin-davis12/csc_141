

filename = "python_sentences.txt"

sentences = [
    "I love learning Python.",
    "Python is great for beginners.",
    "Python makes programming fun."
]

with open(filename, "w") as file:
    for line in sentences:
        file.write(line + "\n")

with open(filename) as file:
    print(file.read())
