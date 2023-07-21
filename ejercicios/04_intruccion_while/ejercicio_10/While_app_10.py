import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_negativos = 0
        suma_positivos = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0

        while True:
            numero = prompt("" , "Ingrese un número (Cancelar para terminar):")

            if numero is None:
                break

            numero = float(numero)

            if numero > 0:
                suma_positivos += numero
                cantidad_positivos += 1
            elif numero < 0:
                suma_negativos += numero
                cantidad_negativos += 1
            else:
                cantidad_ceros += 1

        diferencia = abs(cantidad_positivos - cantidad_negativos)  #ABS DA VALOR ABSOLUTO, LO QUE PASO X PARENTESIS, DEVUELVE SIN SIGNO OSEA POSITIVO

        mensaje = f"Suma acumulada de negativos: {suma_negativos}\n"
        mensaje += f"Suma acumulada de positivos: {suma_positivos}\n"
        mensaje += f"Cantidad de números positivos ingresados: {cantidad_positivos}\n"
        mensaje += f"Cantidad de números negativos ingresados: {cantidad_negativos}\n"
        mensaje += f"Cantidad de ceros: {cantidad_ceros}\n"
        mensaje += f"Diferencia entre la cantidad de positivos y negativos: {diferencia}"

        alert("Resultados", mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
