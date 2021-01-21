import tkinter as tk


class Ventana1:
    def __init__(self, master):
        self.master = master

        self.layout = tk.Frame(self.master, bg="#70a1ff")

        self.textMasa = tk.Label(self.layout,text="Input masa",border="5",
                                 bg="#70a1ff")

        self.textAltura = tk.Label(self.layout,text="Input altura(cm)", bg="#70a1ff")

        self.textIMC = tk.Label(self.layout,text="Output IMC", bg="#70a1ff")

        # Input de la masa corporal.
        self.inputMasa = tk.Entry(self.layout)

        # Input de la altura.
        self.inputAltura = tk.Entry(self.layout)

        # Output del IMC.

        self.outputIMC = tk.Entry(self.layout)

        # Boton para calcular el IMC.
        self.calcularBoton = tk.Button(self.layout,
                                text="Calcular IMC", bg="#7bed9f",
                                width="100", height="5", command=self.calculoIndiceMasaCorporal
                                )


        # Funcion Pack para que se vean todos los componentes de la Interfaz.
        self.textAltura.pack()
        self.inputAltura.pack(pady="5")

        self.textMasa.pack()
        self.inputMasa.pack(pady="5")


        self.textIMC.pack()
        self.outputIMC.pack(pady="5")



        self.layout.pack()
        self.calcularBoton.pack(side="bottom")


    def calculoIndiceMasaCorporal(self):

        try:
            self.outputIMC.delete(0,"end")
            # Comprobacion de que el usuario no esta metiendo los datos en cm.
            self.altura = float(self.inputAltura.get())

            if self.altura > 4:

                self.altura = self.altura / 100

            #Introducimos la masa del usuario.

            self.masa = float(self.inputMasa.get())

            # Calculo del IMC final.
            self.calcularIMC = float(self.masa / (self.altura*self.altura))

            print(self.calcularIMC)

            self.outputIMC.insert(0,self.calcularIMC)

        except:

            #Exepcion que nos devuelve a la pagina principal
            print("Datos incorrectos vuelve a intentarlo!")


def mainWindow():

    # Creando la ventana principal con sus parametros.
    root = tk.Tk()
    root.geometry("300x240")
    root.title("Calculadora IMC")

    app = Ventana1(root)

    # Incializando la ventana principal
    root.mainloop()


if __name__ == '__main__':

    mainWindow()

