import tweepy
import json
import os
from time import sleep
from random import randint

ckey = ''
csecret = ''
actk = ''
actks = ''
bt = ''

# sortear as notas dos alunos


def sortearNotas(n):
    nota = randint(50, 100)

    while (nota % 5 != 0):
        nota = randint(50, 100)

    if (nota >= 80):
        apendice = f'{sortearFraseBoa()}'
    else:
        if n.lower() == 'erich falcão'.lower():
            apendice = 'PODE FAZER O L RAPAZ!!!!'
        elif n.lower() == 'Jonh Alefy'.lower():
            apendice = 'NÃO É BOT MESMO NÃO RAPAZ !!!!!!'
        else:
            apendice = f'{sortearFraseMa()}'

    pescou = sortearPescador()
    if pescou:
        if nota >= 80:
            fPescar = 'MAS VOCE ACABOU PESCANDO!!!!!! QUE COISA FEIA'
        else:
            fPescar = 'E AINDA PESCOU!!!!'
        return f'OLÁ {n.upper().strip()} RSRSRS SUA NOTA DA PROVA - {(nota/10)} , {apendice} {fPescar}'
    else:
        return f'OLÁ {n.upper().strip()} RSRSRS SUA NOTA DA PROVA - {(nota/10)} , {apendice}'


def sortearFraseBoa():
    frases = ["PARABENS !! !", "MUITO BEM !",
              "PERFEITO!!!", "BOA.. ", "DEMAIS !!!", 'SENSACIONAL!!!!', 'VOU TE DAR O RÁDIO DO MEU PAI! !!', 'UAU!!!!!',
              'PRESTOU ATENCAO NA AULA HEIN!!!!! ']
    return frases[randint(0, len(frases)-1)]

# sortear uma frase pra quem tirou nota menos que 80


def sortearFraseMa():
    frases = ["SE ESFORCE ", "TIRE SUAS DUVIDAS NA AULA ",
              "DÁ PRA MELHORAR ", "FOI QUASE", "PRESTE ATENÇÃO NOS FLIP FLOPS"]
    return frases[randint(0, len(frases)-1)]

# sortear a posição de dois pescadores


def sortearPescador():
    num = randint(1, 200)
    if (num > 50):
        return False
    else:
        return True


def tweetar(tweet, photo=False):

    client = tweepy.Client(
        consumer_key=ckey, consumer_secret=csecret, access_token=actk, access_token_secret=actks,
        bearer_token=bt
    )

    auth = tweepy.OAuthHandler(
        ckey, csecret)
    auth.set_access_token(actk, actks)

    api = tweepy.API(auth)
    if not photo:
        client.create_tweet(text=tweet)
    else:
        lista_fotos = [filename for filename in os.listdir("./photos")]
        media = api.media_upload(
            f"./photos/{lista_fotos[randint(0, len(lista_fotos)-1)]}")
        client.create_tweet(text=tweet, media_ids=[media.media_id])


def procurarTweets():
    client = tweepy.Client(
        bt, ckey, csecret, actk, actks)

    auth = tweepy.OAuthHandler(
        ckey, csecret)
    auth.set_access_token(actk, actks)

    api = tweepy.API(auth)

    try:
        with open("replies.json", "r") as f:
            tweets_respondidos = json.load(f)
    except FileNotFoundError:
        tweets_respondidos = []

    mentions = list(tweepy.Cursor(api.mentions_timeline, count=1).items(1))

    # Exibir as menções
    for mention in mentions:
        if not tweets_respondidos:
            print("Autor:", mention.user.name)
            print("ID do Tweet:", mention.id)
            tweets_respondidos = [mention.id, mention.user.id]
            with open("replies.json", "w") as f:
                json.dump(tweets_respondidos, f)
        else:
            if (mention.id != tweets_respondidos[0] and mention.user.id != tweets_respondidos[1]):
                tweets_respondidos = []
                print("Autor:", mention.user.name)
                print("ID do Tweet:", mention.id)

                i = randint(1, 2)
                if i == 1:
                    client.create_tweet(
                        in_reply_to_tweet_id=mention.id, text=sortearNotas(mention.user.name))
                else:
                    if mention.user.name.lower().strip() == 'Mestre'.lower():
                        media = api.media_upload(f"./nEhBot/duvidei.png")
                    else:
                        m = randint(1, 2)
                        if m == 1:
                            media = api.media_upload(f"./nEhBot/low.jpeg")
                        else:
                            media = api.media_upload(f"./nEhBot/neh.png")
                    client.create_tweet(text="", media_ids=[
                                        media.media_id], in_reply_to_tweet_id=mention.id)
                tweets_respondidos = [mention.id, mention.user.id]
                with open("replies.json", "w") as f:
                    json.dump(tweets_respondidos, f)
