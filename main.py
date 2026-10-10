num1 = 0
num2 = 0

def on_logo_pressed():
    global num1, num2
    basic.show_string("=")
    basic.show_number(num1 - num2)
    basic.pause(2000)
    basic.clear_screen()
    basic.show_icon(IconNames.HAPPY)
    num1 = 0
    num2 = 0
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    global num1
    if num1 == 9:
        num1 = 1
    else:
        num1 += 1
    basic.show_number(num1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global num2
    if num2 == 9:
        num2 = 1
    else:
        num2 += 1
    basic.show_number(num2)
input.on_button_pressed(Button.B, on_button_pressed_b)
