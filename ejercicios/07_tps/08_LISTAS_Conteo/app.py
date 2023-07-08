import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        while True:
            numero = prompt("" , prompt="Ingrese un número:")
            if numero is None:  # El usuario presionó Cancelar
                break
            try:
                numero = float(numero)
                self.lista.append(numero)
            except ValueError:
                alert("Error", "Ingrese un número válido.")

    def btn_mostrar_estadisticas_on_click(self):
        suma_negativos = 0
        suma_positivos = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0
        minimo_negativos = float('inf')
        maximo_positivos = float('-inf')
        promedio_negativos = 0

        for numero in self.lista:
            if numero < 0:
                suma_negativos += numero
                cantidad_negativos += 1
                if numero < minimo_negativos:
                    minimo_negativos = numero
            elif numero > 0:
                suma_positivos += numero
                cantidad_positivos += 1
                if numero > maximo_positivos:
                    maximo_positivos = numero
            else:
                cantidad_ceros += 1

        if cantidad_negativos > 0:
            promedio_negativos = suma_negativos / cantidad_negativos

        estadisticas = f'''
        Suma acumulada de los negativos: {suma_negativos}
        Suma acumulada de los positivos: {suma_positivos}
        Cantidad de números positivos ingresados: {cantidad_positivos}
        Cantidad de números negativos ingresados: {cantidad_negativos}
        Cantidad de ceros: {cantidad_ceros}
        Mínimo de los negativos: {minimo_negativos if cantidad_negativos > 0 else 'N/A'}
        Máximo de los positivos: {maximo_positivos if cantidad_positivos > 0 else 'N/A'}
        Promedio de los negativos: {promedio_negativos if cantidad_negativos > 0 else 'N/A'}
        '''

        alert("Estadísticas", estadisticas)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
