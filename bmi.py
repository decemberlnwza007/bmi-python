height = float(input("Enter your hight in centimeters: "))
weight = float(input("Enter your Weight in Kg: "))

height = height / 100

bmi = weight/(height * height)
print('Your body Mass Index is: ', bmi)

if(bmi>0):
	if(bmi<=16):
		print("you are severely underweight")
	elif(bmi<=18.5):
		print("you are underweight")
	elif(bmi<=25):
		print("you are Healthy")
	elif(bmi<=30):
		print("you are overweight")
	else: print("you are severely overweight")
else:("enter valid details")