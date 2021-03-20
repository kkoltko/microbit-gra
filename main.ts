input.onButtonPressed(Button.A, function on_button_pressed_a() {
    Ludzik.change(LedSpriteProperty.X, 1)
})
function onStart() {
    
    Ludzik = game.createSprite(1, 2)
    Ludzik.set(LedSpriteProperty.Blink, 350)
    Punkt = game.createSprite(3, 2)
    game.setScore(0)
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    Ludzik.change(LedSpriteProperty.X, -1)
})
let Punkt : game.LedSprite = null
let Ludzik : game.LedSprite = null
onStart()
basic.forever(function on_forever() {
    if (Ludzik.isTouching(Punkt)) {
        game.addScore(1)
        Punkt.delete()
    }
    
    if (Ludzik.isTouchingEdge()) {
        basic.showNumber(game.score())
        game.gameOver()
    }
    
})
