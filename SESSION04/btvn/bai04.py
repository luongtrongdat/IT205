turn=1
key = True
lucky_number =36
while turn <=5 and key :
    Guess_luck_number = int(input(f"lượt đoán số {turn} mời nhập số của bạn:"))
    if Guess_luck_number == lucky_number :
        print("chúc mừng bạn đã đoán đúng số may mắn ")
        key = False 
    elif Guess_luck_number < lucky_number :
        print("gợi ý : số của bạn nhỏ hơn số may mắn ")
    else :
        print("gợi ý : số của bạn lớn hơn số may mắn ")
    turn += 1