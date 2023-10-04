import qrcode

img=qrcode.make("https://www.youtube.com/watch?v=Tio09Zf5ekg")
img.save("mycode.png")