# a program to grade marks
a= int(input("enter the first subject marks"))
b= int(input("enter the second subject marks"))
c= int(input("enter the third subject marks"))
sum= (a+b+c)/3
if (sum>=70 and sum<=100):
    print ("Excellent, your grade is A")
elif (sum>=60) and (sum<=69):
    print ("Great, your grade is B")
elif (sum>=50) and (sum<=59):
    print ("Good, your grade is C")
elif (sum>=40) and (sum<=49):
    print ("Fair, your grade is D")
elif (sum>=0) and (sum<=39):
    print ("Fail")
else:
    print ("See me in the office")