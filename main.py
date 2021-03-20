def on_button_pressed_a():
    Ludzik.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def onStart():
    global Ludzik, Punkt
    Ludzik = game.create_sprite(1, 2)
    Ludzik.set(LedSpriteProperty.BLINK, 350)
    Punkt = game.create_sprite(3, 2)
    game.set_score(0)

def on_button_pressed_b():
    Ludzik.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Punkt: game.LedSprite = None
Ludzik: game.LedSprite = None
onStart()

def on_forever():
    if Ludzik.is_touching(Punkt):
        game.add_score(1)
        Punkt.delete()
    if Ludzik.is_touching_edge():
        basic.show_number(game.score())
        game.game_over()
basic.forever(on_forever)
