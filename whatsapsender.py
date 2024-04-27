from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Função para enviar a mensagem no WhatsApp
def enviar_mensagem_whatsapp(numero, mensagem):
    # Inicializar o WebDriver do Chrome
    driver = webdriver.Chrome('caminho/para/o/chromedriver')

    # Abrir o WhatsApp Web
    driver.get('https://web.whatsapp.com/')
    input('Após fazer o login no WhatsApp Web, pressione Enter para continuar...')

    # Abrir a conversa com o número fornecido
    driver.get(f'https://web.whatsapp.com/send?phone={numero}&text={mensagem}')

    # Aguardar um pouco para que a página seja carregada completamente
    time.sleep(5)

    # Enviar a mensagem
    try:
        # Localizar o campo de entrada de mensagem e enviar a mensagem
        mensagem_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
        mensagem_input.send_keys(mensagem)
        mensagem_input.send_keys(Keys.RETURN)
        print('Mensagem enviada com sucesso!')
    except Exception as e:
        print('Erro ao enviar a mensagem:', e)

    # Fechar o navegador
    driver.quit()


# Chamar a função para enviar a mensagem
enviar_mensagem_whatsapp('41985311304', 'Teste 123')
