#IMPORT VARI
import json
import requests
from datetime import datetime

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

params ={
    'start':'1',
    'limit':'100',
    'convert':'USD'}

headers={
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':'21c03852-dfba-4439-a322-d113fdf81c38'}

now=datetime.now()

request=requests.get(url=url,params=params,headers=headers).json()

#1)La criptovaluta con il volume maggiore (in $) delle ultime 24 ore
cripto_volume24h_name={}
for task1 in request['data']:
    cripto_volume24h_name[task1['quote']['USD']['volume_24h']] = [task1['name']]
    cripto_highest_volume24h=max(cripto_volume24h_name.items())

#2)Le migliori e peggiori 10 criptovalute (per incremento in percentuale delle ultime 24 ore)
cripto_incrase24h_name={}
for task2 in request['data']:
    cripto_incrase24h_name[task2['quote']['USD']['percent_change_24h']] = [task2['name']]
    list_cripto_worse_incrase24h=list(cripto_incrase24h_name.items())
    list_cripto_worse_incrase24h.sort()
    cripto_worse_incrase24h=list_cripto_worse_incrase24h[0:10]
    list_cripto_highest_incrase24h=list(reversed(list_cripto_worse_incrase24h))
    cripto_highest_incrase24h=list_cripto_highest_incrase24h[0:10]

#3)La quantità di denaro necessaria per acquistare una unità di ciascuna delle prime 20 criptovalute (le prime 20
#criptovalute secondo la classifica predefinita di CoinMarketCap, dunque ordinate per capitalizzazione)
price_cripto = []
for task3 in request['data']:
    price_cripto.append(task3['quote']['USD']['price'])
    price_first20 = price_cripto[0:20]
    total_needed = [sum(price_first20)]

#4)La quantità di denaro necessaria per acquistare una unità di tutte le criptovalute il cui volume delle ultime 24
#ore sia superiore a 76.000.000$
list_price_cripto_volume24h_76000000=[] #Creazione Lista Cripto Volume24h Superiore a 76.000.000$
for task4 in request['data']:
    if task4['quote']['USD']['volume_24h'] > 76000000:
        list_price_cripto_volume24h_76000000.append(task4['quote']['USD']['price'])
        price_cripto_volume24h_76000000 = [sum(list_price_cripto_volume24h_76000000)]

#5)La percentuale che avreste realizzato se aveste comprato una unità di ciascuna delle prime 20 criptovalute il
#giorno prima (ipotizzando che la classifca non sia cambiata)
list_percentchange = []
list_profit_loss = []
actual_spent_price = 0
previous_spent_price = 0
for task5 in request['data']:
    list_percentchange.append(task5['quote']['USD']['percent_change_24h'])
for i in range(20):
    actual_spent_price=price_cripto[i]+actual_spent_price
    previous_price = price_cripto[i] / (1 + ((list_percentchange[i]) / 100))
    previous_spent_price=previous_price+previous_spent_price

percentage=(actual_spent_price-previous_spent_price)/actual_spent_price*100

#6)Le migliori e peggiori 10 criptovalute (per incremento in percentuale degli ultimi 7d)
cripto_incrase7d_name={}
for task6 in request['data']:
    cripto_incrase7d_name[task6['quote']['USD']['percent_change_7d']]=[task6['name']]
    list_cripto_worse_incrase7d=list(cripto_incrase7d_name.items())
    list_cripto_worse_incrase7d.sort()
    cripto_worse_incrase7d=list_cripto_worse_incrase7d[0:10]
    list_cripto_highest_incrase7d=list(reversed(list_cripto_worse_incrase7d))
    cripto_highest_incrase7d=list_cripto_highest_incrase7d[0:10]

#7)Le criptovalute la cui percentuale nelle ultime 24 ore sia superiore a 10% con il loro prezzo
cripto_24h_10per=[]
for task7 in request['data']:
    if task7['quote']['USD']['percent_change_24h']>=10:
        cripto_24h_10per.append(task7['name'])
        cripto_24h_10per.append(task7['quote']['USD']['price'])

#8)Le criptovalute la cui percentuale negli ultimi 7d sia superiore a 10% e il prezzo uguale o inferiore a 10$
low_performer_cripto=[]
for task8 in request['data']:
    if task8['quote']['USD']['percent_change_7d']>=10 and task8['quote']['USD']['price']<=10:
        low_performer_cripto.append(task8['name'])
        low_performer_cripto.append(task8['quote']['USD']['price'])

#9)Le criptovalute che hanno reso il 5% sia nelle 24h sia nei 7d
performer_cripto=[]
for task9 in request['data']:
    if task9['quote']['USD']['percent_change_24h']>5 and task9['quote']['USD']['percent_change_7d']>5:
        performer_cripto.append(task9['name'])

#10)Le criptovalute con un prezzo uguale o inferiore a 1$ che hanno reso il 10% nelle ultime 24h
small_expense_cripto=[]
for task10 in request['data']:
    if task10['quote']['USD']['price']<1 and task10['quote']['USD']['percent_change_24h']>=10:
        small_expense_cripto.append(task10['name'])
        small_expense_cripto.append(task10['quote']['USD']['price'])

data={
    "1)La criptovaluta con il volume maggiore (in $) delle ultime 24 ore":cripto_highest_volume24h,
    "2)Migliori 10 criptovalute per incremento "
    "nelle ultime 24h":cripto_highest_incrase24h,
    "3)Peggiori 10 criptovalute per incremento "
    "nelle ultime 24h":cripto_worse_incrase24h,
    "4)La quantita' di denaro necessaria per acquistare una unita' "
    "di ciascuna delle prime 20 criptovalute":total_needed,
    "5)La quantita' di denaro necessaria per acquistare una unita' di "
    "tutte le criptovalute il cui volume delle ultime 24 ore sia superiore a 76.000.000$":price_cripto_volume24h_76000000,
    "6)La percentuale di guadagno o perdita che avreste realizzato se aveste comprato "
    "una unita' di ciascuna delle prime 20 criptovalute il giorno prima "
    "(ipotizzando che la classifca non sia cambiata)":percentage,
    "7)Le migliori 10 criptovalute per incremento "
    "degli ultimi 7d":cripto_highest_incrase7d,
    "8)Le peggiori 10 criptovalute per incremento "
    "degli ultimi 7d":cripto_worse_incrase7d,
    "9)Le criptovalute la cui percentuale nelle ultime 24h "
    "sia superiore a 10% con il loro prezzo":cripto_24h_10per,
    "10)Le criptovalute la cui percentuale negli ultimi 7d "
    "sia superiore a 10% e il prezzo uguale o inferiore a 10$":low_performer_cripto,
    "11)Le criptovalute che hanno reso il 5% sia nelle 24h sia nei 7d":performer_cripto,
    "12)Le criptovalute con un prezzo uguale o inferiore a 1$ "
    "che hanno reso il 10% nelle ultime 24h":small_expense_cripto
}

with open(str(now.strftime('%d_%m_%Y.json')),'w') as filejson:
    json.dump(data,filejson,indent=4)