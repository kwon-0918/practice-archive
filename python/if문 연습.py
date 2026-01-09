#if문 테스트
time = input("시간 입력: ")

if not time.isdigit():
    print("몰루?")
else:
    time = int(time)

    if time < 8:
        print("괜춘")
    elif time == 9:
        print("낫 배드")
    else:
        print("안 괜춘")