import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x600")  # Tamaño de la ventana
ventana.configure(bg="#ffffff")

# Establecer tamaño y estilo de fuente para los botones
boton_ancho = 5  # Ancho de los botones
boton_alto = 2   # Alto de los botones
tamano_fuente = ("Arial", 16)  # Tamaño de la fuente
color_fondo = "#ffffff"  # Color de fondo (verde)
color_letra = "black"    # Color de la letra
color_borde = "white"    # Color del borde

# Crear un diccionario para los estilos de los botones
estilo_boton = {
    "font": tamano_fuente,
    "width": boton_ancho,
    "height": boton_alto,
    "bg": color_fondo,    # Color de fondo
    "fg": color_letra,    # Color del texto
    "relief": "flat",   # Estilo del contorno
    "bd": 0,              # Ancho del borde
    "highlightbackground": color_borde  # Color del borde
}

# entrada de la operacion o un conjunto de resultado y operacion
entry_superior = tk.Entry(ventana, font=("Arial", 18), justify="right", relief="flat", fg="#909090")
entry_superior.grid(row=0, column=0, columnspan=4, padx=5, pady=3, sticky="ew")

# entrada donde se ingresa el operador o operando
entry_inferior = tk.Entry(ventana, font=("Arial", 20), justify="right", relief="flat", fg="#000000")
entry_inferior.grid(row=1, column=0, columnspan=4, padx=5, pady=3, sticky="ew")

# Inicializar entry_inferior con 0
entry_inferior.insert(0, "0")
valor_actual = 0  # Almacena el valor actual para operaciones acumulativas
operador_actual = ""  # Almacena el operador actual
ultima_operacion = False  # Indica si se acaba de realizar una operación

def presionar(valor):
    
    global ultima_operacion  # Declarar como global para acceder correctamente
    global operador_actual  # Para verificar el estado del operador
    
    def porcentaje():
        try:
            num = float(entry_inferior.get())
            resultado = num / 100  # Calcula el porcentaje
            entry_superior.delete(0, tk.END)
            entry_superior.insert(0, f"{num}%")  # Muestra el cálculo en entry_superior
            entry_inferior.delete(0, tk.END)
            entry_inferior.insert(0, str(resultado))  # Actualiza entry_inferior con el resultado
        except ValueError:
            entry_superior.delete(0, tk.END)
            entry_superior.insert(0, "Error")

    def CE():
        global ultima_operacion  # Necesitamos controlar si ya se completó una operación
        if ultima_operacion:
            # Si ya se ha completado una operación con '=', limpiar ambas entradas
            entry_superior.delete(0, tk.END)
            entry_inferior.delete(0, tk.END)
            entry_inferior.insert(0, "0")
            ultima_operacion = False  # Restablece el estado de la operación
        else:
            # Si no se ha completado una operación, solo limpiar el entry_inferior
            entry_inferior.delete(0, tk.END)
            entry_inferior.insert(0, "0")

    def C():
        entry_superior.delete(0, tk.END)
        entry_inferior.delete(0, tk.END)
        entry_inferior.insert(0, "0")
        global valor_actual, operador_actual, ultima_operacion
        valor_actual = 0
        operador_actual = ""
        ultima_operacion = False

    def backspace():
        contenido = entry_inferior.get()
        if len(contenido) > 1:
            entry_inferior.delete(len(contenido)-1, tk.END)  # Borra el último carácter
        else:
            entry_inferior.delete(0, tk.END)
            entry_inferior.insert(0, "0")  # Si solo queda un carácter, lo reemplaza por 0
            
    def cambiar_signo():
            try:
                num = float(entry_inferior.get())
                resultado = -num  # Cambia el signo
                entry_inferior.delete(0, tk.END)
                entry_inferior.insert(0, str(resultado))  # Actualiza entry_inferior con el nuevo signo
            except ValueError:
                entry_superior.delete(0, tk.END)
                entry_superior.insert(0, "Error")
    
    def inversa():
        global ultima_operacion  # Para manejar el estado de la operación
        try:
            num = float(entry_inferior.get())
            if num != 0:
                resultado = 1 / num
                entry_superior.delete(0, tk.END)
                entry_superior.insert(0, f"1/{num}")  # Muestra como 1/número
                entry_inferior.delete(0, tk.END)
                entry_inferior.insert(0, str(resultado))  # Muestra el resultado en entry_inferior
                
                # Marca que se acaba de realizar una operación
                ultima_operacion = True  
            else:
                entry_superior.delete(0, tk.END)
                entry_superior.insert(0, "Error: 0 no es divisible")
        except ValueError:
            entry_superior.delete(0, tk.END)
            entry_superior.insert(0, "Error")

    def cuadrado():
        global ultima_operacion  # Para manejar el estado de la operación
        try:
            num = float(entry_inferior.get())
            resultado = num ** 2
            entry_superior.delete(0, tk.END)
            entry_superior.insert(0, f"({num})^2")  # Muestra como (número)^2
            entry_inferior.delete(0, tk.END)
            entry_inferior.insert(0, str(resultado))  # Muestra el resultado en entry_inferior
            
            ultima_operacion = True  # Marca que se acaba de realizar una operación
        except ValueError:
            entry_superior.delete(0, tk.END)
            entry_superior.insert(0, "Error")

    def raiz():
        global ultima_operacion  # Para que podamos manejar el estado de la operación
        try:
            num = float(entry_inferior.get())  # Obtiene el número actual en entry_inferior
            if num >= 0:
                resultado = num ** 0.5  # Calcula la raíz cuadrada
                entry_superior.delete(0, tk.END)
                entry_superior.insert(0, f"sqrt({num})")  # Muestra en entry_superior "sqrt(número)"
                entry_inferior.delete(0, tk.END)
                entry_inferior.insert(0, str(resultado))  # Muestra el resultado en entry_inferior

                ultima_operacion = True  # Marca que se acaba de realizar una operación

            else:
                entry_superior.delete(0, tk.END)
                entry_superior.insert(0, "Error: Raíz negativa")
        except ValueError:
            entry_superior.delete(0, tk.END)
            entry_superior.insert(0, "Error")

    def manejar_operador(operador):
        global valor_actual, operador_actual, ultima_operacion

        # Obtiene el número actual de entry_inferior y lo almacena en valor_actual
        if entry_inferior.get() != "0":
            try:
                num = float(entry_inferior.get())
                if operador_actual:  # Si ya hay un operador actual, realiza el cálculo
                    if operador_actual == "+":
                        valor_actual += num
                    elif operador_actual == "-":
                        valor_actual -= num
                    elif operador_actual == "*":
                        valor_actual *= num
                    elif operador_actual == "/":
                        if num != 0:
                            valor_actual /= num
                        else:
                            entry_superior.delete(0, tk.END)
                            entry_superior.insert(0, "Error: 0 no es divisible")
                            return
                else:
                    valor_actual = num  # Si no hay operador actual, simplemente toma el número

                # Actualiza entry_superior
                entry_superior.delete(0, tk.END)
                entry_superior.insert(0, f"{valor_actual} {operador}")  # Muestra el número actual y el operador
                entry_inferior.delete(0, tk.END)
                entry_inferior.insert(0, "0")  # Reinicia entry_inferior

                # Establece el operador actual
                operador_actual = operador
                ultima_operacion = False  # Marca que no se ha realizado una operación
            except ValueError:
                entry_superior.delete(0, tk.END)
                entry_superior.insert(0, "Error")

    def manejar_igual():
        global valor_actual, operador_actual, ultima_operacion  # Declarar como global
        try:
            num = float(entry_inferior.get())  # Obtiene el último número
            if operador_actual:
                # Realiza la operación correspondiente
                resultado = valor_actual  # Guardamos el valor actual para la operación en entry_superior
                if operador_actual == "+":
                    resultado += num
                elif operador_actual == "-":
                    resultado -= num
                elif operador_actual == "*":
                    resultado *= num
                elif operador_actual == "/":
                    if num != 0:
                        resultado /= num
                    else:
                        entry_superior.delete(0, tk.END)
                        entry_superior.insert(0, "Error: 0 no es divisible")
                        return

                # Muestra la operación original (no el resultado parcial) en entry_superior
                entry_superior.delete(0, tk.END)
                entry_superior.insert(0, f"{valor_actual} {operador_actual} {num} =")  # Mantiene el operando original

                # Muestra el resultado en entry_inferior
                entry_inferior.delete(0, tk.END)
                entry_inferior.insert(0, str(resultado))  # Muestra solo el resultado

                # Resetea el operador después de mostrar la operación completa
                operador_actual = ""
                valor_actual = resultado  # Actualiza valor_actual para acumulación de operaciones
                ultima_operacion = True

            else:
                entry_superior.delete(0, tk.END)
                entry_superior.insert(0, "Error: No hay operador")

        except ValueError:
            entry_superior.delete(0, tk.END)
            entry_superior.insert(0, "Error")

    # Funciones que se activan según el valor del botón presionado
    if valor in ['+', '-', '*', '/']:
        manejar_operador(valor)
    elif valor == '=':
        manejar_igual()
    elif valor == 'C':
        C()
    elif valor == 'CE':
        CE()
    elif valor == '⌫':
        backspace()
    elif valor == '%':
        porcentaje()
    elif valor == '1/x':
        inversa()
    elif valor == 'x²':
        cuadrado()
    elif valor == '²√x':
        raiz()
    elif valor == '+/-':
        cambiar_signo()  # Llama a la función de cambio de signo
    elif valor == '.':
        # Añadir un punto decimal solo si no hay uno ya presente
        if '.' not in entry_inferior.get():
            # Si el contenido es "0" o se ha realizado una operación anterior, limpiar antes de añadir el punto
            if entry_inferior.get() == "0" or ultima_operacion:
                entry_inferior.delete(0, tk.END)  # Elimina el 0 o el resultado anterior
                ultima_operacion = False
            entry_inferior.insert(tk.END, '.') 
    else:
        try:
            num = float(valor)  # Comprueba si es un número
            # Si entry_inferior tiene un 0 o acaba de realizarse una operación, sustituir el valor
            if entry_inferior.get() == "0" or ultima_operacion:
                entry_inferior.delete(0, tk.END)  # Elimina el contenido actual
                ultima_operacion = False  # Restablece el estado para próximas entradas

            entry_inferior.insert(tk.END, valor)  # Añade el número al final
        except ValueError:
            entry_superior.delete(0, tk.END)
            entry_superior.insert(0, "Error")
        
# Crear los botones usando el diccionario de estilo
btn_porcentaje = tk.Button(ventana, text="%", command=lambda: presionar('%'), **estilo_boton)
btn_porcentaje.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

btn_ce = tk.Button(ventana, text="CE", command=lambda: presionar('CE'), **estilo_boton)
btn_ce.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

btn_clear = tk.Button(ventana, text="C", command=lambda: presionar('C'), **estilo_boton)
btn_clear.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

btn_backspace = tk.Button(ventana, text="⌫", font=tamano_fuente, width=boton_ancho, height=boton_alto, command=lambda: presionar('⌫'), bg="#4affe9", fg="black", relief="flat", bd=0)
btn_backspace.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

btn_inversa = tk.Button(ventana, text="1/x",  command=lambda: presionar('1/x'), **estilo_boton)
btn_inversa.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

btn_cuadrado = tk.Button(ventana, text="x²",  command=lambda: presionar('x²'), **estilo_boton)
btn_cuadrado.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

btn_raiz = tk.Button(ventana, text="²√x",  command=lambda: presionar('²√x'), **estilo_boton)
btn_raiz.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

btn_dividir = tk.Button(ventana, text="÷",  command=lambda: presionar('/'), **estilo_boton)
btn_dividir.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

# Botones numéricos
btn_7 = tk.Button(ventana, text="7",  command=lambda: presionar('7'), **estilo_boton)
btn_7.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

btn_8 = tk.Button(ventana, text="8",  command=lambda: presionar('8'), **estilo_boton)
btn_8.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

btn_9 = tk.Button(ventana, text="9",  command=lambda: presionar('9'), **estilo_boton)
btn_9.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

btn_multiplicar = tk.Button(ventana, text="*",  command=lambda: presionar('*'), **estilo_boton)
btn_multiplicar.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

btn_4 = tk.Button(ventana, text="4",  command=lambda: presionar('4'), **estilo_boton)
btn_4.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

btn_5 = tk.Button(ventana, text="5",  command=lambda: presionar('5'), **estilo_boton)
btn_5.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

btn_6 = tk.Button(ventana, text="6",  command=lambda: presionar('6'), **estilo_boton)
btn_6.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

btn_restar = tk.Button(ventana, text="-",  command=lambda: presionar('-'), **estilo_boton)
btn_restar.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

btn_1 = tk.Button(ventana, text="1",  command=lambda: presionar('1'), **estilo_boton)
btn_1.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

btn_2 = tk.Button(ventana, text="2",  command=lambda: presionar('2'), **estilo_boton)
btn_2.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

btn_3 = tk.Button(ventana, text="3",  command=lambda: presionar('3'), **estilo_boton)
btn_3.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

btn_sumar = tk.Button(ventana, text="+",  command=lambda: presionar('+'), **estilo_boton)
btn_sumar.grid(row=6, column=3, padx=5, pady=5, sticky="nsew")

btn_masmenos = tk.Button(ventana, text="+/-",  command=lambda: presionar('+/-'), **estilo_boton)
btn_masmenos.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

btn_0 = tk.Button(ventana, text="0",  command=lambda: presionar('0'), **estilo_boton)
btn_0.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")

btn_punto = tk.Button(ventana, text=".",  command=lambda: presionar('.'), **estilo_boton)
btn_punto.grid(row=7, column=2, padx=5, pady=5, sticky="nsew")

btn_igual = tk.Button(ventana, text="=", font=tamano_fuente, width=boton_ancho, height=boton_alto, command=lambda: presionar('='), bg="#4affe9", fg="black", relief="flat", bd=0)
btn_igual.grid(row=7, column=3, padx=5, pady=5, sticky="nsew")

# Configurar las filas y columnas para que se expandan
for i in range(8):  # Para filas
    ventana.grid_rowconfigure(i, weight=1)

for j in range(4):  # Para columnas
    ventana.grid_columnconfigure(j, weight=1)

# Iniciar la ventana principal
ventana.mainloop()