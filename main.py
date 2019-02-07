from tkinter import *
from tkinter import ttk

class Contador(ttk.Frame):
    __valor = 0

    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height=args['height'], width=args['width'])

        self.__label = ttk.Label(self, width=4, font=('Helvetica', 16), text=str(self.__valor))
        self.__label.place(x=168, y=80)
        self.__btnDown = ttk.Button(self, width=3, text="-", command=self._down)
        self.__btnDown.place(x=70,y=250)
        self.__btnUp = ttk.Button(self, width=3, text="+", command=self._up)
        self.__btnUp.place(x=330, y=250)

    def _up(self):
        self.__valor+=1
        self.__label.config(text=str(self.__valor))

    def _down(self):
        self.__valor-=1
        self.__label.config(text=str(self.__valor))




class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Ventana con un contador")
        self.geometry("800x600")

        for c in range(2):
            for f in range(2):
                contador = Contador(self, height=300, width=400)
                contador.place(x=400*c, y=300*f)

    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()