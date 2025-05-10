import yt_dlp
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import sys

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
    directory = filedialog.askdirectory(title="Seleccionar carpeta de destino")
    if directory:
        entry_path.config(state=tk.NORMAL)
        entry_path.delete(0, tk.END)
        entry_path.insert(0, directory)
        entry_path.config(state='readonly')


def show_context_menu(event):
    widget = event.widget
    if widget.winfo_exists():
        try:
            context_menu.post(event.x_root, event.y_root)
        finally:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    width = 480
    height = 250
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.title("YouTube Audio Downloader")

    frame = tk.Frame(root)
    frame.pack(expand=True, padx=20, pady=20)

    label = tk.Label(frame, text="Introduce el enlace de YouTube", font=("Arial", 12))
    entry = tk.Entry(frame, width=50, font=("Arial", 10))

    label_path = tk.Label(frame, text="Carpeta de destino", font=("Arial", 12))
    entry_path = tk.Entry(frame, width=50, font=("Arial", 10)) 

    button_path = tk.Button(frame, text="Elegir carpeta", command=choose_directory, font=("Arial", 10))
    button = tk.Button(frame, text="Descargar", command=start_download, font=("Arial", 10))


    label.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")
    entry.grid(row=1, column=0, columnspan=2, pady=5, sticky="we")

    label_path.grid(row=2, column=0, columnspan=2, pady=5, sticky="w") 
    entry_path.grid(row=3, column=0, columnspan=2, pady=5, sticky="we")
    entry_path.config(state='readonly')

    button_path.grid(row=4, column=0, padx=5, pady=10, sticky="e")
    button.grid(row=4, column=1, padx=5, pady=10, sticky="w")

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    context_menu = tk.Menu(root, tearoff=0, font=("Arial", 12))

    context_menu.add_command(label="Pegar", command=lambda: root.focus_get().event_generate("<<Paste>>"))
    context_menu.add_command(label="Borrar", command=lambda: root.focus_get().delete(0, tk.END))

    if sys.platform == "darwin":
        right_click_event = "<Button-2>"
    else:
        right_click_event = "<Button-3>"

    entry.bind(right_click_event, show_context_menu)
    entry_path.bind(right_click_event, show_context_menu)

    root.mainloop()