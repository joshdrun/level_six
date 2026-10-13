numbers = [11, 25,-2,7,18]
blah = 100000

def is_odd(numero):
    odd = True
    if numero % 2 == 0:
        print("even")
        odd = False

    blah = 50500505000
    print(blah)
    return odd  

print(blah)
for num in numbers:
    if is_odd(num):
        print(f"{num} is odd.")
    else:
        print(f"{num} is even.")

    