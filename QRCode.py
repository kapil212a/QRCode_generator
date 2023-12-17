# most eassy code for creating QRCode of any URL or as user want

import qrcode                 #importing qrcode 
qr=qrcode.QRCode(             #size , version , border define
    version=10,
    box_size=5,
    border=5
)

data=input("enter the URL or name of QR code:")             # add information in QR code
qr.add_data(data)


qr.make(fit=True)
img=qr.make_image(fill="black",back_ground="white")          #decide color and bg of QR code


img.save("image.png")                                         #save image of QRcode by its name
