string = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven"

words = string.split(" ")

dict = {"Zero" : 0, "One" : 1, "Two" : 2, "Three" : 3, "Four" : 4, 
        "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8,
        "Nine" : 9, "Dash" :"-"}

# 1st solution

for w in words:
    if w in dict:
        print(dict[w], end="")
    else:
        print(w[0], end="")

# 2nd solution
print()
for w in words:
    print(dict.get(w, w[0]), end='')

