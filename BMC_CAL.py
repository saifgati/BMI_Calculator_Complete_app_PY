# created by saif gati
print("Welcome to the BMI calculator by Saif Gati")
Name = input("Please enter your name >> ")
weight = float(input(f"Please {Name.upper()} enter your weight in kg >> "))
height = float(input(f"Please {Name.upper()} enter your height in cm >> "))
BMI = float((weight / (height * height)) * 10000)  # the bmi equation
BMI_F = float("{0:.2f}".format(BMI))  # adding this will make only two numbers after . shown
gender = input('your a (male) or (female) >> ')
Msg = ""  # initialise an empty msg
gender_validation = False  # for knowing if the gender is valid
if gender.upper() == "FEMALE":
    print(f"Your BMI is {BMI_F}%")
    gender_validation = True
    if BMI_F < 15.5:
        print(" You are severely underweight !")
        Msg = "Being underweight can represent as many health concerns to an individual as being overweight can. If a " \
              "person is underweight, their body may not be getting the nutrients it needs to build healthy bones, " \
              "skin, and hair. "
    elif 15.5 < BMI_F < 17.5:
        print("You are underweight !")
        Msg = "Being underweight can represent as many health concerns to an individual as being overweight can. If a " \
              "person is underweight, their body may not be getting the nutrients it needs to build healthy bones, " \
              "skin, and hair. "
    elif 17.5 < BMI_F < 24:
        print("Best condition ")
        Msg = "You are good !"
    elif 24 < BMI_F < 29:
        print(" You are overweight !")
        Msg = 'Overweight and obesity may increase the risk of many health problems, including diabetes, ' \
              'heart disease, and certain cancers. If you are pregnant, excess weight may lead to short- and ' \
              'long-term health problems for you and your child. '
    elif 29 < BMI_F < 38.9:
        print("Obese !!!")
        Msg = "Overweight and obesity may increase the risk of many health problems, including diabetes, " \
              "heart disease, and certain cancers. If you are pregnant, excess weight may lead to short- and " \
              "long-term health problems for you and your child. "
    elif BMI_F > 38.9:
        print("you are extremely obese")
        Msg = 'Overweight and obesity may increase the risk of many health problems, including diabetes, ' \
              'heart disease, and certain cancers. If you are pregnant, excess weight may lead to short- and ' \
              'long-term health problems for you and your child. You may have to consult a doctor '
    else:
        print("Invalid")
elif gender.upper() == "MALE":
    print(f"Your BMI is {BMI_F}%")
    gender_validation = True
    if BMI_F < 16.5:
        print(" You are severely underweight !")
        Msg = "Being underweight can represent as many health concerns to an individual as being overweight can. If a " \
              "person is underweight, their body may not be getting the nutrients it needs to build healthy bones, " \
              "skin, and hair. "
    elif 16.5 < BMI_F < 18.5:
        print("You are underweight !")
        Msg = "Being underweight can represent as many health concerns to an individual as being overweight can. If a " \
              "person is underweight, their body may not be getting the nutrients it needs to build healthy bones, " \
              "skin, and hair. "
    elif 18.5 < BMI_F < 25:
        print("Best condition ")
        Msg = "You are good !"
    elif 25 < BMI_F < 30:
        print(" You are overweight !")
        Msg = "Overweight and obesity may increase the risk of many health problems, including diabetes, " \
              "heart disease, and certain cancers. "
    elif 30 < BMI_F < 39.9:
        print("Obese !!!")
        Msg = "Overweight and obesity may increase the risk of many health problems, including diabetes, " \
              "heart disease, and certain cancers. "
    elif BMI_F > 39.9:
        print("you are extremely obese")
        Msg = "Overweight and obesity may increase the risk of many health problems, including diabetes, " \
              "heart disease, and certain cancers.You better see a doctor."
    else:
        print("Invalid")
else:
    print("Invalid gender")
if gender_validation:

    read_more = input("Do you like to read more about ? (yes) ")
    if read_more.upper() == "YES":
        print(Msg)
else:
    print("Good bye...")
