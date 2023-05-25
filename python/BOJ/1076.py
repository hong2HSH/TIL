color = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]
a = input()
b = input()
c = input()

a = color.index(a)
b = color.index(b)
c = color.index(c)

print((a * 10 + b) * 10**c)
