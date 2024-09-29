import pyperclip

# HearGold-codes
steal_hg = "9224670a 00002101 1224670a 00002100 d2000000 00000000"
rare_candy = "94000130 FCFF0000 B2111880 00000000 E0000B74 000000A0 03E70032 00000000 D2000000 00000000"
all_balls = "94000130 fcff0000 62111880 00000000 b2111880 00000000 d5000000 00000384 c0000000 00000017 d7000000 00000d16 dc000000 00000002 d2000000 00000000 94000130 fcff0000 62111880 00000000 b2111880 00000000 d5000000 00000001 c0000000 0000000f d7000000 00000d14 d4000000 00000001 dc000000 00000002 d2000000 00000000 94000130 fcff0000 62111880 00000000 b2111880 00000000 d5000000 000001ec c0000000 00000007 d7000000 00000d54 d4000000 00000001 dc000000 00000002 d2000000 00000000"
max_items = "94000130 fcff0000 62111880 00000000 b2111880 00000000 d5000000 00000384 c0000000 000000a1 d7000000 00000656 dc000000 00000002 d2000000 00000000 94000130 fcff0000 62111880 00000000 b2111880 00000000 10000708 00000087 1000070c 00000088d5000000 00000044c0000000 0000002cd7000000 00000654d4000000 00000001dc000000 00000002d2000000 0000000094000130 fcff000062111880 00000000b2111880 00000000d5000000 000000d5c0000000 00000072d7000000 00000710dc000000 00000002d4000000 00000001d2000000 00000000"

# Platinum-codes
steal_platinum = "92249cde 00002101 12249cde 00002100 d2000000 00000000"

# Pokemon black
steal_black = "521CBAAC 2F06D134 121CBAAC 0000E001 121CBAE6 00002001 121CBACC 00002000 D2000000 00000000"
exp_share = "521CB43C 42819903 121CB440 000046C0 D2000000 00000000"

# Pokemon black 2
steal_black_2 = "521AF628 2F06D134 121AF628 0000E001 121AF662 00002001 121AF648 00002000 D2000000 00000000"
exp_share_2 = "521AEF84 42819903 121AEF88 000046C0 D2000000 00000000"
all_items_2 = "94000130 fcff0000 b2000024 00000000 e001915c 00000054 03840074 03840075 03840076 03840077 0384023b 0384023c 0384023d 0384023f 03840240 03840241 03840244 03840245 03840246 03840247 03840248 03840249 0384024a 0384024b 0384024c 0384024d 0384024e 00000000 d5000000 03840001 c0000000 0000000f d6000000 00018d20 d4000000 00000001 d2000000 00000000 94000130 fcff0000 b2000024 00000000 d5000000 03840037 c0000000 00000039 d6000000 00018d60 d4000000 00000001 d2000000 00000000 94000130 fcff0000 b2000024 00000000 d5000000 03840087 c0000000 0000000d d6000000 00018e48 d4000000 00000001 d2000000 00000000 94000130 fcff0000 b2000024 00000000 d5000000 038400d5 c0000000 00000072 d6000000 00018e80 d4000000 00000001 d2000000 00000000 94000130 fcff0000 b2000024 00000000 d5000000 038401e5 c0000000 0000000f d6000000 0001904c d4000000 00000001 d2000000 00000000 94000130 fcff0000 b2000024 00000000 d5000000 03840219 c0000000 0000001b d6000000 0001908c d4000000 00000001 d2000000 00000000 94000130 fcff0000 b2000024 00000000 d5000000 03840250 c0000000 00000017 d6000000 000190fc d4000000 00000001 d2000000 00000000"

def main():
    while True:
        try:
            get_option()
        except Exception as e:
            print(f"An error occurred: {e}")

def get_option():
    list_of_options = ["New code", "Choose code", "Quit"]

    while True:
        for number, option in enumerate(list_of_options, 1):
            print(f"{number}: {option}")
    
        try:
            choose_code_option = int(input("Number 1-3? ").strip())
            if 1 <= choose_code_option <= 3:
                if choose_code_option == 1:
                    code = input("What's the code? ").strip()
                    code_conversion_option = int(input("Choose conversion type: 1 for replacing all blanks with '+', 2 for replacing every second blank with '+': ").strip())
                    code_converter(code, code_conversion_option)
                elif choose_code_option == 2:
                    choose_game()
                elif choose_code_option == 3:
                    print("Take care!")
                    exit()
            else:
                print(f"Invalid number, please choose between 1 and {len(list_of_options)}.")
        except ValueError:
            print(f"Invalid input, please enter a number between 1 and {len(list_of_options)}.")

def choose_game():
    list_of_games = ['HeartGold', 'Platinum', 'Black', 'Black 2']

    while True:
        for number, option in enumerate(list_of_games, 1):
            print(f"{number}: {option}")

        try:
            choose_game_option = int(input("Number 1-4? ").strip())
            if 1 <= choose_game_option <=4:
                if choose_game_option == 1:
                    print(f"You choose {list_of_games[choose_game_option-1]}")
                    choose_code(choose_game_option)
                    break
                elif choose_game_option == 2:
                    print(f"You choose {list_of_games[choose_game_option-1]}")
                    choose_code(choose_game_option)
                    break
                elif choose_game_option == 3:
                    print(f"You choose {list_of_games[choose_game_option-1]}")
                    choose_code(choose_game_option)
                    break
                elif choose_game_option == 4:
                    print(f"You choose {list_of_games[choose_game_option-1]}")
                    choose_code(choose_game_option)
                    break
            else:
                print(f"Invalid number, please choose between 1 and {len(list_of_games)}")
        except ValueError:
            print("Invalid input, please enter a number between 1 and 4.")


def choose_code(game):
    list_code_hg = ['Steal pokemon', 'Rare candy', 'All balls', 'Max items']
    list_code_platinum = ['Steal pokemon', 'Place holder', 'Place holder 2']
    list_code_black = ['Steal pokemon', 'Exp Share', 'Place holder']
    list_code_black_2 = ['Steal pokemon', 'Exp Share', 'All items']

    list_dict = {
        1: list_code_hg,
        2: list_code_platinum,
        3: list_code_black,
        4: list_code_black_2
    }

    game_selected = list_dict[game]
    
    if 1 <= game <= 4:
        for number, option in enumerate(game_selected, 1):
            print(f"{number}: {option}")
    
        if game == 1:
            try:
                choose_code = int(input(f"Number 1-{len(list_code_hg)}? ").strip())
                if 1 <= choose_code <= 4:
                    codes = [steal_hg, rare_candy, all_balls, max_items]
                    code_conversion_option = int(input("Choose conversion type: 1 for replacing all blanks with '+', 2 for replacing every second blank with '+': ").strip())
                    code_converter(codes[choose_code - 1], code_conversion_option)
                else:
                    print(f"Invalid number, please choose between 1 and {len(list_code_hg)}.")
            except ValueError:
                print(f"Invalid input, please enter a number between 1 and {len(list_code_hg)}.")
        elif game == 2:
            try:
                choose_code = int(input(f"Number 1-{len(list_code_platinum)}? ").strip())
                if 1 <= choose_code <= 3:
                    codes = [steal_platinum]
                    code_conversion_option = int(input("Choose conversion type: 1 for replacing all blanks with '+', 2 for replacing every second blank with '+': ").strip())
                    code_converter(codes[choose_code - 1], code_conversion_option)
                else:
                    print(f"Invalid number, please choose between 1 and {len(list_code_platinum)}.")
            except ValueError:
                print(f"Invalid input, please enter a number between 1 and {len(list_code_platinum)}.")
        elif game == 3:
            try:
                choose_code = int(input(f"Number 1-{len(list_code_black)}? ").strip())
                if 1 <= choose_code <= 3:
                    codes = [steal_black, exp_share]
                    code_conversion_option = int(input("Choose conversion type: 1 for replacing all blanks with '+', 2 for replacing every second blank with '+': ").strip())
                    code_converter(codes[choose_code - 1], code_conversion_option)
            except ValueError:
                print(f"Invalid input, please enter a number between 1 and {len(list_code_black)}.")
        elif game == 4:
            try:
                choose_code = int(input(f"Number 1-{len(list_code_black_2)}? ").strip())
                if 1 <= choose_code <= 3:
                    codes = [steal_black_2, exp_share_2, all_items_2]
                    code_conversion_option = int(input("Choose conversion type: 1 for replacing all blanks with '+', 2 for replacing every second blank with '+': ").strip())
                    code_converter(codes[choose_code - 1], code_conversion_option)
            except ValueError:
                print(f"Invalid input, please enter a number between 1 and {len(list_code_black_2)}.")
        else:
            print("Something went wrong.")

def code_converter(x, conversion_type):
    try:
        if conversion_type == 1:
            new_code = x.replace(" ", "+")
        elif conversion_type == 2:
            parts = x.split(" ")
            new_code = ""
            for i in range(len(parts)):
                if i % 2 == 1 and i < len(parts) - 1:
                    new_code += parts[i] + "+"
                else:
                    new_code += parts[i] + " "
            new_code = new_code.strip()
        else:
            print("Invalid conversion type.")
            return
        
        pyperclip.copy(new_code)
        print("Code has been copied.")
    except Exception as e:
        print(f"Failed to copy code: {e}")

if __name__ == '__main__':
    main()
