from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Configurar el servicio para usar ChromeDriver
service = Service("Drivers/chromedriver.exe")
controlador = webdriver.Chrome(service=service)

# Abrir la página de Facebook
controlador.get("https://www.facebook.com/login/?locale=es_ES")

time.sleep(2)
# Accede a cada elemento de la página a través de su id
usuario = controlador.find_element(By.CLASS_NAME, "_1kbt")
clave = controlador.find_element(By.CLASS_NAME, "_9npi")

time.sleep(2)

# Enviar los datos al formulario
usuario.send_keys("raulpachecoropero@gmail.com")
time.sleep(5)
clave.send_keys("realmadrid51212122")
time.sleep(5)

# Accede al botón de inicio de sesión
boton = controlador.find_element(By.CLASS_NAME, "_42ft")
boton.click()

time.sleep(10)
controlador.quit()