#try:
#except:
#else:
#finally:

while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That's not a number! ")
    #else will run when except doesnt.
    else:
        print("Good job, you entenred a number!")
        break
    #will run no matter what
    finally:
        print("Im in the finally!")
print("Rest of game logic runs!")

def divide(a, b):
    try:
        result = a/b (a/b)
    except ZeroDivisionError:
        print("dont divide by zero please!")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} equals to {result}")
    
print(divide(1,"a"))