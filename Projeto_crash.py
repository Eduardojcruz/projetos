import pyscreenshot 
import  cv2
import pytesseract
from time import sleep
import pyodbc
import os

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-KJN77H7\SQLEXPRESS;"
    "Database=_db_crash_;"
    "Trusted_connection = yes;"
)


print("="*40)
print("           Projeto iniciado")
print("="*40)

conexao = pyodbc.connect(dados_conexao)
print("           Conexão Bem Sucedida")
print("="*40)

cursor = conexao.cursor()

resposta = "0"
resposta_1 = "0"
resposta_2 = "0"
resposta_3 = "0"
resposta_4 = "0"

res_var_0 = "0"
res_var_1 = "0"
res_var_2 = "0"
res_var_3 = "0"
res_var_4 = "0"
res_var_5 = "0"

var_0 = "0"
var_1 = "0"
var_2 = "0"
var_3 = "0"

while True:
    resultado_crash = ""
    while resultado_crash == "":
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        image_crash = pyscreenshot.grab(bbox=(300,350, 600, 435))
        image_crash.save("Crashed.png") 
        img_crashed = cv2.imread('C:/Users/eduar/Desktop/Crashed.png')
        resultado_crash = pytesseract.image_to_string(img_crashed)
   
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    image_valor = pyscreenshot.grab(bbox=(360,430, 570, 600))
    image_valor.save("Imagem.png")
    img_t = cv2.imread('C:/Users/eduar/Desktop/Imagem.png')
    resultado = pytesseract.image_to_string(img_t)
    resultado =  resultado.split("x")
    resultado = resultado[0]
    resultado =  resultado.split("X")
    resultado = resultado[0]
    resultado =  resultado.split(")")
    resultado = resultado[0]
    resultado =  resultado.split("»")
    resultado = resultado[0]
    resultado =  resultado.split("K")
    resultado = resultado[0]
    r = resultado.split("_ ") or resultado.split("_")
    r = r[0]
    if r == ("_ ") or r == ("_"):
         resultado = r[1]
    print("\n")
    print("="*40)
    print(resultado_crash)
    print(resultado)
   
    
    teste = float(resultado)

    if resultado > "2.00":
        resposta_r = "Maior que 2x"   
    else:
        resposta_r = "Menor que 2x"
        
    if teste > 2.00:
        res_var_0 = "=> 2x"
    else:
        res_var_0  = "< 2x"


    nome_v =  f"( 1 )  ||| {resultado} |||"
    
    nome_p = f"( 1 )  ||| {res_var_0} |||"

    cursor.execute( f"""Select valor,
    ((count(validacao))*100/(select count(valor) from crash_resultado  Where valor = '{nome_v}')) as valor_prob  
	from crash_resultado
	group by valor, validacao
	having valor = '{nome_v}' and validacao = 'Maior que 2x'""")
    
    print("_"*40)
    r = cursor.fetchall()
    for i in r:
        print(i)