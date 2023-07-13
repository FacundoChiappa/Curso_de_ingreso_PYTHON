import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

    # Facundo Chiappa

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.txt_numero = customtkinter.CTkEntry(master=self)
        self.txt_numero.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.numero_secreto = random.randrange(1, 100)
        self.numero_intento = 0
        print(self.numero_secreto)

    def btn_mostrar_on_click(self):
        numero_ingresado = int(self.txt_numero.get())
        self.numero_intento += 1
        Titulo= "Perdiste , "

        if numero_ingresado == self.numero_secreto:
            Titulo = "Felicidades , "
            match(self.numero_intento):
                case 1:
                    mensaje=f"{Titulo} Usted es un Psíquico."
                case 2:
                    mensaje=f"{Titulo}Excelente percepción."
                case 3:
                    mensaje=f"{Titulo}Esto es suerte."
                case 4 | 5 | 6:
                    mensaje=f"{Titulo}Excelente técnica."
                case _:
                    mensaje=f"{Titulo}Afortunado en el amor!!"
        elif numero_ingresado < self.numero_secreto:
            mensaje=f"{Titulo}Falta..."
        else:
            mensaje=f"{Titulo}Te pasaste..."
        
        self.txt_numero.delete(0 , 1000)
        alert("" , mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
