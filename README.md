# Number Guessing Game
Um jogo de adivinhação via linha de comando (CLI), onde o computador escolhe um número aleatório entre 1 e 100, e o jogador deve tentar adivinhar dentro de um número limitado de tentativas.

Este projeto é baseado na ideia de: [Number Guessing Game](https://roadmap.sh/projects/number-guessing-game)

## Como funciona
- Escolha um nível de dificuldade: Fácil (10 tentativas), Médio (5 tentativas) ou Difícil (3 tentativas)
- Digite seus palpites.
O jogo informa se o número secreto é maior ou menor.
- Vença acertando o número antes de acabar as tentativas.

## Estrutura do projeto
```
main.py          # Arquivo principal
game_logic.py    # Lógica do jogo
messages.py      # Mensagens exibidas ao usuário
```

## Como executar
**Linux:**
```
python3 main.py
```

**Windows:**
```
python main.py
```