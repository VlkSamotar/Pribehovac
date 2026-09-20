# Zadání: Příběhovač
# Úrovně:
# 🥉 1: Inicializace seznamu slov.
# 🥈 2: Generování sprajtů v cyklu for a přidání do seznamu.
# 🥇 3: Výpočet pozic a práce s indexy.
# 💎 Bonus: Interaktivita po kliknutí.

import arcade

# Nastavení okna
WIDTH = 800
HEIGHT = 600

class StoryApp(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Příběhovač")
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
        # TODO 1: Vytvoř prázdný seznam "words"
        # nápověda: self.words = []
        
        # TODO 2: Vytvoř cyklus "for", který proběhne 6x
        # TODO 3: Uvnitř cyklu vytvoř sprajt (tlačítko) a přidej ho do seznamu
        # nápověda: self.words.append(word)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Slož si svůj vlastní příběh!", 250, 500, arcade.color.WHITE, 20)
        # TODO 4: Vykresli všechny sprajty ze seznamu "words"

if __name__ == "__main__":
    app = StoryApp()
    arcade.run()
