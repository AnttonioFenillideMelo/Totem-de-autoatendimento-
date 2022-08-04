carrinho = []
escolha  = ""
outro = 9
dic = {
    1 : ['1-gof suculendo','2-gof aparmediana','3-gof torrado'],
    2 : ['1-gof saladeno','2-gof no beef','3-gof no oink']
}
print('Bem-vindo ao goflanches')

while outro == 9:
    print('escolha um topico de lanche de acordo com a numeração (1 carnes),(2 veganos)')
    escolha = int(input())
    if escolha == 1:
        while outro == 9 or outro == 1:
            print(dic[1])
            escolha = int(input())
            carrinho.append(dic[1][int(escolha)-1])
            #voltando para outra escolha dentro do cardapio ja
            print('para escolher outro lanche pressione 1, para sair pressione 2, para mudar o cardapio 9')
            outro = int(input())
            if outro == 1:
                print('aqui esta o lanches')
            elif outro == 2:
                print('Obrigado por comprar com a gente :)')
            else:
                print('estamos te enviando para o cardapio principal de novo')
    if escolha == 2:
        while outro == 9 or outro == 1:
            print(dic[2])
            escolha = int(input())
            carrinho.append(dic[2][int(escolha)-1])
            #voltando para outra escolha dentro do cardapio ja
            outro = int(input('quer escolher outro pedido ?'))
            if outro == 1:
                print('Aqui esta os lanches')
            elif outro == 2:
                print('Obrigado por comprar com a gente :)')
            else: 
                print('Estamos te enviando para o menu principal de novo')       
    else:
        print('cardapio não encontrado, porfavor tente outro numero') 