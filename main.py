import qrcode

print('Script para convertir URL a QR')
name=input(' Nombre de la imagen ')
link = input(" Ingresa URL ")
img = qrcode.make(link)
f = open(name+".png", "wb")
img.save(f)
img.show()
f.close()
print("Tarea finalizada")

