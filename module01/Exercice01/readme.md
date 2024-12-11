Objectif:
Nous avons exploré des vulnérabilités de sécurité courantes dans les applications web : l'injection XXE (External XML Entity)

1. Injection XXE :
Nous avons travaillé avec une application Flask vulnérable permettant de parser du XML envoyé par les utilisateurs. L'objectif était de démontrer comment une attaque d'injection XXE peut être utilisée pour accéder au contenu de fichiers système, comme /etc/passwd.

Méthodologie :

Utilisation de l'entité externe : Une entité externe (<!ENTITY xxe SYSTEM "file:///etc/passwd">) est définie dans le fichier XML afin d'inclure le contenu du fichier /etc/passwd. Cette entité est utilisée pour injecter du contenu et exploiter des informations sensibles.
Formulation du XML : Le fichier XML envoyé par l'utilisateur contient cette entité externe. Lorsque l'application tente de parser le fichier XML, elle résout l'entité et affiche le contenu du fichier /etc/passwd.

Méthodologie :

Envoi de requêtes malveillantes : Une attaque CSRF implique généralement l'envoi d'une requête POST malveillante vers un site web, souvent déguisée comme une action légitime, comme une transaction financière.
Utilisation d'un cookie d'authentification : En exploitant le cookie d'authentification, l'attaquant peut effectuer des actions au nom de l'utilisateur authentifié.