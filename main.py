def on_button_a():
    global Control
    Control = 0
    basic.show_string("H")
    while True:
        if Control == 1:
            break
        basic.show_icon(IconNames.SAD)
        basic.pause(100)
        if Control == 1:
            break
        basic.show_icon(IconNames.HAPPY)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_b():
    global Control
    Control = 1
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_gesture_shake():
    global Hand
    Hand = randint(1, 3)
    if Hand == 1:
        basic.show_icon(IconNames.SCISSORS)
    if Hand == 2:
        basic.show_icon(IconNames.CHESSBOARD)
    if Hand == 3:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Hand = 0
Control = 0
Control = 0