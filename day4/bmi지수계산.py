#사용자의 몸무게 (소수점)입력받기 : 56.6
#키 입력받기 ( 170 -> 1.7)
#bmi = 몸무게 / 키 * 키
#당신의 bmi는 **입니다.

weight = float(input("몸무게를 입력하세요 : ")) #50? 50.0
height_cm = float(input("키를 입력하세요 : "))
height_m = height_cm / 100 #cm -> m

bmi = weight / (height_m ** 2)
print("당신의 BMI는",round(bmi,1),"입니다.")
