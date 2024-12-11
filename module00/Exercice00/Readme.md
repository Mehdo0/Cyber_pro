afin d'acceder aux cookies de cette page on a utiliser une faille XSS :

Cela consiste concretement a injecter du code javaScript dans le code html de la page grace a la balse <script> </script> .

la bonne commande est la suivante :

document.getElementById('cookieOutput').innerHTML = 'Cookie value: ' + document.cookie

concretement on va acceder a la div 'cookieOutput' et on va y inserer du code HTML qi va afficher les cookies stocker dans la variable document.cookie .

cette faille peut s'averer tres dangereuse car elle peut permettre a des user d'executer n'importe quel code java sur son site . 

d'apres owasp.org : " Les attaques XSS les plus graves impliquent la divulgation du cookie de session de l'utilisateur, ce qui permet à un attaquant de détourner la session de l'utilisateur et de prendre le contrôle du compte. D'autres attaques dommageables incluent la divulgation des fichiers de l'utilisateur final, l'installation de programmes de type cheval de Troie, la redirection de l'utilisateur vers une autre page ou un autre site, ou la modification de la présentation du contenu."
