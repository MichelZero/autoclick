
# tocando o som ao aperta uma tecla
# Path: main.py

import pygame

# Inicializa o pygame
pygame.init()

# Define o arquivo de som a ser tocado
# som = pygame.mixer.Sound('caminho/para/o/arquivo.mp3')
som = pygame.mixer.Sound('d:/Predator-michel/Music/DJ-Dimitry/topDimitry/Summer 2009 - DJ Dimitry Georgopoulos.mp3')
# "D:\Predator-michel\Music\DJ-Dimitry\topDimitry\Summer 2009 - DJ Dimitry Georgopoulos.mp3"

# Loop principal
while True:
  # Espera por um evento
  for event in pygame.event.get():
    # Se o evento for uma tecla pressionada
    if event.type == pygame.KEYDOWN:
      # Toca o som
      som.play()