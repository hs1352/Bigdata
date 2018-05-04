f=open("새파일",'r',encoding='UTF-8')
lines=f.readlines()
for line in lines:
    print(line)
f.close()