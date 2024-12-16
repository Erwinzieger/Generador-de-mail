# Generador de email funcional!
print('*** BIENVENDIDO AL GENERADOR DE MAIL DE Erwin !')
print()
nombre = input('Introduzca su nombre: ')
apellido = input('Introduzca su apellido: ')
empresa = input('Introduzca el nombre de la empresa de su mail (hotmail,gmail,yahoo,etc): ')
dominio = input('Introduzca el nombre del dominio (.com,.com.ar) ')

nombre = nombre.lower().replace(' ','').strip()
apellido = apellido.lower().replace(' ','').strip()
empresa = empresa.lower().replace(' ','').strip()
dominio = dominio.lower().replace(' ','').strip()

print()
print(f'Su correo de electronico generado es: {nombre}{apellido}@{empresa}{dominio}')
print()

nombre = nombre[:2]
apellido = apellido[:2]

print(f'Otra alternativa es: {nombre}{apellido}@{empresa}{dominio}')

