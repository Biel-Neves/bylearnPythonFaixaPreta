no = input('Qual o seu nome: ').title()
id = int(input('Quantos anos você tem?: '))

if id >= 18:
    print('Você já é de maior', no,
          ', pode dirigir e beber, mas com moderação claro.')
else:
    falta = (18 - id)
    print('Calma', no, ', faltam apenas', falta, ' anos para você fazer 18')
