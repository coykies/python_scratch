#main func than print even or odd
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
#func that check n / 2 = 0 (optimazed smart)
def is_even(n):
    return n % 2 == 0


main()