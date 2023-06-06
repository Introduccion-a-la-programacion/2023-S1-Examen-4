
import Examen4 

Ex = Examen4


salaFut1 = Ex.SalaFutbol("Fut 5", "88556699", "San José", "futsala5gmail.com")
"Error: La cuenta de correo no tiene formato correcto"

salaFut1 = Ex.SalaFutbol("Fut 5", 88556699, "San José", "futsala5@gmail.com")

salaFut1.mostrar()

"Sala Futol 5 = Fut 5"
"Telefono = 88556699, Direccion = San José, Email = futsala@gmail.com" 
"Horario: L a D de 1 a 10 pm"

salaFut1.crearCancha(10000, 10)
salaFut1.crearCancha(10000, 10)
salaFut1.crearCancha(14000, 12)
salaFut1.crearCancha(8000, 8)
salaFut1.crearCancha("10000", "10")
"Error: Los valores deben ser numéricos enteros"

salaFut1.mostrarCanchas()
"Cancha=1, Precio=10000, Capacidad=10"
"Cancha=2, Precio=10000, Capacidad=10"
"Cancha=3, Precio=14000, Capacidad=12"
"Cancha=4, Precio=8000, Capacidad=8"

salaFut1.crearCliente("325801235", "Jorge", "Perez", "Avellano", 45612581, "jperez")
"Error: La cuenta de correo no tiene formato correcto"
salaFut1.crearCliente("325801235", "Jorge", "Perez", "Avellano", 45612581, "jperez@gmail.com")
salaFut1.crearCliente("625801235", "Mario", "Lopez", "Alvarado", 85612581, "mlopez@gmail.com")


salaFut1.buscarCliente("625001235")
"Error: Cliente no encontrado"
salaFut1.buscarCliente("625801235")
"Nombre: Lopez Alvarado, Mario"
"Cedula: 625801235, Teléfono: 85612581 Email: mlopez@gmail.com"


salaFut1.modificarCliente("125801235", "", "", "Mendez", 85612222, "")
"Error: Cliente no encontrado"
salaFut1.modificarCliente("625801235", "", "", "Mendez", 85612222, "")
"Nombre: Lopez Mendez, Mario"
"Cedula: 625801235, Teléfono: 85612222 Email: mlopez@gmail.com"


salaFut1.mostrarClientes()
"Nombre: Perez Avellano, Jorge"
"Cedula: 325801235 Teléfono: 45612581 Email: jperez@gmail.com"

"Nombre: Lopez Mendez, Mario"
"Cedula: 625801235, Teléfono: 85612222 Email: mlopez@gmail.com"

salaFut1.reservarCancha("625801235", 1, "25/6/2023", 18, 1)
"Reserva 1001, Fecha: 25/6/2023, Inicia: 18h Horas: 1, Precio: 10000"
"Cliente "
"Nombre: Lopez Alvarado, Mario"
"Cedula: 625801235, Teléfono: 85612581 Email: mlopez@gmail.com"

salaFut1.reservarCancha("625801235", 1, "25/6/2023", 18, 1)
"Error: Cancha reservada"

salaFut1.reservarCancha("625801235", 1, "25/6/2023", 17, 2)
"Error: Cancha reservada"

salaFut1.reservarCancha("325801235", 4, "25/6/2023", 20, 1)
"Reserva 1002, Fecha: 25/6/2023, Inicia: 20h Horas: 1, Precio: 8000"
"Cliente "
"Nombre: Perez Avellano, Jorge"
"Cedula: 325801235 Teléfono: 45612581 Email: jperez@gmail.com"

salaFut1.reservarCancha("325801235", 4, "25/6/2023", 18, 2)
"Reserva 1003, Fecha: 25/6/2023, Inicia: 18h Horas: 2, Precio: 16000"
"Cliente "
"Nombre: Perez Avellano, Jorge"
"Cedula: 325801235 Teléfono: 45612581 Email: jperez@gmail.com"

salaFut1.borrarReserva(1008)
"Error: Número de reserva no existe"
salaFut1.borrarReserva(1002)
"Reserva borrada"

salaFut1.mostrarReserva(1001)
"Reserva 1001, Fecha: 25/6/2023, Inicia: 18h Horas: 1, Precio: 10000"
"Cliente "
"Nombre: Lopez Alvarado, Mario"
"Cedula: 625801235, Teléfono: 85612581 Email: mlopez@gmail.com"

salaFut1.buscarReservas("25/6/2023")
"Reserva 1001, Fecha: 25/6/2023, Inicia: 18h Horas: 1, Precio: 10000"
"Cliente "
"Nombre: Lopez Alvarado, Mario"
"Cedula: 625801235, Teléfono: 85612581 Email: mlopez@gmail.com"


"Reserva 1003, Fecha: 25/6/2023, Inicia: 18h Horas: 2, Precio: 16000"
"Cliente "
"Nombre: Perez Avellano, Jorge"
"Cedula: 325801235 Teléfono: 45612581 Email: jperez@gmail.com"

salaFut1.crearFactura(1001)
"Factura 1 Fecha 25/6/2023"
"Cliente"
"Nombre: Lopez Alvarado, Mario"
"Cedula: 625801235, Teléfono: 85612581 Email: mlopez@gmail.com"
"Reserva 1001, Fecha: 25/6/2023, Inicia: 18h Horas: 1, Precio: 10000"
"Total 10000"

salaFut1.crearFactura(1003)
"Factura 2 Fecha 25/6/2023"
"Cliente"
"Nombre: Perez Avellano, Jorge"
"Cedula: 325801235 Teléfono: 45612581 Email: jperez@gmail.com"
"Reserva 1003, Fecha: 25/6/2023, Inicia: 19h Horas: 2, Precio: 16000"
"Total 16000"

salaFut1.resumen()
"Factura 1 Fecha 25/6/2023"
"Cliente"
"Nombre: Lopez Alvarado, Mario"
"Cedula: 625801235, Teléfono: 85612581 Email: mlopez@gmail.com"
"Reserva 1001, Fecha: 25/6/2023, Inicia: 18h Horas: 1, Precio: 10000"
"Total 10000"

"Factura 2 Fecha 25/6/2023"
"Cliente"
"Nombre: Perez Avellano, Jorge"
"Cedula: 325801235 Teléfono: 45612581 Email: jperez@gmail.com"
"Reserva 1003, Fecha: 25/6/2023, Inicia: 18h Horas: 2, Precio: 16000"
"Total 16000"

"Resumen"
"======="
"Total Facturas: 2"
"Monto Total: 26000"
"Total horas reservadas: 3"

Ex.SalaFutbol.totalSalas
1
