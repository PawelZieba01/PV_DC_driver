from machine import Pin

red_output = Pin(5,Pin.OUT)
green_output = Pin(18,Pin.OUT)


program_status = 0


def output_state(water_temperature, set_temperature):
    global program_status
    if water_temperature >= set_temperature:
        program_status = 1
    elif water_temperature <= set_temperature - 3:
        program_status = 0
    
    if program_status == 1:
        red_output.value(1)
        green_output.value(1)
    else:
        red_output.value(0)
        green_output.value(1)
        
    return program_status