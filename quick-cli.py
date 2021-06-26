# uploading images
from instapy_cli import client


#show = ipy(username="greyCups50", password="Pearl%75")

username = 'greyCup50'
userPass = 'Pearl%75'

image = './images/image1.png'

text = "no caption needed" + "\r\n" + "#coolpics #beautiful"

with client(username, userPass) as cli:
    cli.upload(image, text)










