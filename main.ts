input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    basic.showString("Hallo, wie geht es euch?")
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.Sad)
        basic.pause(100)
        basic.showIcon(IconNames.Happy)
    }
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    for (let index = 0; index < 4; index++) {
        basic.setLedColors(0x0000ff, 0x0000ff, 0x0000ff)
        basic.pause(1000)
        basic.setLedColors(0xff0000, 0xff0000, 0xff0000)
        basic.pause(1000)
    }
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    radio.sendString("Wie heisst Du?")
})
input.onGesture(Gesture.Shake, function () {
    Hand = randint(1, 3)
    if (Hand == 1) {
        basic.showIcon(IconNames.Scissors)
    }
    if (Hand == 2) {
        basic.showIcon(IconNames.Chessboard)
    }
    if (Hand == 3) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
})
let Hand = 0
radio.setGroup(1)
