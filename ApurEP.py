import json
from math import floor

def espaço():
    print('')

# Declaração de variáveis
totVagas = 9

# Variáveis DEM
totDEM = 0
quoPartDEM = 0
legendaDEM = 25
eleitosDEM = ''
totVagasDEM = 0
votosValidDEMstr = ''
c1 = 0

# Variáveis PSDB
totPSDB = 0
quoPartPSDB = 0
legendaPSDB = 41
eleitosPSDB = ''
totVagasPSDB = 0
votosValidPSDBstr = ''
c2 = 0

# ELEIÇÃO MAJORITÁRIA

luizAntonio = {"nome": "Luiz Antonio", "votos": 617}
hilario = {"nome": "Hilario", "votos": 602}

if luizAntonio['votos'] > hilario['votos']:
    prefeito = "Luiz Antonio"
else:
    prefeito = "Hilario"

# ELEIÇÕES PROPORCIONAIS

# Carregamento dos arquivos json com os votos de cada partido
with open("votosDEM.json", encoding="utf-8") as jsonDEM:
    votosValidDEM = json.load(jsonDEM)
    
with open("votosPSDB.json", encoding="utf-8") as jsonPSDB:
    votosValidPSDB = json.load(jsonPSDB)
    
# Calcula o total de votos de cada partido e salva em uma variável    
for i in votosValidDEM:
    totDEM += i['votos']
totDEM += legendaDEM

for i in votosValidPSDB:
    totPSDB += i['votos']
totPSDB += legendaPSDB

# Totaliza os votos válidos
votosValid = totDEM + totPSDB

# Calcula o quociente eleitoral
quoElei = votosValid / totVagas
quoElei = round(quoElei)

# Calcula o quociente parditário
quoPartDEM = totDEM / quoElei
quoPartDEM = floor(quoPartDEM)
totVagasDEM = quoPartDEM

quoPartPSDB = totPSDB / quoElei
quoPartPSDB = floor(quoPartPSDB)
totVagasPSDB = quoPartPSDB

# Calcula média para sobras
mediaDEM = totDEM / (quoPartDEM + 1)
mediaPSDB = totPSDB / (quoPartPSDB + 1)

# Atribui o número de vagas de cada partido
if mediaDEM > mediaPSDB:
    totVagasDEM += 1
else:
    totVagasPSDB += 1


# Apresentação dos resultados

print("A) QUAL CANDIDATO VENCEU AS ELEIÇÕES MAJORITÁRIAS NO MUNICÍPIO?")
print(f"R: O vencedor das eleições majoritárias foi {prefeito}.")

espaço()

print("B) QUAL O QUOCIENTE ELEITORAL DA ELEIÇÃO?")
print(f'R: O quociente eleitoral é: {quoElei}.')
espaço()

print("C) QUAIS OS QUOCIENTES PARTIDÁRIOS DOS PARTIDOS?")
print(f"""R: Quociente partidário DEM: {quoPartDEM}.
   Quociente partidário PSDB: {quoPartPSDB}.""")
espaço()

print('D) QUAL O NÚMERO DE VAGAS QUE CADA PARTIDO TEVE DIREITO NAS ELEIÇÕES?')
print(f"""R: Número de vagas DEM: {totVagasDEM}.
   Número de vagas PSDB: {totVagasPSDB}.""")
espaço()

print('E) QUAIS OS CANDIDATOS FORAM ELEITOS NAS ELEIÇÕES PROPORCIONAIS?')
print("R: Foram eleitos pelo DEM:")
while c1 < totVagasDEM:
    eleitosDEM += (votosValidDEM[c1]['nome'])
    print(votosValidDEM[c1]['nome'])
    c1 += 1
    
espaço()

print('Foram eleitos pelo PSDB: ')
while c2 < totVagasPSDB:
    print(votosValidPSDB[c2]['nome'])
    c2 += 1
