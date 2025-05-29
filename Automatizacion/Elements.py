from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("Drivers/chromedriver.exe")
controlador = webdriver.Chrome(service=service)

controlador.get("https://www.facebook.com/login/?locale=es_ES")

varios = controlador.find_elements(By.CLASS_NAME, "textinput")
time.sleep(5)
for elemento in varios:
    elemento.send_keys("Hola")
    time.sleep(5)