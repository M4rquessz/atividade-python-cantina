#Projeto de algoritmo: Cantina
from platform import version

o=[1, 2, 3, 4]
p=['Suco', 'Salgado', 'Sanduíche', 'Finalizar']
pre=[5.00, 7.00, 10.00]
re2=0
vt=0
qtd=0

while re2!=4:
    print('OPÇÕES   PRODUTOS   PREÇO')
    print(f'{o[0]}   {p[0]}   {pre[0]}')
    print(f'{o[1]}   {p[1]}   {pre[1]}')
    print(f'{o[2]}   {p[2]}   {pre[2]}')
    print(f'{o[3]}   {p[3]}\n')

    re2=int(input('Escolha sua opção: \n'))

    if re2==1:
        vt+=5
        print(f'Você escolheu {p[0]}, ótima escolha! O valor total de sua compra se encontra em {vt} reais.\n')
        print('Digite 4 se quiser finalizar a compra.\n')
        qtd+=1

    elif re2==2:
        vt+=7
        print(f'Você escolheu {p[1]}, ótima escolha! O valor total de sua compra se encontra em {vt} reais.\n')
        print('Digite 4 se quiser finalizar a compra.\n')
        qtd += 1

    elif re2==3:
        vt+=10
        print(f'Você escolheu {p[2]}, ótima escolha! O valor total de sua compra se encontra em {vt} reais.\n')
        print('Digite 4 se quiser finalizar a compra.\n')
        qtd += 1

    elif re2==4:
        print(f'Você escolheu {p[3]}, finalizando sua compra. Obrigado por comprar conosco!.\n')
        print(f'Sua compra finalizou em {vt} Reais e {qtd} produtos.\n')

    else:
        print('Esse número não está listado! Encerrando o programa...')
        break


