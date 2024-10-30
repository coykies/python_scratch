#main func than print even or odd
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
#func that check n / 2 = 0
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()