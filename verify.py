from main import Card

input_code = input("请输入编码后的卡信息:")
card = Card("", 0, 0, 0, 0)
card.decode(input_code)
print("卡信息如下:\n{}".format(card.info()))
if card.verify():
    print("卡信息验证通过!")
else:
    print("卡信息验证失败!")
    if not card.date_verify():
        print("卡已过期!")