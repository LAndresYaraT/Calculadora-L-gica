import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from truth_table_parser import TruthTableParser
from truth_table_verifier import TruthTableVerifier

class CalculadoraLogicaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Tablas de Verdad")
        self.root.geometry("350x550")
        self.root.configure(bg="#1e1e1e")  # Fondo oscuro

        self.parser = TruthTableParser()
        self.verifier = TruthTableVerifier()

        # === Pantalla superior ===
        self.display = tk.Entry(root, font=("Consolas", 20), justify="right",
                                bg="#2d2d2d", fg="white", insertbackground="white", relief="flat")
        self.display.pack(fill="x", padx=10, pady=(20, 10), ipady=10)

        # === Marco de botones (como una cuadrícula) ===
        frame = tk.Frame(root, bg="#1e1e1e")
        frame.pack(padx=10, pady=10)

        # Botones estilo calculadora
        botones = [
            ["¬", "∧", "∨", "⊕"],
            ["→", "↔", "(", ")"],
            ["p", "q", "r", "s"],
            ["Borrar", "Analizar", "Tabla", "="]
        ]

        for r, fila in enumerate(botones):
            for c, texto in enumerate(fila):
                b = tk.Button(frame, text=texto, font=("Segoe UI", 12, "bold"),
                              bg="#2d2d2d", fg="white", activebackground="#3e3e3e",
                              activeforeground="white", width=7, height=2,
                              relief="flat", command=lambda t=texto: self.click(t))
                b.grid(row=r, column=c, padx=5, pady=5)

        # === Área de resultados ===
        self.text_output = tk.Text(root, wrap="word", height=10,
                                   bg="#252526", fg="white", insertbackground="white",
                                   font=("Consolas", 11), relief="flat")
        self.text_output.pack(padx=10, pady=10, fill="both", expand=True)

    def click(self, texto):
        if texto == "Borrar":
            self.display.delete(0, tk.END)
            self.text_output.delete("1.0", tk.END)
        elif texto == "=":
            expr = self.display.get().strip()
            if expr:
                self.analizar_rapido(expr)
        elif texto == "Analizar":
            self.analizar()
        elif texto == "Tabla":
            self.mostrar_tabla()
        else:
            self.display.insert(tk.END, texto)

    def mostrar_tabla(self):
        expr = self.display.get().strip()
        if not expr:
            messagebox.showwarning("Atención", "Ingresa una expresión lógica.")
            return
        table = self.parser.generate_truth_table(expr)
        self.text_output.delete("1.0", tk.END)
        header = " | ".join(table[0]) + "\n" + "-" * 40 + "\n"
        self.text_output.insert(tk.END, header)
        for row in table[1:]:
            formatted = " | ".join(str(int(v)) if isinstance(v, bool) else str(v) for v in row)
            self.text_output.insert(tk.END, formatted + "\n")

    def analizar_rapido(self, expr):
        self.text_output.delete("1.0", tk.END)
        if self.verifier.verify_tautology(expr):
            self.text_output.insert(tk.END, "✓ Es una TAUTOLOGÍA (siempre verdadera)\n")
        elif self.verifier.verify_contradiction(expr):
            self.text_output.insert(tk.END, "✗ Es una CONTRADICCIÓN (siempre falsa)\n")
        else:
            self.text_output.insert(tk.END, "○ Es una CONTINGENCIA (depende de los valores)\n")

    def analizar(self):
        expr = self.display.get().strip()
        if not expr:
            messagebox.showwarning("Atención", "Ingresa una expresión lógica.")
            return
        expr2 = simpledialog.askstring("Equivalencia", "Ingresa la segunda expresión:")
        if not expr2:
            return
        eq = self.verifier.verify_equivalence(expr, expr2)
        msg = f"¿'{expr}' es equivalente a '{expr2}'? {'Sí' if eq else 'No'}"
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraLogicaGUI(root)
    root.mainloop()
