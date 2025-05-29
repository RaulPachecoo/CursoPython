from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("Drivers/chromedriver.exe")
controlador = webdriver.Chrome(service=service)

controlador.get("https://www.facebook.com/login/?locale=es_ES")

usuario = controlador.find_element(By.XPATH, "//input[@id='email']")
clave = controlador.find_element(By.XPATH, "//input[@id='pass']")

time.sleep(2)

usuario.send_keys("raulpachecoropero@gmail.com")
time.sleep(5)
clave.send_keys("realmadrid51212122")

time.sleep(5)

boton = controlador.find_element(By.XPATH, "//button[@id='loginbutton']")
boton.click()

time.sleep(10)
controlador.quit()