a="123 is a number with 3 digits and 4567 with 4 digits"
list=[int(y) for y in a.split() if y.isdigit()]
print(list)