# image_writer.py
from PIL import Image, ImageDraw, ImageFont
import os

def write_text_on_image(image_path, text_lines):
    """
    Adiciona linhas de texto a uma imagem e a salva com um novo nome.
    
    Args:
        image_path (str): O caminho para a imagem original.
        text_lines (list): Uma lista de strings com o texto a ser adicionado.
    """
    try:
        img = Image.open(image_path)
    except (IOError, SyntaxError) as e:
        print(f"Erro ao abrir a imagem {image_path}: {e}")
        return
        
    draw = ImageDraw.Draw(img)
    try:
        # Tenta usar a fonte 'arial.ttf' se disponível, caso contrário, usa uma fonte padrão
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        print("Fonte 'arial.ttf' não encontrada. Usando a fonte padrão.")
        font = ImageFont.load_default()

    img_width, _ = img.size
    
    # Define as posições e adiciona cada linha de texto à imagem
    y_pos = 10
    text_color = "white"
    for text in text_lines:
        text_width, text_height = draw.textsize(text, font=font)
        x_pos = img_width - text_width - 10  # 10 pixels de margem à direita
        
        # Opcional: Adicionar um retângulo de fundo para o texto
        # draw.rectangle([(x_pos - 5, y_pos - 2), (x_pos + text_width + 5, y_pos + text_height + 2)], fill="black")
        
        draw.text((x_pos, y_pos), text, font=font, fill=text_color)
        y_pos += text_height + 5  # Espaçamento entre as linhas
        
    # Salva a nova imagem com um prefixo
    base, ext = os.path.splitext(os.path.basename(image_path))
    new_filename = f"gps_{base}{ext}"
    output_path = os.path.join(os.path.dirname(image_path), new_filename)
    
    try:
        img.save(output_path)
        print(f"Imagem processada salva em: {output_path}")
    except (IOError, SyntaxError) as e:
        print(f"Erro ao salvar a imagem: {e}")