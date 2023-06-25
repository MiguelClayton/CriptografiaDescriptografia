def vermelho(msg):
    print(f'\033[0:31m{msg}\033[m')


def verde(msg):
    print(f'\033[1;92m{msg}\033[m')


def criaArq(nome):
    try:
        open(nome, 'wt+')
    except:
        vermelho('Erro: falha ao criar o arquivo.')
    else:
        verde('Arquivo criado com sucesso.')


def arqExiste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except (FileExistsError, FileNotFoundError):
        return False
    else:
        return True


def textoDescriptografado(nomearquivo, texto):
    try:
        a = open(nomearquivo, 'at')
    except:
        vermelho('Erro: falha ao editoar arquivo.')
    else:
        try:
            a.writelines(f'{texto}')
            a.close()
        except:
            vermelho('Erro: falha ao escrever os dados')


# troca os algarisms por letras e simbolos aleatorios
def multiplo_desreplace(texto, cont):
    if cont >= 0 and cont <= 10:
        a = str(texto).replace("!", "1").replace("z", "2").replace("E", "3").replace("A", "4").replace(
            "s", "5").replace("G", "6").replace("T", "7").replace("B", "8").replace("?", "9").replace("o", "0")
    elif cont > 10 and cont <= 20:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 20 and cont <= 30:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 30 and cont <= 40:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 40 and cont <= 50:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 50 and cont <= 60:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 60 and cont <= 70:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 70 and cont <= 80:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 80 and cont <= 90:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 90 and cont <= 100:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 100 and cont <= 110:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 110 and cont <= 120:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 120 and cont <= 130:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 130 and cont <= 140:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 140 and cont <= 150:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 150 and cont <= 160:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 160 and cont <= 170:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 170 and cont <= 180:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 180 and cont <= 190:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 190 and cont <= 200:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 200 and cont <= 210:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 210 and cont <= 220:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 220 and cont <= 230:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 230 and cont <= 240:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 240 and cont <= 250:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 250 and cont <= 260:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 260 and cont <= 270:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 270 and cont <= 280:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 280 and cont <= 290:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 290 and cont <= 300:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 300 and cont <= 310:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 310 and cont <= 320:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 320 and cont <= 330:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 330 and cont <= 340:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 340 and cont <= 350:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 350 and cont <= 360:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 360 and cont <= 370:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 370 and cont <= 380:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 380 and cont <= 390:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 390 and cont <= 400:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 400 and cont <= 410:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 410 and cont <= 420:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 420 and cont <= 430:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 430 and cont <= 440:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 440 and cont <= 450:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 450 and cont <= 460:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    elif cont > 460 and cont <= 470:
        a = str(texto).replace("a", "1").replace("b", "2").replace("c", "3").replace("A", "4").replace(
            "P", "5").replace("l", "6").replace("T", "7").replace("Q", "8").replace("?", "9").replace("p", "0")
    elif cont > 470 and cont <= 480:
        a = str(texto).replace("R", "1").replace("q", "2").replace("$", "3").replace("@", "4").replace(
            "H", "5").replace("h", "6").replace("T", "7").replace("O", "8").replace("?", "9").replace("k", "0")
    elif cont > 480 and cont <= 490:
        a = str(texto).replace("I", "1").replace("u", "2").replace("U", "3").replace("G", "4").replace(
            "B", "5").replace("!", "6").replace("T", "7").replace("$", "8").replace("?", "9").replace("A", "0")
    else:
        a = str(texto).replace("!", "1").replace("z", "2").replace("E", "3").replace("A", "4").replace(
            "s", "5").replace("G", "6").replace("T", "7").replace("B", "8").replace("?", "9").replace("o", "0")

    return int(a)


# acessa o codigo a ser descriptografado
codigo = []
if arqExiste('descriptografia.txt') == True:
    arq = open('descriptografia.txt')
    texto = arq.readlines()
    for iten in texto:
        codigo.append(iten)

else:
    criaArq('descriptografia.txt')

# relacao de dados para descripógrafa
alfabeto = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j'),
            (11, 'k'), (12, 'l'), (13, 'm'), (14, 'n'), (15, 'o'), (16, 'p'), (17, 'q'), (18, 'r'), (19, 's'),
            (20, 't'), (21, 'u'), (22, 'v'), (23, 'w'), (24, 'x'), (25, 'y'), (26, 'z'), (27, 'A'), (28, 'B'),
            (29, 'C'), (30, 'D'), (31, 'E'), (32, 'F'), (33, 'G'), (34, 'H'), (35, 'I'), (36, 'J'), (37, 'K'),
            (38, 'L'), (39, 'M'), (40, 'N'), (41, 'O'), (42, 'P'), (43, 'Q'), (44, 'R'), (45, 'S'), (46, 'T'),
            (47, 'U'), (48, 'V'), (49, 'W'), (50, 'X'), (51, 'Y'), (52, 'Z'), (53, 'ç'), (54, '_'), (55, ','),
            (56, '.'), (57, '?'), (58, 'é'), (59, 'ã'), (60, 'Â'), (61, 'á'), (62, 'À'), (63, 'ó'), (64, 'Ó'),
            (65, 'É'), (66, '"'), (67, '-'), (68, ':'), (69, '0'), (70, '1'), (71, '2'), (72, '3'), (73, '4'),
            (74, '5'), (75, '6'), (76, '7'), (77, '8'), (78, '9'), (79, '!'), (80, '@'), (81, '"'), (82, '#'),
            (83, '$'), (84, '%'), (85, '¨'), (86, '&'), (87, '*'), (88, '('), (89, ')'), (90, '+'), (91, '§'),
            (92, '['), (93, ']'), (94, '/'), (95, '{'), (96, '}'), (97, '?'), (98, '°'), (99, '<'),
            (100, '>'), (101, ';'), (102, 'º'), (103, '´'), (104, '`'), (105, "'"), (106, '|'), (107, '^'), (108, '~'),
            (109, 'ê'), (110, 'Ê')]

# descripógrafa letra a letra
cont = 0
print()
descriptografado = ''
for linha in codigo:
    numeral = multiplo_desreplace(linha, cont)
    cont += 1
    variavel = (((numeral / 6869) / 6869) - 9967)
    for bagulho in alfabeto:
        if variavel != bagulho[0]:
            continue
        final = str(bagulho[1]).replace("|", "\n").replace('_', ' ').replace("'", "").replace("[", "").replace("]", "")

# elimina as virgulas do começoo da frase
        descriptografado = final
        linhas = descriptografado.split('\n')
        for i in range(len(linhas)):
            linha = linhas[i].lstrip(',')
            linhas[i] = linha
        texto_sem_virgulas = '\n'.join(linhas)
        print(texto_sem_virgulas,end='')

print()
