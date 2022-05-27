#Пирожок в столовой стоит А рублей и B копеек.
#Определите, сколько рублей и копеек нужно заплатить за N пирожков.
rouble = int(input())
cents = int(input())
n = int(input())
priceCents = n * cents
priceRouble = n * rouble
if priceCents >= 100:
    priceRouble = priceRouble + priceCents // 100
    priceCents = priceCents % 100
print(priceRouble)
print(priceCents)
