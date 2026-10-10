let num1 = 0
let num2 = 0
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    basic.showString("=")
    basic.showNumber(num1 - num2)
    basic.pause(2000)
    basic.clearScreen()
    basic.showIcon(IconNames.Happy)
    num1 = 0
    num2 = 0
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (num1 == 9) {
        num1 = 1
    } else {
        num1 += 1
    }
    
    basic.showNumber(num1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (num2 == 9) {
        num2 = 1
    } else {
        num2 += 1
    }
    
    basic.showNumber(num2)
})
