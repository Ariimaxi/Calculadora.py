from tkinter import *

raiz = Tk()
raiz.title("Calculadora")


miFrame = Frame(raiz)

miFrame.pack()

Operacion = ""

reset_pantalla = False

resultadofinal = 0

# Pantalla #
NumeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=NumeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="white", justify="right")

# Pulsaciones Teclado #


def numeroPulsado(num):
    global Operacion

    if Operacion != "":
        NumeroPantalla.set(num)

        Operacion = ""

    else:
        NumeroPantalla.set(NumeroPantalla.get() + num)


# Botones Row 2 #
boton7 = Button(miFrame, text="7", width=3, command=lambda: numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda: numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda: numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(
    miFrame, text="/", width=3, command=lambda: dividir(NumeroPantalla.get())
)
botonDiv.grid(row=2, column=4)

# Botones Row 3 #
boton4 = Button(miFrame, text="4", width=3, command=lambda: numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda: numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda: numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult = Button(
    miFrame, text="X", width=3, command=lambda: multiplicacion(NumeroPantalla.get())
)
botonMult.grid(row=3, column=4)

# Botones Row 4 #
boton1 = Button(miFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda: numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command=lambda: numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest = Button(
    miFrame, text="-", width=3, command=lambda: resta(NumeroPantalla.get())
)
botonRest.grid(row=4, column=4)

# Botones Row 5 #
boton0 = Button(miFrame, text="0", width=3, command=lambda: numeroPulsado("0"))
boton0.grid(row=5, column=2)
botonComa = Button(miFrame, text=",", width=3, command=lambda: numeroPulsado("."))
botonComa.grid(row=5, column=1)
botonSuma = Button(
    miFrame, text="+", width=3, command=lambda: Sum(NumeroPantalla.get())
)
botonSuma.grid(row=5, column=3)
botonTotal = Button(
    miFrame, text="=", width=3, command=lambda: Total_resultado(NumeroPantalla.get())
)
botonTotal.grid(row=5, column=4)

# Funcionalidad Suma #
def Sum(num):
    global Operacion
    global resultadofinal
    global reset_pantalla

    resultadofinal += int(num)
    Operacion = "Sum"
    reset_pantalla = True

    NumeroPantalla.set(resultadofinal)


# Funcionalidad Resta #
num1 = 0
contador_resta = 0


def resta(num):
    global Operacion

    global resultadofinal

    global num1

    global contador_resta

    global reset_pantalla

    if contador_resta == 0:
        num1 = int(num)
        resultadofinal = num1
    else:
        if contador_resta == 1:
            resultadofinal = num1 - int(num)
        else:
            resultadofinal = int(resultadofinal) - int(num)
        NumeroPantalla.set(resultadofinal)
        resultadofinal = NumeroPantalla.get()

    contador_resta = contador_resta + 1

    Operacion = "resta"
    reset_pantalla = True


# Funcionalidad Multiplicacion #

contador_multi = 0


def multiplicacion(num):
    global Operacion

    global resultadofinal

    global num1

    global contador_multi

    global reset_pantalla

    if contador_multi == 0:
        num1 = int(num)
        resultadofinal = num1

    else:
        if contador_multi == 1:
            resultadofinal = num1 * int(num)
        else:
            resultadofinal = int(resultadofinal) * int(num)
        NumeroPantalla.set(resultadofinal)
        resultadofinal = NumeroPantalla.get()

    contador_multi = contador_multi + 1
    Operacion = "multiplicacion"
    reset_pantalla = True


# Funcionalidad Division #
contador_divi = 0


def dividir(num):

    global Operacion

    global resultadofinal

    global num1

    global contador_divi

    global reset_pantalla

    if contador_divi == 0:
        num1 = float(num)
        resultadofinal = num1

    else:
        if contador_divi == 1:
            resultadofinal = num1 / float(num)
        else:
            resultadofinal = float(resultadofinal) / float(num)
        NumeroPantalla.set(resultadofinal)
        resultadofinal = NumeroPantalla.get()

    contador_divi = contador_divi + 1
    Operacion = "division"
    reset_pantalla = True


# Funcionalidad Signo Igual #
def Total_resultado(num):
    global resultadofinal

    global Operacion

    global contador_resta

    global contador_multi

    global contador_divi

    if Operacion == "Sum":
        NumeroPantalla.set(resultadofinal + int(NumeroPantalla.get()))

        resultadofinal = 0

    elif Operacion == "resta":
        NumeroPantalla.set(resultadofinal - int(NumeroPantalla.get()))

        resultadofinal = 0

        contador_resta = 0
    elif Operacion == "multiplicacion":
        NumeroPantalla.set(resultadofinal * int(NumeroPantalla.get()))

        resultadofinal = 0

        contador_multi = 0

    elif Operacion == "division":
        NumeroPantalla.set(resultadofinal / int(NumeroPantalla.get()))

        resultadofinal = 0

        contador_divi = 0


raiz.mainloop()