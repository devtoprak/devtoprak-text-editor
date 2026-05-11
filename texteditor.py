import tkinter as tk
from tkinter import filedialog, messagebox


width=720
heigth=1280
pencere=tk.Tk()
pencere.geometry(f"{width}x{heigth}")
metin_alani=tk.Text(pencere, bg='black', fg="#39FF14")
metin_alani.pack(expand=True, fill='both')
pencere.title("devtoprak text editor")

def dosyayi_kaydet():
    dosya_yolu=filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt"),
                                                                                ("MarkDown Files", "*.md"),
                                                                                ("All Files", "*.*")
])
    if dosya_yolu:
        icerik=metin_alani.get(1.0, "end")
        with open(dosya_yolu, "w", encoding="utf-8") as dosya:
            dosya.write(icerik)
alt_cerceve=tk.Frame(pencere, bg='black')
alt_cerceve.pack(side='bottom', fill='x')
kaydet_butonu=tk.Button(alt_cerceve, bg='black', fg="#39FF14", text="Kaydet&Save", command=dosyayi_kaydet)
kaydet_butonu.pack(pady=5)

pencere.mainloop()