# Correctifs pour Prévenir les Failles CSRF

Pour protéger votre application contre les attaques CSRF, implémentez les mesures suivantes :

1. **Utilisation de Jetons CSRF** :
   - Associez un jeton unique à chaque session utilisateur.
   - Incluez ce jeton dans les formulaires ou les requêtes sensibles.
   - Validez le jeton côté serveur pour vérifier l'origine de la requête.

2. **Vérification des En-têtes HTTP** :
   - Contrôlez les en-têtes `Origin` et `Referer` pour confirmer que les requêtes proviennent d'une source légitime.

3. **Authentification Supplémentaire pour les Actions Sensibles** :
   - Demandez à l'utilisateur de confirmer les actions critiques, comme un transfert d'argent, via un mot de passe ou une authentification à deux facteurs (2FA).

4. **Mise en Place des Politiques CORS** :
   - Configurez les règles CORS pour n'accepter que les requêtes provenant de domaines de confiance.

En appliquant ces correctifs, vous renforcez la sécurité de votre application et protégez vos utilisateurs contre les attaques CSRF.
