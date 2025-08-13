# exif_processor.py
import exifread
from image_writer import write_text_on_image

def get_exif_data(image_path):
    """
    Lê e retorna os metadados EXIF de uma imagem.
    
    Args:
        image_path (str): O caminho para a imagem.
        
    Retorna:
        dict: Um dicionário com os metadados EXIF, ou None se houver erro.
    """
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
            return tags
    except (IOError, SyntaxError) as e:
        print(f"Erro ao ler os metadados EXIF do arquivo {image_path}: {e}")
        return None

def convert_coordinates(coordinates, hemisphere):
    """
    Converte as coordenadas no formato 'graus,minutos,segundos' para uma string formatada.
    
    Args:
        coordinates (str): A string de coordenadas.
        hemisphere (str): A string do hemisfério (N, S, E, W).
        
    Retorna:
        str: As coordenadas formatadas.
    """
    try:
        parts = str(coordinates).strip('[]').replace(' ', '').split(',')
        if len(parts) < 3:
            return "Coordenada Inválida"
            
        degrees = abs(int(parts[0]))
        minutes = int(parts[1])
        # Converte a fração para segundos e arredonda
        numerator, denominator = map(int, parts[2].split('/'))
        seconds = round(numerator / denominator)
        
        return f"{degrees}°{minutes}'{seconds}\" {hemisphere}"
    except (ValueError, IndexError):
        return "Coordenada Inválida"

def format_date(date_string):
    """
    Formata a data de "YYYY:MM:DD" para "DD/MM/YYYY".
    
    Args:
        date_string (str): A string da data no formato "YYYY:MM:DD".
        
    Retorna:
        str: A data formatada.
    """
    try:
        year, month, day = date_string.split(":")
        return f"{day}/{month}/{year}"
    except (ValueError, IndexError):
        return "Data Inválida"

def process_and_write_image(image_path):
    """
    Extrai dados EXIF, formata as informações e escreve na imagem.
    
    Args:
        image_path (str): O caminho para a imagem a ser processada.
    """
    tags = get_exif_data(image_path)
    if not tags:
        return

    try:
        # Extrai os dados
        gps_latitude = tags.get('GPS GPSLatitude')
        gps_latitude_ref = tags.get('GPS GPSLatitudeRef')
        gps_longitude = tags.get('GPS GPSLongitude')
        gps_longitude_ref = tags.get('GPS GPSLongitudeRef')
        datetime_original = tags.get('EXIF DateTimeOriginal')

        if not all([gps_latitude, gps_latitude_ref, gps_longitude, gps_longitude_ref, datetime_original]):
            print(f"Metadados GPS ou de data não encontrados no arquivo: {image_path}")
            return

        # Converte e formata as informações
        latitude_str = convert_coordinates(gps_latitude, gps_latitude_ref.values)
        longitude_str = convert_coordinates(gps_longitude, gps_longitude_ref.values)
        date_str = format_date(str(datetime_original).split(' ')[0])

        # Cria as linhas de texto para a imagem
        text_lines = [
            f"Lat: {latitude_str}",
            f"Lon: {longitude_str}",
            f"Data: {date_str}"
        ]

        # Chama a função de gravação da imagem
        write_text_on_image(image_path, text_lines)

    except Exception as e:
        print(f"Erro ao processar dados EXIF para {image_path}: {e}")