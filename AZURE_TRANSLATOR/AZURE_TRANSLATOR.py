import requests
from bs4 import BeautifulSoup
import json

# **Defina as configurações essenciais**
subscription_key = "YOUR_KEY"  # **Substitua com sua chave**
endpoint = "YOUR_ENDPOINT"  # **Substitua com seu endpoint**

# **Configuração dos idiomas de tradução**
source_language = "en"
target_language = "pt-br"

def extrair_texto_principal(url):
    """Extrai o texto principal de uma página web para tradução."""
    response = requests.get(url)
    response.raise_for_status()
    
    # **Parse da página usando BeautifulSoup**
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tentativa de obter o conteúdo principal
    # Muitos sites usam a tag <article> para conteúdo principal
    artigo = soup.find('article')
    if artigo:
        texto = artigo.get_text(separator=' ', strip=True)
    else:
        # Se não encontrar <article>, obtém o texto dos <p>
        paragrafos = soup.find_all('p')
        texto = ' '.join([p.get_text(separator=' ', strip=True) for p in paragrafos])

    # Limpeza final do texto (remoção de espaços excessivos e caracteres especiais)
    texto = ' '.join(texto.split())
    return texto

def traduzir_texto(texto):
    """Função para traduzir texto de inglês para português brasileiro."""
    # **URL do serviço de tradução**
    path = '/translate?api-version=3.0'
    params = f'&from={source_language}&to={target_language}'
    url = endpoint + path + params

    # **Cabeçalho e conteúdo da requisição**
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json'
    }
    body = [{'text': texto}]

    # **Faz a requisição ao serviço de tradução**
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()  # **Verifique se a requisição foi bem-sucedida**
    
    # **Extrai e retorna a tradução**
    result = response.json()
    return result[0]['translations'][0]['text']

# Exemplo de uso com URL de entrada
url = "https://exemplo.com/texto-tecnico"  # Substitua pela URL desejada
texto_principal = extrair_texto_principal(url)
texto_traduzido = traduzir_texto(texto_principal)
print(f'Tradução: {texto_traduzido}')
