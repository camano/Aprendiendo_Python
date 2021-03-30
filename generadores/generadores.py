def generarpares(limite):
    num=1

    while num<limite:
        yield num*2
        num=num+1

devuelve=generarpares(10)
print(next(devuelve))
for i in devuelve:
    print(i)