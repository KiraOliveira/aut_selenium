# Script para abrir o Google e buscar o site da James Delivery
# Próximo passo clicar no link

from selenium.webdriver.common.keys import Keys

from selenium import webdriver #importando o driver da web

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.google.com/")

driver.find_element_by_name("q").send_keys("james delivery")

driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

driver.close()
