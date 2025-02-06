import yt_dlp
import os
import tkinter as tk
from tkinter import messagebox
from PyQt5.QtWidgets import QApplication, QFileDialog

def download_audio(link, path):
    try:
        with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': os.path.join(path,'%(title)s.mp3'),'concurrent_fragment_downloads': 5 }) as video:
            title = video.download(link)
    except Exception as e:
        messagebox.showerror("Error", "Ha ocurrido un error al descargar el audio.")
        return 1
    messagebox.showinfo("Info", f"El audio se ha descargado correctamente.")
    

def start_download():
    link = entry.get()
    path = entry_path.get()
    if not path:
        messagebox.showerror("Error", "Por favor, elige una carpeta de destino antes de comenzar la descarga.")
        return 1
    if(link):
        download_audio(link, path)
        return 0
    else:
        messagebox.showerror("Error", "Por favor, introduce un enlace de YouTube válido.")
        return 2
        
def choose_directory():
    app = QApplication([])  # Crear la aplicación Qt
    directory = QFileDialog.getExistingDirectory(None, "Elegir carpeta", "")  # Abrir el selector de carpetas
    if directory:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, directory)
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("YouTube Audio Downloader")

    label = tk.Label(root, text="Introduce el enlace de YouTube")
    entry = tk.Entry(root, width=50)
    button_path = tk.Button(root, text="Elegir carpeta", command=choose_directory)
    button = tk.Button(root, text="Descargar", command=start_download)
    entry_path = tk.Entry(root, width=50)

    label.pack()
    entry.pack()
    button_path.pack(pady=5)
    button.pack()

    root.mainloop()