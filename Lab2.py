def calculate_bmi(weight, height):
    print("Weight = " + str(weight))
    print("Height = " + str(height))

    bmi=weight/(height*height)
    if (bmi < 18.5):
        print("BMI Under Weight = " + str(bmi))
    elif (18.5 <= bmi <= 25.0):
        print("BMI Normal Weight = " + str(bmi))
    else:
        print("BMI Over Weight = " + str(bmi))

calculate_bmi(weight = 66, height=1.76)