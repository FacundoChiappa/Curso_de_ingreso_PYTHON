'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        # Variables para almacenar los resultados
        candidato_mas_votos = None
        candidato_menos_votos = None
        menor_votos = float('inf')
        total_votos = 0
        suma_edades = 0
        cantidad_candidatos = 0

        while True:
            nombre = prompt("Ingrese el nombre del candidato:")
            if nombre is None:  # El usuario presionó Cancelar
                break

            edad = prompt("Ingrese la edad del candidato:")
            if edad is None:  # El usuario presionó Cancelar
                break
            edad = int(edad)

            if edad <= 25:
                alert("Error", "La edad debe ser mayor a 25.")
                continue

            votos = prompt("Ingrese la cantidad de votos del candidato:")
            if votos is None:  # El usuario presionó Cancelar
                break
            votos = int(votos)

            if votos < 0:
                alert("Error", "La cantidad de votos no puede ser menor a cero.")
                continue

            total_votos += votos
            suma_edades += edad
            cantidad_candidatos += 1

            if votos > candidato_mas_votos:
                candidato_mas_votos = votos
            if votos < menor_votos:
                candidato_menos_votos = (nombre, edad)
                menor_votos = votos

        if cantidad_candidatos > 0:
            promedio_edades = suma_edades / cantidad_candidatos
        else:
            promedio_edades = 0

        print("Resultados:")
        print("a. Candidato con más votos:", candidato_mas_votos)
        print("b. Candidato con menos votos:", candidato_menos_votos)
        print("c. Promedio de edades de los candidatos:", promedio_edades)
        print("d. Total de votos emitidos:", total_votos)




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
