# Řešení: Příběhovač
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
        
        # 🥉 1: Vytvoření prázdného seznamu
        self.words = []
        
        # 🥈 2: Generování slovních tlačítek
        for i in range(6):
            # 🥇 3: Výpočet pozice (příklad výpočtu)
            word_x = 100 + i * 120
            word = arcade.SpriteSolidColor(100, 50, arcade.color.WHITE)
            word.center_x = word_x
            word.center_y = 300
            
            # Přidání do seznamu
            self.words.append(word)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Slož si svůj vlastní příběh!", 250, 500, arcade.color.WHITE, 20)
        for word in self.words:
            word.draw()

if __name__ == "__main__":
    app = StoryApp()
    arcade.run()
