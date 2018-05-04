f= open("sample.txt",'w',encoding='UTF-8')

odd=['70','60','55','75','95','90','80','80','85','100']
for i in odd:
    data=i
    f.write(data+"\n")
f.close()


f=open("sample.txt",encoding='UTF-8')
lines=f.readlines()
f.close()

total=0

for line in lines:
    score=int(line)
    total+=score

    average=total/lines.__len__()

f=open("result.txt",'w',encoding='UTF-8')
f.write("총합:%d, 평균:%d"%(total,average))