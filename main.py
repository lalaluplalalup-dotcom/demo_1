Hand = 0

def on_gesture_shake():
    global Hand
    Hand = randint(1, 3)
    if Hand == 1:
        basic.show_icon(IconNames.HEART)
    if Hand == 2:
        basic.show_icon(IconNames.NO)
    if Hand == 3:
        basic.show_icon(IconNames.TSHIRT)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
