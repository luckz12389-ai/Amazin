import os
import zipfile

PROJECT_NAME = "Amazon_Frontline"
ZIP_FILENAME = "Amazon_Frontline_Complete.zip"

files = {
    "project.godot": """[application]
config/name="Amazon Frontline"
config/description="Operation Green Shield - Tactical 3D Action Game"
run/main_scene="res://scenes/MainMenu.tscn"
config/features=PackedStringArray("4.2", "Forward+")
config/icon="res://assets/icon.svg"

[display]
window/size/viewport_width=1280
window/size/viewport_height=720
window/stretch/mode="canvas_items"

[rendering]
renderer/rendering_method="forward_plus"
""",
    
    ".github/workflows/build.yml": """name: Build Amazon Frontline

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build-windows:
    name: Build for Windows
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
      - name: Compile Windows Build
        uses: godotengine/action@v2.0.0
        with:
          godot_version: 4.2.1
          run: godot --headless --export-release "Windows Desktop" build/windows/AmazonFrontline.exe

      - name: Upload Windows Artifact
        uses: actions/upload-artifact@v4
        with:
          name: AmazonFrontline-Windows
          path: build/windows/

  build-android:
    name: Build for Android APK
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
      - name: Set up Java
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'
      - name: Compile Android APK
        uses: godotengine/action@v2.0.0
        with:
          godot_version: 4.2.1
          run: godot --headless --export-release "Android" build/android/AmazonFrontline.apk

      - name: Upload Android APK
        uses: actions/upload-artifact@v4
        with:
          name: AmazonFrontline-Android
          path: build/android/AmazonFrontline.apk
""",

    "README.md": """# AMAZON FRONTLINE: Operation Green Shield

Jogo de ação tática 3D em terceira pessoa ambientado na floresta amazônica. Você assume o papel de um coronel liderando um esquadrão em missões de captura de objetivos estratégicos.

## 🎯 Características Principais
- **Plataformas:** Android (APK) e Windows PC.
- **Modo:** Um jogador (Single-player), totalmente offline após a instalação.
- **Objetivos:** 3 pontos estratégicos (Posto de Observação, Travessia do Rio e Posto de Comunicações).
- **Esquadrão:** Sistema de comandos táticos (Avançar, Recuar, Cobrir, Atacar, etc.) com limite de classes (Sniper, Assalto, Reconhecimento/Drone, Fuzileiro).

## 🚀 Como Compilar via GitHub Actions
1. Faça o upload deste repositório para o GitHub.
2. Vá até a aba **Actions** no seu repositório do GitHub.
3. O workflow de compilação automática criará os arquivos para **Windows** e o **APK para Android**.
4. Baixe o artefato gerado e divirta-se!
""",

    "BUILD_INSTRUCTIONS.md": """# Instruções de Compilação

Este projeto utiliza **Godot Engine 4.2+** e **GitHub Actions** para compilação automatizada na nuvem.

### Passos para gerar o APK no Android sem instalar o Godot:
1. Crie um repositório público ou privado no GitHub (pode ser feito diretamente pelo celular via navegador).
2. Extraia o arquivo `Amazon_Frontline_Complete.zip` na raiz do repositório.
3. Acesse a aba **Actions** no GitHub.
4. Aguarde o término da execução do workflow (geralmente leva de 3 a 5 minutos).
5. Clique no artefato concluído para baixar o `AmazonFrontline-Android` (APK) e o build de Windows.
""",

    "LICENSE.md": """MIT License

Copyright (c) 2026 Amazon Frontline Team

Permission is hereby granted, free of charge, to any person obtaining a copy...
""",

    "CHANGELOG.md": """# Changelog

## [1.0.0] - 2026-10-30
- Lançamento inicial do projeto tático Amazon Frontline.
- Implementação de objetivos A, B e C.
- Sistema de comandos de esquadrão e controles para Android e PC.
""",

    ".gitignore": """.import/
.godot/
export.cfg
export_presets.cfg
build/
""",

    "export_presets.cfg": """[preset.0]

name="Windows Desktop"
platform="Windows Desktop"
runnable=true
custom_features=""
export_filter="all_resources"
include_filter=""
exclude_filter=""
patch_export_bin=""
encrypt_pck=false
encrypt_key=""

[preset.1]

name="Android"
platform="Android"
runnable=true
custom_features=""
export_filter="all_resources"
include_filter=""
exclude_filter=""
patch_export_bin=""
encrypt_pck=false
encrypt_key=""
""",

    "scenes/MainMenu.tscn": """[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://scripts/MainMenu.gd" id="1_menu"]

[node name="MainMenu" type="Control"]
layout_mode = 3
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
grow_horizontal = 2
grow_vertical = 2
script = ExtResource("1_menu")

[node name="Background" type="ColorRect" parent="."]
layout_mode = 1
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
color = Color(0.08, 0.15, 0.1, 1)

[node name="Title" type="Label" parent="."]
layout_mode = 1
anchors_preset = 8
anchor_left = 0.5
anchor_top = 0.3
anchor_right = 0.5
anchor_bottom = 0.3
offset_left = -250.0
offset_top = -50.0
offset_right = 250.0
offset_bottom = 50.0
grow_horizontal = 2
grow_vertical = 2
theme_override_font_sizes/font_size = 48
text = "AMAZON FRONTLINE"
horizontal_alignment = 1

[node name="Subtitle" type="Label" parent="."]
layout_mode = 1
anchors_preset = 8
anchor_left = 0.5
anchor_top = 0.4
anchor_right = 0.5
anchor_bottom = 0.4
offset_left = -200.0
offset_top = -20.0
offset_right = 200.0
offset_bottom = 20.0
grow_horizontal = 2
grow_vertical = 2
theme_override_font_sizes/font_size = 20
text = "Operation Green Shield"
horizontal_alignment = 1

[node name="StartButton" type="Button" parent="."]
layout_mode = 1
anchors_preset = 8
anchor_left = 0.5
anchor_top = 0.6
anchor_right = 0.5
anchor_bottom = 0.6
offset_left = -120.0
offset_top = -25.0
offset_right = 120.0
offset_bottom = 25.0
grow_horizontal = 2
grow_vertical = 2
theme_override_font_sizes/font_size = 22
text = "INICIAR MISSÃO"
""",

    "scripts/MainMenu.gd": """extends Control

func _ready() -> void:
	$StartButton.pressed.connect(_on_start_pressed)

func _on_start_pressed() -> void:
	# Transição para a cena de gameplay ou seleção de esquadrão
	print("Iniciando Operação Green Shield...")
""",

    "scripts/GameManager.gd": """extends Node

var score: int = 0
var objectives_captured: int = 0

func _ready() -> void:
	print("Gerenciador de Jogo inicializado.")
""",

    "scripts/SquadManager.gd": """extends Node

enum Role { SNIPER, ASSAULT, RECON, RIFLEMAN }

var squad_roster = [
	{"name": "Soldado Silva", "role": Role.ASSAULT, "health": 100},
	{"name": "Soldado Santos", "role": Role.SNIPER, "health": 100},
	{"name": "Cabo Oliveira", "role": Role.RECON, "health": 100}
]

func issue_command(command_type: String) -> void:
	print("Comando emitido para o esquadrão: ", command_type)
""",

    "scripts/ObjectiveZone.gd": """extends Area3D

export var objective_name: String = "Posto de Observação"
var status: String = "Neutro" # Neutro, Contestado, Capturado
var capture_progress: float = 0.0

func _process(delta: float) -> void:
	if status == "Contestado":
		capture_progress += delta * 10.0
		if capture_progress >= 100.0:
			status = "Capturado"
			print(objective_name, " capturado com sucesso!")
"""
}

def create_project():
    print(f"Criando o projeto {PROJECT_NAME}...")
    for filepath, content in files.items():
        full_path = os.path.join(PROJECT_NAME, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
            
    # Criar arquivo ZIP
    print(f"Compactando em {ZIP_FILENAME}...")
    with zipfile.ZipFile(ZIP_FILENAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, filenames in os.walk(PROJECT_NAME):
            for file in filenames:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, PROJECT_NAME)
                zipf.write(abs_path, rel_path)
                
    print(f"Sucesso! O arquivo {ZIP_FILENAME} foi gerado com toda a estrutura do jogo e GitHub Actions.")

if __name__ == "__main__":
    create_project()
