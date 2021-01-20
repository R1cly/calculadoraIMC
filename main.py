import tkinter as tk


class Ventana1:
    def __init__(self, master):
        self.master = master

        self.layout = tk.Label(self.master, bg="#70a1ff")


        #Input de la masa corporal.
        self.inputMasa = tk.Entry(self.master)

        #Input de la altura.
        self.inputAltura = tk.Entry(self.master,width="200")

        #Output del IMC.

        self.outputIMC = tk.Entry(self.master, bg="red")

        # Boton para calcular el IMC.
        self.calcularBoton = tk.Button(self.master,
                                text="Calcular IMC", bg="#7bed9f",
                                width="100", height="5", command=self.calculoIndiceMasaCorporal
                                )


        # Funcion Pack para que se vean todos los componentes de la Interfaz.
        self.inputAltura.pack()
        self.inputMasa.pack()
        self.outputIMC.pack()
        self.layout.pack()
        self.calcularBoton.pack(side="bottom")


    def calculoIndiceMasaCorporal(self):

        try:

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
    root.geometry("500x700")
    root.title("Calculadora IMC")

    app = Ventana1(root)

    # Incializando la ventana principal
    root.mainloop()

if __name__ == '__main__':

    mainWindow()
    print("")
