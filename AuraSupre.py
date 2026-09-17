import flet as aura
import random


def main(pagina: aura.Page):
    pagina.title = "jojodle"

    # =====================================
    # Dados salvos externos
    # =====================================

    GENERO = [
        "homem",
        "mulher",
        "Animal",
    ]

    TIPODEHABILIDADE = [
        "Stands de Curto Alcance",
        "Stands de Longo Alcance",
        "Stands Automáticos",
        "Stands com Alcance Irrelevante",
        "Stands Materializados",
        "Stands de Ataque Psicológico",
        "Stands de Precognição",
        "Stands de Reconhecimento",
        "Stands Colônia",
        "Stands Evoluídos",
        "Stands Conscientes",
        "Stands Compartilhados",
    ]

    TIPODEFORMA = [
        "Stands Humanoides Naturais",
        "Stands Humanoides Artificiais",
        "Stands Não Humanoides Naturais",
        "Stands Não Humanoides Artificiais",
    ]

    AFILIAÇÃO = [
        "sem afiliação",
        "Passione",
        "grupo joestar",
        "familia do dio",
        "agente do dio",
    ]

    PARTES = [
        "Phantom Blood",
        "Battle Tendency",
        "Stardust Crusaders",
        "Diamond is Unbreakable",
        "Vento Aureo",
        "Stone Ocean",
    ]

    LADO = [
        "Aliados",
        "Inimigos",
    ]

    # =====================================
    # DADOS DOS PERSONAGENS
    # =====================================

    PERSONAGENS = [

        # ======================================
        # PARTE 3 - STARDUST CRUSADERS
        # ======================================

        {
            "nome": "Jotaro Kujo",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance",
                "Stands Conscientes"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Stardust Crusaders",
            "lado": "Aliados"
        },

        {
            "nome": "Joseph Joestar",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Longo Alcance",
                "Stands de Reconhecimento"
            ],
            "tipo_de_forma": "Stands Não Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Stardust Crusaders",
            "lado": "Aliados"
        },

        {
            "nome": "Muhammad Avdol",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Longo Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Stardust Crusaders",
            "lado": "Aliados"
        },

        {
            "nome": "Noriaki Kakyoin",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Longo Alcance",
                "Stands de Reconhecimento"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Stardust Crusaders",
            "lado": "Aliados"
        },

        {
            "nome": "Jean Pierre Polnareff",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Stardust Crusaders",
            "lado": "Aliados"
        },

        {
            "nome": "Iggy",
            "genero": "Animal",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance",
                "Stands Materializados"
            ],
            "tipo_de_forma": "Stands Não Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Stardust Crusaders",
            "lado": "Aliados"
        },

        {
            "nome": "DIO",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance",
                "Stands Conscientes"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "agente do dio",
            "parte": "Stardust Crusaders",
            "lado": "Inimigos"
        },

        {
            "nome": "Hol Horse",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Longo Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "agente do dio",
            "parte": "Stardust Crusaders",
            "lado": "Inimigos"
        },

        {
            "nome": "Vanilla Ice",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "agente do dio",
            "parte": "Stardust Crusaders",
            "lado": "Inimigos"
        },

        {
            "nome": "N'Doul",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Longo Alcance",
                "Stands de Reconhecimento"
            ],
            "tipo_de_forma": "Stands Não Humanoides Naturais",
            "afiliacao": "agente do dio",
            "parte": "Stardust Crusaders",
            "lado": "Inimigos"
        },

        # ======================================
        # PARTE 4 - DIAMOND IS UNBREAKABLE
        # ======================================

        {
            "nome": "Josuke Higashikata",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Diamond is Unbreakable",
            "lado": "Aliados"
        },

        {
            "nome": "Okuyasu Nijimura",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Diamond is Unbreakable",
            "lado": "Aliados"
        },

        {
            "nome": "Koichi Hirose",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance",
                "Stands Evoluídos"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Diamond is Unbreakable",
            "lado": "Aliados"
        },

        {
            "nome": "Rohan Kishibe",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance",
                "Stands de Ataque Psicológico"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "sem afiliação",
            "parte": "Diamond is Unbreakable",
            "lado": "Aliados"
        },

        {
            "nome": "Shigekiyo Yangu",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands Colônia",
                "Stands de Longo Alcance"
            ],
            "tipo_de_forma": "Stands Não Humanoides Naturais",
            "afiliacao": "sem afiliação",
            "parte": "Diamond is Unbreakable",
            "lado": "Aliados"
        },

        {
            "nome": "Yukako Yamagishi",
            "genero": "mulher",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "sem afiliação",
            "parte": "Diamond is Unbreakable",
            "lado": "Aliados"
        },


        {
            "nome": "Yoshikage Kira",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance",
                "Stands Evoluídos"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "sem afiliação",
            "parte": "Diamond is Unbreakable",
            "lado": "Inimigos"
        },

        {
            "nome": "Keicho Nijimura",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands Colônia",
                "Stands de Longo Alcance"
            ],
            "tipo_de_forma": "Stands Não Humanoides Naturais",
            "afiliacao": "sem afiliação",
            "parte": "Diamond is Unbreakable",
            "lado": "Inimigos"
        },

        {
            "nome": "Tonio Trussardi",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Não Humanoides Naturais",
            "afiliacao": "sem afiliação",
            "parte": "Diamond is Unbreakable",
            "lado": "Aliados"
        },

        # ======================================
        # PARTE 5 - VENTO AUREO
        # ======================================

        {
            "nome": "Giorno Giovanna",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance",
                "Stands Evoluídos"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "Passione",
            "parte": "Vento Aureo",
            "lado": "Aliados"
        },

        {
            "nome": "Bruno Bucciarati",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "Passione",
            "parte": "Vento Aureo",
            "lado": "Aliados"
        },

        {
            "nome": "Guido Mista",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Longo Alcance",
                "Stands Colônia"
            ],
            "tipo_de_forma": "Stands Não Humanoides Naturais",
            "afiliacao": "Passione",
            "parte": "Vento Aureo",
            "lado": "Aliados"
        },

        {
            "nome": "Narancia Ghirga",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Longo Alcance",
                "Stands de Reconhecimento"
            ],
            "tipo_de_forma": "Stands Não Humanoides Naturais",
            "afiliacao": "Passione",
            "parte": "Vento Aureo",
            "lado": "Aliados"
        },

        {
            "nome": "Leone Abbacchio",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Longo Alcance",
                "Stands de Reconhecimento"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "Passione",
            "parte": "Vento Aureo",
            "lado": "Aliados"
        },

        {
            "nome": "Pannacotta Fugo",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance",
                "Stands Conscientes"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "Passione",
            "parte": "Vento Aureo",
            "lado": "Aliados"
        },

        {
            "nome": "Trish Una",
            "genero": "mulher",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "Passione",
            "parte": "Vento Aureo",
            "lado": "Aliados"
        },

        {
            "nome": "Diavolo",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance",
                "Stands de Precognição"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "Passione",
            "parte": "Vento Aureo",
            "lado": "Inimigos"
        },

        {
            "nome": "Risotto Nero",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "Passione",
            "parte": "Vento Aureo",
            "lado": "Inimigos"
        },

        {
            "nome": "Polpo",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands Automáticos",
                "Stands de Longo Alcance"
            ],
            "tipo_de_forma": "Stands Não Humanoides Artificiais",
            "afiliacao": "Passione",
            "parte": "Vento Aureo",
            "lado": "Inimigos"
        },

        # ======================================
        # PARTE 6 - STONE OCEAN
        # ======================================

        {
            "nome": "Jolyne Cujoh",
            "genero": "mulher",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Stone Ocean",
            "lado": "Aliados"
        },

        {
            "nome": "Ermes Costello",
            "genero": "mulher",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "sem afiliação",
            "parte": "Stone Ocean",
            "lado": "Aliados"
        },

        {
            "nome": "Emporio Alniño",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Reconhecimento"
            ],
            "tipo_de_forma": "Stands Não Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Stone Ocean",
            "lado": "Aliados"
        },

        {
            "nome": "Foo Fighters",
            "genero": "Animal",
            "tipo_de_habilidade": [
                "Stands Colônia",
                "Stands Conscientes"
            ],
            "tipo_de_forma": "Stands Não Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Stone Ocean",
            "lado": "Aliados"
        },

        {
            "nome": "Weather Report",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Longo Alcance",
                "Stands de Reconhecimento"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Stone Ocean",
            "lado": "Aliados"
        },

        {
            "nome": "Narciso Anasui",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "grupo joestar",
            "parte": "Stone Ocean",
            "lado": "Aliados"
        },

        {
            "nome": "Enrico Pucci",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance",
                "Stands Evoluídos",
                "Stands de Precognição"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "sem afiliação",
            "parte": "Stone Ocean",
            "lado": "Inimigos"
        },

        {
            "nome": "Gwess",
            "genero": "mulher",
            "tipo_de_habilidade": [
                "Stands de Curto Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "sem afiliação",
            "parte": "Stone Ocean",
            "lado": "Inimigos"
        },

        {
            "nome": "Lang Rangler",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Longo Alcance"
            ],
            "tipo_de_forma": "Stands Humanoides Naturais",
            "afiliacao": "sem afiliação",
            "parte": "Stone Ocean",
            "lado": "Inimigos"
        },

        {
            "nome": "Rikiel",
            "genero": "homem",
            "tipo_de_habilidade": [
                "Stands de Longo Alcance",
                "Stands de Reconhecimento"
            ],
            "tipo_de_forma": "Stands Não Humanoides Naturais",
            "afiliacao": "familia do dio",
            "parte": "Stone Ocean",
            "lado": "Inimigos"
        }

    ]

    # =====================================
    # LÓGICA DO JOGO (personagem secreto)
    # =====================================

    secreto = random.choice(PERSONAGENS)

    VERDE = "#2e7d32"
    AMARELO = "#f9a825"
    VERMELHO = "#c62828"
    CINZA = "#616161"

    def cor_valor(guess, alvo):
        return VERDE if guess == alvo else VERMELHO

    def cor_lista(lista_guess, lista_alvo):
        set_guess = set(lista_guess)
        set_alvo = set(lista_alvo)
        if set_guess == set_alvo:
            return VERDE
        elif set_guess & set_alvo:
            return AMARELO
        else:
            return VERMELHO

    def cor_parte(guess, alvo):
        if guess == alvo:
            return VERDE
        if guess in PARTES and alvo in PARTES:
            distancia = abs(PARTES.index(guess) - PARTES.index(alvo))
            if distancia == 1:
                return AMARELO
        return VERMELHO

    def celula(texto, cor, largura=140):
        return aura.Container(
            content=aura.Text(
                texto,
                color="white",
                size=12,
                text_align=aura.TextAlign.CENTER
            ),
            bgcolor=cor,
            width=largura,
            padding=25,
            border_radius=6,
            alignment=aura.Alignment.CENTER
        )

    cabecalho = aura.Row(
        controls=[
            celula("Nome", CINZA),
            celula("Gênero", CINZA),
            celula("Habilidade", CINZA),
            celula("Forma", CINZA),
            celula("Afiliação", CINZA),
            celula("Parte", CINZA),
            celula("Lado", CINZA),
        ],
        scroll=aura.ScrollMode.AUTO
    )

    tentativas = aura.Column()
    mensagem = aura.Text(size=20, weight=aura.FontWeight.BOLD)

    caixa_texto = aura.TextField(
        label="Digite o nome do personagem",
        width=400
    )

    Sugestoes = aura.Column()

    def escolher(nome_escolhido):
        personagem = next(
            (p for p in PERSONAGENS if p["nome"] == nome_escolhido), None
        )
        if personagem is None:
            return

        linha = aura.Row(
            controls=[
                celula(
                    personagem["nome"],
                    VERDE if personagem["nome"] == secreto["nome"] else VERMELHO
                ),
                celula(personagem["genero"], cor_valor(personagem["genero"], secreto["genero"])),
                celula(
                    ", ".join(personagem["tipo_de_habilidade"]),
                    cor_lista(personagem["tipo_de_habilidade"], secreto["tipo_de_habilidade"])
                ),
                celula(personagem["tipo_de_forma"], cor_valor(personagem["tipo_de_forma"], secreto["tipo_de_forma"])),
                celula(personagem["afiliacao"], cor_valor(personagem["afiliacao"], secreto["afiliacao"])),
                celula(personagem["parte"], cor_parte(personagem["parte"], secreto["parte"])),
                celula(personagem["lado"], cor_valor(personagem["lado"], secreto["lado"])),
            ],
            scroll=aura.ScrollMode.AUTO
        )
        tentativas.controls.insert(0, linha)

        if personagem["nome"] == secreto["nome"]:
            mensagem.value = f"🎉 Você acertou! Era {secreto['nome']}!"
            mensagem.color = VERDE
            caixa_texto.disabled = True

        caixa_texto.value = ""
        Sugestoes.controls.clear()
        pagina.update()

    def pesquisar(e):
        texto = caixa_texto.value.strip().lower()
        Sugestoes.controls.clear()
        if texto == "":
            pagina.update()
            return
        for personagem in PERSONAGENS:
            nome = personagem["nome"]
            if texto in nome.lower():
                Sugestoes.controls.append(
                    aura.TextButton(
                        content=aura.Text(nome),
                        on_click=lambda e, n=nome: escolher(n)
                    )
                )
        pagina.update()

    caixa_texto.on_change = pesquisar

    pagina.add(
        caixa_texto,
        Sugestoes,
        mensagem,
        cabecalho,
        tentativas
    )


aura.run(
    main,
    view=aura.AppView.WEB_BROWSER
)