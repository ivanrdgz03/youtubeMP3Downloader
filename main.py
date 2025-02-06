import yt_dlp
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def download_audio(link, path):
    try:
        with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': os.path.join(path,'%(title)s.mp3'),'concurrent_fragment_downloads': 5 }) as video:
            title = video.download(link)
    except Exception as e:
        messagebox.showerror("Error", "Ha ocurrido un error al descargar el audio.")
        return 1
    messagebox.showinfo("Info", f"El audio se ha descargado correctamente.")
    return 0
    

def start_download():
    link = entry.get()
    path = entry_path.get()
    if not path:
        messagebox.showerror("Error", "Por favor, elige una carpeta de destino antes de comenzar la descarga.")
        return 1
    if(link):
        if download_audio(link, path) == 0:
            entry.delete(0, tk.END)
            return 0
    else:
        messagebox.showerror("Error", "Por favor, introduce un enlace de YouTube válido.")
        return 2
        
def choose_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, directory)
        
if __name__ == "__main__":
    root = tk.Tk()
    width = 480
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.title("YouTube Audio Downloader")
    
    frame = tk.Frame(root)
    frame.pack(expand=True)

    label = tk.Label(frame, text="Introduce el enlace de YouTube", font=("Arial", 14))
    entry = tk.Entry(frame, width=50, font=("Arial", 12))
    button_path = tk.Button(frame, text="Elegir carpeta", command=choose_directory, width=15, height=2)
    button = tk.Button(frame, text="Descargar", command=start_download, width=15, height=2)
    entry_path = tk.Entry(frame, width=50)

    label.grid(row=0, column=0, columnspan=2, pady=5)
    entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
    button_path.grid(row=2, column=0, padx=5, pady=10, sticky="e")
    button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    root.mainloop()