# Importação da biblioteca pandas para formatação dos dados csv
import pandas as pd
tabela = pd.read_csv('../pythonProject3/br-capes-bolsistas-uab.csv', encoding='unicode_escape', sep=';')

# estrutura visual de apresentação do programa
print(" ")
print('-----------------------------------------------')
print('--  Bem vindo ao consulta bolsas de estudo!  --')
print('-----------------------------------------------')

# Estrutura de repetição para que ao final de cada pesquisa o usuário retorne ao menu inicial até escolher a opção sair
op = 0
while op != 5:
    print(' ')
    print('1 - Consulta bolsa 0')
    print('2 - Consulta por nome')
    print('3 - Consulta média anual')
    print('4 - Ranking bolsas')
    print('5 - Sair')
    print(' ')
    op = int(input('    Escolha uma opção: '))

# estrutura Match para que usuário escolha a operação a ser realizada pelo programa
    match op:
# Caso 1 Váriavel "anob0" recebe a informação do usuário e torna-se padrão de controle para criação de novo dataframe "bolsista0" contando apenas com os alunos do ano solicitado. Comando "Reset_index" para zerar o indice e chamar apenas a linha 01 do dataframe
        case 1:
            anob0 = int(input('Digite o ano desejado no formato _ _ _ _ :'))
            bolsista0 = tabela[tabela['AN_REFERENCIA'] == anob0]
            bolsista0 = bolsista0.reset_index()
            print('')
            print('=>O Bolsista 0 é :')
            print(bolsista0.head(1)[['NM_BOLSISTA', 'CPF_BOLSISTA', 'NM_ENTIDADE_ENSINO', 'CD_MOEDA', 'VL_BOLSISTA_PAGAMENTO']])
# CASO-2 Variável "nome" recebe o valor do usuário alterando seu formato para maiúscula com comando "upper" e torna-se parametro para o comando "contains" buscar apenas itens correspondentes que serão exibidos apenas nas tabelas restantes do comando drop.
        case 2:
            nome = str(input('Digite o nome do aluno:')).upper()
            aluno = tabela[tabela['NM_BOLSISTA'].str.contains(nome)]
            print(' ')
            print(aluno.drop(['ME_REFERENCIA', 'CPF_BOLSISTA', 'SG_DIRETORIA', 'SG_SISTEMA_ORIGEM', 'CD_MODALIDADE_SGB', 'DS_MODALIDADE_PAGAMENTO', ], axis=1))
# CASO-3 Variavel "anomedia" recebe o valor do usuário e torna-se parametro de controle para que a média da variável,"valor" seja apenas a média das linhas que são iguais a variavel "anomedia" na comparação,da coluna "An referencia". Utilizado o comando Round para deixar a visualização do usuário mais agradável.
        case 3:
            anomedia = int(input('Digite o ano desejado no formato _ _ _ _ :'))
            valor = tabela[tabela['AN_REFERENCIA'] == anomedia]
            print(' ')
            print('A média anual para', anomedia, 'é de:R$', (round(valor['VL_BOLSISTA_PAGAMENTO'].mean(), 2)))
# CASO-4 Variavel "nota" recebe os valores reordenados da tabela com base na coluna "VL_BOlSISTA_PAGAMENTO", com isso é possivel chamar para exibição os três primeiros e três ultimos valores.
        case 4:
            nota = tabela.sort_values('VL_BOLSISTA_PAGAMENTO')
            print('As três maiores bolsas são:')
            print(nota[-3:])
            print('As três menoes bolsas são:')
            print(nota[0:3])
# CASO-5 Saida do programa
        case 5:
            print('Programa encerrado!')
# CASO-_ Caso o usuário digite um valor inválido o programa retorna a informação solicitando uma nova escolha.
        case _:
            print("Opção inválida, tente novamente!")
