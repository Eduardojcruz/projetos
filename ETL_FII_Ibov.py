import requests
import pandas as pd


url = "https://statusinvest.com.br/category/advancedsearchresult"

querystring = {"search":"{\"Segment\":\"\",\"Gestao\":\"\",\"my_range\":\"0;20\",\"dy\":{\"Item1\":null,\"Item2\":null},\"p_vp\":{\"Item1\":null,\"Item2\":null},\"percentualcaixa\":{\"Item1\":null,\"Item2\":null},\"numerocotistas\":{\"Item1\":null,\"Item2\":null},\"dividend_cagr\":{\"Item1\":null,\"Item2\":null},\"cota_cagr\":{\"Item1\":null,\"Item2\":null},\"liquidezmediadiaria\":{\"Item1\":null,\"Item2\":null},\"patrimonio\":{\"Item1\":null,\"Item2\":null},\"valorpatrimonialcota\":{\"Item1\":null,\"Item2\":null},\"numerocotas\":{\"Item1\":null,\"Item2\":null},\"lastdividend\":{\"Item1\":null,\"Item2\":null}}","CategoryType":"2"}

payload = ""
headers = {
    "cookie": "_adasys=b5e71c3e-3f06-4eb9-9eca-c07c1632580d; _gcl_au=1.1.1405140049.1673352303; _ga=GA1.3.2082132420.1673352303; _gid=GA1.3.899018268.1673352303; __cf_bm=eEfXrCisvAnvsGuk_FRtXPqmD6r70wQCmnoLS.m9i8I-1673352327-0-AYDSqkLDqGUK+Cp1XchA1fEOi/AZApuSlGpuma10PdaDwipP2HbFFBBmnxmf3W0TB8mTURp2geYsTTKeMeIhwW/iCAaIlC1WzEQIbDiyQOll0LfJZtcFF763vOgex6nNh8r0/7hREEhYMpnYnd3r3BQ=; __hstc=176625274.97b853aac05fe8eed90568d877dbaa8b.1673352332284.1673352332284.1673352332284.1; hubspotutk=97b853aac05fe8eed90568d877dbaa8b; __hssrc=1; __hssc=176625274.1.1673352332284; _fbp=fb.2.1673352333340.1958066890; _gat_UA-142136095-1=1",
    "authority": "statusinvest.com.br",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer": "https://statusinvest.com.br/fundos-imobiliarios/busca-avancada",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

json_res = response.json()
res = []

for i in json_res:
    res.append(i)

df = pd.json_normalize(res)
df = pd.DataFrame(df)
df.to_csv('FII.csv', encoding='utf-8', index=False, sep=';',decimal =',' )