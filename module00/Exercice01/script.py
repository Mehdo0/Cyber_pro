from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
import time

# Configurer Selenium
driver = webdriver.Chrome()  # Utilisez webdriver.Firefox() si vous utilisez Firefox
driver.get("http://localhost:8080")  # Remplacez par l'URL réelle

# Charger les charges utiles depuis le fichier payload.txt
payload_file = "payload.txt"
with open(payload_file, "r", encoding="utf-8") as file:
    payloads = file.readlines()

# Variables pour suivre les tests réussis
total_payloads = len(payloads)
successful_payloads = 0

# Fonction pour gérer les alertes
def handle_alert():
    try:
        alert = driver.switch_to.alert
        alert.accept()
        return True  # Alerte gérée avec succès
    except NoAlertPresentException:
        return False  # Pas d'alerte présente

# Boucle pour exécuter chaque charge utile
for payload in payloads:
    payload = payload.strip()  # Supprimer les espaces ou sauts de ligne
    if not payload:  # Ignorer les lignes vides
        continue


    try:
        # Trouver l'input et insérer le texte
        input_field = driver.find_element(By.ID, "inputText")
        input_field.clear()  # Effacer l'input avant d'entrer un nouveau payload
        input_field.send_keys(payload)

        # Cliquer sur le bouton Submit
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
        submit_button.click()

        # Vérifier s'il y a une alerte après soumission
        if handle_alert():
            print(payload)
            successful_payloads +=1


    except UnexpectedAlertPresentException as e:
        if handle_alert():
            successful_payloads += 1

# Fermer le navigateur proprement
driver.quit()

# Calculer et afficher le taux de succès
success_rate = (successful_payloads / total_payloads) * 100
print("\n--- Résultats des tests ---")
print(f"Total de charges utiles testées : {total_payloads}")
print(f"Charges utiles réussies : {successful_payloads}")
print(f"Taux de succès : {success_rate:.2f}%")
