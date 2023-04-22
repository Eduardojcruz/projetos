import pandas as pd



def read_files(path, name_file, year_date, type_file):


    _file = f'{path}{name_file}{year_date}.{type_file}'

    colspecs = [(2,10),
                (10,12),
                (12,24),
                (27,39),
                (56,69),
                (69,82),
                (82,95),
                (108,121),
                (152,170),
                (170,188)
    ]

    names = ["Data_pregao","codbdi","Sigla_acao","Nome_acao","Preco_Abertura","Preco_Maximo","Preco_Minimo","Preco_Fechamento","QTD_Negocios","Volume_negocio"]

    df = pd.read_fwf(_file, colspecs = colspecs, names = names, skiprows = 1)
    
    return df



def filter_stock(df):
    df = df [df["codbdi"]==2]
    df = df.drop(["codbdi"], 1)
    return df



def parse_date(df):
    df["Data_pregao"] = pd.to_datetime(df["Data_pregao"], format = "%Y%m%d")
    return df



def parse_values(df):
    df["Preco_Abertura"]= (df["Preco_Abertura"]/100).astype(float)
    df["Preco_Maximo"]= (df["Preco_Maximo"]/100).astype(float)
    df["Preco_Minimo"]= (df["Preco_Minimo"]/100).astype(float)
    df["Preco_Fechamento"]= (df["Preco_Fechamento"]/100).astype(float)
    df["Volume_negocio"]= df['Volume_negocio'] = pd.to_numeric(df['Volume_negocio'], errors="coerce").fillna(0).astype('int64')
    df["QTD_Negocios"]= df['QTD_Negocios'] = pd.to_numeric(df['QTD_Negocios'], errors="coerce").fillna(0).astype('int64')
    
    return df



def concat_files(path, name_file, year_date, type_file, final_file):
    for i, y in enumerate(year_date):
        df = read_files(path, name_file, y, type_file)
        df = filter_stock(df)
        df = parse_date(df)
        df = parse_values(df) 
        if i==0:
            df_final = df
        else:
            df_final = pd.concat([df_final,df])
    df_final.to_csv(f'{path}//{final_file}', index=False)



year_date=['2018','2019','2020','2022']
path = f'caminho'
name_file = 'COTAHIST_A'
type_file = 'txt'
final_file = 'all_bovespa.csv'
concat_files(path, name_file, year_date, type_file, final_file)


