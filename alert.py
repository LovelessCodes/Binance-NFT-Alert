from colorama import Fore, Style
import requests
import platform
import time
import json
import math
import os

def PrintTitle(status, amount, left, artist):
    if "win" in platform.system().lower():
        os.system("cls")
    if "lin" in platform.system().lower():
        os.system("clear")
    spaces = 50
    if status == 200: stat = f"{Fore.GREEN}{status}{Fore.RESET}"
    else: stat = f"{Fore.YELLOW}{status}{Fore.RESET}"
    if 0 < amount < 10:
        amnt = f"{Fore.GREEN}{amount}{Fore.LIGHTBLACK_EX}/16{Fore.RESET}] "
    elif amount > 0:
        amnt = f"{Fore.GREEN}{amount}{Fore.LIGHTBLACK_EX}/16{Fore.RESET}]"
    else:
        amnt = f"{Fore.YELLOW}{amount}{Fore.LIGHTBLACK_EX}/16{Fore.RESET}] "
    if left > 9: lefty = f"{Fore.YELLOW}{left} secs{Fore.RESET}] "
    elif left == 1: lefty = f"{Fore.GREEN}{left} sec{Fore.RESET}]   "
    else: lefty = f"{Fore.GREEN}{left} secs{Fore.RESET}]  "
    print(
        f"{Fore.YELLOW}          ,EE,        \n" +
        f"        .m@@@@K.      \n" +
        f"       n@@@zz@@@n`    \n" +
        f"      'H@q-  'p@p'    " +
        f"{Fore.LIGHTYELLOW_EX}    _______ _______ _______ \n"+
        f"   {Fore.YELLOW}~QB^ ` ^BB^ ` ^BQ~ " +
        f"{Fore.LIGHTYELLOW_EX}   |    |  |    ___|_     _|\n"+
        f"   {Fore.YELLOW}~QB^ ` ^BB^ ` ^BQ> " +
        f"{Fore.LIGHTYELLOW_EX}   |       |    ___| |   |  \n"+
        f"   {Fore.YELLOW}   'p@q-  'p@p'    " +
        f"{Fore.LIGHTYELLOW_EX}   |__|____|___|     |___| \n"+
        f"   {Fore.YELLOW}    n@@@zz@@@n`    " +
        f"{Fore.RED}            Alerter\n"
        f"   {Fore.YELLOW}     .m@@@@K.      \n" +
        f"          ,EE,        {Fore.RESET}\n\n" +
        f" ┌{'─'*(math.ceil((spaces-len(artist))/2))}{Fore.BLUE}{Fore.LIGHTBLUE_EX}{artist}{Fore.RESET}{'─'*(math.floor((spaces-len(artist))/2))}┐ \n"+
        f" │{' '*spaces}│ \n"+
        f" │               STATUS:  [{stat}]{' '*21}│ \n"+
        f" │               AMOUNT:  [{amnt}{' '*19}│ \n"+
        f" │{' '*spaces}│ \n"+
        f" │{' '*spaces}│ \n"+
        f" │               REFRESH: [{lefty}{' '*16}│ \n"+
        f" │{' '*spaces}│ \n"+
        f" └{'─'*spaces}┘ "
    )

config = json.load(open("config.json", "r+"))
urls = {
    "products": "https://www.binance.com/bapi/nft/v1/friendly/nft/artist-product-list",
    "artist": f"https://www.binance.com/bapi/nft/v1/public/nft/home-artist-detail?artistId={config['artist']}"
}
data = {"amountFrom": "", "amountTo": "", "creatorId": config['artist'], "currency": "", "keyword": "", "orderBy": "list_time", "orderType": -1, "page": 1, "reSale": 0, "rows": 16, "tradeType": ""}
k = 0

while True:
    r = requests.get(urls['artist'], timeout=2.5)
    artist = r.json()['data']
    r = requests.post(urls['products'], json=data, timeout=2.5)
    stat = r.status_code
    if r.status_code == 200:
        k = r.json()['data']['total']
    else:
        k = 0
    if stat == 200:
        r = r.json()
        if r['data']['total'] > 0:
            data = {
                'username': 'Binance NFT Alerter',
                'embeds': [
                    {
                        'type': 'rich',
                        'title': f"NEW DROP BY: @{artist['nickName']}",
                        'description': f"There's {r['data']['total']} NFTs dropped!",
                        'author': {
                            'name': f"@{artist['nickName']}",
                            'url': f"https://www.binance.com/en/nft/shopWindow?reSale=0&tradeType=&currency=&amountFrom=&amountTo=&keyword=&orderBy=list_time&orderType=-1&isBack=1&uid={config['artist']}&order=list_time%40-1",
                            'icon_url': artist['avatarUrl']
                        }
                    }
                ]
            }
            requests.post(config['webhook'], json=data)
            for i in range(0, 300):
                PrintTitle(stat, k, 60-i, f" @{artist['nickName']} ")
                time.sleep(1)
            continue
    for i in range(0, 60):
        PrintTitle(stat, k, 60-i, f" @{artist['nickName']} ")
        time.sleep(1)
    continue