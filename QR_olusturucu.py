import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode

def qrCreate():
    url=url_girdi.get()

    if url:
        qr_url=pyqrcode.create(url)
        dosya_yolu=filedialog.asksaveasfilename(defaultextension=".svg",filetypes=[("SVG Dosyaları","*.svg")])

        if dosya_yolu:
            qr_url.svg(dosya_yolu, scale=8)
            durum_etiketi.config(text="QR Kod oluşturuldu.")

uygulama_pencere=tk.Tk()
uygulama_pencere.title("QR Kod Oluşturucu")

etiket=tk.Label(uygulama_pencere,text="URL'yi giriniz:")
url_girdi=tk.Entry(uygulama_pencere,width=40)
qr_button=tk.Button(uygulama_pencere,text="QR Kodu Oluştur",command=qrCreate)
durum_etiketi=tk.Label(uygulama_pencere,text="")

etiket.grid(row=0,column=0,padx=10,pady=10)
url_girdi.grid(row=0,column=1,padx=10,pady=10)
qr_button.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
durum_etiketi.grid(row=2,column=0,columnspan=2, padx=10,pady=10)

uygulama_pencere.mainloop()
