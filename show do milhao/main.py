import customtkinter as ctk
from tkinter import messagebox
from perguntas import selecionar_perguntas
import threading
import time

# ================= CONFIGURAÇÕES =================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1200x700")
app.title("Show do Milhão")

# ================= VARIÁVEIS =================

jogador = ""
pontuacao = 0
indice_pergunta = 0
tempo_restante = 45

valores = [
    1000,
    2000,
    5000,
    10000,
    20000,
    50000,
    100000,
    250000,
    500000,
    1000000
]

perguntas_jogo = selecionar_perguntas()

# ================= FUNÇÕES =================

def iniciar_jogo():

    global jogador

    nome = entrada_nome.get()

    if nome == "":
        messagebox.showwarning(
            "Aviso",
            "Digite seu nome!"
        )
        return

    jogador = nome

    tela_inicio.pack_forget()

    tela_jogo.pack(fill="both", expand=True)

    mostrar_pergunta()

    iniciar_timer()


def mostrar_pergunta():

    global tempo_restante

    tempo_restante = 45

    pergunta = perguntas_jogo[indice_pergunta]

    label_pergunta.configure(
        text=pergunta["pergunta"]
    )

    label_dificuldade.configure(
        text=f"Dificuldade: {pergunta['dificuldade']}"
    )

    label_numero.configure(
        text=f"Pergunta {indice_pergunta + 1} de 10"
    )

    label_premio.configure(
        text=f"Prêmio atual: R$ {pontuacao:,}".replace(",", ".")
    )

    proximo_valor = valores[indice_pergunta]

    label_risco.configure(
        text=f"""
Se parar agora: R$ {pontuacao:,}

Próxima pergunta vale:
R$ {proximo_valor:,}

Se errar: perde tudo
        """.replace(",", ".")
    )

    for i in range(4):

        botoes[i].configure(
            text=pergunta["alternativas"][i],
            fg_color="#1F6AA5"
        )

    atualizar_timer()


def verificar_resposta(resposta):

    global indice_pergunta
    global pontuacao

    pergunta = perguntas_jogo[indice_pergunta]

    correta = pergunta["resposta"]

    if resposta == correta:

        botoes_texto_verde()

        pontuacao = valores[indice_pergunta]

        label_feedback.configure(
            text="✅ RESPOSTA CORRETA!",
            text_color="#00FF88"
        )

        app.after(2000, proxima_pergunta)

    else:

        label_feedback.configure(
            text="❌ VOCÊ PERDEU TUDO!",
            text_color="red"
        )

        app.after(2500, fim_de_jogo)


def proxima_pergunta():

    global indice_pergunta

    indice_pergunta += 1

    label_feedback.configure(text="")

    if indice_pergunta >= 10:
        vitoria()
    else:
        mostrar_pergunta()


def vitoria():

    salvar_ranking()

    messagebox.showinfo(
        "PARABÉNS",
        f"""
VOCÊ GANHOU O JOGO!

Jogador: {jogador}

Prêmio:
R$ {pontuacao:,}
        """.replace(",", ".")
    )

    mostrar_ranking()

    app.destroy()


def fim_de_jogo():

    salvar_ranking()

    messagebox.showerror(
        "Fim de jogo",
        f"""
Jogador: {jogador}

Você saiu com:
R$ 0
        """
    )

    mostrar_ranking()

    app.destroy()


def desistir():

    salvar_ranking()

    messagebox.showinfo(
        "Desistiu",
        f"""
Você decidiu parar!

Prêmio:
R$ {pontuacao:,}
        """.replace(",", ".")
    )

    mostrar_ranking()

    app.destroy()


# ================= TIMER =================

def iniciar_timer():

    def contar():

        global tempo_restante

        while tempo_restante > 0:

            time.sleep(1)

            tempo_restante -= 1

            atualizar_timer()

        if tempo_restante == 0:

            label_feedback.configure(
                text="⏰ TEMPO ESGOTADO!",
                text_color="orange"
            )

            app.after(2000, fim_de_jogo)

    thread = threading.Thread(target=contar)

    thread.daemon = True

    thread.start()


def atualizar_timer():

    label_timer.configure(
        text=f"⏳ {tempo_restante}s"
    )


# ================= EFEITOS =================

def botoes_texto_verde():

    correta = perguntas_jogo[indice_pergunta]["resposta"]

    for botao in botoes:

        if botao.cget("text") == correta:

            botao.configure(
                fg_color="green"
            )


# ================= RANKING =================

def salvar_ranking():

    with open("ranking.txt", "a", encoding="utf-8") as arquivo:

        arquivo.write(
            f"{jogador} - R$ {pontuacao}\n"
        )


def mostrar_ranking():

    try:

        with open("ranking.txt", "r", encoding="utf-8") as arquivo:

            ranking = arquivo.read()

            messagebox.showinfo(
                "RANKING",
                ranking
            )

    except:

        pass


# ================= TELA INICIAL =================

tela_inicio = ctk.CTkFrame(app)

tela_inicio.pack(fill="both", expand=True)

titulo = ctk.CTkLabel(
    tela_inicio,
    text="SHOW DO MILHÃO",
    font=("Arial", 48, "bold")
)

titulo.pack(pady=60)

subtitulo = ctk.CTkLabel(
    tela_inicio,
    text="Digite seu nome para começar",
    font=("Arial", 22)
)

subtitulo.pack(pady=20)

entrada_nome = ctk.CTkEntry(
    tela_inicio,
    width=400,
    height=50,
    font=("Arial", 20),
    placeholder_text="Seu nome"
)

entrada_nome.pack(pady=20)

botao_iniciar = ctk.CTkButton(
    tela_inicio,
    text="COMEÇAR",
    width=300,
    height=60,
    font=("Arial", 24, "bold"),
    command=iniciar_jogo
)

botao_iniciar.pack(pady=40)

# ================= TELA JOGO =================

tela_jogo = ctk.CTkFrame(app)

topo = ctk.CTkFrame(
    tela_jogo,
    height=100
)

topo.pack(fill="x", padx=20, pady=20)

label_numero = ctk.CTkLabel(
    topo,
    text="",
    font=("Arial", 20)
)

label_numero.pack(side="left", padx=20)

label_timer = ctk.CTkLabel(
    topo,
    text="45s",
    font=("Arial", 28, "bold"),
    text_color="#FFD700"
)

label_timer.pack(side="right", padx=20)

label_premio = ctk.CTkLabel(
    tela_jogo,
    text="",
    font=("Arial", 28, "bold"),
    text_color="#00FF88"
)

label_premio.pack(pady=10)

label_dificuldade = ctk.CTkLabel(
    tela_jogo,
    text="",
    font=("Arial", 20),
    text_color="#FFD700"
)

label_dificuldade.pack()

label_pergunta = ctk.CTkLabel(
    tela_jogo,
    text="",
    font=("Arial", 30, "bold"),
    wraplength=900,
    justify="center"
)

label_pergunta.pack(pady=40)

frame_botoes = ctk.CTkFrame(
    tela_jogo,
    fg_color="transparent"
)

frame_botoes.pack(pady=20)

botoes = []

for i in range(4):

    botao = ctk.CTkButton(
        frame_botoes,
        text="",
        width=500,
        height=65,
        font=("Arial", 20),
        corner_radius=15,
        command=lambda i=i: verificar_resposta(
            botoes[i].cget("text")
        )
    )

    botao.pack(pady=12)

    botoes.append(botao)

label_feedback = ctk.CTkLabel(
    tela_jogo,
    text="",
    font=("Arial", 26, "bold")
)

label_feedback.pack(pady=20)

label_risco = ctk.CTkLabel(
    tela_jogo,
    text="",
    font=("Arial", 18),
    justify="center"
)

label_risco.pack(pady=10)
# ================= CARDS DE DECISÃO =================

frame_decisao = ctk.CTkFrame(
    tela_jogo,
    fg_color="transparent"
)

frame_decisao.pack(pady=30)

# ===== CARD PARAR =====

card_parar = ctk.CTkFrame(
    frame_decisao,
    width=280,
    height=180,
    corner_radius=20,
    fg_color="#1E293B"
)

card_parar.pack(
    side="left",
    padx=20
)

card_parar.pack_propagate(False)

titulo_parar = ctk.CTkLabel(
    card_parar,
    text="PARAR AGORA",
    font=("Arial", 24, "bold"),
    text_color="#FFD700"
)

titulo_parar.pack(pady=(20,10))

texto_parar = ctk.CTkLabel(
    card_parar,
    text="""
Ficar com o
prêmio atual
    """,
    font=("Arial", 18),
    justify="center"
)

texto_parar.pack()

botao_parar = ctk.CTkButton(
    card_parar,
    text="PARAR",
    width=180,
    height=45,
    fg_color="#D97706",
    hover_color="#F59E0B",
    font=("Arial", 18, "bold"),
    command=desistir
)

botao_parar.pack(pady=15)

# ===== CARD CONTINUAR =====

card_continuar = ctk.CTkFrame(
    frame_decisao,
    width=280,
    height=180,
    corner_radius=20,
    fg_color="#1E293B"
)

card_continuar.pack(
    side="left",
    padx=20
)

card_continuar.pack_propagate(False)

titulo_continuar = ctk.CTkLabel(
    card_continuar,
    text="CONTINUAR",
    font=("Arial", 24, "bold"),
    text_color="#00FF88"
)

titulo_continuar.pack(pady=(20,10))

texto_continuar = ctk.CTkLabel(
    card_continuar,
    text="""
Responder a próxima

Se errar:
PERDE TUDO
    """,
    font=("Arial", 18),
    justify="center",
    text_color="#FF5555"
)

texto_continuar.pack()

botao_continuar = ctk.CTkButton(
    card_continuar,
    text="JOGAR",
    width=180,
    height=45,
    fg_color="#15803D",
    hover_color="#16A34A",
    font=("Arial", 18, "bold")
)

botao_continuar.pack(pady=15)

# ================= INICIAR =================

app.mainloop()