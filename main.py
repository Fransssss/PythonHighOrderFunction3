#

from ways import text
from ways import loud
from ways import quiet

# ----------------------
# simple program practice to understand high order of function
# choose to say something in certain way and related function would be called
# ----------------------

print("\n Say something...")
print("1. LOUDLY")
print("2. quietly")
print("e. Exit")
choice = input("choice: ").lower()

while choice != 'e':
    if choice == '1':
        say_loud = text(loud)
        say_loud = "\n[ " + say_loud + " ]"
        print(say_loud)

    elif choice == '2':
        say_quiet = text(quiet)
        say_quiet = "\n[ " + say_quiet + " ]"
        print(say_quiet)

    else:
        print("\n[ Invalid choice ]")

    print("\n Say something...")
    print("1. LOUDLY")
    print("2. quietly")
    print("e. Exit")
    choice = input("choice: ").lower()

print("\n== Exit Program ==")
