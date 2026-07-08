name = "Abhi"
age = 19
collage = "TSSM BSCOER"

print(3**4)

print(name != collage)

if age >= 19:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")


math = 91
science = 89 
english = 70
physics = 95
chemistry = 86

cal_total_marks = math + science + english + physics + chemistry
cal_average_marks = cal_total_marks / 5

print(cal_average_marks)

if cal_average_marks >= 90 :
    print("Grade A")
elif cal_average_marks >= 75 :
    print("Grade B")
elif cal_average_marks >= 60 :
    print("Grade C")
elif cal_average_marks >= 40 :
    print("Grade D")
else:
    print("Fail")