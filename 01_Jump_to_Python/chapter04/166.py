# f=open("foo.txt",'w',encoding='UTF-8')
# f.write("인생은 너무 짧네요. 그래서 당신은 파이썬이필요해요")
# f.close()

with open("foo.txt",'w') as f:
    f.write("인생은 너무 짧네요. 그래서 당신은 파이썬이 필요해요")