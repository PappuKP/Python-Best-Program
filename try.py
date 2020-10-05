print("hello world")

try:
    a =int(input("Enter the value "))
    if a>6:
        print("the number you entered is greater than 6")
    else:
        print("I guess it is less than 6")
except Exception as e:
    print(f"there is error in this program {e} ")
finally:
    print("we are done!")            