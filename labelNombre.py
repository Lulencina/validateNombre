import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe", options=options)
driver.get("https://lavandanatural.com/account/register/")
driver.maximize_window()
time.sleep(3)


requirement = ()     #Expected Result
labelObtained = ()      #Actual Result

def compareLabels():
    if requirement in labelObtained:
        print("Pass")
    else:
        print("Fail")



campoNombre = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[3]/form/div[1]/label")   
#Aquí identificamos el elemento

labelCampoNombre = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[3]/form/div[1]/label").text
#Aquí extraemos el texto dentro del elemento

labelObtained =labelCampoNombre

print(labelObtained)

requirement = 'NOMBRE'

compareLabels()


driver.close()