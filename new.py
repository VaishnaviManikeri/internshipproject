#by taking input it will check the grade

x = int(input("enter marks"))
if x < 25:
    print("Grade:F")
elif x <= 44 and x >= 25:
    print("GRADE:E")
elif x <= 49 and x >= 45:
    print("GRADE:D") 
elif x <= 59 and x >= 50:
    print("GRADE:c")
elif x <= 69 and x >= 50:
    print("GRADE:B")
elif x <= 70:
    print("GRADE:A") 
else:
    print("invalid marks entered")
