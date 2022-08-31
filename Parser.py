# Gabriel Antonio Gomes de Farias - PUC-PR/2022

"""
ENUNCIADO
Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a
linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional
escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma
da expressão (sintaxe).
A entrada será fornecida por um arquivo de textos que será carregado em linha de comando,
com a seguinte formatação:
1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões
lógicas estão no arquivo.
2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.
A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída
para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais.
Gramática:
Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.
Constante="T"|"F".
Proposicao=[a−z0−9]+
FormulaUnaria=AbreParen OperadorUnario Formula FechaParen
FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen
AbreParen="("
FechaParen=")"
OperatorUnario="¬"
OperatorBinario="∨"|"∧"|"→"|"↔"

Cada  expressão  lógica  avaliada  pode  ter  qualquer  combinação  das  operações  de  negação,
conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações.
Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em
qualquer expressão de entrada.
Para  validar  seu  trabalho,  você  deve  incluir  no  repl.it,  no  mínimo  três  arquivos  contendo
números  diferentes  de  expressões  proposicionais.  O  professor  irá  incluir  um  arquivo  de  testes  extra
para validar seu trabalho. Para isso, caberá ao professor incluir o arquivo no seu repl.it e rodar o seu
programa carregando o arquivo de testes.
"""

# ---------FUNCÕES-------------#
def validar():
    comeco_arquivo = False  # determina inicio do arquivo
    qtd_expressoes = 0  # nmr de expressões q o codigo ira verificar
    verificadas = 0  # total q o código verificou
    try:
        texto = open(str(input("Digite o nome do arquivo de texto.\n>> ")), 'r')
        '''
        OBS INSERIR o nome do arquivo completo ex: teste1.txt
        '''
        for linha in texto:
            if not comeco_arquivo:
                qtd_expressoes = int(linha[0])
                comeco_arquivo = True
            else:
                char = str(linha)
                dividir = char.split("\n")
                palavra = str(dividir[0])
                validado = validar_string(palavra)
                if validado:
                    print("válida")
                    verificadas += 1
                    if verificadas >= qtd_expressoes:
                        break
                else:
                    print("inválida")
                    verificadas += 1
                    if verificadas >= qtd_expressoes:
                        break
    except:
        print("ERRO: Arquivo não existe, verifique o nome.")
# LINHA 71 à 147 OP PRINCIPAIS
def constante(expressao):
    if expressao == 'T' or expressao == 'F':
        return True
    return False


def verificar_parenteses(letra):
    if letra == ')':
        return 'fechar'
    elif letra == '(':
        return 'abrir'
    return ''


def contar_parenteses(expressao):
    parenteses = 0
    for letra in expressao:
        if verificar_parenteses(letra) == 'abrir' and parenteses >= 0:
            parenteses += 1
        if verificar_parenteses(letra) == 'fechar' and parenteses > 0:
            parenteses -= 1
    return parenteses


def proposicao(letra):
    if (letra.isalpha() and letra.islower()) or letra.isnumeric():
        # valida apenas caso letra for minuscula e alfanúmerica
        return True
    return False


def espaco(letra):
    if letra == ' ':
        return True
    return False


def backslash(expressao):
    for i in range(len(expressao)):
        if expressao[i] == '\\':
            return True
    return False


def op_latex(expressao, i):
    op_tam = 0
    operador = "binario"

    try:
        if expressao[i + 1] == 'n' and expressao[i + 2] == 'e' and expressao[i + 3] == 'g':
            op_tam = 3
            operador = "unario"

        elif expressao[i + 1] == 'l' and expressao[i + 2] == 'o' and expressao[i + 3] == 'r':
            op_tam = 3

        elif expressao[i + 1] == 'v' and expressao[i + 2] == 'e' and expressao[i + 3] == 'e':
            op_tam = 3

        elif (expressao[i + 1] == 'l' and expressao[i + 2] == 'a' and expressao[i + 3] == 'n' and expressao[
            i + 4] == 'd'):
            op_tam = 4

        elif expressao[i + 1] == 'w' and expressao[i + 2] == 'e' and expressao[i + 3] == 'd' and expressao[
            i + 4] == 'g' and expressao[i + 5] == 'e':
            op_tam = 5

        elif (expressao[i + 1] == 'r' and expressao[i + 2] == 'i' and expressao[i + 3] == 'g' and expressao[
            i + 4] == 'h' and expressao[i + 5] == 't' and expressao[i + 6] == 'a' and expressao[i + 7] == 'r' and
              expressao[i + 8] == 'r' and expressao[i + 9] == 'o' and expressao[i + 10] == 'w'):
            op_tam = 10

        elif (expressao[i + 1] == 'l' and expressao[i + 2] == 'e' and expressao[i + 3] == 'f' and expressao[
            i + 4] == 't' and expressao[i + 5] == 'r' and expressao[i + 6] == 'i' and expressao[i + 7] == 'g' and
              expressao[i + 8] == 'h' and expressao[i + 9] == 't' and expressao[i + 10] == 'a' and expressao[
                  i + 11] == 'r' and expressao[i + 12] == 'r' and expressao[i + 13] == 'o' and expressao[
                  i + 14] == 'w'):
            op_tam = 14

    except IndexError:
        return 0, ""
    return op_tam, operador


# VALIDAÇÃO EXPRESSÂO
def validar_exp(expressao, i, operador):
    exp_tam = -1
    temp = ""
    total_parenteses = 0

    if operador == "unario":
        if constante(expressao[i]):
            letra = expressao[i + 1]
            if verificar_parenteses(letra) == 'fechar':
                exp_tam += 1
                return True, exp_tam
            else:
                return False, -1

        for j in range(i, len(expressao) - 1):
            if verificar_parenteses(expressao[i]) == 'abrir':
                if verificar_parenteses(expressao[j]) == 'abrir' and total_parenteses >= 0:
                    total_parenteses += 1
                elif verificar_parenteses(expressao[j]) == 'fechar' and total_parenteses > 0:
                    total_parenteses -= 1
                    if total_parenteses == 0:
                        break
            else:
                if verificar_parenteses(expressao[j]) == 'fechar' and not espaco(expressao[j + 1]):
                    break

            temp += expressao[j]
            exp_tam += 1

    elif operador == "binario":
        for j in range(i, len(expressao)):
            if verificar_parenteses(expressao[i]) == 'abrir':
                if verificar_parenteses(expressao[j]) == 'fechar':
                    total_parenteses += 1
                elif verificar_parenteses(expressao[j]) == 'fechar':
                    total_parenteses -= 1
                    if total_parenteses == 0:
                        break
            else:
                if verificar_parenteses(expressao[j]) == 'fechar' or espaco(expressao[j]):
                    break

            temp += expressao[j]
            exp_tam += 1

    if verificar_parenteses(expressao[i]) == 'abrir':
        expressao_full = temp + ")"
        exp_tam += 1
    else:
        expressao_full = temp

    resultado_expressao = validar_string(expressao_full)

    return resultado_expressao, exp_tam


# Validação booleana, retorna se é valida ou invalida
def validar_string(expressao):
    resultado = True
    operador = ""
    estado = 1

    if contar_parenteses(expressao) != 0:
        return False

    if backslash(expressao):
        i = 0
        while i < len(expressao):
            letra = expressao[i]
            if estado == 1:
                if verificar_parenteses(letra) != 'abrir':
                    return False
                estado += 1

            elif estado == 2:
                tam_op, operador = op_latex(expressao, i)
                if tam_op == 0:
                    return False
                i += tam_op
                estado += 1

            elif estado == 3:
                if not espaco(letra):
                    return False
                estado += 1

            elif estado == 4:
                resultado_expressao, tam_exp = validar_exp(expressao, i, operador)
                i += tam_exp

                if resultado_expressao:
                    if operador == "binario":
                        estado += 1
                    elif operador == "unario":
                        return True
                else:
                    return False

            elif estado == 5:
                if espaco(letra):
                    estado += 1
                else:
                    return False

            elif estado == 6:
                resultado_expressao, tam_exp = validar_exp(expressao, i, operador)
                i += tam_exp

                if not resultado_expressao:
                    return False
                return True

            i += 1
    else:
        for i in range(len(expressao)):
            con = constante(expressao)
            prop = proposicao(expressao[i])

            if not con and not prop:
                return False
    return resultado
# --------FINAL-FUNÇÕES--------#


# ---------LOOP----------------#
validar()
#---------FIM-LOOP-------------#
