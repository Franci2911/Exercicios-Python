nomeProduto = input('Digite o nome do produto : ')
categoriaProduto = input('Digite o nome da categoria : ')
quantidadeEstoque = (input('Digite a quantidade no estoque : '))

qtdeMin_alimentos = 50
qtdeMin_bebidas = 75
qtdeMin_limpeza = 30

if nomeProduto and categoriaProduto and quantidadeEstoque:
    quantidadeEstoque = int(quantidadeEstoque)

    if categoriaProduto == 'alimentos':
        if quantidadeEstoque < qtdeMin_alimentos:
            print(f'Solicitar {nomeProduto} à equipe de compras, temos apenas {quantidadeEstoque} unidades em estoque')
    elif categoriaProduto == 'bebidas':
        if quantidadeEstoque < qtdeMin_bebidas:
            print(f'Solicitar {nomeProduto} à equipe de compras, temos apenas {quantidadeEstoque} unidades em estoque')
    else:
        if quantidadeEstoque < qtdeMin_limpeza:
            print(f'Solicitar {nomeProduto} à equipe de compras, temos apenas {quantidadeEstoque} unidades em estoque')

else:
    print('Preencha as informações corretamente...')



