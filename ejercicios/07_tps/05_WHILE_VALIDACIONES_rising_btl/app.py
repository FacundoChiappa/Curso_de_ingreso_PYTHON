import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.simpledialog import askstring as prompt
import customtkinter

#Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada por ventanas emergentes solamente (dialog prompt) y luego asignarla a cuadros de textos.

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        validado = False
        while not validado:
            apellido = prompt("" , "Ingrese el apellido:")
            edad = prompt("" ,"Ingrese la edad:")
            estado = self.combobox_tipo.get()
            legajo = prompt("" , "Ingrese el legajo:")

            if apellido and edad and estado and legajo:
                if not edad.isdigit() or int(edad) < 18 or int(edad) > 90:
                    alert("Error", "La edad debe ser un número entre 18 y 90.")
                elif not legajo.isdigit() or len(legajo) != 4 or legajo.startswith('0'):
                    alert("Error", "El número de legajo debe ser numérico de 4 cifras sin ceros a la izquierda.")
                else:
                    self.txt_apellido.delete(0 , "end")
                    self.txt_apellido.insert(0 , apellido)
                    self.txt_edad.delete(0 , "end")
                    self.txt_edad.insert(0 , edad)
                    self.txt_legajo.delete(0 , "end")
                    self.txt_legajo.insert(0 ,legajo)
                    validado = True
            else:
                alert("Error", "Todos los campos son requeridos.")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
