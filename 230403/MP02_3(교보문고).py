membership = input("회원 등급 입력: ")
parkingTime = int(input("주차 시간 입력: "))

if membership == "플래티넘" or membership == "골드":
    parkingTime -= 120
elif membership == "실버" or membership == "프렌즈":
    purchased = int(input("구매 금액 입력: "))
    if purchased >= 30000:
        parkingTime -= 120
    elif purchased >= 10000:
        parkingTime -= 60
elif membership == "비회원":
    purchased = int(input("구매 금액 입력: "))
    if purchased >= 50000:
        parkingTime -= 120
    elif purchased >= 30000:
        parkingTime -= 60    
if parkingTime < 0:
    parkingTime = 0
fee = parkingTime // 10 * 1000
print(f"주차요금은 {fee}원입니다")
