from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialiser le navigateur avec WebDriver Manager
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://todomvc.com/examples/angular/dist/browser/#/all')

# Ajouter un délai pour s'assurer que la page est complètement chargée
time.sleep(5)

# Fonction pour attendre que les éléments soient présents
def wait_for_element(by, value, timeout=20):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# Créer une nouvelle tâche
new_todo_input = wait_for_element(By.CLASS_NAME, 'new-todo')
new_todo_input.send_keys('Apprendre Selenium')
new_todo_input.send_keys(Keys.ENTER)

# Vérifier la création de la tâche
time.sleep(2)  # Ajouter un délai pour permettre à la tâche d'apparaître dans la liste
todo_list_items = driver.find_elements(By.CSS_SELECTOR, '.todo-list li label')
tasks = [item.text for item in todo_list_items]
assert 'Apprendre Selenium' in tasks, "La tâche 'Apprendre Selenium' n'a pas été trouvée dans la liste."

print("La tâche 'Apprendre Selenium' a été créée avec succès.")

# Fermer le navigateur
driver.quit()
