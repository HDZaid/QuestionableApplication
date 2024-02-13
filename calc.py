import tkinter as tk
from tkinter import ttk
import numpy as np

class LinearAlgebraCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Álgebra Lineal")

        # Configuración del fondo azul
        master.configure(bg='#3498db')

        # Configuración de la fuente Bubblegum para toda la aplicación
        bubblegum_font = ('Bubblegum', 12)
        master.option_add("*Font", bubblegum_font)

        self.matrix_label = tk.Label(master, text="Ingrese la matriz (separe las filas con ';'):", bg='#3498db', fg='white')
        self.matrix_label.pack(pady=10)

        self.matrix_entry = tk.Entry(master, width=50)
        self.matrix_entry.pack(pady=10)

        self.operation_label = tk.Label(master, text="Seleccione la operación:", bg='#3498db', fg='white')
        self.operation_label.pack(pady=10)

        self.operation_var = tk.StringVar()
        operations = ["Suma", "Resta", "Multiplicación", "Transpuesta", "Determinante"]
        self.operation_dropdown = ttk.Combobox(master, textvariable=self.operation_var, values=operations)
        self.operation_dropdown.pack(pady=10)

        # Configuración del botón con color rojo oscuro y bordes redondeados
        style = ttk.Style()
        style.configure('TButton', foreground='white', background='#c0392b', font=bubblegum_font)
        self.calculate_button = ttk.Button(master, text="Calcular", command=self.calculate_result, style='TButton')
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", bg='#3498db', fg='white', font=bubblegum_font)
        self.result_label.pack(pady=10)

    def calculate_result(self):
        matrix_str = self.matrix_entry.get()
        operation = self.operation_var.get()

        try:
            # Parsear la entrada de la matriz
            matrix = np.matrix([row.split() for row in matrix_str.split(';')], dtype=float)

            # Realizar la operación seleccionada
            result = None
            if operation == "Suma":
                result = np.sum(matrix, axis=0)
            elif operation == "Resta":
                result = np.subtract(matrix[0], matrix[1])
            elif operation == "Multiplicación":
                result = np.dot(matrix[0], matrix[1].transpose())
            elif operation == "Transpuesta":
                result = matrix.transpose()
            elif operation == "Determinante":
                result = np.linalg.det(matrix)

            # Mostrar el resultado
            result_text = f"Resultado de {operation}:\n{result}"
            self.result_label.config(text=result_text)

        except Exception as e:
            self.result_label.config(text="Error al realizar la operación. Verifica la entrada.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LinearAlgebraCalculatorApp(root)
    root.mainloop()
