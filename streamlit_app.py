height = int(input('키(cm): '))

if height < 100:
    print('탑승 불가')
elif height < 130:  # 100 이상 130 미만인 경우
    print('보호자 동행시 탑승가능')
elif height < 195:  # 130 이상 195 미만인 경우
    print('탑승가능')
else:              # 195 이상인 모든 경우
    print('탑승불가')
