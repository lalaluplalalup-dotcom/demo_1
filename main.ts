input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    Control = 0
    basic.showString("H")
    while (true) {
        if (Control == 1) {
            break;
        }
        basic.showIcon(IconNames.Sad)
        basic.pause(100)
        if (Control == 1) {
            break;
        }
        basic.showIcon(IconNames.Happy)
    }
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    Control = 1
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
let Control = 0
Control = 0
