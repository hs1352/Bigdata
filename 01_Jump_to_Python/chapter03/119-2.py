# coding: cp949
card = input("ī�带 �����ϰ� �ֽ��ϱ�?(y/n): ")
partnership = input("��Űýó �ý� �����Դϱ�? (y/n)")

if card == 'y':     card=True
else:               card=False
if partnership == 'y':      partnership = True
else:                       partnership = False

if card == True and partnership == True:
        print("�ýø�Ÿ������")
else:
    print("�ɾ�ž� �մϴ�.")