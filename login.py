import tkinter as tk
from tkinter import ttk, messagebox

class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        #ventana principal
        self.geometry('300x130')
        self.title('Login')
        self.configure(bg='white')
        self.resizable(width=False, height=False)

        # configuracion del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # Creamos los componentes
        self._crear_componentes()
    # Definir el metodo crear_componentes
    def _crear_componentes(self):
        # usuario
        usuario_etiqueta = ttk.Label(self, text='Usuario: ')
        usuario_etiqueta.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        usuario_etiqueta.configure(background='white')
        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        # password
        password_etiqueta = ttk.Label(self, text='Password: ')
        password_etiqueta.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        password_etiqueta.configure(background='white')
        self.password_entrada = ttk.Entry(self, show='*')
        self.password_entrada.grid(row=1, column=1, padx=5, pady=20, sticky=tk.W)

        # boton Login
        login_boton = ttk.Button(self, text='Login', command=self._login)
        login_boton.grid(row=3, column=0, columnspan=2)

    def _login(self):
        messagebox.showinfo('Datos Login',
                            f'usuario: {self.usuario_entrada.get()}, Password: {self.password_entrada.get()}')


if __name__ == '__main__':
    login_ventana = Login()
    login_ventana.mainloop()