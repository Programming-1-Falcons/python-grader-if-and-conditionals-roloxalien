grade = int(input("wut ur grade lol (points/500)"))
percentage = (grade/500)*100

print("Your points: " + str(grade) + "/500")
print("Your percentage: " + str(percentage) + "%")

if percentage < 50:
    print("Your grade is F")
elif percentage > 50 and percentage < 60:
     print("Your grade is D")
elif percentage > 60 and percentage < 75:
     print("Your grade is C")
elif percentage > 75 and percentage < 89:
     print("Your grade is B")
elif percentage > 89:
    print("Your grade is A")

