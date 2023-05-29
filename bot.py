import re
import json
import schedule
import markovify
from time import sleep
from tweepyCli import *
from random import randint, choice

dados = []

nomes = ['Itapipoca', 'Uirapuru', 'Pacatuba:', 'Samarte', 'Dom', 'Quixote', 'Sócrates',
         'Portugal', 'Manel', 'Itaiçaba', 'Marina', 'Dona', 'Carolinas', 'Hiago', 'Mendes', 'Batista', 'Milton', 'Valdeci', 'Gelita', 'Mr', 'Jobs', 'Karlos', 'Quimero', 'Zulda', 'Bené', 'Herzog', 'Leonardo', 'Fibonacci', 'Mauro', 'Sartre', 'The Sound of Silence of Live', 'Lenz', 'César', 'Manolin', 'Mestre', 'Santiago', 'Dragão do Mar de Arte e Cultura', 'Helsinque', 'Vivaldi', 'Luiz', 'Januário', 'Fábio Campos', 'Jocélio Leal', 'Ari de Sá', 'Chico Bilas', 'Dilma', 'Trump', 'Putin', 'Oscar Wilde', 'Alisson', 'Nogueira',
         'Brasil', 'Argentina', 'Warren Buffett', 'John Havard', 'Mucuripe', 'Chico', 'Ricardo', 'Liebmann', 'Eike', 'Cunha', 'Marcelo', 'Odebrech', 'Jânio', 'Patek Philippe', 'Pirambu', 'Pirambu Digital', 'Zé de William', 'Gilmar', 'Rua Torres Câmara', 'Aldeota', 'Bonavides', 'Tolle', 'Big Data', 'R$', 'República das Bananas', 'Recife', 'Fernando', 'Bugueiro', 'Pedão', 'Fabrício', 'Paia', 'Meira', 'Google', 'Facebook', 'Amazon', 'Jornal do Povo', 'Agostinho', 'Raimundo Placebo', 'Facundo Placebo', 'Macedo', 'Sandrinha', 'Made in China', 'C-Jovem', 'Finlândia', 'Pedro', 'Damasceno', 'João Jornal', 'Francisco Lucas', 'Alvaro Maia', 'Alisson Chaves', 'Matheus Vieira', 'Lucas Gabriel', 'Juninho', 'Carvalho', 'Alexsandro Costa', 'Drummond', 'Merlin', 'Excalibur', 'Yuval Harari', 'Cerol', 'Jaozuzé', 'Bila', 'Lan House', 'Bruno', 'Jornal O POVO', 'Berners', 'Lee', 'LPs', 'Balão Mágico', 'Moacir Franco', 'Orlando Silva', 'Marciano Ponciano', 'Piramba', 'Arac*ti', 'Empresa Y', 'Dragão Digital', 'Vale do Jaguaribe', 'Cinderela', 'Petrobras', 'Dragão do Mar', 'Alaninha', 'República das Bananas', 'Repúblicas de Bananas', 'Orlando', 'Eduard Snowden', 'Seu Agnaldo', 'Ottawa', 'Perfume Atkinson', 'Pusanfa Tarde', 'Rio!', 'Bill', 'Gates', 'Microsoft', 'Angelita', 'Iate Clube', 'Totonho Laprovitera', 'Canoa', 'Demócrito', 'Drummar', 'Oppenheimer', 'Einstein', 'George', 'Ney', 'Serjão', 'Fidel', 'Moana', 'Beira Mar', 'Vick', 'Vaporub', 'Lula Presidente', 'Ceará', 'Gilberto', 'Freyre', 'Maracanmarte', 'Augusto Pontes', 'Antonio Barbosa', 'Jorjão', 'Empresa X', 'Alantejo', 'Viana', 'Piauí', 'SOU MAURO:', 'Zé de WIlliam', 'Izolda', 'Cela', 'Alice', 'Carioca de Morais', 'PADETEC', 'Getúlio', 'Túlio', 'Sapoti', 'Juá', 'Jabuticaba', 'Ribeiro', 'Platão', 'Waze', 'Pagodinho', 'Iracema', 'África', 'Petrobrás', 'Carl Segan',
         'Dorothy Lamour']
siglas = ['PIB', 'MP:', 'IFCE', 'EMBRAPII',
          'AF,', 'R$', 'EUA', 'NASA', 'AG', 'IA', 'LF', 'IFCE,', 'AF?', 'TUI?', 'AF', 'ENEM.', 'ENEM', 'SBC', 'SBC,', 'RUI', 'RUI,', 'RUI.', 'UFC', 'UFC,', 'CNPQ', 'AF/AG', 'PADATEC.', 'BAYGON', 'CUFA,', 'CUFA', 'ANU', 'CPQD', 'LP', 'MPB', 'COELCE', 'UNESCO']


def nadei():

    frasesEfeito = ['Sensacional!', 'Incrível!', 'Demais!', 'Que felicidade!', 'Fenomenal alunos!', 'Agora ensinar', 'Agora é aula!', 'Agora é dormir!', 'Azulzinho faz efeito RSRSRSRS..', 'Espetacular!', 'Fantástico!',
                    'Maravilhoso!',   'Excelente!', 'Simplesmente incrível!', 'Que maravilha !', 'É de arrepiar!', 'Aula já já RSRSRS..',                 'Fantástico !', 'Sem palavras!', 'Excepcional!', 'UM Mergulho sobre a Arte !']

    praias = ['de Majorlândia', 'de Canoa Quebrada', 'de Iracema', 'de Itapipoca', 'de Caraubás', 'de Quixaba', 'de Lagoa do Mato', 'de Fontainha', 'de Parajuru',
              'do Futuro', 'de Mucuripe', 'do Cumbuco', 'de Lagoinha', 'de Morro Branco', 'de Jericoacoara', 'de Uruaú', 'de Flexeiras', 'de Guajiru', 'de Icaraí', 'de Tatajuba']

    km = randint(2, 50)
    frase = "Só hoje nadei {}km's na Praia {}. {}".format(km,
                                                          praias[randint(0, len(praias)-1)], frasesEfeito[randint(0, len(frasesEfeito)-1)])
    return frase


def palavraAleatoria():
    with open("./base/maurotextos.txt") as f:
        textos = f.readlines()
        textos = list(set(textos))

        for i in range(len(textos)):
            textos[i] = re.sub(
                r'[^\w\sáéíóúâêîôûàèìòùãõñçñ\'\n/:,.\-!*\-|\.{1,3}]+', '', textos[i])
            textos[i] = re.sub(
                r"([!?]\s*)([a-z])", lambda match: match.group(1) + match.group(2).upper(), textos[i])

    txt = "".join(textos)
    words = txt.split()
    word = choice(words)

    while len(word) < 4:
        txt = "".join(textos)
        words = txt.split()
        word = choice(words)

    return word.capitalize().strip()


def aula():
    i = randint(1, 10)
    # ja dei uma aula de
    # adicionar dois topicos
    conteudos = [palavraAleatoria(), 'Flip-Flops', 'ChatGPT', 'Viagra', 'Metaverso', 'Açúcar', 'Sal', 'Marcianos', 'Natação', 'Rádio do meu Pai', 'Transistores',
                 'Iracema Digital', 'Dirigir carro', 'Planeta Jovem', 'Francês', 'Rico fala Inglês', 'Estudante nas Brenhas', "Caixa D'gua"]

    intro = ['Aula de Hoje:', 'Já dei aula de',
             'Uma aula de', 'Vamos estudar', 'Conteúdo hoje será ']
    if i > 4:
        pal = conteudos[0]
        if pal[-1].isalpha():
            pal = pal + '.'
        elif pal[-1] == ',':
            pal = pal.replace(",", '.')
        return f'{choice(intro)} {pal}'
    else:
        i = randint(1, 50)
        if i > 20:
            return f'{choice(intro)} {choice(conteudos)}.'
        else:
            return f'{choice(intro)} {choice(conteudos)} e {choice(conteudos)}.'


def funcaoCache(frase, op='g'):
    global dados
    if op.lower() == 'c':  # comparar

        try:
            f = open('cache.json', 'r', encoding="utf-8")
        except FileNotFoundError:
            return False
        try:
            dados = json.load(f)
        except:
            dados = []
        if dados:
            for txt in dados:
                if frase.lower()+"\n" == txt.lower():
                    f.close()
                    return True
                elif frase.lower() == txt.lower():
                    f.close()
                    return True
                elif frase.lower() in txt.lower() and len(frase) > len(txt)+2:
                    f.close()
                    return True
        f.close()
        return False

    elif op.lower() == 'g':
        f = open('cache.json', 'w', encoding="utf-8")

        dados.append(frase)

        json.dump(dados, f, ensure_ascii=False)
        f.close()


def tratarInacabadas(frase):
    lista = frase.split()

    if not lista[0].isalnum() and len(lista) > 1:
        lista[1] = lista[1].capitalize()
    for sig in siglas:
        for i, item in enumerate(lista):
            if item.lower() == sig.lower():
                lista[i] = sig.upper()
            if ('.' in item or '!' in item or '?' in item or ';' in item) and item != lista[-1]:
                lista[i+1] = lista[i+1].capitalize()
            if item == lista[-1]:
                if item.isalnum() and item[-1].isalnum():
                    lista[i] = f'{item}.'
                if ':' in item and not ('.' in item or '!' in item or '?' in item):
                    lista[i] = item.replace(':', '.')
                if ',' in item and not ('.' in item or '!' in item or '?' in item):
                    lista[i] = lista[i].replace(',', '.')
                if ',' in item or '.' and ('.' in item or '!' in item or '?' in item):
                    lista[i] = lista[i].replace(',', '')
                    lista[i] = lista[i].replace('.', '')

    frase = ' '.join(lista)

    if frase[-1].isalnum():
        frase = f'{frase}.'

    return frase


def verificarNomesSiglas(texto):
    texto = re.sub(
        r'([!.?;]\s*)(\w)', lambda match: match.group(1) + match.group(2).upper(), texto)

    for nome in nomes:
        if nome.lower() in texto.lower():
            if (texto[texto.find(nome.lower()) - 1] == ' '):
                texto = texto.replace(nome.lower(), nome, -1)
    return texto


def textosNormais():
    with open("./base/maurotextos.txt") as f:
        text = f.readlines()
        text = list(set(text))

        # falta liberar os 3 pontinhos e ()
        for i in range(len(text)):
            text[i] = re.sub(
                r'[^\w\sáéíóúâêîôûàèìòùãõñçñ\'\n/:,.\-()!?;*\-|\.{1,3}]+', '', text[i])
            text[i] = re.sub(
                r"([!?]\s*)([a-z])", lambda match: match.group(1) + match.group(2).upper(), text[i])

    modeloNormal = markovify.NewlineText(text)

    fraseNormal = None
    t = randint(1, 500)

    while fraseNormal == None:
        if (t < 100):
            if (t < 10):
                fraseNormal = modeloNormal.make_short_sentence(
                    init_state=None, tries=50000, max_words=7, max_overlap_ratio=0.7, test_output=False, max_chars=280, state_size=1).strip().capitalize() + "!"
            else:
                fraseNormal = modeloNormal.make_short_sentence(
                    init_state=None, tries=50000, max_words=12, max_overlap_ratio=0.8, test_output=False, max_chars=280, state_size=3).strip().capitalize()
        elif (t < 200):
            fraseNormal = modeloNormal.make_short_sentence(
                init_state=None, tries=10000, max_words=7, max_overlap_ratio=0.7, test_output=False, max_chars=280, state_size=3).strip().capitalize()
        else:
            fraseNormal = modeloNormal.make_sentence(
                init_state=None, tries=10000, min_words=10, max_words=40, max_overlap_ratio=0.8, test_output=False, max_chars=280, state_size=4).strip().capitalize()
        l = fraseNormal.split()
        if len(l[-1]) < 5:
            fraseNormal = None

        for i in range(len(l)):
            try:
                if (len(l[i]) == 1 and l[i].isalpha()) and len(l[i+1]) == 1:
                    fraseNormal = None
            except:
                pass

    fraseNormal = verificarNomesSiglas(fraseNormal)

    return tratarInacabadas(fraseNormal)


def textosFormais():
    with open("./base/maurotextos.txt") as f:
        textos = f.readlines()
        textos = list(set(textos))

        for i in range(len(textos)):
            textos[i] = re.sub(
                r'[^\w\sáéíóúâêîôûàèìòùãõñçñ\'\n/:,.\-()!;*\-|\.{1,3}]+', '', textos[i])
            textos[i] = re.sub(
                r"([!?]\s*)([a-z])", lambda match: match.group(1) + match.group(2).upper(), textos[i])

    with open("./base/introducoes.txt") as j:
        intro = j.readlines()

        for i in range(len(intro)):
            intro[i] = re.sub(
                r'[^\w\s/áéíóúâêîôûàèìòùãõñçñ\'\n/:,*]+', '', intro[i])
            intro[i] = re.sub(
                r"([!?]\s*)([a-z])", lambda match: match.group(1) + match.group(2).upper(), intro[i])

    with open("./base/encerramentos.txt") as k:
        enc = k.readlines()
        for i in range(len(enc)):
            enc[i] = re.sub(
                r'[^\w\sáéíóúâêîôûàèìòùãõñçñ\'\n/:,.()!;?*]+', '', enc[i])
            enc[i] = re.sub(
                r"([!?]\s*)([a-z])", lambda match: match.group(1) + match.group(2).upper(), enc[i])
            enc[i] = verificarNomesSiglas(enc[i])

    modeloTextos = markovify.NewlineText(textos)
    modeloIntro = markovify.NewlineText(intro)
    modeloEnc = markovify.NewlineText(enc)

    sentencaEnc = None
    sentencaIntro = None
    sentencaTextos = None

    while sentencaEnc == None:
        sentencaEnc = modeloEnc.make_sentence(
            init_state=None, tries=5000, max_words=10, state_size=2)

    while sentencaIntro == None:
        sentencaIntro = modeloIntro.make_sentence(
            init_state=None, tries=5000, max_words=10, state_size=2)

    while sentencaTextos == None:
        sentencaTextos = modeloTextos.make_sentence(
            init_state=None, tries=50000, min_words=5, max_words=25, max_overlap_ratio=0.8, state_size=4, test_output=False)
        rec = funcaoCache(sentencaTextos, 'c')
        if rec:
            sentencaTextos = None

        l = sentencaTextos.split()
        if len(l[-1]) < 5:
            sentencaTextos = None
        else:
            for i in range(len(l)):
                try:
                    if len(l[i]) == 1 and len(l[i+1]) == 1:
                        sentencaTextos = None
                except:
                    pass

    fraseFormal = f'{sentencaIntro.strip()}:\n{tratarInacabadas(sentencaTextos.strip().capitalize())}.\n- {tratarInacabadas(sentencaEnc.strip())}'
    fraseFormal = verificarNomesSiglas(fraseFormal)
    return fraseFormal


def poesias():

    with open("./base/mauropoemas.txt") as f:
        poemas = f.readlines()
        poemas = list(set(poemas))

        for i in range(len(poemas)):
            poemas[i] = re.sub(
                r'[^\w\sáéíóúâêîôûàèìòùãõñçñ\'\n/:,.\-()!;*\?-|\.{1,3}]+', '', poemas[i])
            poemas[i].replace("\n", "")

    modeloPoemas = markovify.NewlineText(poemas)

    poema = ''
    verso = None
    for k in range(2):
        for j in range(4):
            verso = modeloPoemas.make_sentence(
                init_state=None, tries=2000, min_words=2, max_words=7, state_size=2, test_output=False).strip().capitalize()
            lV = verso.split()
            for i in range(len(lV)):
                try:
                    if len(lV[i]) <= 1 and len(lV[i+1]) <= 1:
                        verso = modeloPoemas.make_sentence(
                            init_state=None, tries=2000, min_words=2, max_words=15, state_size=2, test_output=False).strip().capitalize()
                except:
                    pass
            poema += verso + '\n'
        if (k != 1):
            poema += '\n'

    return poema


def run():
    num = randint(1, 1000)

    if num < 100:
        if num > 10:
            poema = poesias()
            tweetar(poema)
            # tweetar(poema)
        else:
            rapido = nadei()

            test = randint(1, 500)
            if test > 10:
                tweetar(rapido)
            else:
                tweetar(rapido, True)
    else:
        if num < 200:
            textoFormal = textosFormais()
            rec = funcaoCache(textoFormal, 'c')
            if rec:
                while funcaoCache(textoFormal, 'c'):
                    textoFormal = textosFormais()
            test = randint(1, 200)
            if test > 10:
                tweetar(textoFormal)
            else:
                tweetar(textoFormal, True)
            funcaoCache(textoFormal)
        else:
            i = randint(1, 200)

            if i > 30:
                texto = textosNormais()
                rec = funcaoCache(texto, 'c')
                if rec:
                    while funcaoCache(texto, 'c'):
                        texto = textosNormais()
                test = randint(1, 800)
                if test > 100:
                    tweetar(texto)
                    funcaoCache(texto)
                else:
                    test = randint(1, 2)
                    if test == 1:
                        tweetar(texto, True)
                        funcaoCache(texto)
                    else:
                        tweetar("", True)
            else:
                aulaHj = aula()
                rec = funcaoCache(aulaHj, 'c')
                if rec:
                    while funcaoCache(aulaHj, 'c'):
                        aulaHj = aula()
                tweetar(aulaHj)
                funcaoCache(aulaHj)


# run()
# agenda a tarefa em horários aleatórios entre 30 e 90min
schedule.every(randint(30, 90)).minutes.do(run)
schedule.every(30).minutes.do(procurarTweets)
# procurarTweets()

# loop principal para executar as tarefas agendadas
while True:
    schedule.run_pending()
    sleep(1)
