#score study in us
score = int(input("Score: "))

#grade A
if score >= 90 and score <= 100:
    print("Grade: A")
#grade B
elif score >= 80 and score < 90:
    print("Grade: B")
#grade C
elif score >= 70 and score < 80:
    print("Grade: C")
#grade D
elif score >= 60 and score < 70: 
    print("Grade: D")
#grade F
else: 
    print("Grade: F")
    
