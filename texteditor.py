import sys
import tkinter as tk
from tkinter import filedialog, messagebox


width=720
heigth=1280
pencere=tk.Tk()
pencere.geometry(f"{width}x{heigth}")
metin_alani=tk.Text(pencere, bg='black', fg="#39FF14", insertbackground='white', selectbackground='yellow', selectforeground='black')
metin_alani.pack(expand=True, fill='both')
pencere.title("devtoprak text editor")

def dosya_ac():
    dosya_yolu=filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("MarkDown Files", "*.md"), ("All Files", "*.*")])
    if dosya_yolu:
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            metin_alani.delete("1.0", "end")
            metin_alani.insert("1.0", dosya.read())

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
kaydet_butonu.pack(side='left', pady=5, padx=5)
ac_butonu = tk.Button(alt_cerceve, bg='black', fg='#39FF14', text='Dosya Aç&Open File', command=dosya_ac)
ac_butonu.pack(side='left', padx=5, pady=5)

if len(sys.argv) > 1:
    gelen_dosya=sys.argv[1]
    with open(gelen_dosya, "r", encoding="utf-8") as f:
        metin_alani.insert("1.0", f.read())
pencere.mainloop()

