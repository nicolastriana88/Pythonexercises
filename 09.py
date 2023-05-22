producto=input('Agrege un producto: ')
valor=float(input('De el valor del producto: '))
cantidad=int(input('Cantidad del producto: '))

subtotal=valor*cantidad
iva= subtotal * 0.16
descuento= subtotal * 5 / subtotal
total= subtotal + iva
totalpagar= total - descuento

print('El subtotal del producto ' + producto + ' es ' + format(subtotal) + ' usd')
print('El valor del descuento ' + producto + ' es ' + format(descuento)+ ' usd')  
print('El total del producto ' + producto + ' es ' + format(total)+ ' usd')
print('El iva del producto ' + producto + ' es ' + format(iva)+ ' usd')
print('El total a pagar del producto ' + producto + ' es ' + format(totalpagar)+ ' usd')