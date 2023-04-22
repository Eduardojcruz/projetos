import requests
import pandas as pd

url = "https://statusinvest.com.br/category/advancedsearchresult"

querystring = {"search":"{\"Segment\":\"\",\"my_range\":\"-20;100\",\"forecast\":{\"upsideDownside\":{\"Item1\":null,\"Item2\":null},\"estimatesNumber\":{\"Item1\":null,\"Item2\":null},\"revisedUp\":true,\"revisedDown\":true,\"consensus\":[]},\"dy\":{\"Item1\":null,\"Item2\":null},\"p_L\":{\"Item1\":null,\"Item2\":null},\"peg_Ratio\":{\"Item1\":null,\"Item2\":null},\"p_VP\":{\"Item1\":null,\"Item2\":null},\"p_Ativo\":{\"Item1\":null,\"Item2\":null},\"margemBruta\":{\"Item1\":null,\"Item2\":null},\"margemEbit\":{\"Item1\":null,\"Item2\":null},\"margemLiquida\":{\"Item1\":null,\"Item2\":null},\"p_Ebit\":{\"Item1\":null,\"Item2\":null},\"eV_Ebit\":{\"Item1\":null,\"Item2\":null},\"dividaLiquidaEbit\":{\"Item1\":null,\"Item2\":null},\"dividaliquidaPatrimonioLiquido\":{\"Item1\":null,\"Item2\":null},\"p_SR\":{\"Item1\":null,\"Item2\":null},\"p_CapitalGiro\":{\"Item1\":null,\"Item2\":null},\"p_AtivoCirculante\":{\"Item1\":null,\"Item2\":null},\"roe\":{\"Item1\":null,\"Item2\":null},\"roic\":{\"Item1\":null,\"Item2\":null},\"roa\":{\"Item1\":null,\"Item2\":null},\"liquidezCorrente\":{\"Item1\":null,\"Item2\":null},\"pl_Ativo\":{\"Item1\":null,\"Item2\":null},\"passivo_Ativo\":{\"Item1\":null,\"Item2\":null},\"giroAtivos\":{\"Item1\":null,\"Item2\":null},\"receitas_Cagr5\":{\"Item1\":null,\"Item2\":null},\"lucros_Cagr5\":{\"Item1\":null,\"Item2\":null},\"liquidezMediaDiaria\":{\"Item1\":null,\"Item2\":null},\"vpa\":{\"Item1\":null,\"Item2\":null},\"lpa\":{\"Item1\":null,\"Item2\":null},\"valorMercado\":{\"Item1\":null,\"Item2\":null}}","CategoryType":"13"}

payload = ""
headers = {
    "cookie": "_adasys=b5e71c3e-3f06-4eb9-9eca-c07c1632580d; _gcl_au=1.1.1405140049.1673352303; _ga=GA1.3.2082132420.1673352303; _gid=GA1.3.899018268.1673352303; __hstc=176625274.97b853aac05fe8eed90568d877dbaa8b.1673352332284.1673352332284.1673352332284.1; hubspotutk=97b853aac05fe8eed90568d877dbaa8b; __hssrc=1; _fbp=fb.2.1673352333340.1958066890; __cf_bm=IYi08BIOo._.Fkf4zOoANBrc09Wt_b9mV.m0gn6glSU-1673353436-0-AeRDVWzfzjyJWb2PijFmk2fLFgGNx/hPO5YC0r1W1PPqGawcB0ob9QqQWHtB7nQK8GUkUk8NA1gWcx/qCLf3xeta8RSj5wRH0uKBR5oPJbJMbW81sZycT4w9xoAXvqeBSSuCyblMIX3CVolrnQ69gGo=; __hssc=176625274.3.1673352332284; _gat_UA-142136095-1=1",
    "authority": "statusinvest.com.br",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer": "https://statusinvest.com.br/reits/busca-avancada",
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
df.to_csv('REIT_EUA.csv', encoding='utf-8', index=False, sep=';',decimal =',' )