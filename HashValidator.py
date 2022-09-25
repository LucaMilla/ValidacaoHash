import pandas as pd
import numpy as np
import hashlib as hl

df = pd.read_excel('TabelaDeFrases.xlsx', index_col=False)
df['SHA256 Validado'], df['MD5 Validado'] = '', ''

def hashValidation(phrase, sha256, md5):
    shaPhrase = hl.sha256(phrase.encode('utf-8')).hexdigest()
    md5Phrase = hl.md5(phrase.encode('utf-8')).hexdigest()

    shaCompared = 'Correto' if sha256 == shaPhrase else 'Incorreto'
    md5Compared = 'Correto' if md5 == md5Phrase else 'Incorreto'
    return shaCompared, md5Compared

for i in range(len(df)):
    df['SHA256 Validado'].iloc[i], df['MD5 Validado'].iloc[i] = hashValidation(
                                df.iloc[i, :]['Phrase'], 
                                df.iloc[i, :]['SHA256'], 
                                df.iloc[i, :]['MD5']
                                )

df.to_excel(excel_writer='TabelaCompleta.xlsx', index=False)