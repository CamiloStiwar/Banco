import random
from persona import Persona

class CuentaBancaria:
    def __init__(self, saldoInicial,personaPropietaria):
        self.numeroCuenta = random.randint(1000,10000)
        self.saldo = saldoInicial
        self.propietario = personaPropietaria
    
    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo = self.saldo - monto
            print("Retiro Exitoso")

    def consignar(self, monto):
        self.saldo = self.saldo + monto

    def consultarSaldo(self):
        print("_____________")
        print("Cuenta: ",self.numeroCuenta)
        print("Saldo: ",self.saldo)
        print("_____________")

def buscarCuentas(mensajeOperacion, listaDeCuentas):
    numCuentaABuscar = int(input(mensajeOperacion))
    for cuentaIteracion in listaDeCuentas:
        if cuentaIteracion.numeroCuenta == numCuentaABuscar:
            return cuentaIteracion
    return False

def buscarPersona(cedula, listaDePersonas):
    for persona in listaDePersonas:
        if persona.documento == cedula:
            return persona
    
    return False

listaDeCuentas = []
listaDePersonas = []

while True:
    operacion = input("Ingrese N para crear una nueva cuenta, S para consultar el saldo, R para retirar y C para consignar: ")
    if operacion == "N":
        saldoInicial = float(input("Bienvenido al banco XYZ. Para crear su cuenta bancaria, ingrese el saldo inicial de la cuenta: "))

        cedula = input("Por favor digite su número de cedula: ")
        
        personaEncontrada = buscarPersona(cedula, listaDePersonas)
        
        if not personaEncontrada:
            nuevaPersona = Persona("Daniel", 48, 23432, "dslc@gmasdk.com", "sdsadas", "Colombiano", "ingeniero", "1006206063")
            listaDePersonas.append(nuevaPersona)
            nuevaCuenta = CuentaBancaria(saldoInicial, nuevaPersona)
            listaDeCuentas.append(nuevaCuenta)
            print("Cuenta creada con exito, su numero de cuenta es ", nuevaCuenta.numeroCuenta)
        else:
            nuevaCuenta = CuentaBancaria(saldoInicial, personaEncontrada)
            listaDeCuentas.append(nuevaCuenta)        

    elif operacion == "S":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta que quiere consultar: ", listaDeCuentas)
        if not resultadoBusqueda:
            print("Cuenta no encontrada.")
        else:
            resultadoBusqueda.consultarSaldo()
    elif operacion == "R":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta de la que desea retirar: ", listaDeCuentas)
        if not resultadoBusqueda:
            print("Cuenta no encontrada.")
        else:
            monto = float(input("Ingrese el monto que desea retirar: "))
            resultadoBusqueda.retirar(monto)
    elif operacion == "C":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta a la que desea consignar: ", listaDeCuentas)
        if not resultadoBusqueda:
            print("Cuenta no encontrada.")
        else:
            monto = float(input("Ingrese el monto que desea consignar: "))
            if monto < 10000:
                resultadoBusqueda.consignar(monto)
                print("Consignación exitosa.")
            if monto > 10000:
                impuesto = monto * (4/1000)
                monto = monto - impuesto
                resultadoBusqueda.consignar(monto)
                print(f"Consignación exitosa y se ha cobrado {impuesto} de impuestos.")
    else:
        print("Operación incorrecta")


