input.onButtonPressed(Button.A, function () {
    Ludzik.change(LedSpriteProperty.X, 1)
})
function onStart () {
    Ludzik = game.createSprite(0, 2)
    Ludzik.set(LedSpriteProperty.Blink, 350)
    Punkt = game.createSprite(4, 2)
    game.setScore(0)
}
input.onButtonPressed(Button.B, function () {
    Ludzik.change(LedSpriteProperty.X, -1)
})
let Punkt: game.LedSprite = null
let Ludzik: game.LedSprite = null
if (Ludzik.isTouching(Punkt)) {
    game.addScore(1)
    Punkt.delete()
}
