'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        postulantes_nb_asp_js_ssr_25_40 = 0
        postulante_jr_menor_edad = None
        suma_edades_femenino = 0
        suma_edades_masculino = 0
        suma_edades_nb = 0
        cantidad_femenino = 0
        cantidad_masculino = 0
        cantidad_nb = 0
        cantidad_python = 0
        cantidad_js = 0
        cantidad_asp_net = 0

        for i in range(10):
            nombre = prompt("" , prompt="Ingrese el nombre del postulante:")
            if nombre is None:  # El usuario presionó Cancelar
                break

            edad = prompt("" , prompt="Ingrese la edad del postulante:")
            if edad is None:  # El usuario presionó Cancelar
                break
            edad = int(edad)

            genero = prompt("" , prompt="Ingrese el género del postulante (F-M-NB):")
            if genero is None:  # El usuario presionó Cancelar
                break

            tecnologia = prompt("" , prompt="Ingrese la tecnología del postulante (PYTHON - JS - ASP.NET):")
            if tecnologia is None:  # El usuario presionó Cancelar
                break

            puesto = prompt("" , prompt="Ingrese el puesto del postulante (Jr - Ssr - Sr):")
            if puesto is None:  # El usuario presionó Cancelar
                break

            if genero == "NB" and (tecnologia == "ASP.NET" or tecnologia == "JS") and 25 <= edad <= 40 and puesto == "Ssr":
                postulantes_nb_asp_js_ssr_25_40 += 1

            if puesto == "Jr":
                if postulante_jr_menor_edad is None or edad < postulante_jr_menor_edad[1]:
                    postulante_jr_menor_edad = (nombre, edad)

            if genero == "F":
                suma_edades_femenino += edad
                cantidad_femenino += 1
            elif genero == "M":
                suma_edades_masculino += edad
                cantidad_masculino += 1
            elif genero == "NB":
                suma_edades_nb += edad
                cantidad_nb += 1

            if tecnologia == "PYTHON":
                cantidad_python += 1
            elif tecnologia == "JS":
                cantidad_js += 1
            elif tecnologia == "ASP.NET":
                cantidad_asp_net += 1

        if cantidad_femenino > 0:
            promedio_edades_femenino = suma_edades_femenino / cantidad_femenino
        else:
            promedio_edades_femenino = 0

        if cantidad_masculino > 0:
            promedio_edades_masculino = suma_edades_masculino / cantidad_masculino
        else:
            promedio_edades_masculino = 0

        if cantidad_nb > 0:
            promedio_edades_nb = suma_edades_nb / cantidad_nb
        else:
            promedio_edades_nb = 0

        porcentaje_femenino = (cantidad_femenino / 10) * 100
        porcentaje_masculino = (cantidad_masculino / 10) * 100
        porcentaje_nb = (cantidad_nb / 10) * 100

        tecnologia_mas_postulantes = None
        cantidad_max_postulantes = 0

        if cantidad_python > cantidad_max_postulantes:
            tecnologia_mas_postulantes = "PYTHON"
            cantidad_max_postulantes = cantidad_python

        if cantidad_js > cantidad_max_postulantes:
            tecnologia_mas_postulantes = "JS"
            cantidad_max_postulantes = cantidad_js

        if cantidad_asp_net > cantidad_max_postulantes:
            tecnologia_mas_postulantes = "ASP.NET"
            cantidad_max_postulantes = cantidad_asp_net

        print("Resultados:")
        print("a. Cantidad de postulantes NB entre 25 y 40 años, que programan en ASP.NET o JS y se postulan para puesto Ssr:", postulantes_nb_asp_js_ssr_25_40)
        print("b. Nombre del postulante Jr con menor edad:", postulante_jr_menor_edad[0] if postulante_jr_menor_edad else "-")
        print("c. Promedio de edades por género:")
        print("   - Femenino:", promedio_edades_femenino)
        print("   - Masculino:", promedio_edades_masculino)
        print("   - NB:", promedio_edades_nb)
        print("d. Tecnología con más postulantes:", tecnologia_mas_postulantes)
        print("e. Porcentaje de postulantes por género:")
        print("   - Femenino:", porcentaje_femenino, "%")
        print("   - Masculino:", porcentaje_masculino, "%")
        print("   - NB:", porcentaje_nb, "%")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
