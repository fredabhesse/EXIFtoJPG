# main.py
import os
from tkinter import Tk, filedialog
from exif_processor import process_and_write_image

def select_directory():
    """
    Abre uma caixa de diálogo para que o usuário selecione um diretório.
    
    Retorna:
        str: O caminho para o diretório selecionado, ou None se a seleção for cancelada.
    """
    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title="Selecione o diretório com as imagens JPG")
    root.destroy()
    return directory

def main():
    """
    Função principal do programa.
    """
    selected_dir = select_directory()
    if not selected_dir:
        print("Nenhum diretório selecionado. Encerrando o programa.")
        return

    print(f"Processando imagens no diretório: {selected_dir}")
    for filename in os.listdir(selected_dir):
        if filename.lower().endswith(".jpg"):
            image_path = os.path.join(selected_dir, filename)
            process_and_write_image(image_path)

if __name__ == "__main__":
    main()