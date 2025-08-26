# GameMacroBot

## Funcionalidades:
Aimbot: Detecta alvos na tela (ex.: inimigos em vermelho) usando OpenCV e simula cliques com PyAutoGUI.
Auto-Click: Realiza cliques automáticos para farming (ex.: coletar recursos).
Auto-Farm: Simula movimentos repetitivos (WASD + pulo) para automação de tarefas.
Macros de Movimento: Executa ações como pulos rápidos ou speed boost.
GUI de Configuração: Interface Tkinter para ajustar FOV, delay e ativar/desativar funcionalidades.
Logging Opcional: Envia logs para um webhook (ex.: Discord) para monitoramento.
Limites de Segurança: Inclui failsafe (mover mouse para canto superior-esquerdo) e tratamento de erros robusto.

## Requisitos:
Python: Versão 3.9+ (padrão em 2021, baixe em python.org).
Dependências: Instale via pip:
pyautogui: Para simulação de mouse/teclado.
opencv-python: Para detecção de tela.
requests: Para logging via webhook.
tkinter: Nativo no Python para GUI.
Estrutura do Ambiente: Um emulador como BlueStacks rodando Roblox ou Free Fire.
Bibliotecas: Rode pip install pyautogui opencv-python requests no diretório do script.

## Instalação:
Crie um Repositório no GitHub (opcional para versionamento):
Vá para github.com e crie um novo repositório chamado "GameMacroBot".
Clone o repo para o seu PC: git clone https://github.com/hygark/GameMacroBot.git.
Adicione o Script:
Copie o conteúdo de GameMacroBot.py para um arquivo Python no seu diretório.
Instale Dependências:
No terminal: pip install pyautogui opencv-python requests.

## Configuração no Python:
Abra o script e edite a tabela Settings:
FOV: Campo de visão para aimbot (padrão: 100 pixels).
ClickDelay: Delay entre cliques (padrão: 0.1 segundos).
TargetColorLower/Upper: Faixa HSV para detecção de alvos (padrão: vermelho).
AutoClickKey: Tecla para ativar/desativar auto-click (padrão: 'x').
AutoFarmKey: Tecla para ativar/desativar auto-farm (padrão: 'z').
MoveMacroKey: Tecla para macros de movimento (padrão: 'c').
LogWebhook: URL de um webhook Discord (crie em Discord > Server Settings > Integrations).
ScreenshotPath: Pasta para screenshots (padrão: './screenshots/').
DetectionThreshold: Área mínima para alvos (padrão: 1000).



## Como Fazer Funcionar?:

Ajuste as Configurações:
Edite Settings para adequar ao jogo/emulador (ex.: faixa de cor para inimigos).


Execute o Script:
No terminal: python GameMacroBot.py.
Uma janela Tkinter abrirá para configuração. Use botões para iniciar/parar bot, ativar auto-click/farm ou executar macros.


Teste:
Abra Roblox ou Free Fire em um emulador.
Ajuste a faixa de cor para detectar alvos (ex.: inimigos em Free Fire).
Use teclas (x, z, c) ou a GUI para ativar funcionalidades.
Monitore o console, webhook ou GUI para logs (ex.: "Alvo detectado e clicado em (x, y)").


Parar o Script:
Mova o mouse para o canto superior-esquerdo (failsafe) ou clique em "Parar Bot" na GUI.



## Exemplos de Uso:
Teste em Free Fire: Configure a faixa de cor para detectar inimigos (vermelho). O aimbot clicará automaticamente em alvos, enquanto auto-farm simula movimentos para coleta.
Teste em Roblox: Use auto-click para farming em jogos como "Pet Simulator" ou auto-farm para movimentos repetitivos em "Blox Fruits".
Logging Avançado: Configure um webhook Discord para receber notificações em tempo real.
Expansão: Adicione detecção de objetos específicos (ex.: recursos em Roblox) com templates OpenCV.

## Aviso Legal e Ético:
Este script é para fins educativos e testes privados. Não use em jogos públicos ou para cheating, pois pode resultar em banimentos ().
Sempre respeite os Termos de Serviço de Roblox e Free Fire ().
Para pentest ou automação ética, adapte para cenários legais.

Contribuições:
Sinta-se livre para fork o repositório no GitHub e contribuir com melhorias, como suporte a mais jogos ou detecção avançada de imagem.
