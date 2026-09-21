import requests

CURRENCY_IDENTIFIERS = {
    "Currency",
    "Fragments",
    "EnshroudingCrystals",
    "Keepers",
    "AllflameEmbers",
    "Runegrafts",
    "Ancestor",
    "Expedition",
    "DeliriumOrbs",
    "Catalysts",
    "Oils",
    "Delve",
    "Essences",
    "MapKey",
    "MapsSpecial",
    "MapsUnique",
}

URL = "https://www.pathofexile.com/api/trade/data/static"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

response = requests.get(URL, headers=headers).json()
result = response["result"]
currencies_list = []

for item in result:
    if item["id"] not in CURRENCY_IDENTIFIERS:
        continue
    for entry in item["entries"]:
        if (entry["text"].strip() != ''):
            currencies_list.append(entry["text"])

with open("data/currencies.txt", "w") as f:
    f.writelines("\n".join(currencies_list))