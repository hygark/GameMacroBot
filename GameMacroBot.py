# GameMacroBot.py - Bot de automação para Roblox e Free Fire (2021)
# Criado por hygark (2021)
# Descrição: Script Python para automação em Roblox/Free Fire, com aimbot, auto-click, auto-farm e macros de movimento. Usa PyAutoGUI para inputs, OpenCV para detecção de tela e Tkinter para GUI.
# Nota: Use apenas para testes educacionais em ambientes privados. Automação em jogos pode violar os Termos de Serviço de Roblox/Free Fire.

import pyautogui
import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
import time
import threading
import requests
import os

# Configurações personalizáveis
Settings = {
    'FOV': 100,  # Campo de visão para aimbot (pixels)
    'ClickDelay': 0.1,  # Delay entre cliques (segundos)
    'TargetColorLower': (0, 100, 100),  # Faixa HSV inferior para alvos (ex.: vermelho)
    'TargetColorUpper': (10, 255, 255),  # Faixa HSV superior
    'AutoClickKey': 'x',  # Tecla para ativar/desativar auto-click
    'AutoFarmKey': 'z',  # Tecla para ativar/desativar auto-farm
    'MoveMacroKey': 'c',  # Tecla para macros de movimento
    'LogWebhook': '',  # URL de webhook para logging (ex.: Discord)
    'ScreenshotPath': './screenshots/',  # Pasta para screenshots
    'DetectionThreshold': 1000,  # Área mínima para considerar alvo
    'StopFlag': False,  # Flag para parar o script
}

# Estado do script
ScriptState = {
    'IsRunning': False,
    'AutoClickActive': False,
    'AutoFarmActive': False,
    'TotalDetections': 0,
    'TotalClicks': 0,
    'TotalFarmCycles': 0,
}

# Função para enviar logs (console e webhook)
def log_message(level, message):
    print(f"[{level}] [{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}")
    if Settings['LogWebhook']:
        try:
            requests.post(Settings['LogWebhook'], json={'content': f'[{level}] GameMacroBot: {message}'})
        except Exception as e:
            print(f"[ERROR] Falha ao enviar log: {e}")

# Função para capturar e processar tela
def detect_targets():
    try:
        # Capturar screenshot
        screenshot = pyautogui.screenshot()
        img_rgb = np.array(screenshot.rgb)
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
        img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

        # Detectar alvos na faixa de cor
        mask = cv2.inRange(img_hsv, Settings['TargetColorLower'], Settings['TargetColorUpper'])
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        targets = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > Settings['DetectionThreshold']:
                x, y, w, h = cv2.boundingRect(contour)
                targets.append({'x': x + w // 2, 'y': y + h // 2, 'area': area})
                ScriptState['TotalDetections'] += 1
        return targets[:5]  # Limitar a 5 alvos por frame
    except Exception as e:
        log_message('ERROR', f'Erro ao processar imagem: {e}')
        return []

# Função para aimbot
def aimbot():
    targets = detect_targets()
    if targets:
        for target in targets:
            pyautogui.moveTo(target['x'], target['y'])
            pyautogui.click()
            ScriptState['TotalClicks'] += 1
            log_message('INFO', f'Alvo detectado e clicado em ({target["x"]}, {target["y"]})')
            time.sleep(Settings['ClickDelay'])

# Função para auto-click
def auto_click():
    while ScriptState['AutoClickActive'] and not Settings['StopFlag']:
        pyautogui.click()
        ScriptState['TotalClicks'] += 1
        log_message('INFO', 'Auto-click executado')
        time.sleep(Settings['ClickDelay'])

# Função para auto-farm (ex.: movimentos repetitivos)
def auto_farm():
    moves = ['w', 'a', 's', 'd', 'space']  # Simula WASD + pulo
    while ScriptState['AutoFarmActive'] and not Settings['StopFlag']:
        for move in moves:
            pyautogui.keyDown(move)
            time.sleep(0.1)
            pyautogui.keyUp(move)
        ScriptState['TotalFarmCycles'] += 1
        log_message('INFO', 'Ciclo de auto-farm executado')
        time.sleep(0.5)

# Função para macros de movimento (ex.: speed boost ou pulo)
def move_macro():
    # Simula pulo rápido ou movimento (ex.: Free Fire fly/speed)
    pyautogui.keyDown('space')
    time.sleep(0.1)
    pyautogui.keyUp('space')
    pyautogui.keyDown('shift')
    time.sleep(0.1)
    pyautogui.keyUp('shift')
    log_message('INFO', 'Macro de movimento executado')

# Função principal do bot
def run_bot():
    if ScriptState['IsRunning']:
        log_message('ERROR', 'Bot já está em execução!')
        return
    ScriptState['IsRunning'] = True
    log_message('INFO', 'GameMacroBot iniciado.')

    # Criar pasta para screenshots
    if not os.path.exists(Settings['ScreenshotPath']):
        os.makedirs(Settings['ScreenshotPath'])

    # Loop principal
    while not Settings['StopFlag']:
        aimbot()
        time.sleep(0.1)  # Evitar sobrecarga

    ScriptState['IsRunning'] = False
    log_message('INFO', 'GameMacroBot parado.')

# GUI com Tkinter
class MacroBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('GameMacroBot - Inflavelle')
        self.root.geometry('400x300')

        # Labels e inputs
        tk.Label(root, text='GameMacroBot', font=('Arial', 16, 'bold')).pack(pady=10)
        tk.Label(root, text='FOV (pixels):').pack()
        self.fov_entry = tk.Entry(root)
        self.fov_entry.insert(0, str(Settings['FOV']))
        self.fov_entry.pack()

        tk.Label(root, text='Click Delay (s):').pack()
        self.delay_entry = tk.Entry(root)
        self.delay_entry.insert(0, str(Settings['ClickDelay']))
        self.delay_entry.pack()

        # Botões
        tk.Button(root, text='Iniciar Bot', command=self.start_bot).pack(pady=5)
        tk.Button(root, text='Parar Bot', command=self.stop_bot).pack(pady=5)
        tk.Button(root, text='Ativar Auto-Click', command=self.toggle_auto_click).pack(pady=5)
        tk.Button(root, text='Ativar Auto-Farm', command=self.toggle_auto_farm).pack(pady=5)
        tk.Button(root, text='Executar Macro de Movimento', command=self.run_move_macro).pack(pady=5)
        tk.Button(root, text='Salvar Configurações', command=self.save_settings).pack(pady=5)

        # Log
        self.log_text = tk.Text(root, height=5, width=50)
        self.log_text.pack(pady=10)

        # Listener de teclas
        pyautogui.FAILSAFE = True  # Mover mouse para canto superior-esquerdo para parar
        self.root.bind('<KeyPress>', self.key_listener)

    def log(self, message):
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)

    def start_bot(self):
        threading.Thread(target=run_bot, daemon=True).start()
        self.log('Bot iniciado.')

    def stop_bot(self):
        Settings['StopFlag'] = True
        ScriptState['AutoClickActive'] = False
        ScriptState['AutoFarmActive'] = False
        self.log('Bot parado.')

    def toggle_auto_click(self):
        ScriptState['AutoClickActive'] = not ScriptState['AutoClickActive']
        if ScriptState['AutoClickActive']:
            threading.Thread(target=auto_click, daemon=True).start()
            self.log('Auto-click ativado.')
        else:
            self.log('Auto-click desativado.')

    def toggle_auto_farm(self):
        ScriptState['AutoFarmActive'] = not ScriptState['AutoFarmActive']
        if ScriptState['AutoFarmActive']:
            threading.Thread(target=auto_farm, daemon=True).start()
            self.log('Auto-farm ativado.')
        else:
            self.log('Auto-farm desativado.')

    def run_move_macro(self):
        threading.Thread(target=move_macro, daemon=True).start()
        self.log('Macro de movimento executado.')

    def save_settings(self):
        Settings['FOV'] = int(self.fov_entry.get())
        Settings['ClickDelay'] = float(self.delay_entry.get())
        self.log('Configurações salvas.')

    def key_listener(self, event):
        if event.keysym == Settings['AutoClickKey']:
            self.toggle_auto_click()
        elif event.keysym == Settings['AutoFarmKey']:
            self.toggle_auto_farm()
        elif event.keysym == Settings['MoveMacroKey']:
            self.run_move_macro()

# Iniciar GUI
if __name__ == '__main__':
    pyautogui.PAUSE = 0.01  # Reduzir latência de inputs
    root = tk.Tk()
    app = MacroBotGUI(root)
    root.mainloop()