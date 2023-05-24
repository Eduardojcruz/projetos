import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time

# Obter os argumentos de login e senha
login = sys.argv[1]
senha = sys.argv[2]
cam_arquivo = sys.argv[3]
nome = sys.argv[4]
email_msg = sys.argv[5]
corpo = sys.argv[6]

# Configurar as informações do servidor SMTP
host = "smtp.gmail.com"
port = 587

# Criar uma conexão com o servidor SMTP
server = smtplib.SMTP(host, port)
server.starttls()
server.login(login, senha)



# Construir o email
corpo = email_msg

email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = login
email_msg['Subject'] = corpo


email_msg.attach(MIMEText(corpo, "html"))

cam_arquivo = cam_arquivo
nome = nome

# Anexar o arquivo PDF
with open(cam_arquivo, 'rb') as attachment:
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attachment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition', f'attachment; filename={nome}')
    email_msg.attach(att)

# Enviar o email
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()
