import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size=10,#size of the box where qr code will be displayed
    border=5 #it is the  white part of the image --border in all 4 sides with white colour

)

data ="http://localhost/food-order/"
#as i have given the at of the my channel  like the same way  you can give anything
#if you don't want to redirect and create for normal txt that write text in the quotes

qr.add_data(data)
qr.make(fit =True)
img = qr.make_image(fill="black",back_colour="white")
img.save("test.png")