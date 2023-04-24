"""
Um teste para fazer calculos de probabilidades para o proximo numero no crash

"""

import pyscreenshot 
import  cv2
import pytesseract
from time import sleep
import pyodbc
import os

#Conexão com o sql server
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

#loop infinito que fica tirando print da tela até encontrar algo diferente de vazio para anota o valor que parou o crash

while True:
    #loop do crash
    resultado_crash = ""
    while resultado_crash == "":
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        image_crash = pyscreenshot.grab(bbox=(300,350, 600, 435))
        image_crash.save("Crash.png") 
        img_crashed = cv2.imread('C:/Users/eduar/Desktop/Crashed.png')
        resultado_crash = pytesseract.image_to_string(img_crashed)

    #print do valor que parou o crash
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    image_valor = pyscreenshot.grab(bbox=(360,430, 570, 600))
    image_valor.save("Imagem.png")
    img_t = cv2.imread('C:/Users/eduar/Desktop/Imagem.png')
    #limpando o valor
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
   
    #teste de valores e insert no banco os valores
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

    #segunda parte
    cursor.execute(f"""
                  select validacao_posibilidade, 
((count (validacao)*100)/ 
(select count(validacao_posibilidade) as total from crash_resultado
where validacao_posibilidade = '{nome_p}' ))
as possibilidade 
from crash_resultado
group by validacao_posibilidade, validacao
having validacao_posibilidade = '{nome_p}' and validacao = 'Maior que 2x'              
                   
""")
    
    r = cursor.fetchall()
    for i in r:
        print(i)
        print("_"*40)  

    if var_0 != "0":
        
        nome_c =  f"( 1 2 )  ||| {resultado} ||| {var_0} |||"
        
        nome_t =  f"( 1 2 )  ||| {res_var_0} ||| {res_var_1} |||"

        cursor.execute( f"""Select valor,
        ((count(validacao))*100/(select count(valor) from crash_resultado  Where valor = '{nome_c}')) as valor_prob  
    	from crash_resultado
    	group by valor, validacao
    	having valor = '{nome_c}' and validacao = 'Maior que 2x'""")
        
        
        y = cursor.fetchall()
        for uu in y:
            print(uu)
            print("_"*40)
        
        cursor.execute(f"""
                      select validacao_posibilidade, 
    ((count (validacao)*100)/ 
    (select count(validacao_posibilidade) as total from crash_resultado
    where validacao_posibilidade = '{nome_t}' ))
    as possibilidade 
    from crash_resultado
    group by validacao_posibilidade, validacao
    having validacao_posibilidade = '{nome_t}' and validacao = 'Maior que 2x'              
                       
    """)
    xx = cursor.fetchall()
   #terceira parte
    for ii in xx:
        print(ii)
        
    if var_1 != "0":
        
        nome_c =  f"( 1 2 3)  ||| {resultado} ||| {var_0} ||| {var_1} |||"
        
        nome_t =  f"( 1 2 3)  ||| {res_var_0} ||| {res_var_1} ||| {res_var_2} |||"

        cursor.execute( f"""Select valor,
        ((count(validacao))*100/(select count(valor) from crash_resultado  Where valor = '{nome_c}')) as valor_prob  
    	from crash_resultado
    	group by valor, validacao
    	having valor = '{nome_c}' and validacao = 'Maior que 2x'""")
        
        
        y = cursor.fetchall()
        for uu in y:
            print(uu)
       
        
        cursor.execute(f"""
                      select validacao_posibilidade, 
    ((count (validacao)*100)/ 
    (select count(validacao_posibilidade) as total from crash_resultado
    where validacao_posibilidade = '{nome_t}' ))
    as possibilidade 
    from crash_resultado
    group by validacao_posibilidade, validacao
    having validacao_posibilidade = '{nome_t}' and validacao = 'Maior que 2x'              
                       
    """)
        xx = cursor.fetchall()
        for ii in xx:
            print(ii)
            print("_"*40)  
        
    if var_2 != "0":
        
         nome_2v =  f"( 1 2 3 4 )  ||| {resultado} ||| {var_0} ||| {var_1} ||| {var_2} |||"
         
         nome_2t =   f"( 1 2 3 4 )  ||| {res_var_0} ||| {res_var_1} ||| {res_var_2} ||| {res_var_3} |||"

         cursor.execute( f"""Select valor,
         ((count(validacao))*100/(select count(valor) from crash_resultado  Where valor = '{nome_2v}')) as valor_prob  
     	from crash_resultado
     	group by valor, validacao
     	having valor = '{nome_2v}' and validacao = 'Maior que 2x'""")
         
         
         y = cursor.fetchall()
         for uu in y:
             print(uu)
        
         
         cursor.execute(f"""
                       select validacao_posibilidade, 
     ((count (validacao)*100)/ 
     (select count(validacao_posibilidade) as total from crash_resultado
     where validacao_posibilidade = '{nome_2t}' ))
     as possibilidade 
     from crash_resultado
     group by validacao_posibilidade, validacao
     having validacao_posibilidade = '{nome_2t}' and validacao = 'Maior que 2x'              
                        
     """)
         xx = cursor.fetchall()
         for ii in xx:
             print(ii)
             print("_"*40)  
                 
    if var_3 != "0":
         
            nome_3v =   f"( 1 2 3 4 5 )  ||| {resultado} ||| {var_0} |||| {var_1} ||| {var_2} ||| {var_3} |||"
            
            nome_3t =    f"( 1 2 3 4 5 )  ||| {res_var_0} ||| {res_var_1} |||| {res_var_2} ||| {res_var_3} ||| {res_var_4} |||"
            cursor.execute( f"""Select valor,
            ((count(validacao))*100/(select count(valor) from crash_resultado  Where valor = '{nome_3v}')) as valor_prob  
        	from crash_resultado
        	group by valor, validacao
        	having valor = '{nome_3v}' and validacao = 'Maior que 2x'""")
            
            
            y = cursor.fetchall()
            for uu in y:
                print(uu)
           
            
            cursor.execute(f"""
                          select validacao_posibilidade, 
        ((count (validacao)*100)/ 
        (select count(validacao_posibilidade) as total from crash_resultado
        where validacao_posibilidade = '{nome_3t}' ))
        as possibilidade 
        from crash_resultado
        group by validacao_posibilidade, validacao
        having validacao_posibilidade = '{nome_3t}' and validacao = 'Maior que 2x'              
                           
        """)
            xx = cursor.fetchall()
            for ii in xx:
                print(ii)
                print("_"*40) 
                
             
    if resposta != "0":
         print() 
         print("="*40) 
         nome_db =  f"( 1 )  ||| {resposta} |||"
         valor_db =  nome_db
         resultado_db = resultado
         validacao_db = resposta_r
         validacao_posibilidade =f"( 1 )  ||| {res_var_0} |||"
         comando = f"""insert into crash_resultado(valor, resultado, validacao,validacao_posibilidade )
         Values('{valor_db}','{resultado_db}','{validacao_db}', '{validacao_posibilidade}')"""
         cursor.execute(comando)
         cursor.commit()
         print("( 1 ) Update Realizado")
    
    if resposta_1 != "0":
        nome_db = f"( 1 2 )  ||| {resposta} ||| {resposta_1} |||"
        valor_db = nome_db
        resultado_db = resultado
        validacao_db =resposta_r
        validacao_posibilidade =f"( 1 2 )  ||| {res_var_0} ||| {res_var_1} |||"
        
        comando = f"""insert into crash_resultado(valor, resultado, validacao,validacao_posibilidade )
        Values('{valor_db}','{resultado_db}','{validacao_db}', '{validacao_posibilidade}')"""
        cursor.execute(comando)
        cursor.commit()
        print("( 1 2 ) Update Realizado")
    #quarta parte
    if resposta_2 != "0":
        nome_db = f"( 1 2 3)  ||| {resposta} ||| {resposta_1} ||| {resposta_2} |||"
        valor_db = nome_db
        resultado_db = resultado
        validacao_db = resposta_r
        validacao_posibilidade = f"( 1 2 3)  ||| {res_var_0} ||| {res_var_1} ||| {res_var_2} |||"
        
        
        comando = f"""insert into crash_resultado(valor, resultado, validacao,validacao_posibilidade )
        Values('{valor_db}','{resultado_db}','{validacao_db}', '{validacao_posibilidade}')"""
        cursor.execute(comando)
        cursor.commit()
        print("( 1 2 3) Update Realizado")
        
        
    if resposta_3 != "0":
        nome_db = f"( 1 2 3 4 )  ||| {resposta} ||| {resposta_1} ||| {resposta_2} ||| {resposta_3} |||"
        valor_db =  nome_db
        resultado_db = resultado
        validacao_db = resposta_r 
        validacao_posibilidade = f"( 1 2 3 4 )  ||| {res_var_0} ||| {res_var_1} ||| {res_var_2} ||| {res_var_3} |||"
        
        comando = f"""insert into crash_resultado(valor, resultado, validacao,validacao_posibilidade )
        Values('{valor_db}','{resultado_db}','{validacao_db}', '{validacao_posibilidade}')"""
        cursor.execute(comando)
        cursor.commit()
        print("( 1 2 3 4 ) Update Realizado")
        
    if resposta_4 != "0":
        nome_db = f"( 1 2 3 4 5 )  ||| {resposta} ||| {resposta_1} |||| {resposta_2} ||| {resposta_3} ||| {resposta_4} |||"
        valor_db = nome_db
        resultado_db = resultado
        validacao_db = resposta_r

        validacao_posibilidade = f"( 1 2 3 4 5 )  ||| {res_var_0} ||| {res_var_1} |||| {res_var_2} ||| {res_var_3} ||| {res_var_4} |||"
        
        comando = f"""insert into crash_resultado(valor, resultado, validacao,validacao_posibilidade )
        Values('{valor_db}','{resultado_db}','{validacao_db}', '{validacao_posibilidade}')"""
        cursor.execute(comando)
        cursor.commit()
        print("( 1 2 3 4 5 ) Update Realizado")
        
           
    resposta_4 = resposta_3 
    resposta_3 = resposta_2
    resposta_2 = resposta_1
    resposta_1 = resposta
    resposta = resultado
    res_var_4 = res_var_3
    res_var_3 = res_var_4
    res_var_3 = res_var_2
    res_var_2 = res_var_1
    res_var_1 = res_var_0
    var_3 = var_2
    var_2 = var_1     
    var_1 = var_0
    var_0 = resultado

    print()
    print("="*40)
    sleep(10)
    os.system('cls')