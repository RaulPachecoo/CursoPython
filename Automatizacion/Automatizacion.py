#Aunque aparezaca un error funciona correctamente
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Especifica la ruta al controlador Chrome usando Service
service = Service("Drivers/chromedriver.exe")  # Ajusta esta ruta según la ubicación de tu archivo chromedriver.exe

# Ahora inicializa el navegador usando el objeto Service
driver = webdriver.Chrome(service=service)

driver.maximize_window()

# Accede a la URL deseada
driver.get("https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F%3Flocale%3Des_ES")

driver.close()
