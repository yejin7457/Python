membership = input("회원 등급 입력: ")
parkingTime = int(input("주차 시간 입력: "))

if membership == "플래티넘":
    if parkingTime <= 120:
        print("주차비는 0원입니다")
    else:
        fee = (parkingTime - 120) // 10 * 1000
        print(f"주차 요금은 {fee}원입니다")
if membership == "골드":
    if parkingTime <= 120:
        print("주차비는 0원입니다")
    else:
        fee = (parkingTime - 120) // 10 * 1000
        print(f"주차 요금은 {fee}원입니다")
if membership == "실버":
    purchased = int(input("구매 금액 입력: "))
    if purchased >= 30000:
        if (parkingTime <= 120):
            print("주차비는 0원입니다")
        else:
            fee = (parkingTime - 120) // 10 * 1000
            print(f"주차 요금은 {fee}원입니다")

    else:
        if purchased >= 10000:
            if (parkingTime <= 60):
                print("주차비는 0원입니다")
            else:
                fee = (parkingTime - 60) // 10 * 1000
                print(f"주차 요금은 {fee}원입니다")
        else:
            fee = parkingTime // 10 * 1000
            print(f"주차 요금은 {fee}원입니다")
if membership == "프렌즈":
    purchased = int(input("구매 금액 입력: "))
    if purchased >= 30000:
        if (parkingTime <= 120):
            print("주차비는 0원입니다")
        else:
            fee = (parkingTime - 120) // 10 * 1000
            print(f"주차 요금은 {fee}원입니다")

    else:
        if purchased >= 10000:
            if (parkingTime <= 60):
                print("주차비는 0원입니다")
            else:
                fee = (parkingTime - 60) // 10 * 1000
                print(f"주차 요금은 {fee}원입니다")
        else:
            fee = parkingTime // 10 * 1000
            print(f"주차 요금은 {fee}원입니다")
if membership == "비회원":
    purchased = int(input("구매 금액 입력: "))
    if purchased >= 50000:
        if (parkingTime <= 120):
            print("주차비는 0원입니다")
        else:
            fee = (parkingTime - 120) // 10 * 1000
            print(f"주차 요금은 {fee}원입니다")

    else:
        if purchased >= 30000:
            if (parkingTime <= 60):
                print("주차비는 0원입니다")
            else:
                fee = (parkingTime - 60) // 10 * 1000
                print(f"주차 요금은 {fee}원입니다")
        else:
            fee = parkingTime // 10 * 1000
            print(f"주차 요금은 {fee}원입니다")

    