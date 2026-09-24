"""
================================================================================
          STUDENTSKÁ VERZE: SLOVNÍ PIANO (PŘÍBĚHOVAČ) 🎹✍️
          Téma: Práce se seznamy (lists) a cyklem for v Pythonu
================================================================================

ÚKOLY PRO STUDENTY:
Tento soubor obsahuje připravenou kostru aplikace. Tvým úkolem je doplnit kód
na označených místech (hledej komentáře s TODO).

🥉 ÚROVEŇ 1 – Inicializace a příprava (Základní) - TODO 1
🥈 ÚROVEŇ 2 – Generování kláves v cyklu for (Pokročilá) - TODO 2
🥇 ÚROVEŇ 3 – Interaktivita a přehrávání (Komplexní) - TODO 3

================================================================================
"""

import arcade

# Rozměry okna aplikace
WIDTH = 800
HEIGHT = 600

class StoryPianoApp(arcade.Window):
    def __init__(self):
        # Spuštění rodičovského okna s rozměry a titulkem
        super().__init__(WIDTH, HEIGHT, "Slovní Piano - Příběhovač (Studentská verze)")
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
        # Načtení vestavěného zvukového efektu (coin z retro zdrojů)
        try:
            self.sound = arcade.load_sound(":resources:sounds/coin1.wav")
        except Exception:
            self.sound = None

        # ======================================================================
        # 🥉 ÚROVEŇ 1 – TODO 1: Inicializace a příprava seznamů
        # ======================================================================
        # Úkoly:
        # 1. Vytvoř seznam slov 'self.word_pool' obsahující přesně 8 různých slov.
        #    Slova by měla jít poskládat do zajímavých vět (např. podměty, slovesa, příslovce...).
        #    Příklad: ["Babička", "Snědla", "Kyselou", "Houbu", "Za", "Velkým", "Lesem", "Rychle"]
        # 2. Vytvoř prázdný seznam 'self.story', kam budeme ukládat složená slova příběhu.
        # 3. Inicializuj prázdné SpriteListy pro klávesy ('self.words') a tlačítka ('self.buttons').
        #
        # Nápověda:
        # - Seznam s prvky vytvoříš takto: seznam = ["prvek1", "prvek2"]
        # - Prázdný seznam vytvoříš takto: seznam = []
        # - Nový SpriteList z knihovny arcade vytvoříš takto: arcade.SpriteList()
        
        # --- ZDE DOPLŇ SVŮJ KÓD PRO TODO 1 ---
        self.word_pool = []  # Přidej sem 8 slov
        self.story = None      # Inicializuj jako prázdný seznam
        self.words = None      # Inicializuj jako nový SpriteList
        self.buttons = None    # Inicializuj jako nový SpriteList
        # -------------------------------------

        # ======================================================================
        # 🥈 ÚROVEŇ 2 – TODO 2: Generování kláves v cyklu for
        # ======================================================================
        # Úkoly:
        # 1. Napiš cyklus 'for', který se zopakuje přesně 8krát (pro každé slovo z word_pool).
        # 2. V cyklu spočítej souřadnici 'key_x' pro každou klávesu tak, aby ležely vedle sebe v řadě:
        #    - První klávesa (index 0) začíná na X = 85.
        #    - Každá další je posunuta o 90px doprava (využij řídicí proměnnou cyklu 'i').
        # 3. Vytvoř sprajt klávesy 'word_sprite' pomocí arcade.SpriteSolidColor o šířce 80, výšce 160 a bílé barvě.
        # 4. Do vytvořeného sprajtu ulož přidružené slovo z 'self.word_pool' pod atributem 'word_sprite.text_val'
        #    a index klávesy pod 'word_sprite.note_index'.
        # 5. Přidej sprajt do seznamu 'self.words' pomocí metody .append().
        #
        # Nápověda:
        # - Cyklus for pro rozsah: for i in range(pocet):
        # - Vytvoření obdélníkového sprajtu: sprite = arcade.SpriteSolidColor(sirka, vyska, barva)
        # - Nastavení pozice sprajtu: sprite.center_x = ... a sprite.center_y = ... (použij výšku 320)
        # - Přidání sprajtu do SpriteListu: seznam_sprajtu.append(sprite)
        
        # --- ZDE DOPLŇ SVŮJ KÓD PRO TODO 2 ---
        # (Napiš cyklus for, který vygeneruje klávesy a přidá je do self.words)
        
        # -------------------------------------

        # Pomocný kód pro tvorbu ovládacích tlačítek (neměň jej):
        if self.buttons is not None:
            # Zelené tlačítko PLAY
            self.play_button = arcade.SpriteSolidColor(140, 45, arcade.color.WHITE)
            self.play_button = arcade.color.APPLE_GREEN
            self.play_button.center_x = 300
            self.play_button.center_y = 200
            self.buttons.append(self.play_button)

            # Červené tlačítko RESET
            self.reset_button = arcade.SpriteSolidColor(140, 45, arcade.color.WHITE)
            self.reset_button = arcade.color.RED
            self.reset_button.center_x = 500
            self.reset_button.center_y = 200
            self.buttons.append(self.reset_button)

        # Pomocné proměnné pro přehrávání melodií (playback) a bonusy
        self.playback_index = -1
        self.playback_timer = 0.0
        self.active_playback_sprite = None

    def on_draw(self):
        # Vyčištění obrazovky
        self.clear()
        
        # Vykreslení hlavního záhlaví a instrukcí
        arcade.draw_text("Slovní Piano - Příběhovač 🎹", WIDTH / 2, 540, arcade.color.NAVY_BLUE, 24, bold=True, anchor_x="center")
        arcade.draw_text("Klikáním na klávesy slož svůj příběh a tóny. Stiskni PLAY pro přehrání.", WIDTH / 2, 500, arcade.color.NAVY_BLUE, 12, anchor_x="center")
        
        # Ochrana před spuštěním s nedokončeným TODO 1
        if self.words is None or self.buttons is None:
            arcade.draw_text("Chyba: Seznamy words nebo buttons nejsou inicializovány! (TODO 1)", WIDTH / 2, 300, arcade.color.RED, 16, bold=True, anchor_x="center")
            return

        # Vykreslení kláves slovního piana
        self.words.draw()
        
        # Vykreslení textů na jednotlivých klávesách
        for sprite in self.words:
            # Kontrola, zda sprajt má atribut text_val (z TODO 2)
            text_to_draw = getattr(sprite, 'text_val', "?")
            arcade.draw_text(
                text_to_draw, 
                sprite.center_x, 
                sprite.center_y, 
                arcade.color.BLACK, 
                font_size=11, 
                bold=True,
                anchor_x="center", 
                anchor_y="center"
            )
            
        # Vykreslení funkčních tlačítek PLAY a RESET
        self.buttons.draw()
        
        # Texty na funkčních tlačítkách
        arcade.draw_text(
            "PLAY ▶", 
            self.play_button.center_x, 
            self.play_button.center_y, 
            arcade.color.WHITE, 
            font_size=13, 
            bold=True, 
            anchor_x="center", 
            anchor_y="center"
        )
        
        arcade.draw_text(
            "RESET 🔄", 
            self.reset_button.center_x, 
            self.reset_button.center_y, 
            arcade.color.WHITE, 
            font_size=13, 
            bold=True, 
            anchor_x="center", 
            anchor_y="center"
        )
            
        # Vykreslení modrého panelu pro zobrazení vytvořeného příběhu
        arcade.draw_lbwh_rectangle_filled(50, 40, 700, 100, arcade.color.DARK_BLUE)
        arcade.draw_lbwh_rectangle_outline(50, 40, 700, 100, arcade.color.NAVY_BLUE, 3)
        
        # Zobrazení vznikajícího příběhu na panelu
        arcade.draw_text("Tvůj příběh (a melodie):", 70, 115, arcade.color.LIGHT_GRAY, 11, bold=True)
        
        full_sentence = " ".join(self.story) if self.story else "... ticho ..."
        arcade.draw_text(full_sentence, 70, 65, arcade.color.YELLOW, 16, bold=True)

    def on_update(self, delta_time):
        # Pomocný kód pro automatické přehrávání příběhu (neměň jej)
        if self.playback_index >= 0:
            self.playback_timer += delta_time
            if self.playback_timer >= 0.7:
                if self.active_playback_sprite:
                    self.active_playback_sprite.color = arcade.color.LIGHT_GRAY
                    self.active_playback_sprite = None
                
                if self.story and self.playback_index < len(self.story):
                    current_word = self.story[self.playback_index]
                    for sprite in self.words:
                        if getattr(sprite, 'text_val', None) == current_word:
                            sprite.color = arcade.color.YELLOW
                            self.active_playback_sprite = sprite
                            if self.sound:
                                try:
                                    note_idx = getattr(sprite, 'note_index', 0)
                                    arcade.play_sound(self.sound, speed=0.5 + note_idx * 0.1)
                                except Exception:
                                    pass
                            break
                    self.playback_index += 1
                    self.playback_timer = 0.0
                else:
                    self.playback_index = -1
                    if self.words:
                        for sprite in self.words:
                            if self.story and getattr(sprite, 'text_val', None) in self.story:
                                sprite.color = arcade.color.LIGHT_GRAY
                            else:
                                sprite.color = arcade.color.WHITE

    def on_mouse_press(self, x, y, button, modifiers):
        # Během automatického přehrávání zamezíme přerušení klikáním
        if self.playback_index >= 0:
            return

        # Ochrana před chybou při spuštění bez splněného TODO 1
        if self.words is None or self.story is None:
            return

        # ======================================================================
        # 🥇 ÚROVEŇ 3 – TODO 3: Detekce kliknutí a interaktivita
        # ======================================================================
        # Tvým úkolem je naimplementovat reakci na kliknutí myši.
        #
        # ČÁST A: Kliknutí na tlačítko RESET
        # Úkoly:
        # 1. Zkontroluj, zda uživatel klikl na self.reset_button (použij metodu .collides_with_point((x, y))).
        # 2. Pokud ano, vymaž celý seznam příběhu 'self.story' (použij metodu .clear()).
        # 3. Nastav barvu všem klávesám v 'self.words' zpět na bílou (arcade.color.WHITE) pomocí jednoduchého cyklu for.
        #
        # ČÁST B: Kliknutí na tlačítko PLAY
        # Úkoly:
        # 1. Zkontroluj, zda kliknutí koliduje s self.play_button.
        # 2. Pokud ano a v self.story jsou nějaká slova (len(self.story) > 0), spusť přehrávání:
        #    - Nastav self.playback_index = 0
        #    - Nastav self.playback_timer = 0.7
        #
        # ČÁST C: Kliknutí na jednotlivé klávesy se slovy
        # Úkoly:
        # 1. Pomocí metody arcade.get_sprites_at_point((x, y), self.words) získej seznam sprajtů, na které se kliklo.
        # 2. Projdi tyto sprajty v cyklu 'for'.
        # 3. Pro každý kliknutý sprajt:
        #    - Přidej jeho textovou hodnotu (sprite.text_val) do seznamu příběhu 'self.story' (použij metodu .append()).
        #    - Změň barvu sprajtu na světle šedou (arcade.color.LIGHT_GRAY).
        #    - Přehraj tón piana pomocí arcade.play_sound:
        #      arcade.play_sound(self.sound, speed=0.5 + sprite.note_index * 0.1)
        #      (Poznámka: vlož přehrání zvuku do bloku try-except, aby hra nespadla, pokud zvuk nefunguje).
        
        # --- ZDE DOPLŇ SVŮJ KÓD PRO TODO 3 ---
        # (Napiš obsluhu kliknutí pro RESET, PLAY a klávesy se slovy)

        # -------------------------------------

if __name__ == "__main__":
    # Vytvoření a spuštění aplikace
    app = StoryPianoApp()
    arcade.run()
