var1 =1

def vartest():
    global var1
    var = var1+1

def vartest2():
    print(var1)
    
vartest()

print(var1)

vartest2()