from selenium import webdriver 
import time

# abrir o navegador
navegador = webdriver.Chrome()

# iria para a página do Google Flights
link = "https://www.google.com/travel/flights/search?tfs=CBwQAhosEgoyMDI1LTA2LTEyagwIAhIIL20vMDZnbXJyEAgDEgwvZy8xcHh5eXp4M3IaLBIKMjAyNS0wNi0xOGoQCAMSDC9nLzFweHl5engzcnIMCAISCC9tLzA2Z21yQAFIAXABggELCP___________wGYAQE&hl=pt-BR&gl=BR"
navegador.get(link)

time.sleep(5)

# pegar o preço da passagem mais barata
preco = navegador.find_element("class name", "bU1Yvc").text


# preco.txt
with open("preco.txt", "w") as arquivo:
    arquivo.write(preco)



