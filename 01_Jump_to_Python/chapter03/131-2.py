# coding: cp949
my_data=[1,1,1,4,2,44,6,8]
print(my_data)
ud = set(my_data)
print(ud)

for element in ud:
    print(element)

td=(1,2,3,77)
for element in td:
    print(element)

strd="hello"
for i in strd:
    print(i)

dicd={"이름":"박가은",
        "나이":26,
        "취미":"수영"}
for element in dicd:
    print(element)
for key in dicd:
    print(key + str(dicd[key]))

