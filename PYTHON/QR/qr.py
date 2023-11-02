from PIL import ImageTk ,Image, ImageDraw, ImageFont
import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox



def generar_qr():
    link = entry_link.get()

    # Generar el QR
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#13152E", back_color="white")
    
    #cambiar tamano de qr
    newSize = 310
    qr_img = qr_img.resize((newSize,newSize))

    #llamo el logo
    logo = Image.open("recursos/logo.png")
    logoSize = logo.size
    ancho = logoSize[0]
    alto = logoSize[1]
    print(logoSize)

    #crear imagen con los datos faltantes
    width, height = 279, 310
    imagen = Image.new("RGB", (width, height), color="white")
    dibujar = ImageDraw.Draw(imagen)
    fuente = ImageFont.truetype("arial.ttf", size=25)
    odt = odtEntry.get()
    fecha = fechaEntry.get()
    texto = f"\nODT: {odt}\nFECHA: {fecha}"
    dibujar.text((20, 100), texto, font=fuente, fill="#13152E")

    #llamo a la foto de datos
    datos = Image.open("recursos/datos.png")
    
    #pegar todas las imagenes
    final = Image.new("RGB",(logo.size[0],500),color="white")
    final.paste(logo,(0,0))
    final.paste(qr_img,(0,alto))
    final.paste(datos,(0,438))
    final.paste(imagen,(310,128))
    
    
    #cambiar el tamano de imagen final
    # finalSize = final.size
    # final = final.resize(((finalSize[0]-300),(finalSize[1]-250)))

    QRfinal = ImageTk.PhotoImage(final)
    qr_label.config(image=QRfinal)
    qr_label.image = QRfinal


def guardar_qr():
    qr_img = qr_label.image
    qr_img = ImageTk.getimage(qr_img)
    if qr_img:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Imágenes PNG", "*.png")])
        if file_path:
            qr_img.save(file_path)
            messagebox.showinfo("QR Guardado", "El QR se ha guardado exitosamente.")

# Crear la ventana principal
window = tk.Tk()
window.title("Generador de QR con Logo")
window.geometry("600x600")

# Crear campo de texto para el enlace
label_link = tk.Label(window, text="Enlace:")
label_link.pack()
entry_link = tk.Entry(window)
entry_link.pack()

#crear campos para fecha y odt
odtLabel = tk.Label(window, text="ODT")
odtLabel.pack()
odtEntry = tk.Entry(window)
odtEntry.pack()
fechaLabel = tk.Label(window, text="FECHA")
fechaLabel.pack()
fechaEntry = tk.Entry(window)
fechaEntry.pack()

# Crear el botón de generación de QR
btn_generar = tk.Button(window, text="Generar QR", command=generar_qr)
btn_generar.pack()

# Crear el botón de guardar QR
btn_guardar = tk.Button(window, text="Guardar QR", command=guardar_qr)
btn_guardar.pack()

# Mostrar el QR generado
qr_label = tk.Label(window, text="imgaen del QR")
qr_label.pack(pady=10)



# Ejecutar la ventana
window.mainloop()



