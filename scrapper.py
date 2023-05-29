import re
import requests
from bs4 import BeautifulSoup


i = 1

# textos = re.sub('[^a-zA-Z\n\.]', ' ', textos)


def gravar(posts):
    arq = open('maurotextos.txt', '+a')
    intro = open('buffer2.txt', '+a')
    enc = open('buffer.txt', '+a')

    ehOFim = False
    if arq:
        for i in range(len(posts)):
            if posts[i] != None:

                string = str(posts[i].text)
                print(string)
                if 'Mauro Oliveira' in string:
                    ehOFim = True

                if ehOFim:
                    enc.writelines(f'{string}\n\n')
                else:
                    if len(string) >= 2 and '(' in string and ')' in string and string.find('(') < 5:
                        intro.writelines(f'{string}\n')
                    else:
                        arq.writelines(f'{string}\n')
        arq.write('\n')
    arq.close()
    intro.close()


for i in range(22):

    site = requests.get(f'https://amauroboliveira.wordpress.com/page/{i}/')
    soup = BeautifulSoup(site.content, 'html.parser')

    container = soup.find_all(class_='entry-content')
    for posts in container:
        posts = posts.find_all('p')

        for p in posts:
            for a in p.find_all('a'):
                a.decompose()

        print(posts)
        print("\n\n")
        gravar(posts)

        i += 1
