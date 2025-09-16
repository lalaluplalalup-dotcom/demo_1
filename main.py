def on_button_a():
    basic.show_string("Hallo, wie geht es euch?")
    for index in range(4):
        basic.show_icon(IconNames.SAD)
        basic.pause(100)
        basic.show_icon(IconNames.HAPPY)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    for index2 in range(4):
        basic.set_led_colors(0x0000ff, 0x0000ff, 0x0000ff)
        basic.pause(1000)
        basic.set_led_colors(0xff0000, 0xff0000, 0xff0000)
        basic.pause(1000)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_ab():
    global led_x, led_y
    led_x = 0
    led_y = 2
    led.plot(led_x, led_y)
    while True:
        led_x += Math.map(input.acceleration(Dimension.X), -1023, 1023, -1, 5)
        led.plot(led_x, led_y)
        basic.set_led_color(0x00ff00)
        if led_x < 0 or led_x > 4:
            basic.set_led_color(0xff0000)
            basic.show_icon(IconNames.NO)
            basic.pause(2000)
            basic.show_leds("""
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                """)
input.on_button_event(Button.AB, input.button_event_click(), on_button_ab)

def on_button_b():
    radio.send_string("\"Hey, bist Du da?\"")
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
led_y = 0
led_x = 0
radio.set_group(1)