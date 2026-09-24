"""
================================================================================
          PROJEKT: SLOVNÍ PIANO (PŘÍBĚHOVAČ) 🎹✍️
          Téma: Práce se seznamy (lists) a cyklem for v Pythonu
================================================================================

CÍL CVIČENÍ:
- Naučit se vytvářet a používat seznamy (lists) v Pythonu.
- Osvojit si procházení seznamů pomocí cyklu 'for'.
- Pochopit práci s indexy prvků a dynamické výpočty (např. pozice prvků na obrazovce).
- Využít metodu list.append() pro dynamické přidávání prvků.
- Spojit principy hudebního piana (tvorba melodií, přehrávání, reset) s prací s textem.

ČEMU SE VYHNOUT:
- Nepoužívej složité externí knihovny, vystačíme si s knihovnou 'arcade'.
- Nepiš kód pro každé tlačítko zvlášť (nepoužívej duplicitní kód). Místo toho generuj 
  tlačítka elegantně v cyklu 'for'.
- Vyhni se tvrdému kódování (hardcoding) pozic, pokud je lze spočítat vzorcem.

--------------------------------------------------------------------------------
ZADÁNÍ JEDNOTLIVÝCH ÚROVNÍ:

🥉 ÚROVEŇ 1 – Inicializace a příprava (Základní)
--------------------------------------------------------------------------------
Připrav datové struktury pro naši aplikaci.
1. Vytvoř seznam slov 'word_pool' obsahující přesně 8 slov (např. ["Jednou", "Drak", ...]).
2. Připrav prázdný seznam 'story', do kterého budeme ukládat slova tvořící příběh.
3. Inicializuj prázdné seznamy sprajtů (arcade.SpriteList()) pro klávesy ('self.words')
   a pro funkční tlačítka ('self.buttons').

Příklad inicializace prázdného seznamu:
>>> muj_seznam = []

🥈 ÚROVEŇ 2 – Generování kláves v cyklu for (Pokročilá)
--------------------------------------------------------------------------------
Vygeneruj klávesy slovního piana vedle sebe vodorovně v jedné řadě.
1. Pomocí cyklu 'for i in range(8)' vytvoř 8 sprajtů kláves (arcade.SpriteSolidColor).
2. Spočítej souřadnici X pro každou klávesu tak, aby byly rovnoměrně rozmístěny:
   key_x = 85 + i * 90
3. Každému sprajtu přiřaď text z 'word_pool' pod atributem '.text_val' a index pod '.note_index'.
4. Přidej sprajt klávesy do seznamu 'self.words' pomocí metody '.append()'.
5. Vytvoř a přidej tlačítka "PLAY" (zelené) a "RESET" (červené) do seznamu 'self.buttons'.

Ukázka cyklu pro generování:
>>> for i in range(8):
>>>     key_x = start_x + i * spacing

🥇 ÚROVEŇ 3 – Interaktivita a přehrávání (Komplexní)
--------------------------------------------------------------------------------
Vdechni aplikaci život v metodě 'on_mouse_press' a 'on_update'.
1. Při kliknutí na klávesu se slovem:
   - Přidej slovo do seznamu 'self.story' (metoda .append()).
   - Změň barvu kliknuté klávesy na světle šedou (arcade.color.LIGHT_GRAY).
   - Přehraj odpovídající tón piana. Výška tónu (pitch/speed) bude záviset na indexu klávesy:
     speed = 0.5 + word_sprite.note_index * 0.1
2. Při kliknutí na "RESET":
   - Vymaž seznam příběhu (self.story.clear()).
   - Vrať barvu všem klávesám zpět na bílou (arcade.color.WHITE).
3. Při kliknutí na "PLAY":
   - Spusť sekvenční přehrávání zaznamenaných slov a tónů příběhu jedno po druhém s časovým odstupem!

💎 BONUS PRO MISTRY:
--------------------------------------------------------------------------------
1. Přidej vizuální indikaci přehrávání: během automatického přehrávání (PLAY) postupně 
   rozsvěcuj (např. žlutou barvou) ty klávesy, jejichž slovo se právě přehrává.
2. Přidej možnost zadat vlastní slovo přes konzoli a přidat ho na konec piana jako novou klávesu!

================================================================================
🔥 Pamatuj: Programování je jako skládání příběhu – řádek po řádku dává smysl celku!
================================================================================
"""

import arcade

# Rozměry okna aplikace
WIDTH = 800
HEIGHT = 600

class StoryPianoApp(arcade.Window):
    def __init__(self):
        # Spuštění rodičovského okna s rozměry a titulkem
        super().__init__(WIDTH, HEIGHT, "Slovní Piano - Příběhovač")
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
        # Načtení vestavěného zvukového efektu (coin z retro zdrojů)
        # Použijeme try-except pro případ, že na počítači není správně nakonfigurováno audio zařízení.
        try:
            self.sound = arcade.load_sound(":resources:sounds/coin1.wav")
        except Exception:
            self.sound = None

        # ============================================
        # 🥉 ÚROVEŇ 1 – Inicializace a příprava seznamů
        # ============================================
        
        # Slovní zásoba, která slouží jako klávesy piana (přesně 8 slov)
        self.word_pool = ["Jednou", "Drak", "Našel", "Ztracený", "Klíč", "Pod", "Zámkem", "Doma"]
        
        # Seznam pro uložení vznikajícího příběhu/melodie (zde budeme ukládat vybraná slova)
        self.story = []
        
        # Inicializace SpriteListů pro klávesy a funkční tlačítka
        self.words = arcade.SpriteList()
        self.buttons = arcade.SpriteList()

        # ============================================
        # 🥈 ÚROVEŇ 2 – Generování kláves v cyklu for
        # ============================================
        
        # Generujeme 8 kláves vedle sebe
        for i in range(8):
            # Výpočet pozice pro každé tlačítko klávesy tak, aby ležely vedle sebe
            key_x = 85 + i * 90
            key_y = 320
            
            # Vytvoření bílého obdélníkového sprajtu (připomíná klávesu piana)
            word_sprite = arcade.SpriteSolidColor(80, 160, arcade.color.WHITE)
            word_sprite.center_x = key_x
            word_sprite.center_y = key_y
            
            # Uložení přidruženého slova a indexu tónu přímo do sprajtu
            word_sprite.text_val = self.word_pool[i]
            word_sprite.note_index = i
            
            # Přidání klávesy do našeho seznamu sprajtů
            self.words.append(word_sprite)

        # Vytvoření zeleného tlačítka PLAY
        self.play_button = arcade.SpriteSolidColor(140, 45, arcade.color.APPLE_GREEN)
        self.play_button.center_x = 300
        self.play_button.center_y = 200
        self.buttons.append(self.play_button)

        # Vytvoření červeného tlačítka RESET
        self.reset_button = arcade.SpriteSolidColor(140, 45, arcade.color.RED)
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
        
        # Vykreslení kláves slovního piana
        self.words.draw()
        
        # Vykreslení textů na jednotlivých klávesách
        for sprite in self.words:
            arcade.draw_text(
                sprite.text_val, 
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
            arcade.color.RED, 
            font_size=13, 
            bold=True, 
            anchor_x="center", 
            anchor_y="center"
        )
        
        arcade.draw_text(
            "RESET 🔄", 
            self.reset_button.center_x, 
            self.reset_button.center_y, 
            arcade.color.RED, 
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
        # ============================================
        # 🥇 ÚROVEŇ 3 & 💎 BONUS – Automatické přehrávání příběhu
        # ============================================
        
        # Pokud probíhá přehrávání (playback_index >= 0)
        if self.playback_index >= 0:
            self.playback_timer += delta_time
            # Interval mezi jednotlivými slovy/tóny (0.7 sekundy)
            if self.playback_timer >= 0.7:
                # 💎 BONUS: Vracíme předchozí zvýrazněnou klávesu na barvu označující, že je v příběhu
                if self.active_playback_sprite:
                    self.active_playback_sprite.color = arcade.color.LIGHT_GRAY
                    self.active_playback_sprite = None
                
                # Zkontrolujeme, zda máme ještě co přehrávat
                if self.playback_index < len(self.story):
                    current_word = self.story[self.playback_index]
                    
                    # Najdeme klávesu odpovídající aktuálnímu přehrávanému slovu
                    for sprite in self.words:
                        if sprite.text_val == current_word:
                            # 💎 BONUS: Zvýrazníme klávesu při přehrávání žlutě
                            sprite.color = arcade.color.YELLOW
                            self.active_playback_sprite = sprite
                            
                            # Přehrajeme odpovídající tón piana podle indexu klávesy
                            if self.sound:
                                try:
                                    # pitch/speed se mění od 0.5 do 1.2 dle indexu
                                    arcade.play_sound(self.sound, speed=0.5 + sprite.note_index * 0.1)
                                except Exception:
                                    pass
                            break
                    
                    # Posuneme se na další slovo
                    self.playback_index += 1
                    self.playback_timer = 0.0
                else:
                    # Konec přehrávání - ukončíme cyklus
                    self.playback_index = -1
                    # Vracíme všechny klávesy v příběhu zpět do standardního kliknutého vzhledu (světle šedá)
                    for sprite in self.words:
                        if sprite.text_val in self.story:
                            sprite.color = arcade.color.LIGHT_GRAY
                        else:
                            sprite.color = arcade.color.WHITE

    def on_mouse_press(self, x, y, button, modifiers):
        # Během automatického přehrávání zamezíme přerušení klikáním
        if self.playback_index >= 0:
            return

        # ============================================
        # 🥇 ÚROVEŇ 3 – Detekce kliknutí
        # ============================================

        # 1. Kontrola kliknutí na tlačítko RESET
        if self.reset_button.collides_with_point((x, y)):
            self.story.clear()
            for sprite in self.words:
                sprite.color = arcade.color.WHITE
            return

        # 2. Kontrola kliknutí na tlačítko PLAY
        if self.play_button.collides_with_point((x, y)):
            if self.story:
                self.playback_index = 0
                self.playback_timer = 0.7  # Nastavíme tak, aby první tón zazněl ihned
                # Pro vizuální efekt začátku přehrávání zresetujeme tónové klávesy
                for sprite in self.words:
                    if sprite.text_val in self.story:
                        sprite.color = arcade.color.LIGHT_GRAY
            return

        # 3. Kontrola kliknutí na jednotlivé klávesy se slovy
        clicked_sprites = arcade.get_sprites_at_point((x, y), self.words)
        for sprite in clicked_sprites:
            # Přidání vybraného slova do příběhu
            self.story.append(sprite.text_val)
            
            # Změna barvy klávesy pro indikaci, že byla použita v příběhu
            sprite.color = arcade.color.LIGHT_GRAY
            
            # Přehrání tónu piana - pitch (speed) se mění s indexem klávesy (0.5 až 1.2)
            if self.sound:
                try:
                    arcade.play_sound(self.sound, speed=0.5 + sprite.note_index * 0.1)
                except Exception:
                    pass

if __name__ == "__main__":
    # Vytvoření a spuštění aplikace
    app = StoryPianoApp()
    arcade.run()
