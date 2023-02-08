import _thread
from display_handling import display
from temp_api import read_ds_sensor, change_temp_factor
from output_api import output_state
from time import sleep
from machine import Timer, Pin, freq


#========================================================================================================
freq(240000000)

global_time = 0
set_temperature = 50
water_temperature = 0.0
program_status = 0

#=========================================================================================================
def global_time_inc(Timer):
    global global_time
    global_time += 1

global_timer = Timer(1)
global_timer.init(period=10, mode=Timer.PERIODIC, callback=global_time_inc)
#==========================================================================================================

result_temp = [set_temperature ,water_temperature]

def thread0():
    while True:
        global water_temperature
        global set_temperature
        set_temperature = change_temp_factor(set_temperature)
        water_temperature = read_ds_sensor()

_thread.start_new_thread(thread0,())     
     
while True:
    if global_time % 100 == 0:
        display(water_temperature, set_temperature, program_status, global_time)
    if global_time % 43 == 0:
        program_status = output_state(water_temperature, set_temperature)