SP = float(67836.43)
RJ = float(36678.66)
MG = float(29229.88)
ES = float(27165.48)
outros = float(19849.53)

soma = SP + RJ + MG + ES + outros

pSP = float((100 * SP) / soma)
pRJ = float((100 * RJ) / soma)
pMG = float((100 * MG) / soma)
pES = float((100 * ES) / soma)
poutros = float((100 * outros) / soma)

print("O percentual de SP é: ",pSP,"%")
print("O percentual de RJ é: ",pRJ,"%")
print("O percentual de MG é: ",pMG,"%")
print("O percentual de ES é: ",pES,"%")
print("O percentual de outros estados é: ",poutros,"%")

