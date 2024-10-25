age = int(input("Enter your age: "))

if age < 5:
    print("you should play with toys")
elif age >= 5 and age <= 12:
    print("You can play outdoor game.")
elif age >= 13 and age <= 17:
    print("You might enjoy video games.")
else:
    print("You can try hiking or traveling.")