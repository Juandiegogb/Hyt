import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image

def insert_images_from_folder(pdf_filename, folder_path):
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    story = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_path = os.path.join(folder_path, filename)
            story.append(Image(image_path))

    doc.build(story)

def main():
    # Nombre del archivo PDF a generar
    pdf_filename = 'recursos/archivo.pdf'

    # Carpeta que contiene las imágenes
    folder_path = 'recursos'

    # Generar el archivo PDF con las imágenes
    insert_images_from_folder(pdf_filename, folder_path)

if __name__ == "__main__":
    main()
