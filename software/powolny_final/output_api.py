from machine import Pin

led_output = Pin(5,Pin.OUT)

program_status = 0


def output_state(water_temperature, set_temperature):
    global program_status
    if water_temperature >= set_temperature:
        program_status = 1
    elif water_temperature <= set_temperature - 3:
        program_status = 0
    
    if program_status == 1:
        led_output.value(1)
    else:
        led_output.value(0)
        
    return program_status