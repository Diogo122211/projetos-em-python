import tkinter as tk
from database import get_connection
from gui_admin import menu_admin
from gui_aluno import menu_alunos

def verificar_login(email, senha):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT perfil FROM usuarios WHERE email=? AND senha=?",
            (email, senha)
        )
        resultado = cursor.fetchone()

        if resultado:
            return {"perfil": resultado[0]}
        return None


def tela_login_gui():
    resultado = {"usuario": None}

    def fazer_login():
        email = entry_email.get()
        senha = entry_senha.get()

        usuario = verificar_login(email, senha)

        if usuario:
            resultado["usuario"] = usuario
            
            if usuario["perfil"] == "admin":
              menu_admin(janela)
              
            if usuario["perfil"] == "aluno":
                  menu_alunos(janela)
           
        else:
            label_erro.config(text="Email ou senha inválidos")

    janela = tk.Tk()
    janela.title("Login - Faculdade")
    janela.geometry("600x300")
    janela.resizable(False, False)

    imagem = tk.PhotoImage(file="assets/logo.png")

    label_img = tk.Label(janela, image=imagem)
    label_img.image = imagem
    label_img.pack(pady=10)

    tk.Label(janela, text="Email", font=("Arial", 13)).pack()
    entry_email = tk.Entry(janela)
    entry_email.pack()

    tk.Label(janela, text="Senha", font=("Arial", 13)).pack()
    entry_senha = tk.Entry(janela, show="*")
    entry_senha.pack()

    tk.Button(janela, text="Entrar", command=fazer_login).pack(pady=10)

    label_erro = tk.Label(janela, text="", fg="red")
    label_erro.pack()

    janela.mainloop()
    
    

    return resultado["usuario"]

