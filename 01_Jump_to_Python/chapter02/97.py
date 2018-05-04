# coding: cp949
dish_stack=[]
dish_stack.append('d1')
dish_stack.append('d2')
dish_stack.append('d3')
dish_stack.append('d4')
print("식판현황: ",end='')
print(dish_stack)

while(dish_stack):
        print("{0} 식판 걸겆이를 합니다.".format(dish_stack.pop()))
