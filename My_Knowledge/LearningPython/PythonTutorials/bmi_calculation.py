name1 = "BeoKa"
height_m1 = 1.8
weight_kg1 = 108

name2 = "BeoKa's Sister"
height_m2 =  1.6
weight_kg2 = 60

name3 = "BeoKa's Father"
height_m3 = 1.78
weight_kg3 = 60

def bmi_calculation(name, height, weight):
	bmi = weight / (height ** 2)
	print("bmi: ")

	if bmi < 25:
		return name + " not overweight"
	else:
		return name + " is overweight"

result1 = bmi_calculation(name1, height_m1, weight_kg1)
result2 = bmi_calculation(name2, height_m2, weight_kg2)
result3 = bmi_calculation(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)
