from datetime import datetime

anoNasc = int(input("fala aí o ano que voce nasceu: "))
mesNasc = int(input("fala ai numero do mes que voce nasceu: "))
diaNasc = int(input("fala ai o dia que voce nasceu: "))

dataNasc = datetime(anoNasc, mesNasc, diaNasc)

dataAtual = datetime.now()

idadeGeral = dataAtual - dataNasc

idadeDias = (dataAtual - dataNasc).days

anos = idadeGeral.days // 365
meses = (idadeGeral.days % 365) // 30
dias = (idadeGeral.days % 365) % 30

print("Considerando que voce nasceu em ({}/{}/{}), sua idade em dias e: {} dias ".format(diaNasc, mesNasc, anoNasc, idadeDias))
print("Já a sua idade no geral e: {} anos, {} meses e {} dias.".format(anos, meses, dias))
