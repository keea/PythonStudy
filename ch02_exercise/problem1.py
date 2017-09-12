# 이름과 나이를 입력받아 사용자가 100살이 되는 연도를 화면에 출력.

name = input("이름을 입력하시오 : ")
age = int(input("나이를 입력하시오 : "))

cuntAge = 100 
leftAge = cuntAge - age # 100세 까지 남은 나이.
hundredYear = 2017 + leftAge # 100세가 되는 연도
print(name,"씨는",hundredYear,"에 100살이시네요!")
