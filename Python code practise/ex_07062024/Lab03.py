#Write a program that calculates and displays grades

score = int(input("Enter the score:"))

if score >= 90 and score<=100:
    print("Your Grade is: A")
elif score >= 80 and score<=90:
    print("Your Grade is: B")
elif score >= 70 and score<=80:
    print("Your Grade is: C")

elif score >= 60 and score<=70:
    print("Your Grade is: D")

elif score >= 50 and score<=60:
    print("Your Grade is: E")

elif score >= 0 and score<=50:
    print("Your Grade is: F")

else:
    print("Invalid Score")