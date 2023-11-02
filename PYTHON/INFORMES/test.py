import os

raiz = "C:/Users/Lenovo/Dropbox/PROYECTOS JUAN DIEGO/PYTHON/TEST/MINI MATRIZ"

ubicaciones = dict()

for i in os.listdir(raiz):
    filtrada = i.split("-")
    filtrada = filtrada[0]
    ubicacion = raiz + '/' + i + '/'
    key = {filtrada:ubicacion}
    ubicaciones.update(key)

print(ubicaciones)




##leer las carpetas de kizeo

kizeo = 'C:/Users/Lenovo/Dropbox/PROYECTOS JUAN DIEGO/PYTHON/TEST/HANDLER'
kizeo = os.listdir(kizeo)
print(kizeo)