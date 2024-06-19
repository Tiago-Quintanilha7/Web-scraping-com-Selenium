from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)





navegador.get('https://www.hashtagtreinamentos.com/?origemurl=75502579145&gad_source=1&gclid=Cj0KCQjw4MSzBhC8ARIsAPFOuyV8pjgdW7DZGIYZY6NGMv9q0gm1Pkxh2KVXMRVLWXiLQRtywRn2NrcaAnyqEALw_wcB')
navegador.find_element(By.ID, 'firstname').send_keys('Tiago')
navegador.find_element(By.ID, 'email').send_keys('tiago@gmail.com')
navegador.find_element(By.CLASS_NAME, 'botao-formulario').click()







input('press enter')



