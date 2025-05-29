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
link_recuperacion = controlador.find_element(By.LINK_TEXT, "¿Has olvidado los datos de la cuenta?")
link_recuperacion.click()

correo = controlador.find_element(By.ID, "identify_email")
correo.send_keys("raulpachecoropero@gmail.com")

time.sleep(2)

boton_recuperacion = controlador.find_element(By.NAME, "did_submit")
boton_recuperacion.click()

time.sleep(5)

boton_recuperacion_2 = controlador.find_element(By.CLASS_NAME, "_aklu")
boton_recuperacion_2.click()

# Finalmente no se puede ya que Facebook envía un código al correo electrónico.
# En otras páginas que tienen captcha tampoco se puede.

time.sleep(5)
controlador.quit()