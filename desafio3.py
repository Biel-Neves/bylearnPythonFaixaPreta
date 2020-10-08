from time import sleep
lp = 20
nome = input('Senhor: Qual o seu nome viajante: ').title()
din = float(20)
esp = str('')


print('Senhor: Seja-Bem vindo ao mundo de Englad', nome,
      ', Mas tome cuidado pois há ladrões que há aqui.')
sleep(1)
arma = input(
    'Senhor: Para você se proteger irei te dar uma, escolha uma: Espada, Arco, Cajado.').title()
sleep(1)
print('Senhor: Cuidado, um deles apareceu atrás de você!!')
sleep(1)
print('---BATALHA---')
acao = input('Atacar \n Corre \n Fingir de Morto \n').title()

if acao == 'Atacar':
    print('Você levou -5 lp')
    print('Bandido: HAHAHA, Você é uma vergonha para todos de tão inutil')
    (lp - 5)
if acao == 'Fingir de Morto':
    print('O bandido roubou todas as suas moedas e sua arma')
    arma == 0
    din == 0
if acao == 'Correr':
    print('-- O ladrão te pegou pela costa e te matou --')
    print('--- GAME OVER ---')
else:
    res = input('Senhor: Você está bem?').title()
    if res == 'Sim':
        print('Senhor: Então levante do chão garoto!! Onde já se viu isso?!?!?!?')
    else:
        print('Senhor: Terei que fazer um poção para você.')
        print('-- Você toma um líquido viscoso e verde que o senhor lhe oferece --')
        print('-- Você ganhou 5 LP --')
        (lp + 5)
