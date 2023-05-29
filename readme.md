# Bot do Mauro 

O bot do Mauro foi uma pequena brincadeira idealizada por mim e alguns amigos da faculdade pro Twitter, em *homenagem* ao profº Mauro OIiveira. 
Foi codificado inteiramente por mim em 2 semanas, e provavelmente não irão haver mais atualizações.

## Beautiful Soup 4 (Web-Scrapping)

O *BS4* foi usado somente para fazer o Web-Scrapping inicial dos textos do professor Mauro Oliveira, para que eu conseguisse tanto classificá-los 
(em textos, poemas ou artigos acadêmicos) quanto para que eu conseguisse treinar o meu modelo de Markov para que gerasse as frases.

## Markov Chains 

Utilizei a biblioteca **Markovify** em Python para organizar os textos e treinar o modelo para gerar as frases. Elas costumam não fazer 100% de sentido. Achamos que seria mais engraçado se fosse assim.
> Comentário: Minha intenção inicial era fazer com *GPT-2*, mas infelizmente meu computador atual não consegue suportar. Talvez, isso tenha deixado o bot mais engraçado.

## Tweepy (Manipular a API do Twitter)

Por fim, utilizei a biblioteca do Tweepy pra fazer a conexão com a API do Twitter, basicamente criar tweets e responder tweets.

