Exploration des Failles de Sécurité : CSRF et Template Injection

Dans les deux derniers prompts, nous avons exploré deux types de vulnérabilités web : Cross-Site Request Forgery (CSRF) et Server-Side Template Injection (SSTI).

1. CSRF (Cross-Site Request Forgery)
Objectif : Comprendre comment une attaque CSRF fonctionne en exploitant une application web vulnérable pour effectuer une action non souhaitée au nom de l'utilisateur.
Méthodologie :
Nous avons observé comment un formulaire sans vérification CSRF pouvait être utilisé pour exécuter une action, comme un transfert d'argent, sans l'approbation de l'utilisateur.
En utilisant des payloads CSRF spécifiques, nous avons montré comment manipuler le comportement du serveur en utilisant des formulaires HTML non sécurisés.
Des techniques comme l'injection de script JavaScript et l'utilisation de balises <form> sans token CSRF ont été démontrées comme vecteurs d'attaque.
2. Template Injection
Objectif : Explorer comment une vulnérabilité SSTI permet à un attaquant d'exécuter du code arbitraire sur le serveur.
Méthodologie :
Nous avons utilisé des techniques pour accéder aux objets Python dans le contexte de la templating engine Jinja2, permettant d'exécuter des commandes système comme ls ou cat /etc/passwd.
En exploitant des objets Python accessibles via le MRO (Method Resolution Order), nous avons démontré comment contourner la sécurité pour accéder aux fichiers système sensibles.
