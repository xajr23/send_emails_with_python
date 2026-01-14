import smtplib #smtp es un protocolo para que los mails pasen de compu a compu
from email.message import EmailMessage
from string import Template #nos va a permitir sustituir texto con $ por variables
from pathlib import Path #nos va a permitir acceder a index.html

#Accedemos a index.html con Path. Usamos read_text para que lo lea como un string. 
# Usamos template para poder usar .substitute
html = Template(Path("index.html").read_text())

email = EmailMessage()
email["from"] = "Xavier Jimenez"
email["to"] = "xajr23@gmail.com"
email["subject"] = "You won 1.000.000 dollars"

#usamos html de 2do parametro para que envie el contenido y lo analice de acuerdo a q es un archivo html
email.set_content(html.substitute({"name": "TinTin"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() #parte del protocolo smtp y es como un saludo
    smtp.starttls() #tls es un mecanismo de cifrado para conectarnos de manera segura al servidor smtp
    smtp.login("pythoncourse2310@gmail.com", "mkei cjqn ytvm fnkl") #ponemos el correo q va a enviar el mail
    smtp.send_message(email)
    print("all good")