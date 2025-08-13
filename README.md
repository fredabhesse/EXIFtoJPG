# Leitor e Gravador de Metadados EXIF
Este projeto é uma ferramenta simples para ler e gravar metadados EXIF em arquivos de imagem JPG. Ele permite que você extraia informações EXIF, como a data de criação e as coordenadas GPS, e as utilize para inserir um carimbo de data e hora e a localização diretamente nas fotos.

O programa abre uma janela de seleção de arquivos (File Explorer) no Windows, facilitando a escolha das imagens a serem processadas.

## Estrutura do Projeto
main.py: O script principal que contém a lógica para a interface do usuário, seleção de arquivos, leitura de metadados e gravação das informações na imagem.

exif_utils.py: Módulo com funções auxiliares para extração e manipulação dos dados EXIF.

image_processing.py: Módulo que lida com a parte de processamento da imagem, como a criação do carimbo de data e hora e a adição da informação de GPS.

requirements.txt: Lista das dependências do projeto.

## Funcionalidades
Leitura de Metadados EXIF: Extrai dados como DateTimeOriginal e GPSInfo de arquivos JPG.

Interface Gráfica Simples: Utiliza uma janela nativa do Windows para a seleção de arquivos, proporcionando uma experiência familiar e intuitiva.

Gravação de Dados na Imagem: Adiciona as informações de data e localização diretamente na foto, criando um carimbo visual.

Processamento em Lote: Suporta a seleção de múltiplos arquivos para processamento simultâneo.

