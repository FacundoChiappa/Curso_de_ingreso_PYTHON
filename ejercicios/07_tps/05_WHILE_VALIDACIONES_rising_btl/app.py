import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.simpledialog import askstring as prompt
import customtkinter


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
        apellido = self.txt_apellido.get()
        edad = self.txt_edad.get()
        estado_civil = self.combobox_tipo.get()
        legajo = self.txt_legajo.get()

        # Validación de datos
        if not apellido:
            alert("Error", "Debe ingresar el apellido.")
            return

        if not edad:
            alert("Error", "Debe ingresar la edad.")
            return
        try:
            edad = int(edad)
        except ValueError:
            alert("Error", "La edad debe ser un número entero.")
            return
        if edad < 18 or edad > 90:
            alert("Error", "La edad debe estar entre 18 y 90 años.")
            return

        if not estado_civil:
            alert("Error", "Debe seleccionar el estado civil.")
            return

        if not legajo:
            alert("Error", "Debe ingresar el número de legajo.")
            return
        try:
            legajo = int(legajo)
        except ValueError:
            alert("Error", "El número de legajo debe ser un número entero.")
            return
        if legajo < 1000 or legajo > 9999:
            alert("Error", "El número de legajo debe ser de 4 cifras (sin ceros a la izquierda).")
            return

        # Asignación a cuadros de texto
        self.txt_apellido.set_text(apellido)
        self.txt_edad.set_text(str(edad))
        self.combobox_tipo.set_text(estado_civil)
        self.txt_legajo.set_text(str(legajo))

        alert("Validación exitosa", "Los datos han sido validados y asignados correctamente.")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
