import json
with open("dados.json") as dados_empresa:
    dados = json.load(dados_empresa)

somatotal = 0
somanaodias = 0
menorvalor = 0
maiorvalor = 0
contmedia = 0
contdias = 0

for dic_lista in dados:
    if dic_lista["valor"] < menorvalor:
        menorvalor = dic_lista["valor"]
        
    if dic_lista["valor"] > maiorvalor:
        maiorvalor = dic_lista["valor"]
                
    somatotal = somatotal + dic_lista["valor"]
   
    if dic_lista["valor"] > 0:
        contmedia = contmedia + 1
        
media = somatotal / contmedia  

menorvalordifzero = maiorvalor
        
for dic_lista in dados:

    if dic_lista["valor"] < menorvalordifzero and dic_lista["valor"] != 0:
        menorvalordifzero = dic_lista["valor"]
    
    if dic_lista["valor"] > media:
        contdias = contdias + 1

print(f"O menor valor de faturamento ocorrido é: R$ {menorvalor:.2f} reais.")
print(f"O menor valor de faturamento ocorrido diferente de zero é R$ {menorvalordifzero:.2f} reais.")
print(f"O maior valor de faturamento ocorrido é R$ {maiorvalor:.2f} reais.")
print(f"O todal de dias no mês em que o valor de faturamento diário foi superior à média mensal é {contdias} dias.")