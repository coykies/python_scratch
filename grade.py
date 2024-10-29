#score study in us
score = int(input("Score: "))

#grade A
if 90 <= score <= 100:
    print("Grade: A")
#grade B
elif 80 <= score < 90:
    print("Grade: B")
#grade C
elif 70 <= score < 80:
    print("Grade: C")
#grade D
elif 60 <= score < 70: 
    print("Grade: D")
#grade F
else: 
    print("Grade: F")

