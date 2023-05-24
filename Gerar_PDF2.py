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

