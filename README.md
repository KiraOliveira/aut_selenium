# aut_selenium
Automação com Selenium + Python

13/11 - Iniciando configuração de ambiente.

14/11 - Finalizado configuração e primeiro scrip.
Passos que foram seguidos:

- Python
    3.8.5 - Acabei usando essa, pois não deu certo instalar a versão 3.8.2, talvez devido a minha versão do Ubuntu ser a 20.04.
    Pyenv - https://github.com/pyenv/pyenv#installation
- Editor
    Vou usar o VSCode mesmo, devido a questão do Atom na versão 20.04, não funcionar o Terminal interno.
- Browsers
    Firefox
    Chrome      
- Webdrivers
    Chromedriver - https://chromedriver.chromium.org/downloads
    Comandos usados - unzip chromedriver_linux64.zip , sudo cp chromedriver /usr/local/bin
    Geckodriver - https://github.com/mozilla/geckodriver/releases
    Comandos usados - tar xvvf geckodriver-v0.26.0-linux64.tar.gz , sudo cp geckodriver /usr/local/bin
- Docker - https://docs.docker.com/engine/install/ubuntu/


15/11 - Primeiros Scripts de Testes.

Créditos para https://www.javatpoint.com/selenium-python e Dunossauro https://www.youtube.com/watch?v=Pax0jiAcTWs&t=784s&ab_channel=EduardoMendes

Comecei com um simples:

1 - Import;
2 - Abrir o navegador;
3 - Maximizar;
4 - Acessar o Google;
5 - Buscar o site solicitado;
6 - Fechar o navegador.

Usei o Chrome nesse início.
