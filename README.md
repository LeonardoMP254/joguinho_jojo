# 🎭 JoJoDle — Jogo de Adivinhação

Um jogo de adivinhação inspirado no universo de **JoJo's Bizarre Adventure**, desenvolvido como uma atividade de programação utilizando **Python** e **Flet**.

O objetivo do jogo é descobrir qual é o **personagem secreto**, utilizando as informações apresentadas a cada tentativa para chegar à resposta correta.

---

## 🎮 Sobre o projeto

No início de cada partida, o sistema escolhe aleatoriamente um personagem entre os personagens cadastrados.

O jogador deve digitar o nome de um personagem e escolher uma das sugestões apresentadas.

Após cada tentativa, o jogo mostra várias características do personagem e utiliza **cores para indicar o quanto a tentativa se aproxima do personagem secreto**.

Entre as características analisadas estão:

* 👤 Nome
* ⚧️ Gênero
* 💥 Tipo de habilidade
* 👾 Forma do Stand
* 🏴 Afiliação
* 📖 Parte de JoJo
* ⚔️ Lado

O personagem secreto é escolhido de forma aleatória utilizando a biblioteca `random`.

---

## 🧩 Como funciona

O jogador começa digitando o nome de um personagem.

Enquanto o nome é digitado, o programa pesquisa os personagens cadastrados e apresenta sugestões que correspondem ao texto digitado.

Depois que um personagem é escolhido, suas características são comparadas com as características do personagem secreto.

### 🟩 Verde

Indica que a informação está correta.

### 🟨 Amarelo

Indica uma correspondência parcial.

No caso da **Parte**, o amarelo também pode indicar que a Parte escolhida está próxima da Parte do personagem secreto.

### 🟥 Vermelho

Indica que a informação não corresponde ao personagem secreto.

---

## 🗃️ Dados dos personagens

Os personagens são armazenados em uma lista de dicionários chamada `PERSONAGENS`.

Cada personagem possui informações como:

```python
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
}
```

O projeto possui personagens das seguintes partes:

* **Parte 1 — Phantom Blood**
* **Parte 2 — Battle Tendency**
* **Parte 3 — Stardust Crusaders**
* **Parte 4 — Diamond is Unbreakable**
* **Parte 5 — Vento Aureo**
* **Parte 6 — Stone Ocean**

As categorias de Parte estão cadastradas no próprio programa.

---

## ⚙️ Tecnologias utilizadas

* 🐍 **Python**
* 🎨 **Flet**
* 🎲 **Random**
* 🗂️ **Listas**
* 📦 **Dicionários**
* 🔄 **Funções**
* 🔍 **Pesquisa de personagens**
* 🎯 **Estruturas condicionais**
* 🧮 **Comparação de listas e conjuntos**

---

## 🧠 Conceitos de programação utilizados

Durante o desenvolvimento foram utilizados diversos conceitos de programação.

### Listas

As listas foram utilizadas para armazenar categorias e informações, como gêneros, habilidades, partes e personagens.

```python
GENERO = [
    "homem",
    "mulher",
    "Animal"
]
```

### Dicionários

Os personagens são representados através de dicionários, permitindo armazenar várias características de cada personagem.

### Funções

O projeto utiliza várias funções para organizar a lógica do jogo, como:

```python
cor_valor()
cor_lista()
cor_parte()
celula()
escolher()
pesquisar()
```

Essas funções dividem o funcionamento do programa em partes menores.

### Randomização

O personagem secreto é escolhido aleatoriamente:

```python
secreto = random.choice(PERSONAGENS)
```

### Comparação de conjuntos

As habilidades dos personagens são comparadas utilizando `set()`, permitindo verificar se existem habilidades em comum entre a tentativa e o personagem secreto.

---

## 🖥️ Interface

A interface foi desenvolvida utilizando **Flet**, permitindo criar elementos gráficos através do Python.

O jogador possui:

* Campo para digitar o personagem;
* Lista de sugestões;
* Mensagem de resultado;
* Tabela com as tentativas;
* Células coloridas para representar as dicas.

Quando o jogador acerta o personagem secreto, o sistema exibe uma mensagem de vitória e desativa o campo de entrada.

---

## 📂 Estrutura do projeto

```text
JoJoDle/
│
├── AuraSupre.py
└── README.md
```

---

## ▶️ Como executar

### 1. Instale o Python

Tenha o Python instalado em sua máquina.

### 2. Instale o Flet

No terminal:

```bash
pip install flet
```

### 3. Execute o projeto

```bash
python AuraSupre.py
```

O projeto utiliza o Flet para executar a aplicação em uma interface web.

---

## 🎯 Objetivo da atividade

O principal objetivo desta atividade foi praticar conceitos de **Python**, principalmente:

* Manipulação de listas;
* Manipulação de dicionários;
* Criação e utilização de funções;
* Estruturas condicionais;
* Pesquisa de dados;
* Comparação de informações;
* Geração de valores aleatórios;
* Desenvolvimento de interface gráfica com Flet.

Além disso, o projeto transforma esses conceitos em um jogo interativo, tornando a atividade mais prática e dinâmica.

---

## 👨‍💻 Autor

**Leonardo A. Leão**

Estudante de programação — **2IE-DS**

Projeto desenvolvido para fins **educacionais**.
