for i in [1,2,3,"r"]:
    print("hola")

for u in "hola@ff.com":
    print("gooo",end=" ")


email=False
for f in "hola@amigo":
    if (f=="@"):
        email=True
    

if email==True:
    print("EL correo es correcto")
else:
    print("El email no es corrrecto")