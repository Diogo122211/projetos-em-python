import random

todas_perguntas = [

    # ---------------- FÁCEIS ----------------

    {
        "pergunta": "Qual é a capital do Brasil?",
        "alternativas": [
            "São Paulo",
            "Brasília",
            "Rio de Janeiro",
            "Salvador"
        ],
        "resposta": "Brasília",
        "dificuldade": "Fácil"
    },

    {
        "pergunta": "Quanto é 7 x 8?",
        "alternativas": [
            "54",
            "56",
            "64",
            "48"
        ],
        "resposta": "56",
        "dificuldade": "Fácil"
    },

    {
        "pergunta": "Qual planeta é conhecido como planeta vermelho?",
        "alternativas": [
            "Marte",
            "Vênus",
            "Júpiter",
            "Saturno"
        ],
        "resposta": "Marte",
        "dificuldade": "Fácil"
    },

    {
        "pergunta": "Qual linguagem estamos usando no projeto?",
        "alternativas": [
            "Java",
            "Python",
            "C++",
            "PHP"
        ],
        "resposta": "Python",
        "dificuldade": "Fácil"
    },

    {
        "pergunta": "Qual animal é conhecido como rei da selva?",
        "alternativas": [
            "Tigre",
            "Leão",
            "Elefante",
            "Urso"
        ],
        "resposta": "Leão",
        "dificuldade": "Fácil"
    },

    {
        "pergunta": "Quantos lados tem um triângulo?",
        "alternativas": [
            "5",
            "4",
            "3",
            "6"
        ],
        "resposta": "3",
        "dificuldade": "Fácil"
    },

    {
        "pergunta": "Qual oceano banha o Brasil?",
        "alternativas": [
            "Pacífico",
            "Atlântico",
            "Índico",
            "Ártico"
        ],
        "resposta": "Atlântico",
        "dificuldade": "Fácil"
    },

    {
        "pergunta": "Qual é a cor formada pela mistura de azul e amarelo?",
        "alternativas": [
            "Verde",
            "Roxo",
            "Laranja",
            "Vermelho"
        ],
        "resposta": "Verde",
        "dificuldade": "Fácil"
    },

    {
        "pergunta": "Qual é o maior animal terrestre?",
        "alternativas": [
            "Girafa",
            "Elefante",
            "Hipopótamo",
            "Rinoceronte"
        ],
        "resposta": "Elefante",
        "dificuldade": "Fácil"
    },

    {
        "pergunta": "Qual estrela ilumina a Terra?",
        "alternativas": [
            "Lua",
            "Marte",
            "Sol",
            "Saturno"
        ],
        "resposta": "Sol",
        "dificuldade": "Fácil"
    },

    {
        "pergunta": "Qual é o resultado de 15 - 7?",
        "alternativas": [
            "6",
            "7",
            "8",
            "9"
        ],
        "resposta": "8",
        "dificuldade": "Fácil"
    },

    {
        "pergunta": "Qual instrumento é usado para escrever no quadro?",
        "alternativas": [
            "Pincel",
            "Caneta",
            "Giz",
            "Lápis"
        ],
        "resposta": "Giz",
        "dificuldade": "Fácil"
    },

    {
        "pergunta": "Qual é a primeira letra do alfabeto?",
        "alternativas": [
            "B",
            "C",
            "A",
            "D"
        ],
        "resposta": "A",
        "dificuldade": "Fácil"
    },

    # ---------------- MÉDIAS ----------------

    {
        "pergunta": "Quem pintou a Mona Lisa?",
        "alternativas": [
            "Van Gogh",
            "Picasso",
            "Leonardo da Vinci",
            "Michelangelo"
        ],
        "resposta": "Leonardo da Vinci",
        "dificuldade": "Médio"
    },

    {
        "pergunta": "Qual é o maior planeta do sistema solar?",
        "alternativas": [
            "Terra",
            "Júpiter",
            "Saturno",
            "Netuno"
        ],
        "resposta": "Júpiter",
        "dificuldade": "Médio"
    },

    {
        "pergunta": "Qual elemento químico possui símbolo O?",
        "alternativas": [
            "Ouro",
            "Oxigênio",
            "Prata",
            "Ósmio"
        ],
        "resposta": "Oxigênio",
        "dificuldade": "Médio"
    },

    {
        "pergunta": "Em que continente fica o Egito?",
        "alternativas": [
            "Europa",
            "Ásia",
            "África",
            "Oceania"
        ],
        "resposta": "África",
        "dificuldade": "Médio"
    },

    {
        "pergunta": "Qual empresa criou o Windows?",
        "alternativas": [
            "Apple",
            "Google",
            "Microsoft",
            "IBM"
        ],
        "resposta": "Microsoft",
        "dificuldade": "Médio"
    },

    {
        "pergunta": "Qual é a moeda oficial do Japão?",
        "alternativas": [
            "Won",
            "Yuan",
            "Iene",
            "Dólar"
        ],
        "resposta": "Iene",
        "dificuldade": "Médio"
    },

    {
        "pergunta": "Quantos jogadores um time de futebol possui em campo?",
        "alternativas": [
            "10",
            "11",
            "12",
            "9"
        ],
        "resposta": "11",
        "dificuldade": "Médio"
    },

    {
        "pergunta": "Quem escreveu Dom Casmurro?",
        "alternativas": [
            "Machado de Assis",
            "Clarice Lispector",
            "José de Alencar",
            "Paulo Coelho"
        ],
        "resposta": "Machado de Assis",
        "dificuldade": "Médio"
    },

    {
        "pergunta": "Qual linguagem é mais usada para desenvolvimento web no navegador?",
        "alternativas": [
            "Python",
            "JavaScript",
            "C",
            "Java"
        ],
        "resposta": "JavaScript",
        "dificuldade": "Médio"
    },

    {
        "pergunta": "Quem foi o primeiro homem a pisar na Lua?",
        "alternativas": [
            "Buzz Aldrin",
            "Neil Armstrong",
            "Yuri Gagarin",
            "Michael Collins"
        ],
        "resposta": "Neil Armstrong",
        "dificuldade": "Médio"
    },

    {
        "pergunta": "Qual é o maior oceano do planeta?",
        "alternativas": [
            "Atlântico",
            "Pacífico",
            "Índico",
            "Ártico"
        ],
        "resposta": "Pacífico",
        "dificuldade": "Médio"
    },

    {
        "pergunta": "Qual país é conhecido pela Torre Eiffel?",
        "alternativas": [
            "Itália",
            "Portugal",
            "França",
            "Alemanha"
        ],
        "resposta": "França",
        "dificuldade": "Médio"
    },

    {
        "pergunta": "Qual componente é considerado o cérebro do computador?",
        "alternativas": [
            "HD",
            "Memória RAM",
            "Processador",
            "Fonte"
        ],
        "resposta": "Processador",
        "dificuldade": "Médio"
    },

    # ---------------- DIFÍCEIS ----------------

    {
        "pergunta": "Qual é a velocidade aproximada da luz?",
        "alternativas": [
            "300 mil km/s",
            "150 mil km/s",
            "1 milhão km/s",
            "30 mil km/s"
        ],
        "resposta": "300 mil km/s",
        "dificuldade": "Difícil"
    },

    {
        "pergunta": "Quem desenvolveu a teoria da relatividade?",
        "alternativas": [
            "Newton",
            "Galileu",
            "Einstein",
            "Tesla"
        ],
        "resposta": "Einstein",
        "dificuldade": "Difícil"
    },

    {
        "pergunta": "Qual país venceu a Copa do Mundo de 2002?",
        "alternativas": [
            "Alemanha",
            "Brasil",
            "Argentina",
            "França"
        ],
        "resposta": "Brasil",
        "dificuldade": "Difícil"
    },

    {
        "pergunta": "Qual linguagem é usada para estilizar páginas web?",
        "alternativas": [
            "HTML",
            "Python",
            "CSS",
            "Java"
        ],
        "resposta": "CSS",
        "dificuldade": "Difícil"
    },

    {
        "pergunta": "Qual é o menor país do mundo?",
        "alternativas": [
            "Mônaco",
            "Vaticano",
            "Malta",
            "Luxemburgo"
        ],
        "resposta": "Vaticano",
        "dificuldade": "Difícil"
    },

    {
        "pergunta": "Qual estrutura de dados utiliza o conceito LIFO?",
        "alternativas": [
            "Fila",
            "Pilha",
            "Árvore",
            "Lista"
        ],
        "resposta": "Pilha",
        "dificuldade": "Difícil"
    },

    {
        "pergunta": "Qual cientista criou as leis da gravidade?",
        "alternativas": [
            "Einstein",
            "Galileu",
            "Newton",
            "Tesla"
        ],
        "resposta": "Newton",
        "dificuldade": "Difícil"
    },

    {
        "pergunta": "Qual comando em Python é usado para criar uma função?",
        "alternativas": [
            "func",
            "function",
            "define",
            "def"
        ],
        "resposta": "def",
        "dificuldade": "Difícil"
    },

    {
        "pergunta": "Qual país sediou a Copa do Mundo de 2014?",
        "alternativas": [
            "Alemanha",
            "Brasil",
            "Rússia",
            "África do Sul"
        ],
        "resposta": "Brasil",
        "dificuldade": "Difícil"
    },

    {
        "pergunta": "Qual é o símbolo químico da prata?",
        "alternativas": [
            "Pt",
            "Pr",
            "Ag",
            "Au"
        ],
        "resposta": "Ag",
        "dificuldade": "Difícil"
    }

]

def selecionar_perguntas():
    return random.sample(todas_perguntas, 10)