from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("Drivers/chromedriver.exe")
controlador = webdriver.Chrome(service=service)

controlador.get("https://www.facebook.com/login/?locale=es_ES")

usuario = controlador.find_element(By.CSS_SELECTOR, "input.inputtext._55r1.inputtext._1kbt.inputtext._1kbt")
clave = controlador.find_element(By.CSS_SELECTOR, "input.inputtext._55r1.inputtext._9npi.inputtext._9npi")

time.sleep(2)

usuario.send_keys("raulpachecoropero@gmail.com")
time.sleep(5)
clave.send_keys("realmadrid51212122")

time.sleep(5)

boton = controlador.find_element(By.CSS_SELECTOR, "button._42ft._4jy0._52e0._4jy6._4jy1.selected._51sy")
boton.click()

time.sleep(10)
controlador.quit()