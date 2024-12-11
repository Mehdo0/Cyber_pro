Comment éviter les failles CSRF
Pour prévenir les attaques Cross-Site Request Forgery (CSRF) dans votre application web, voici quelques bonnes pratiques :

Utiliser un token CSRF : Assurez-vous d'inclure un token CSRF dans chaque formulaire et vérifiez-le sur le serveur avant d'autoriser une requête. Utilisez un générateur de token aléatoire pour éviter les reproductions.
Vérifier l'origin de la requête : Avant d'exécuter une action, vérifiez l'origine de la requête pour s'assurer qu'elle provient du même domaine que le site web.
Limiter la portée des formulaires : N'autorisez pas les formulaires à exécuter des actions sensibles (comme les transferts d'argent) sans vérification explicite et sécurisée.
Limiter les types de requêtes autorisées : Ne permettez que les requêtes POST pour certaines actions sensibles et n'autorisez pas les requêtes GET qui pourraient être facilement manipulées.
Mettre en œuvre un cache de session : Utilisez un cache de session pour les formulaires afin d'éviter qu'un utilisateur ne soumette un formulaire avec une session expirée ou volée.