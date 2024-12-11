# Exploitation et Analyse de la Faille CSRF

## Description

Ce projet explore la faille **CSRF (Cross-Site Request Forgery)**, une vulnérabilité critique permettant à un attaquant d'exécuter des actions malveillantes au nom d'un utilisateur authentifié. Nous avons simulé une exploitation de cette faille en créant une page malveillante capable d'effectuer un transfert d'argent à l'insu de l'utilisateur.

## Méthodologie

1. **Analyse d'une Application Web Vulnérable** :
   - Étude d'une application web contenant un formulaire de transfert d'argent sans mécanisme de protection anti-CSRF.
   - Identification de la faille via l'absence de vérifications côté serveur (ex. : jetons CSRF).

2. **Exploitation de la Faille** :
   - Création d'une page malveillante contenant un formulaire caché et un script automatisant l'envoi d'une requête POST vers le site vulnérable.
   - Exploitation de la session utilisateur active pour soumettre des actions non autorisées.
