import tkinter as tk

def menu_admin(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    tk.Label(janela, text="MENU ADMIN", font=("Segoe UI", 18)).pack(pady=20)

    tk.Button(janela, text="Gerenciar Alunos").pack(pady=10)
    tk.Button(janela, text="Sair", command=janela.quit).pack(pady=20)