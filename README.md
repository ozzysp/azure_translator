# 🌐 Tradutor de Textos Técnicos com Azure AI 🌐

Bem-vindo ao projeto de **Tradutor de Textos Técnicos**! 🚀 Este projeto foi criado como parte do meu curso de introdução à Inteligência Artificial, com o objetivo de traduzir textos técnicos diretamente de páginas web. O projeto utiliza a **API de Tradução do Azure AI** para traduzir conteúdos de inglês para português brasileiro 🇧🇷.

## 📚 Visão Geral do Projeto

Neste projeto, aprendi a:
- Criar uma **conta no Azure**.
- Configurar o serviço de Tradução, obtendo a **chave de API** e o **endpoint**.
- Usar Python para conectar-se ao Azure e realizar traduções de textos.
- Extrair automaticamente o texto principal de uma URL usando web scraping.

Este projeto foi um grande desafio, especialmente na **configuração inicial do Azure** e na **obtenção da chave de API**! 🗝️

---

## 🛠️ Instalação e Configuração do Projeto

Vamos configurar o ambiente para rodar o projeto! 🖥️

### 1. Pré-requisitos

Para seguir adiante, você precisa de:
- Uma conta no [Azure](https://azure.microsoft.com/) (use o plano gratuito!).
- [Python 3](https://www.python.org/downloads/) instalado na sua máquina.
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/) para editar o código (opcional, mas recomendado).
- Uma **chave de API** e o **endpoint** do serviço de Tradução do Azure.

### 2. Configurando a Conta no Azure e Obtendo a Chave de API 🔑

1. **Acesse o [portal do Azure](https://portal.azure.com/)** e crie uma conta (use o plano gratuito).
2. No painel, **clique em "Criar um recurso"** e procure por **"Translator"**.
3. Selecione o **serviço de Tradução** (Translator) e clique em **"Criar"**.
4. Configure o serviço com as seguintes opções:
   - **Plano de Preço:** selecione o plano gratuito.
   - **Região:** escolha uma região próxima de você.
5. Clique em **Revisar + Criar** e depois em **Criar**.
6. Após a criação, vá para o recurso e copie:
   - **Chave de Assinatura (Subscription Key)**
   - **URL do Endpoint**

**Guarde bem esses dados!** Vamos precisar deles mais tarde para configurar nosso código.

### 3. Clonar o Projeto e Instalar Dependências 📁

1. **Clone este repositório** ou baixe o código do projeto.
2. Abra o terminal no VS Code e crie um ambiente virtual:
```bash
   python -m venv venv
```

No windows
```bash
  .\venv\Scripts\activate
```
Mac/Linux
```bash
  source venv/bin/activate
```

Instale as dependências
```bash
  pip install requests beautifulsoup4
```
4. Configurar e Rodar o Projeto ⚙️
Abra o arquivo translator.py e insira suas informações do Azure:

Substitua "YOUR_KEY" pela sua chave de API.
Substitua "YOUR_ENDPOINT" pelo seu endpoint.
No terminal, com o ambiente virtual ativo, execute o código:

```bash
  python translator.py
```
O programa irá acessar a URL que você especificou, extrair o texto principal e traduzi-lo para o português brasileiro! 🎉

📝 Estrutura do Código
O código possui duas funções principais:

extrair_texto_principal(url): Obtém o texto principal da página web usando web scraping.
traduzir_texto(texto): Traduz o texto de inglês para português brasileiro usando a API de Tradução do Azure.
Exemplo de Uso
Para rodar o código, basta inserir a URL desejada no código e executar o comando python translator.py no terminal. A saída mostrará o texto traduzido diretamente no console!

🙏 Agradecimentos
Este projeto só foi possível graças ao curso de introdução à IA que me guiou em cada passo do caminho. Foi um desafio, mas também uma oportunidade de crescer e aprender mais sobre o mundo da programação e da Inteligência Artificial.

Obrigado a todos os professores e colegas que me ajudaram! Espero continuar minha jornada e aprender ainda mais sobre IA e desenvolvimento de software. 🚀

🎉 Próximos Passos
Esse é só o começo! Quero aprimorar o projeto, adicionando novos recursos e tentando expandir minhas habilidades. 😄

📫 Dúvidas? Entre em contato!
Se tiver alguma dúvida sobre o código ou sobre como configurá-lo, sinta-se à vontade para entrar em contato comigo.

Agora você está pronto para rodar o projeto e começar a traduzir seus próprios textos técnicos diretamente da web!




