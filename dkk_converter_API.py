import requests
import emoji

# API = 298ddcd1058b3fe19a234340fdaffcd2
# FRÅN https://fixer.io/dashboard / Lösenord är sparat via Chrome

def main():

    print(emoji.emojize("Välkommen! :thumbs_up: :red_heart: :Denmark:", language='alias'))

    try:
        amount_dkk = int(input("Hur mycket danska kronor? "))
        dkk_converter(amount_dkk)
    except ValueError:
        print("Siffror utan decimaler, tack.")

def dkk_converter(amount):
    api_key = "298ddcd1058b3fe19a234340fdaffcd2"
    url =  f"http://data.fixer.io/api/latest?access_key={api_key}&symbols=DKK,SEK"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data['success']:
        dkk_to_eur = data['rates']['DKK']
        #print(dkk_to_eur)
        sek_to_eur = data['rates']['SEK']
        #print(sek_to_eur)
        dkk_to_sek = sek_to_eur / dkk_to_eur
        #print(dkk_to_sek)
        from_dkk_to_sek = amount * dkk_to_sek

        print(f"{amount} danska kronor är {round(from_dkk_to_sek, 2)} i svenska kronor")
        next_step(from_dkk_to_sek)
    else:
        print("Error fetching exchange rates:", data.get("error"))

def next_step(dkk_to_sek):

    try:
        next_step = input("Är ni flera som ska dela på kostnaden? Y/N ").lower()

        if next_step == "y":
            how_many = int(input("Hur många? "))
            split_amount(dkk_to_sek, how_many)
        elif next_step == "n":
            print(f"Då var vi klara, ha det gott.")
        else:
            print("Fel input, testa Y eller N.")
    except ValueError:
        print("Använd siffror.")

def split_amount(amount: float, next_step: float):
    splitted_amount = amount / next_step

    print(f"Alla ska betala {round(splitted_amount, 2)} svenska kronor var. \nAvrundat uppåt: {round(splitted_amount, 0)}")

# Ta fram input för hur mycket DKK du betalat
# Konvertera från DKK till SEK
# Hitta ett verktyg som alltid har aktuell valuta och uppdaterar det
# Lägg in alternativ för att kunna dela upp kostnaden (SEK) på upp till 4 personer

if __name__ == '__main__':
    main()