import pandas as pd

# Creating a dataframe with the Pokémon game order and information
pokemon_games = {
    "Order": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Game": [
        "Pokémon FireRed/LeafGreen (Gen I Remake)",
        "Pokémon HeartGold/SoulSilver (Gen II Remake)",
        "Pokémon Ruby/Sapphire/Emerald (Gen III)",
        "Pokémon Diamond/Pearl/Platinum (Gen IV)",
        "Pokémon Black/White (Gen V)",
        "Pokémon Black 2/White 2 (Gen V)",
        "Pokémon X/Y (Gen VI)",
        "Pokémon Omega Ruby/Alpha Sapphire (Gen III Remake)",
        "Pokémon Sun/Moon (Gen VII)",
        "Pokémon Let's Go, Pikachu!/Eevee! (Gen I Remake)",
        "Pokémon Sword/Shield (Gen VIII)"
    ],
    "Description": [
        "Remakes of the original Red/Blue games with updated graphics and features.",
        "Remakes of Gold/Silver with enhanced graphics and additional content.",
        "Introduce a new region and more complex mechanics. Play Emerald for the expanded storyline.",
        "New region, new mechanics like the physical/special split, and improvements in graphics. Play Platinum for more content.",
        "A fresh start with a completely new set of Pokémon and significant gameplay changes.",
        "Direct sequels to Black/White with new story and mechanics.",
        "First games on the Nintendo 3DS, introducing 3D graphics and Mega Evolutions.",
        "Remakes of Ruby/Sapphire with updated graphics and features introduced in X/Y.",
        "Introduce the Alola region and new mechanics like Z-Moves and regional variants. Play Ultra Sun/Ultra Moon for enhanced versions.",
        "Simplified remakes of the original games with mechanics inspired by Pokémon GO. Nostalgic trip with modern visuals.",
        "First mainline games on the Nintendo Switch, featuring new mechanics like Dynamax and open-world elements."
    ],
    "Checked": [False] * 11
}

df = pd.DataFrame(pokemon_games)

# Saving the dataframe to an Excel file with ";" as the delimiter
file_path = "/Users/liridonbislimi/Desktop/pokemon/Pokemon_Game_Order.xlsx"
df.to_excel(file_path, index=False, sep=";")