import emoji
# Samma som den andra fast utan API, manuell input av hur mycket DKK är värt

def main():

    print(emoji.emojize("Välkommen! :thumbs_up: :red_heart: :Denmark:", language='alias'))

    try:
        amount_dkk = int(input("Hur mycket danska kronor? "))
        dkk_converter(amount_dkk)
    except ValueError:
        print("Siffror utan decimaler, tack.")

def dkk_converter(amount):
    # DKK * 1.52 = SEK
    dkk_value = amount * 1.52 # Ändra efter * till senaste kursen, senast ändrad 26/4-24

    print(f"{amount} danska kronor är {round(dkk_value, 2)} i svenska kronor")
    next_step(dkk_value)

def next_step(dkk_to_sek):
    try:
        next_step = input("Är ni flera som ska dela på kostnaden? Y/N ").lower()

        if next_step == "y":
            how_many = int(input("Hur många? "))
            split_amount(dkk_to_sek, how_many)
        elif next_step == "n":
            print(emoji.emojize(f"{dkk_to_sek}SEK:Sweden: är det det blir då, puss och hejdå :red_heart:"))
        else:
            print("Fel input, testa Y eller N.")
    except ValueError:
        print("Använd siffror.")

def split_amount(amount: float, next_step: float):
    splitted_amount = amount / next_step

    print(f"Alla ska betala {round(splitted_amount, 2)} svenska kronor var. \nAvrundat uppåt: {round(splitted_amount, 0)}")

if __name__ == '__main__':
    main()