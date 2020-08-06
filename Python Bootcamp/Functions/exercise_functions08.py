#callback function

def callback(sum):
    print (f"Sum = {sum}")

def main(a,b,callback = None):
    print (f" Adding {a} + {b}")
    if callback:
        callback(a+b)

main(1,1,callback)