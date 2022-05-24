number_grade = input("Enter your grade here")

letter_grade = "F"

# your code here
def grade(number_grade):
    if int(number_grade)>=90:
        return "A"
    else:
        if int(number_grade)>=80:
            return "B"
        else:
            if int(number_grade)>=70:
                return "C"
            else:
                if int(number_grade)>=60:
                    return "D"
                else:
                    return letter_grade
                
print("your number:", str(number_grade), "your grade:", grade(number_grade))